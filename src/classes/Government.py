from Act import Act
from Party import Party

from typing import List

class Government():
    def __init__(self,
                 gov_id: int,
                 gov_year: str,
                 list_of_acts: List[Act],
                 parties_in_charge: List[Party]):
        self.gov_id = gov_id
        self.gov_year = gov_year
        self.list_of_acts = list_of_acts
        self.parties_in_charge = parties_in_charge