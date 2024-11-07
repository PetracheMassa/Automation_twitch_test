import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from logging_setup import setup_logger

# Initialize logger
setup_logger()


def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "Samsung Galaxy S8+"})
    driver = webdriver.Chrome(options=chrome_options)
    logging.warning("Browser setup complete with mobile emulation for Samsung Galaxy S8+")
    return driver


def handle_cookie_popup(driver):
    try:
        # Wait for the "Accept" button to be clickable and then click on it
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-a-target='consent-banner-accept']"))
        )
        accept_button.click()
        logging.info("Clicked on 'Accept' button.")

        # Wait until the popup disappears
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@data-a-target='consent-banner-accept']"))
        )
        logging.info("Pop-up successfully closed.")
    except (NoSuchElementException, TimeoutException) as e:
        logging.error("Failed to close the pop-up: %s", e)


def test_twitch_search():
    logging.info("Starting the test")

    driver = setup_browser()
    driver.get("https://m.twitch.tv")  # Access mobile version directly
    logging.info("Navigated to Twitch mobile site")
    time.sleep(3)

    handle_cookie_popup(driver)

    try:
        search_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Search']")))
        ActionChains(driver).move_to_element(search_icon).click(search_icon).perform()
        logging.info("Clicked on search icon")
    except NoSuchElementException:
        logging.error("Search icon not found.")

    search_box = driver.find_element(By.XPATH, "//input[@type='text']")
    search_box.send_keys("StarCraft II")
    logging.info("Entered 'StarCraft II' in search box")
    time.sleep(2)
    search_box.submit()

    actions = ActionChains(driver)
    for _ in range(2):
        # Scroll to the next section
        actions.scroll_by_amount(0, 500).perform()
        logging.info("Scrolled to next section")
        time.sleep(1)

    streamer = driver.find_element(By.XPATH, "(//*[@data-a-target='preview-card-title'])[1]")
    streamer.click()
    logging.info("Clicked on the first streamer")
    time.sleep(5)

    time.sleep(10)
    driver.save_screenshot("streamer_screenshot.png")
    logging.info("Screenshot taken and saved as 'streamer_screenshot.png'")

    driver.quit()
    logging.info("Test completed successfully")
