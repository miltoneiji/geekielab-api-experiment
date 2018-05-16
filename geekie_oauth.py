# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac
import random
import time
import urllib


class OAuthClient:

    def __init__(self, shared_secret, user_id, organization_id):
        self.shared_secret = shared_secret
        self.user_id = user_id
        self.organization_id = organization_id

    def get_oauth_params(self):
        http_method = "POST"
        base_url = "https://www.geekielab.com.br/login/launch"

        nonce = self._get_random_hash()
        current_time = self._get_current_timestamp()

        oauth_params = {
            "oauth_consumer_key": self.organization_id,
            "oauth_nonce": nonce,
            "oauth_signature_method": "HMAC-SHA1",
            "oauth_timestamp": current_time,
            "oauth_version": "1.0",
            "user_id": self.user_id,
        }

        parameter_string = "oauth_consumer_key={}&oauth_nonce={}&oauth_signature_method=HMAC-SHA1&oauth_timestamp={}&oauth_version=1.0&user_id={}".format(
            self.organization_id,
            nonce,
            current_time,
            self.user_id,
        )

        signature_base =  self._generate_signature_base_string(
            http_method=http_method,
            base_url=base_url,
            parameter_string=parameter_string,
        )

        signing_key = self._generate_signing_key(
            consumer_secret=self.shared_secret,
            oauth_token_secret="", # Geekie OAuth doesn't use the oaut token secret
        )

        oauth_signature = self._generate_oauth_signature(
            signature_base=signature_base,
            signing_key=signing_key,
        )

        oauth_params["oauth_signature"] = oauth_signature

        return oauth_params

    def _generate_signature_base_string(self, http_method, base_url, parameter_string):
        return "{}&{}&{}".format(
            http_method,
            urllib.quote(base_url, ""),
            urllib.quote(parameter_string),
        )

    def _generate_signing_key(self, consumer_secret, oauth_token_secret):
        return "{}&".format(
            urllib.quote(consumer_secret, ""),
        )

    def _generate_oauth_signature(self, signature_base, signing_key):
        return base64.b64encode(hmac.new(signing_key, signature_base, hashlib.sha1).digest())

    def _get_random_hash(self):
        return hashlib.sha1(str(random.getrandbits(32))).hexdigest()

    def _get_current_timestamp(self):
        return int(time.time())
