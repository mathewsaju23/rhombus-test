import pytest
from playwright.sync_api import sync_playwright

STORAGE_STATE = "ui-tests/auth_state.json"


@pytest.fixture(scope="function")
def unauth_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def auth_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=STORAGE_STATE)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
