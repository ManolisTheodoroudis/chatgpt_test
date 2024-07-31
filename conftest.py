import pytest
from playwright.sync_api import sync_playwright, Playwright, Browser
from utils.logger import Logger_Utils
from config.config import CONF
import os
import shutil

@pytest.fixture(scope="session")
def browser():
    try:
        CONF.logger.info("Setting up Playwright and browser")
        playwright_instance = sync_playwright().start()
        browser_instance = playwright_instance.chromium.launch(
            headless=False,
            args=["--window-position=0,0"],
            slow_mo=3000
        )
        yield browser_instance
    except Exception as e:
        CONF.logger.error(f"Error during browser setup: {e}")
        raise
    finally:
        CONF.logger.info("Tearing down Playwright and browser")
        browser_instance.close()
        playwright_instance.stop()

@pytest.fixture(scope="function")
def page(browser, request):
    test_name = request.node.name
    video_dir = os.path.join(CONF.log_folder, test_name)
    os.makedirs(video_dir, exist_ok=True)

    CONF.logger.info(f"Creating a new page with video recording for test: {test_name}")
    context = browser.new_context(
        viewport={"width": 1920, "height": 1000},
        record_video_dir=video_dir
    )
    # Set default timeout for the context
    context.set_default_timeout(60000)  # Timeout in milliseconds
    page = context.new_page()
    yield page

    CONF.logger.info(f"Closing the page for test: {test_name}")
    page.close()
    context.close()

    # Handle video saving on failure
    if request.node.rep_call.failed:
        video_path = os.path.join(video_dir, f"{test_name}.webm")
        CONF.logger.info(f"Video saved for failed test: {video_path}")
    else:
        # Clean up video directory if test passes
        if os.path.exists(video_dir):
            shutil.rmtree(video_dir)
        CONF.logger.info(f"Removed video directory for passed test: {test_name}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook gets called after every test call and stores the result in the item
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_sessionstart(session):
    Logger_Utils().setup_logger()
    CONF.logger.info("Pytest execution begins")

def pytest_sessionfinish(session, exitstatus):
    CONF.logger.info("Pytest execution finished")

def pytest_runtest_setup(item):
    test_name = item.name
    CONF.logger.info(f"Starting test: {test_name}")

def pytest_runtest_teardown(item, nextitem):
    test_name = item.name
    CONF.logger.info(f"Finished test: {test_name}")