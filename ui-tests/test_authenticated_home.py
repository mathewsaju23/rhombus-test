import re
from playwright.sync_api import Page, expect


def test_authenticated_home_loads(auth_page: Page):
    auth_page.goto("https://rhombusai.com")

    # Assert authenticated-only UI appears
    expect(
        auth_page.get_by_text(re.compile("new project", re.IGNORECASE))
    ).to_be_visible(timeout=15000)
