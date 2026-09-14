from playwright.sync_api import Page, expect


def test_login_with_invalid_creds(page: Page, config: dict):
    page.goto(config["base_url"])

    expect(page.get_by_role("link", name="Log in")).to_be_visible()
    page.get_by_role("link", name="Log in").click()

    login_user(page, "name@email.com", "********")

    expect(page.locator("#content-desktop .common-flash-info")).to_have_text(
        "Invalid email or password."
    )


def test_search_project_in_company(page: Page, config: dict):
    page.goto(config["login_url"])
    login_user(page, config["email"], config["password"])

    project_name = "Python manufacture"
    search_project(page, project_name)

    expect(page.get_by_role("heading", name=project_name)).to_be_visible()


def search_project(page: Page, project_name: str):
    page.locator("#content-desktop #search").fill(project_name)


def login_user(page: Page, email: str, password: str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role("button", name="Sign in").click()
