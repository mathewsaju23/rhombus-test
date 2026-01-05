import os
import re
from playwright.sync_api import Page, expect

TEST_FILE = os.path.abspath("test-data/messy_input.csv")


def test_dataset_upload(auth_page: Page):
    auth_page.goto("https://rhombusai.com")

    # Click + (add dataset)
    auth_page.locator("button:has(svg.lucide-plus)").first.click()

    # Click Browse Here
    auth_page.get_by_text("Browse Here", exact=True).click()

    # Select file
    auth_page.locator("input[type='file']").set_input_files(TEST_FILE)

    # Confirm attach
    auth_page.get_by_role("button", name="Attach", exact=True).click()
