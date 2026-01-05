import re
from playwright.sync_api import Page, expect

BASE_URL = "https://rhombusai.com"


def test_auth_entry_point_visible(unauth_page: Page):
    unauth_page.goto(BASE_URL)

    expect(unauth_page).to_have_title(re.compile("Rhombus", re.IGNORECASE))

    login_button = unauth_page.get_by_role(
        "button", name=re.compile("log in", re.IGNORECASE)
    )

    expect(login_button).to_be_visible()
