import requests
import yaml
import os


class ApiClient:
    """封装 Requests 请求，统一处理 Token、请求头、响应"""

    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), "..", "config", "settings.yaml")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
        self.base_url = self.config["base_url"]
        self.session = requests.Session()
        self.token = None

    def login(self):
        """登录并获取 Token"""
        login_data = self.config["login"]
        url = f"{self.base_url}/login"
        resp = self.session.post(url, json=login_data)
        assert resp.status_code == 200, f"登录失败: {resp.text}"
        result = resp.json()
        self.token = result.get("token")
        assert self.token, f"未获取到 Token: {result}"
        # 设置后续请求的 Authorization 头
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}"
        })
        return self.token

    def get(self, path, params=None):
        """GET 请求"""
        url = f"{self.base_url}{path}"
        resp = self.session.get(url, params=params)
        return resp

    def post(self, path, json_data=None):
        """POST 请求"""
        url = f"{self.base_url}{path}"
        resp = self.session.post(url, json=json_data)
        return resp

    def put(self, path, json_data=None):
        """PUT 请求"""
        url = f"{self.base_url}{path}"
        resp = self.session.put(url, json=json_data)
        return resp

    def delete(self, path):
        """DELETE 请求"""
        url = f"{self.base_url}{path}"
        resp = self.session.delete(url)
        return resp
