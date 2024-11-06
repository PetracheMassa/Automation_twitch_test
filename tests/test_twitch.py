from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "Pixel 2"})  # Setează dispozitivul emulat
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def handle_pop_up(driver):
    try:
        pop_up = driver.find_element(By.XPATH, "//*[@class='modal-class']")  # Actualizează acest locator
        if pop_up:
            close_button = pop_up.find_element(By.XPATH, "//*[text()='Close']")  # Localizează butonul de închidere
            close_button.click()
            print("Pop-up închis.")
    except:
        print("Niciun pop-up de închis.")

def test_twitch_search():
    driver = setup_browser()
    driver.get("https://www.twitch.tv")
    time.sleep(3)

    # Pasul 2: Clic pe iconul de căutare
    search_icon = driver.find_element(By.XPATH, "//*[@aria-label='Search']")
    search_icon.click()

    # Pasul 3: Introduce "StarCraft II" în căutare
    search_box = driver.find_element(By.XPATH, "//input[@type='text']")
    search_box.send_keys("StarCraft II")
    time.sleep(2)
    search_box.submit()

    # Pasul 4: Derulează de două ori
    actions = ActionChains(driver)
    for _ in range(2):
        actions.scroll_by_amount(0, 500).perform()
        time.sleep(1)

    # Pasul 5: Selectează un streamer
    streamer = driver.find_element(By.XPATH, "(//*[@data-a-target='preview-card-title'])[1]")
    streamer.click()
    time.sleep(5)

    # Pasul 6: Așteaptă încărcarea și capturează screenshot
    handle_pop_up(driver)
    time.sleep(10)
    driver.save_screenshot("streamer_screenshot.png")

    driver.quit()
