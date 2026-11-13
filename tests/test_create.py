from src.admin_functions.create import create_party

def test_party():
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

