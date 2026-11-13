from typing import Dict

from src.classes.Party import Party
from src.classes.Government import Government
from src.classes.Act import Act
from src.utilities.validators import validate_string, validate_int


def create_party(party_features) -> Party:
    party_id = validate_int(party_features["party_id"])
    party_name = validate_string(party_features["party_name"])
    program_website = validate_string(party_features["program_website"])
    party_website = validate_string(party_features["party_website"])
    party_pic_path = validate_string(party_features["party_pic_path"])
    return Party(
        party_id=party_id,
        party_name=party_name,
        program_website=program_website,
        party_website=party_website,
        party_pic_path=party_pic_path,
    )

def create_government():
    return 0

def create_act():
    return 0