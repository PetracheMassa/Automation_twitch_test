from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Inițializează ChromeDriver
service = Service('/usr/local/bin/chromedriver')  # Specifică calea dacă este necesar
driver = webdriver.Chrome(service=service)

# Deschide o pagină web pentru test
driver.get("https://www.google.com")
print(driver.title)  # Ar trebui să printeze titlul paginii Google
driver.quit()
