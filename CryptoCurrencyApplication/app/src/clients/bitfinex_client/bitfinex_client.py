from typing import List, Any, Optional
from src.clients.http_client import HTTPClient


class BitfinexClient(HTTPClient):

    def __init__(
        self,
        secretKey: str,
        base_path: Optional[str] = '...',
        supported_codes: Optional[List[int]] = [],
    ):
        self.secretKey = secretKey
        super().__init__(
            headers={...},
            base_path=base_path,
            supported_codes=supported_codes,
        )

    def get_signature(self, params: dict[str, Any]) -> str:
        """Get signature"""
        ...

    def compose_headers(self) -> dict:
        """Compose headers"""
        ...
