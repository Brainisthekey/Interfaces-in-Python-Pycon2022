from api.bs4_parser import HTMLParser
from api.interfaces import SMTPService
from api.models import ActivationEmailData, ConformationEmailData


class MailHogSMTP(SMTPService):
    """MailHog SMTP inbox"""

    def __init__(self, parser: HTMLParser):
        self.parser: HTMLParser = parser

    def _decode_message_content(self, message: dict) -> str:
        """
        Decode message content

        Parameters
        ----------
        `message`
            Response message dict which contains the information about email

        Returns
        ----------
        `str`
            Return decoded content of email if exist, otherwise an empty string
        """
        ...

    def cleanup_inbox(self) -> None:
        """
        Cleanup inbox

        Raises
        ----------
        `RequestException`
            Exception during delete all the messages from inbox
        """
        ...

    def get_last_message_content(self) -> str:
        """
        Get the last message content

        Returns
        ----------
        `str`
            Decoded email content
        """
        ...

    def get_environment_activation_data(self) -> ActivationEmailData:
        """
        Get environment activation email content

        Returns
        ----------
        ActivationEmailData
            Parsed email activation content, in case of missing values content would have `None` values
        """
        ...

    def get_environment_conformation_data(self) -> ConformationEmailData:
        """
        Get environment conformation email content

        Returns
        ----------
        ConformationEmailData
            Parsed email conformation content, in case of missing values content would have `None` values
        """
        ...
