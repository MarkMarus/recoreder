import json
import requests
from configparser import ConfigParser

class DolphinAPI:
    def __init__(self, config: ConfigParser):
        self.config = config
        self.config.read("app.conf")

    def auth(self):
        data = { "username": self.config['dolphin']['email'],
                 "password": self.config['dolphin']['password'] }
        try:
            access_token = requests.get("https://anty-api.com/auth/login", data=data).json()["token"]
        except json.decoder.JSONDecodeError:
            return False
        else:
            self.access_token = access_token
            return access_token

    def get_profiles(self) -> dict:
        headers = { "Authorization": f"Bearer {self.config['dolphin']['token']}" }
        profiles = requests.get('https://anty-api.com/browser_profiles', headers=headers).json()["data"]
        return profiles

    def start_profile(self, profile_id: str, headless=False) -> str:
        resp = requests.get(f"http://localhost:3001/v1.0/browser_profiles/{profile_id}/"
                            f"start?automation=1&headless={int(headless)}")
        for retry in range(3):
            if b"automation" not in resp.content:
                if retry == 2:
                    self.stop_profile(profile_id)
                    port = self.start_profile(profile_id)
            else:
                port = resp.json()["automation"]["port"]
                return port

    def stop_profile(self, profile_id: str) -> None:
        requests.get(f"http://localhost:3001/v1.0/browser_profiles/{profile_id}/stop")