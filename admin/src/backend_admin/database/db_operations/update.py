from backend_admin.classes.Party import Party
from backend_admin.classes.PartyProgram import PartyProgram
from backend_admin.classes.Government import Government
from backend_admin.classes.Act import Act
from backend_admin.classes.Party_In_Government import PartyInGovernment
from backend_admin.database.db_connection.context_manager import get_session

def update_party(party_to_update: Party):
    with get_session() as session:
        party = session.get(Party, party_to_update.party_id)
        if party:
            party.party_name = party_to_update.party_name
            party.party_website = party_to_update.party_website
            party.party_pic_path = party_to_update.party_pic_path

def update_party_program(party_program_to_update: PartyProgram):
    with get_session() as session:
        party_program = session.get(PartyProgram, party_program_to_update.party_id)
        if party_program:
            party_program.year = party_program_to_update.year
            party_program.program_website = party_program_to_update.program_website
            party_program.is_current = party_program_to_update.is_current
            party_program.source_pdf_path = party_program_to_update.source_pdf_path
            party_program.processed_pdf_path = party_program_to_update.processed_pdf_path

def update_government(government_to_update: Government):
    with get_session() as session:
        government = session.get(Government, government_to_update.government_id)
        if government:
            government.year = government_to_update.year
            government.is_current = government_to_update.is_current

def update_act(act_to_update: Act):
    with get_session() as session:
        act = session.get(Act, act_to_update.act_id)
        if act:
            act.act_title = act_to_update.act_title
            act.act_description = act_to_update.act_description
            act.act_link = act_to_update.act_link

def update_party_in_government(g_to_update: Government, p_to_update: Party, pg_to_update: PartyInGovernment):
    with get_session() as session:
        par_gov = session.get(PartyInGovernment, pg_to_update.government_id)
        if par_gov:
            par_gov.government_id = g_to_update.government_id
            par_gov.party_id = p_to_update.party_id