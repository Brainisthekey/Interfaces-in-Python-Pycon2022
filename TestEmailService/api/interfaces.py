from abc import ABC, abstractmethod
from api.models import ActivationEmailData, ConformationEmailData


class MessageParser(ABC):
    """Abstract Parse message content"""

    @abstractmethod
    def __init__(self, parser: object, content: str) -> None:
        """
        Initialize parser with the dependencies

        Parameters
        ----------
        `parser`
            The dependencies parser object
        
        `content`
            Content to be parsed
        """
        raise NotImplementedError()

    @abstractmethod
    def parse_environment_activation_data(self) -> ActivationEmailData:
        """
        Get environment environment_activation data

        Returns
        ----------
        ActivationEmailData
            Return parsed activation email data
        """
        raise NotImplementedError()
    
    @abstractmethod
    def parse_environment_conformation_data(self) -> ConformationEmailData:
        """
        Get environment conformation data

        Returns
        ----------
        ConformationEmailData
            Return parsed activation email data
        """
        raise NotImplementedError()


class SMTPService(ABC):
    """Abstract SMTP Email service"""

    @abstractmethod
    def __init__(self, parser: MessageParser) -> None:
        """
        Initialize SMTP service with the dependencies

        Parameters
        ----------
        `parser`
            Email content parser
        """
        raise NotImplementedError()

    @abstractmethod
    def cleanup_inbox() -> None:
        """Cleanup inbox after read the content"""
        raise NotImplementedError()

    @abstractmethod
    def get_last_message_content(self) -> str:
        """Get the last message from inbox"""
        raise NotImplementedError()
    
    @abstractmethod
    def get_environment_activation_data(self, message_content: dict) -> ActivationEmailData:
        """
        Parse and return activation message content

        Parameters
        ----------
        `message_content`
            Response message which contains the information about the email
        
        Returns
        ----------
        ActivationEmailData
            Return parsed activation email data
        """
        raise NotImplementedError()
    
    @abstractmethod
    def get_environment_conformation_data(self, message_content: dict) -> ConformationEmailData:
        """
        Parse and return conformation message content

        Parameters
        ----------
        `message_content`
            Response message which contains the information about the email
        
        Returns
        ----------
        ConformationEmailData
            Return parsed conformation email data
        """
        raise NotImplementedError()
