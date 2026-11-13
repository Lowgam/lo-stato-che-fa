class Party:
    def __init__(self,
                 party_id: int,
                 party_name: str,
                 program_website: str,
                 party_website: str,
                 party_pic_path: str | None = None,):
        self.party_id = party_id
        self.party_name = party_name
        self.program_website = program_website
        self.party_website = party_website
        self.party_pic_path = party_pic_path
