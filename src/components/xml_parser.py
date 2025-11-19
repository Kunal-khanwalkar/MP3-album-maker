import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self, logger):
        self.logger = logger

    def parse(self, xml_string) -> dict[str, any]:
        self.logger.debug(f"Parsing XML file with contents: %s", xml_string)
        self.root = ET.fromstring(xml_string)
        return self._parse(self.root)

    def _parse(self, element):
        widget = {
            'type': element.tag,
            'attributes': element.attrib,
            'children': []
        }
        for child in element:
            widget['children'].append(self._parse(child))
        return widget