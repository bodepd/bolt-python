from typing import Callable

from slack_bolt.logger import get_bolt_logger
from slack_bolt.middleware.middleware import Middleware
from slack_bolt.request import BoltRequest
from slack_bolt.response import BoltResponse


class UrlVerification(Middleware):  # type: ignore
    def __init__(self):
        self.logger = get_bolt_logger(UrlVerification)

    def process(
        self, *, req: BoltRequest, resp: BoltResponse, next: Callable[[], BoltResponse],
    ) -> BoltResponse:
        if self._is_url_verification_request(req.body):
            return self._build_success_response(req.body)
        else:
            return next()

    # -----------------------------------------

    @staticmethod
    def _is_url_verification_request(body: dict) -> bool:
        return body is not None and body.get("type", None) == "url_verification"

    @staticmethod
    def _build_success_response(body: dict) -> BoltResponse:
        return BoltResponse(status=200, body={"challenge": body.get("challenge")})