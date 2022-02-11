"""
User Contributed Levels
"""


import base64

import xss_trainer.levels.meta as meta


class EscapeChars(meta.BaseLevel):
    """
    Bens level for escape Characters
    """

    levelname = "Escape Characters"
    template = "EscapeChars.html"
    author = "Sharkmoos"

    def sanitise(self, data):
        # This is more of a level 2/3 difficulty
        payload = (data.replace("'", "\\'")).replace('"', '\\"')
        return payload

class Encoding(meta.BaseLevel):
    """
    Base 64 Encoding is a thing
    """
    levelname = "Encoding"
    template ="Encoding.html"
    author = "Sharkmoos"

    def sanitise(self, data):
        payload = (data.replace("<", "")).replace(">","")
        # We are expecting a b64 string, so we need to add out own padding if thats not what they give us
        try:
        # Rather than using .decode('base64') and leave it as bytex, let's format a nice string
            decoded_payload = base64.b64decode(payload.encode('ascii')).decode('ascii')
        except Exception:
            decoded_payload = ("Input did not have correct encoding")

        return decoded_payload
