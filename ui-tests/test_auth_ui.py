import re
from playwright.sync_api import Page, expect

BASE_URL = "https://rhombusai.com"


def test_auth_entry_point_visible(page: Page):
    page.goto(BASE_URL)

    # Validate homepage loaded
    expect(page).to_have_title(re.compile("Rhombus", re.IGNORECASE))

    # # Validate Login button is visible
    login_button = page.get_by_role("button", name=re.compile("Log In", re.IGNORECASE))

    expect(login_button).to_be_visible()
