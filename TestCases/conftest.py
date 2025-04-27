from selenium.webdriver.chrome.options import Options
from Utilities.config_reader import ConfigReader
from PageObjects.LoginObjects import LoginPage
from selenium import webdriver
import allure
import pytest
import os

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests on"
    )

@pytest.fixture(scope="function", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="function", autouse=True)
def setup(browser, request):
    global driver
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    browser_name = request.config.getoption("--browser").lower()
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options)
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function", autouse=False)
def login_fixture(setup):
    data = ConfigReader()
    username = data.get("username")
    password = data.get("password")
    baseurl = data.get("baseurl")
    driver = setup
    driver.get(baseurl)
    lp = LoginPage(driver)
    lp.set_workemail(username)
    lp.set_password(password)
    lp.click_login()
    try:
        username = lp.get_username()
        assert username == "John Sinha"
    except:
        assert False, "Login Failed, username not found"


def pytest_html_report_title(report):
    report.title = "Test Result Report"

# Add screenshot on failed testcases
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        filepath = os.getcwd()
        if (report.skipped and xfail) or (report.failed and not xfail) or report.passed:
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = file_name.replace("/", "_")
            file_path = f"{filepath}\Screenshots\\{file_name}"
            _capture_screenshot(file_path)
            if file_name:
                html = '<div> <img src="%s"' \
                       ' alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
                allure.attach.file(file_path, name="Screenshot After Execution",
                                   attachment_type=allure.attachment_type.PNG)
        report.extra = extra


#  capture screenshot
def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)