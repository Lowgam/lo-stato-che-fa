from src.classes.Party import Party
from src.classes.PartyProgram import PartyProgram
from src.classes.Government import Government
from src.classes.Parties_In_Government import PartiesInGovernment
from src.classes.Act import Act
from src.database.context_manager import get_session

def create_new_party():
    with get_session() as session:
        new_party = Party(
            party_name="Test1",
            party_website="https://test1.com",
            party_pic_path="x/x/x",
        )
        session.add(new_party)

def create_new_party_program():
    with get_session() as session:
        new_party_program = PartyProgram(
            party_id=1,
            year=2020,
            program_website="https://program1.com",
        )
        session.add(new_party_program)

def create_new_government():
    with get_session() as session:
        new_government = Government(
            year=2020,
        )
        session.add(new_government)


def create_new_act():
    with get_session() as session:
        new_act = Act(
            government_id=1,
            act_title="xxx",
            act_description="xxx",
            act_link="xxx",
        )
        session.add(new_act)

def create_new_parties_in_government():
    with get_session() as session:
        new_parties_in_government = PartiesInGovernment(
            party_id=1,
            government_id=1,
        )
        session.add(new_parties_in_government)