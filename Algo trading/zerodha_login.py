import os
import sys
import logging
import contextlib

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppresses TensorFlow logging (0 = all, 1 = warning, 2 = error, 3 = fatal)

# Context manager to suppress stdout and stderr
@contextlib.contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

# Disable logging for Selenium WebDriver
logging.getLogger('selenium').setLevel(logging.CRITICAL)

def get_enctoken():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Suppress all output during WebDriver initialization
    with suppress_output():
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")  # Suppress WebDriver logging
        # Ensure the browser window remains open after the script completes
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

    # Open the Zerodha login page
    driver.get('https://kite.zerodha.com/')

    try:
        print("Waiting for the user to complete login manually...")

        # Wait for the login process to complete (URL change)
        wait = WebDriverWait(driver, 120)
        wait.until(EC.url_contains("dashboard"))  # Adjust based on URL after login

        # Once logged in, capture the cookies
        cookies = driver.get_cookies()
        for cookie in cookies:
            if "enctoken" in cookie['name']:
                return cookie['value']

    except Exception as e:
        print(f"An error occurred: {e}")
