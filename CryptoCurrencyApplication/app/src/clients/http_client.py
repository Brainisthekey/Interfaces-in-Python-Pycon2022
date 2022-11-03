from enum import Enum
from typing import List, Optional
import requests
from requests.models import Response
from http.client import HTTPException


class RequestType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "DELETE"
    DELETE = "PATCH"


class HTTPClient:
    """Base HTTP client"""

    def __init__(
        self,
        headers: dict,
        supported_codes: List[int],
        base_path: str,
    ):
        self.headers = headers
        self.supported_codes = supported_codes
        self.base_path = base_path
        self.args = {"headers": self.headers}

    def request(
        self,
        type: RequestType,
        path: str,
        params: Optional[dict] = None,
        body: Optional[dict] = None,
        data: Optional[dict] = None
    ) -> Response:
        """Request processor"""
        self.args.update({"url": self.base_path + path})

        match type:
            case RequestType.GET:
                response = requests.get(**dict(self.args, params=params))
            case RequestType.POST:
                response = requests.post(**dict(self.args, params=params, data=data))
            case RequestType.PUT:
                response = requests.put(**dict(self.args, params=params, body=body))
            case RequestType.DELETE:
                response = requests.delete(**self.args)
            case RequestType.PATCH:
                response = requests.patch(**dict(self.args, params=params, body=body))
            case _:
                raise HTTPException('Exception occurred during processing the request')

        return self.handle_response(response)

    def handle_response(self, response: Response) -> Response:
        """Handle the response"""
        if response.status_code in self.supported_codes:
            return response
        raise HTTPException('Exception occurred during processing the request')
