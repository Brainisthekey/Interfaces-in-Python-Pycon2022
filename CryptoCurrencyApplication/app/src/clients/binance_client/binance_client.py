from typing import Any, List, Optional
from src.clients.http_client import HTTPClient


class BinanceClient(HTTPClient):
    """Binance client"""

    def __init__(
        self,
        secretKey: str,
        base_path: Optional[str] = '...',
        supported_codes: Optional[List[int]] = [...],
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
