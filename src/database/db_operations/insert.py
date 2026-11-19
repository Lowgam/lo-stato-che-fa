from src.classes.Party import Party
from src.classes.PartyProgram import PartyProgram
from src.classes.Government import Government
from src.classes.Party_In_Government import PartyInGovernment
from src.classes.Act import Act
from src.database.context_manager import get_session

def create_new_party(party_details : dict):
    with get_session() as session:
        new_party = Party(
            party_name = party_details["party_name"],
            party_website = party_details["party_website"],
            party_pic_path = party_details["party_pic_path"]
        )
        session.add(new_party)

        # new_party = Party(
        #     party_name="Test1",
        #     party_website="https://test1.com",
        #     party_pic_path="x/x/x",
        # )
        # session.add(new_party)

def create_new_party_program(party_program_details : dict):
    with get_session() as session:
        new_party_program = PartyProgram(
            party_id = party_program_details["party_id"],
            year = party_program_details["year"],
            program_website = party_program_details["program_website"],
        )
        session.add(new_party_program)

    # with get_session() as session:
    #     new_party_program = PartyProgram(
    #         party_id=1,
    #         year=2020,
    #         program_website="https://program1.com",
    #     )
    #     session.add(new_party_program)

def create_new_government(government_details : dict):
    with get_session() as session:
        new_government = Government(
            year = government_details["year"],
        )
        session.add(new_government)

    # with get_session() as session:
    #     new_government = Government(
    #         year=2020,
    #     )
    #     session.add(new_government)

def create_new_act():
    with get_session() as session:
        new_act = Act(
            government_id=1,
            act_title="xxx",
            act_description="xxx",
            act_link="xxx",
        )
        session.add(new_act)

def create_new_party_in_government(p: Party, g: Government):
    with get_session() as session:
        p.government_rel.append(g)
        session.add_all([p, g])
