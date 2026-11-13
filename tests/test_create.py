from src.admin_functions.create import create_party, create_government


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
