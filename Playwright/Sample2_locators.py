from playwright.sync_api import Page ,expect
import re

def test_orange_Login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name=" Login").click()
    expect(page.locator(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")).to_be_visible()