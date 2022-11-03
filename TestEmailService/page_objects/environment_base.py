from typing import TypeVar
from api.mailhog import MailHogSMTP
from api.bs4_parser import HTMLParser
from api.models import ActivationEmailData, ConformationEmailData
from api.interfaces import MessageParser, SMTPService


SMTP_Service = TypeVar('SMTP_Service', bound=SMTPService)
Parser = TypeVar('Parser', bound=MessageParser)


class EnvironmentMailObject:

    def __init__(self, smtp_service: SMTP_Service = MailHogSMTP, parser: Parser = HTMLParser) -> None:
        self.environment_parser: SMTP_Service = smtp_service(parser)

    def get_activation_email_content(self) -> ActivationEmailData:
        """Get last activation email content"""
        last_activation_email: ActivationEmailData = self.environment_parser.get_environment_activation_data()
        return last_activation_email

    def get_conformation_email_content(self) -> ConformationEmailData:
        """Get last conformation email content"""
        last_conformation_email: ConformationEmailData = self.environment_parser.get_environment_conformation_data()
        return last_conformation_email
