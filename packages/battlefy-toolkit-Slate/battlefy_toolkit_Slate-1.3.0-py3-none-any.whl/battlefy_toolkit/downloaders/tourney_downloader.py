import glob
import logging
from _typeshed import StrOrBytesPath
from os.path import join, isfile, exists
from typing import Optional, Set, List, Union, Generator, Tuple, Iterable

from battlefy_toolkit.caching.fileio import load_json_from_file, save_as_json_to_file
from battlefy_toolkit.downloaders.download_utils import fetch_json
from battlefy_toolkit.downloaders.org_downloader import get_tournament_ids
from battlefy_toolkit.endpoints.addresses import TOURNAMENT_INFO_FETCH_ADDRESS_FORMAT, STAGE_INFO_FETCH_ADDRESS_FORMAT, \
    TEAMS_FETCH_ADDRESS_FORMAT, TOURNAMENT_BASIC_INFO_FETCH_ADDRESS_FORMAT
from battlefy_toolkit.org_lists.splatoon_orgs import ORG_SLUGS


def get_basic_tournament_info(tournament_id: str) -> Optional[dict]:
    return fetch_json(TOURNAMENT_BASIC_INFO_FETCH_ADDRESS_FORMAT.format(tourney_id=tournament_id))


def get_tourney_info_file(tourney_id_to_fetch: str) -> Optional[dict]:
    """
    Get the tourney contents corresponding to the given tourney id.
    This is an API call.
    :param tourney_id_to_fetch: The Battlefy id.
    :return: The tourney contents, or None.
    """
    tourney_contents = fetch_json(TOURNAMENT_INFO_FETCH_ADDRESS_FORMAT.format(tourney_id=tourney_id_to_fetch))

    if len(tourney_contents) == 0:
        logging.error(f'Nothing exists at {tourney_id_to_fetch=}.')
        return None

    if isinstance(tourney_contents, list):
        tourney_contents = tourney_contents[0]

    return tourney_contents


def get_tourney_teams_file(tourney_id_to_fetch: str) -> Optional[List[dict]]:
    teams_contents = fetch_json(TEAMS_FETCH_ADDRESS_FORMAT.format(tourney_id=tourney_id_to_fetch))

    if len(teams_contents) == 0:
        logging.error(f'Nothing exists at {tourney_id_to_fetch=}.')
        return None

    if not isinstance(teams_contents, list):
        teams_contents = [teams_contents]

    return teams_contents


def get_stage_ids_for_tourney(tourney_id_to_fetch: str) -> Set[str]:
    """
    Returns stage ids for the specified tourney.
    This is an API call.
    """
    tourney_contents = get_tourney_info_file(tourney_id_to_fetch) or set()
    return set(tourney_contents.get('stageIDs', set()))


def get_stage_file(stage_id_to_fetch: str) -> Optional[dict]:
    """
    Returns the stage file for specified tourney and stage id.
    This in an API call.
    """
    if not stage_id_to_fetch:
        raise ValueError(f'Expected id {stage_id_to_fetch=}')

    _stage_contents = fetch_json(STAGE_INFO_FETCH_ADDRESS_FORMAT.format(stage_id=stage_id_to_fetch))
    if len(_stage_contents) == 0:
        logging.error(f'Nothing exists at {stage_id_to_fetch=}')
        return None

    if isinstance(_stage_contents, list):
        _stage_contents = _stage_contents[0]

    return _stage_contents


def get_or_fetch_tourney_info_file(t_id, tournament_info_cache_path: Union[StrOrBytesPath, int, None]):
    # First, attempt to find the existing tournament info.
    if tournament_info_cache_path and exists(tournament_info_cache_path):
        filename: str = f'{t_id}.json'
        matched_tourney_files = glob.glob(join(tournament_info_cache_path, f'*{filename}'))
        full_path = matched_tourney_files[0] if len(matched_tourney_files) else join(tournament_info_cache_path, filename)
        if isfile(full_path):
            return load_json_from_file(full_path) or dict()
        else:
            contents = get_tourney_info_file(t_id)
            save_as_json_to_file(full_path, contents)
            return contents
    return get_tourney_info_file(t_id)


def get_or_fetch_tourney_ids(
        orgs_to_fetch: Optional[Iterable[str]] = None,
        cache_path: Union[None, StrOrBytesPath, int] = None) -> Generator[Tuple[str, dict], None, None]:
    """
    Get a generator of tourney ids and their tournament info files.
    Note: each org is iterated, and each tournament id has its tournament info read (needed to verify that
    it is indeed a splatoon game!)
    Each organisation that we iterate over is an API call.

    :param orgs_to_fetch: List of org slugs to get from Battlefy, or None to get from the ORG_SLUGS that we watch.
    :param cache_path: If you have a folder of tournament info files, the function will check for already downloaded
    info files in form '{tournament_id}.json' in this directory.
    """
    if orgs_to_fetch is None:
        orgs_to_fetch = ORG_SLUGS

    for org in orgs_to_fetch:
        tournaments = get_tournament_ids(org)
        if tournaments:
            for t_id in tournaments:
                tournament_info = get_or_fetch_tourney_info_file(t_id, cache_path)
                if tournament_info:
                    name = tournament_info.get("gameName")
                    if name.startswith("Splatoon"):
                        yield t_id, tournament_info
