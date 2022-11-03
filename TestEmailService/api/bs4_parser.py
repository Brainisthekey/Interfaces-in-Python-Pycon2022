from bs4 import BeautifulSoup
from api.interfaces import MessageParser
from api.models import ActivationEmailData, ConformationEmailData


class HTMLParser(MessageParser):
    """Parse HTML content of the email message"""

    def __init__(self, parser: BeautifulSoup, content: str):
        """Initialize parser with dependencies"""
        self.parser: BeautifulSoup = parser(content, features="html.parser")

    def parse_environment_activation_data(self) -> ActivationEmailData:
        """
        Parse environment activation data

        Returns
        ----------
        ActivationEmailData
            Parsed activation email content
        """
        ...

    def parse_environment_conformation_data(self) -> ConformationEmailData:
        """
        Parse environment conformation data

        Returns
        ----------
        ConformationEmailData
            Parsed conformation email content
        """
        ...
