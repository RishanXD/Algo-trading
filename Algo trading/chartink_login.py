import os
import sys
import logging
import contextlib

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # TensorFlow only prints errors now

# Suppress selenium and other external logs
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

def chartink_login():    
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Suppress all output during WebDriver initialization
    with suppress_output():
        chrome_options = webdriver.ChromeOptions()
        # Suppressing additional WebDriver logs
        chrome_options.add_argument("--log-level=3")
        driver = webdriver.Chrome(options=chrome_options)

    # Open the login page
    driver.get('https://chartink.com/login')

    try:
        # Wait until the login button is clickable
        wait = WebDriverWait(driver, 60)
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-callback="onSubmitloginform"]')))

        print("Waiting for the user to complete chartink login manually...")

        # Wait for the login to complete (URL change after redirection)
        current_url = driver.current_url

        # Monitor URL changes
        wait.until(EC.url_changes(current_url))

        # Once the URL changes (redirection occurs), capture all cookies
        cookies = driver.get_cookies()

        # Store only relevant cookies in a dictionary
        Dict = {}
        for cookie in cookies:
            if "remember" in cookie['name']:
                Dict[cookie['name']] = cookie['value']
        return Dict        

    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

    finally:
        # Close the browser after retrieving the cookies
        driver.quit()
