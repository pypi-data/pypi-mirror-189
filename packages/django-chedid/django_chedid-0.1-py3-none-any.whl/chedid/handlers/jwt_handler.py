from .default_handler import DefaultHandler
from ..utils import unpack_jwt, pack_jwt


class JWTHandler(DefaultHandler):
    def pre_process_data(self, data):
        # unpacking requests
        found, self.profile, request, self.key, bad_request = unpack_jwt(data["jwt"])

        # Verifying request
        if not found:
            if bad_request:
                return False, {"detail": "Invalid request"}
            return False, {"detail": "Invalid credentials"}

        return True, request

    def post_process_data(self, data):
        return pack_jwt(data, key=self.key)

