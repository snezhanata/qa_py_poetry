import os

from selene import have
from selene.support.shared import browser
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')
API_URL = os.getenv('api_url')
WEB_URL = os.getenv('web_url')
browser.config.base_url = WEB_URL


def test_login():
    """Successful authorization to some demowebshop (UI)"""
    browser.open("/login")
    browser.element("#Email").send_keys(LOGIN)
    browser.element("#Password").send_keys(PASSWORD).press_enter()
    browser.element(".account").should(have.text(LOGIN))


'''
$ curl -sSL https://install.python-poetry.org | python3 -
$ export PATH="$HOME/.local/bin:$PATH"

Note: Need to add the following rows to /private/etc/bashrc file, it will allow to skip previous command in future
# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

$ poetry init
$ poetry add pytest
$ poetry add selene==2.0.0b14
$ poetry add pylint --group dev
'''