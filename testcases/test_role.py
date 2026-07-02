"""角色管理 - 接口测试"""

import pytest
import yaml
import os
import time


def load_role_data():
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "role_data.yaml")
    with open(data_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestRole:
    """角色管理模块测试"""

    def test_role_list(self, api):
        """验证查询角色列表"""
        resp = api.get("/system/role/list")
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("code") == 200
        assert data.get("rows") is not None

    def test_add_role(self, api):
        """验证新增角色"""
        role_data = load_role_data()["add_role"]["normal"].copy()
        suffix = str(int(time.time()))[-5:]
        role_data["roleName"] = f"test_role_{suffix}"
        role_data["roleKey"] = f"test_role_{suffix}"

        resp = api.post("/system/role", json_data=role_data)
        assert resp.status_code == 200
        result = resp.json()
        assert result.get("code") == 200, f"新增角色失败: {result}"
