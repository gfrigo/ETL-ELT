from typing import List, Dict

class HtmlCollectorSpy():

    def __init__(self) -> None:
        self.collects_essential_information_attributes = {}

    def collects_essential_information(self, html:str) -> List[Dict[str, str]]:
        self.collects_essential_information_attributes['html'] = html
        return [{"name" : 'some_name', "link" : 'https://somelink.com'}]