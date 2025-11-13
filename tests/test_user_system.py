import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from unittest.mock import patch
from services.user_system import UserSystem



def test_register_creates_user(tmp_path):
    file = tmp_path / "users.json"
    system = UserSystem(filename=file)

    with patch("builtins.input", side_effect=["test@example.com"]), \
         patch("getpass.getpass", side_effect=["password", "password"]):
        system.register()

    assert "test@example.com" in system.users
    assert system.users["test@example.com"] == "password"


def test_login_success(tmp_path):
    file = tmp_path / "users.json"
    system = UserSystem(filename=file)
    system.users = {"test@example.com": "secret"}
    system.save_users()

    with patch("builtins.input", side_effect=["test@example.com"]), \
         patch("getpass.getpass", return_value="secret"):
        result = system.login()
        assert result == "test@example.com"
