from backend_admin.classes.Party import Party
from backend_admin.classes.PartyProgram import PartyProgram
from backend_admin.classes.Government import Government
from backend_admin.classes.Act import Act
from backend_admin.database.db_connection.context_manager import get_session

def create_new_party(party_details : dict):
    with get_session() as session:
        new_party = Party(
            party_name = party_details["party_name"],
            party_website = party_details["party_website"],
            party_pic_path = party_details["party_pic_path"]
        )
        session.add(new_party)

def create_new_party_program(party_program_details : dict):
    with get_session() as session:
        new_party_program = PartyProgram(
            party_id = party_program_details["party_id"],
            year = party_program_details["year"],
            program_website = party_program_details["program_website"],
            source_pdf_path = party_program_details["source_pdf_path"],
            processed_pdf_path = party_program_details["processed_pdf_path"],
        )
        session.add(new_party_program)

def create_new_government(government_details : dict):
    with get_session() as session:
        new_government = Government(
            year = government_details["year"],
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

def create_new_party_in_government(p: Party, g: Government):
    with get_session() as session:
        p.government_rel.append(g)
        session.add_all([p, g])
