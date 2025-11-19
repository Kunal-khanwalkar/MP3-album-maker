from .components.component_factory import ComponentFactory
from .components.xml_parser import XMLParser

class GUI:
    def __init__(self, logger):
        self.logger = logger
        self.component_factory = ComponentFactory(self.logger)
        self.xml_parser = XMLParser(self.logger)

    def start(self, wireframe_path):
        with open(wireframe_path, 'r') as file:
            wireframe_content = file.read()
            self.widget_tree = self.xml_parser.parse(wireframe_content)
            self.logger.debug("Widget Tree generated", self.widget_tree)

        root = self.component_factory.component_generator(self.widget_tree)
        self.logger.warn("Component library generated")

        self.component_factory.start(root)
        self.logger.warn("GUI started successfully.")