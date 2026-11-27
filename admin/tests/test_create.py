import pytest
from backend_admin.admin_functions.create import create_party, create_government, create_act
from backend_admin.database.db_operations.insert import create_new_party, create_new_government, create_new_party_program, create_new_party_in_government
from backend_admin.classes.Party import Party
from backend_admin.classes.Government import Government
from backend_admin.classes.PartyProgram import PartyProgram
from backend_admin.classes.Party_In_Government import PartyInGovernment
from backend_admin.database.db_connection.context_manager import get_session

#First tests
@pytest.mark.skip(reason="validated")
def test_create_party():
    party_features = {
        "party_id": 1,
        "party_name": "PD",
        "program_website": "xxx",
        "party_website": "yyy",
        "party_pic_path": "zzz"
    }

    party_1 = create_party(party_features)
    assert party_1.party_id == 1
    assert party_1.party_name == "PD"
    assert party_1.program_website == "xxx"
    assert party_1.party_website == "yyy"
    assert party_1.party_pic_path == "zzz"
@pytest.mark.skip(reason="validated")
def test_create_government():
    gov_features = {
        "gov_id": 1,
        "gov_year": "2026",
        "parties_in_charge": [{
            "party_id": 1,
            "party_name": "PD",
        },
        {
            "party_id": 2,
            "party_name": "Ulivo",
        }],
        "list_of_acts": [{
            "act_id": 1,
            "title": "Act 1",
            "description": "xxx",
        }],
    }
    gov_1 = create_government(gov_features)
    assert gov_1.gov_id == 1
    assert gov_1.gov_year == "2026"
    assert gov_1.parties_in_charge == [{
        "party_id": 1,
        "party_name": "PD"
        },
        {
            "party_id": 2,
            "party_name": "Ulivo",
        }]
    assert gov_1.list_of_acts == [{
        "act_id": 1,
        "title": "Act 1",
        "description": "xxx"
        }]
@pytest.mark.skip(reason="validated")
def test_create_act():
    act_features = {
        "act_id": 1,
        "title": "Act 1",
        "description": "xxx",
        "act_link": "www"
    }
    act_1 = create_act(act_features)
    assert act_1.act_id == 1
    assert act_1.title == "Act 1"
    assert act_1.description == "xxx"
    assert act_1.act_link == "www"

#Fake instantiations
m5s = Party(
    party_name="M5S",
    party_website="m5s.it",
    party_pic_path="bla/bla/bla.jpg"
)

party_program_details = PartyProgram(
    year = 2026,
    program_website = "m5s/program.it",
)

gov_2026 = Government(
    year="2026",
)

def test_create_new_party_with_dict(party_details = m5s):
    with get_session() as session:
        new_party = create_new_party(party_details)
        assert new_party.party_id == 1
        assert new_party.party_name == "M5S"
        assert new_party.party_website == "m5s.it"
        assert new_party.party_pic_path == "bla/bla/bla.jpg"

def test_create_new_party_program_with_dict(party_program_details = party_program_details):
    with get_session() as session:
        new_party_program = create_new_party_program(party_program_details)
        assert new_party_program.party_id == 1
        assert new_party_program.year == "2026"
        assert new_party_program.program_website == "m5s/program.it"

def test_create_new_government_with_dict(government_details = gov_2026):
    with get_session() as session:
        new_government = create_new_government(government_details)
        assert new_government.gov_id == 1
        assert new_government.year == "2026"
        assert new_government.is_current == True

def test_create_new_parties_in_government_with_dict(p = m5s, g = gov_2026):
    p_id = m5s.party_id
    g_id = gov_2026.government_id
    insert_party_in_gov = create_new_party_in_government(p, g)
    with get_session() as session:
        party_in_db = session.get(Party, p_id)
        gov_in_db = session.get(Government, g_id)
        assert p_id is not None
        assert p_id == 1
        assert g_id is not None
        assert gov_in_db in party_in_db.government_rel

