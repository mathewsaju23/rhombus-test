import os
import re
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect

load_dotenv()

EMAIL = os.getenv("RHOMBUS_EMAIL")
PASSWORD = os.getenv("RHOMBUS_PASSWORD")

STORAGE_STATE = "ui-tests/auth_state.json"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://rhombusai.com")

        page.get_by_role("button", name=re.compile("log in", re.IGNORECASE)).click()

        page.get_by_label(re.compile("email", re.IGNORECASE)).fill(EMAIL)
        page.get_by_role("textbox", name=re.compile("password", re.IGNORECASE)).fill(
            PASSWORD
        )

        # Click primary login submit button
        page.get_by_role("button", name="Log In", exact=True).click()

        # Validate dashboard loaded
        # expect(page).to_have_url(re.compile("dashboard", re.IGNORECASE))
        expect(
            page.get_by_text(re.compile("new project", re.IGNORECASE))
        ).to_be_visible(timeout=15000)

        # Save authenticated session
        context.storage_state(path=STORAGE_STATE)

        browser.close()


if __name__ == "__main__":
    main()
