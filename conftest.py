import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def request_context(playwright_instance):
    request_context = playwright_instance.request.new_context()
    yield request_context
    request_context.dispose()
