from src.classes.Act import Act
from src.classes.Party import Party

from typing import List

class Government():
    def __init__(self,
                 gov_id: int,
                 gov_year: str,
                 parties_in_charge: List[Party],
                 list_of_acts: List[Act] | None = None):
        self.gov_id = gov_id
        self.gov_year = gov_year
        self.list_of_acts = list_of_acts
        self.parties_in_charge = parties_in_charge