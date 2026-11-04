import hashlib
import hmac
import json
import time
import unittest

from killb.webhook import Webhook

SECRET = "test-webhook-secret"
NOW = 1_793_000_000

EVENT = {
    "id": "evt-1",
    "data": {"id": "ramp-1", "status": "COMPLETED", "note": "café"},
    "event": "RAMP",
    "action": "UPDATE",
    "updatedAt": "2026-11-04T12:00:00.000Z",
    "createdAt": "2026-11-04T12:00:00.000Z",
    "attempts": 1,
}
RAW_BODY = json.dumps(EVENT, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sign(raw_body: bytes, timestamp: int, secret: str = SECRET) -> dict:
    signature = hmac.new(secret.encode(), f"{timestamp}.".encode() + raw_body, hashlib.sha256).hexdigest()
    return {"X-KillB-Signature": f"t={timestamp},v1={signature}"}


class VerifySignatureTest(unittest.TestCase):
    def setUp(self):
        self.webhook = Webhook(SECRET)

    def verify(self, raw_body, headers, **kwargs):
        kwargs.setdefault("now", NOW)
        return self.webhook.verify_signature(raw_body, headers, **kwargs)

    def test_accepts_a_request_signed_as_killb_signs_it(self):
        self.assertTrue(self.verify(RAW_BODY, sign(RAW_BODY, NOW)))

    def test_accepts_the_body_as_str(self):
        self.assertTrue(self.verify(RAW_BODY.decode("utf-8"), sign(RAW_BODY, NOW)))

    def test_matches_the_header_name_case_insensitively(self):
        header = sign(RAW_BODY, NOW)["X-KillB-Signature"]
        self.assertTrue(self.verify(RAW_BODY, {"x-killb-signature": header}))

    def test_rejects_a_tampered_body(self):
        tampered = RAW_BODY.replace(b"COMPLETED", b"FAILED")
        self.assertFalse(self.verify(tampered, sign(RAW_BODY, NOW)))

    def test_rejects_a_re_serialized_body(self):
        re_serialized = json.dumps(json.loads(RAW_BODY)).encode()
        self.assertFalse(self.verify(re_serialized, sign(RAW_BODY, NOW)))

    def test_rejects_another_secret(self):
        self.assertFalse(self.verify(RAW_BODY, sign(RAW_BODY, NOW, "other-secret")))

    def test_rejects_old_and_future_timestamps(self):
        self.assertFalse(self.verify(RAW_BODY, sign(RAW_BODY, NOW - 301)))
        self.assertFalse(self.verify(RAW_BODY, sign(RAW_BODY, NOW + 301)))

    def test_accepts_the_edge_of_the_tolerance(self):
        self.assertTrue(self.verify(RAW_BODY, sign(RAW_BODY, NOW - 300)))

    def test_honours_a_custom_tolerance(self):
        headers = sign(RAW_BODY, NOW - 60)
        self.assertFalse(self.verify(RAW_BODY, headers, tolerance_seconds=30))
        self.assertTrue(self.verify(RAW_BODY, headers, tolerance_seconds=120))

    def test_rejects_a_missing_header(self):
        self.assertFalse(self.verify(RAW_BODY, {}))

    def test_rejects_malformed_headers(self):
        for header in ["v1=abc", f"t={NOW}", "t=abc,v1=abc", f"t={NOW},t={NOW},v1=abc", "garbage", "t=١٢٣,v1=abc"]:
            with self.subTest(header=header):
                self.assertFalse(self.verify(RAW_BODY, {"X-KillB-Signature": header}))

    def test_accepts_any_matching_v1(self):
        header = sign(RAW_BODY, NOW)["X-KillB-Signature"].replace("v1=", "v1=0000,v1=")
        self.assertTrue(self.verify(RAW_BODY, {"X-KillB-Signature": header}))

    def test_raises_without_a_secret(self):
        with self.assertRaises(ValueError):
            Webhook(None).verify_signature(RAW_BODY, sign(RAW_BODY, NOW), now=NOW)

    def test_uses_the_current_time_by_default(self):
        current = int(time.time())
        self.assertTrue(self.webhook.verify_signature(RAW_BODY, sign(RAW_BODY, current)))


if __name__ == "__main__":
    unittest.main()
