import json
import requests
import config


class DolphinAPI:
    def __init__(self):
        self.email = config.EMAIL
        self.password = config.PASSWORD
        self.token = config.API_TOKEN

    def auth(self, username: str = None, password: str = None):
        # if not username and not password:
        #     username = self.config['dolphin']['email']
        #     password = self.config['dolphin']['password']
        # data = { "username": username,
        #          "password":  password}
        # try:
        #     access_token = requests.post("https://anty-api.com/auth/login", data=data).json()["token"]
        # except json.decoder.JSONDecodeError:
        #     return False
        # else:
        #     self.config['dolphin']['token'] = access_token
        #     self.config['dolphin']['email'] = username
        #     self.config['dolphin']['password'] = password
        #     with open('app.conf', 'w') as f:
        #         self.config.write(f)
        #     return True
        return True

    def get_profiles(self) -> list:
        headers = { "Authorization": f"Bearer {self.token}" }
        profiles = requests.get('https://anty-api.com/browser_profiles', headers=headers).json()["data"]
        return profiles

    def get_proxies(self) -> list:
        headers = { "Authorization": f"Bearer {self.token}" }
        profiles = requests.get('https://anty-api.com/browser_profiles', headers=headers).json()["data"]
        return profiles

    def start_profile(self, profile_id: str, headless=False) -> str:
        resp = requests.get(f"http://localhost:3001/v1.0/browser_profiles/{profile_id}/"
                            f"start?automation=1&headless={int(headless)}")
        if b"automation" not in resp.content:
            self.stop_profile(profile_id)
            port = self.start_profile(profile_id)
        else:
            port = resp.json()["automation"]["port"]
        return port

    def stop_profile(self, profile_id: str) -> None:
        requests.get(f"http://localhost:3001/v1.0/browser_profiles/{profile_id}/stop")
