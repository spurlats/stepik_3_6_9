import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Select a language")


@pytest.fixture(scope="function")
def language (request):
    language = request.config.getoption("language")
    return language

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit