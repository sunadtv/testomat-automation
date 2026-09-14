from playwright.sync_api import Page, expect


def test_login_with_invalid_creds(page: Page):
    open_home_page(page)

    expect(page.get_by_role("link", name="Log in")).to_be_visible()
    page.get_by_role("link", name="Log in").click()

    login_user(page, "name@email.com", "********")

    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid email or password.")

def test_search_project_in_company(page: Page):
    open_sign_in_page(page)
    login_user(page, "email", "password")
    
    project_name = "Python manufacture"
    search_project(page, project_name)

    expect(page.get_by_role("heading", name=project_name)).to_be_visible()


def open_home_page(page: Page):
    page.goto("https://testomat.io/")

def open_sign_in_page(page: Page):
    page.goto("https://app.testomat.io/users/sign_in")

def search_project(page: Page, project_name: str):
    page.locator("#content-desktop #search").fill(project_name)

def login_user(page: Page, email: str, password: str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role("button", name="Sign in").click()
    
