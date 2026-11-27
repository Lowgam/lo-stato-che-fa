from backend_admin.classes.Party import Party
from backend_admin.classes.Government import Government
from backend_admin.classes.Act import Act
from backend_admin.utilities.validators import validate_string, validate_int


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
        party_pic_path=party_pic_path
    )

def create_government(gov_features) -> Government:
    gov_id = validate_int(gov_features["gov_id"])
    gov_year = validate_string(gov_features["gov_year"])
    parties_in_charge = gov_features["parties_in_charge"]
    list_of_acts = gov_features["list_of_acts"]
    return Government(
        gov_id=gov_id,
        gov_year=gov_year,
        parties_in_charge=parties_in_charge,
        list_of_acts=list_of_acts
    )

def create_act(act_features) -> Act:
    act_id = validate_int(act_features["act_id"])
    title = validate_string(act_features["title"])
    description = validate_string(act_features["description"])
    link = validate_string(act_features["act_link"])
    return Act(
        act_id=act_id,
        title=title,
        description=description,
        act_link=link
    )