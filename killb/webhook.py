import hashlib
import hmac
import time
from typing import Mapping, Optional, Union

SIGNATURE_HEADER = "X-KillB-Signature"
DEFAULT_TOLERANCE_SECONDS = 300


class Webhook:
    """
        Verifies the signature of webhooks sent by KillB.

        KillB signs every webhook with the X-KillB-Signature header:
        ``t=<unix seconds>,v1=<signature>``, where the signature is the lowercase hex
        HMAC-SHA256 of ``t + "." + raw_body`` keyed with your webhook secret.

        It doesn't call the API, so it can be used on its own, without a Client:

            webhook = Webhook(secret="your_webhook_secret")

        Attributes
        ----------
        secret : str
            The webhook secret configured for your KillB webhook.

        Methods
        -------
        verify_signature(raw_body, headers, tolerance_seconds=300, now=None) -> bool
            Returns True when the request was signed by KillB with this secret.
    """
    def __init__(self, secret: Optional[str]):
        self.secret = secret

    def verify_signature(self, raw_body: Union[bytes, str], headers: Mapping[str, str],
                         tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
                         now: Optional[float] = None) -> bool:
        """
            Verifies the X-KillB-Signature header of a webhook request.

            Pass the body exactly as received (for example ``await request.body()`` in FastAPI or
            ``request.get_data()`` in Flask), not a parsed and re-serialized object: ``json.dumps``
            changes spacing and escaping, and the signature won't match.

            Parameters
            ----------
            raw_body : bytes or str
                The raw request body. A str is encoded as UTF-8.
            headers : Mapping[str, str]
                The request headers. The header name is matched case-insensitively.
            tolerance_seconds : int, optional
                Maximum age of the signature timestamp, in either direction. Default 300.
            now : float, optional
                Current Unix time in seconds, for tests. Default ``time.time()``.

            Returns
            -------
            bool
                True when a v1 signature matches and the timestamp is within the tolerance.

            Raises
            ------
            ValueError
                When no webhook secret is configured.

            Example
            -------
            @app.post("/webhooks/killb")
            async def killb_webhook(request: Request):
                if not webhook.verify_signature(await request.body(), request.headers):
                    raise HTTPException(status_code=401, detail="Invalid signature")
                event = json.loads(await request.body())
        """
        if not self.secret:
            raise ValueError("A webhook secret is required to verify webhook signatures")

        header = _get_header(headers, SIGNATURE_HEADER)
        if not header:
            return False

        timestamps = []
        signatures = []
        for part in header.split(","):
            key, separator, value = part.partition("=")
            if not separator:
                continue
            key, value = key.strip(), value.strip()
            if key == "t":
                timestamps.append(value)
            elif key == "v1":
                signatures.append(value)
        if len(timestamps) != 1 or not signatures:
            return False

        timestamp = timestamps[0]
        if not timestamp.isascii() or not timestamp.isdigit():
            return False
        current = time.time() if now is None else now
        if abs(current - int(timestamp)) > tolerance_seconds:
            return False

        body = raw_body.encode("utf-8") if isinstance(raw_body, str) else raw_body
        expected = hmac.new(self.secret.encode("utf-8"), timestamp.encode("ascii") + b"." + body,
                            hashlib.sha256).hexdigest()
        return any(hmac.compare_digest(expected, signature) for signature in signatures)


def _get_header(headers: Mapping[str, str], name: str) -> Optional[str]:
    value = headers.get(name)
    if value is None:
        lowered = name.lower()
        for key, candidate in headers.items():
            if key.lower() == lowered:
                value = candidate
                break
    return value if isinstance(value, str) else None
