from typing import Optional
from pydantic import BaseModel


class ActivationEmailData(BaseModel):
    activation_link: Optional[str] = None
    invite_code: Optional[str] = None


class ConformationEmailData(BaseModel):
    environment_link: Optional[str] = None
    voucher: Optional[str] = None
