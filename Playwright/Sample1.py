import pytest
from playwright.sync_api import Page

@pytest.mark.EX1
def test_browserlaunch(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://public.testrail.adsw.amazon.dev/index.php?/runs/view/1916020&group_by=tests:assignedto_id&group_order=asc")
    page1= context.new_page()
    page1.goto("https://www.w3schools.com")

@pytest.mark.EX2
def test_browserlaunchshortcut(page:Page):
    page.goto("https://www.w3schools.com/")