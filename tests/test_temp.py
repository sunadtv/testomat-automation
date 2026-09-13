from playwright.sync_api import Page, expect


def test_open_home_page(page: Page):
    page.goto("https://testomat.io/")

    expect(page.get_by_role("link", name="Log in")).to_be_visible()
    page.get_by_role("link", name="Log in").click()

    page.locator("#content-desktop #user_email").fill("name@email.com")
    page.locator("#content-desktop #user_password").fill("********")
    page.get_by_role("button", name="Sign in").click()

    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid email or password.")
