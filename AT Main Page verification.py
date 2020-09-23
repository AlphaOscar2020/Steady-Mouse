from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.steadymouse.com/")

logo_img = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.XPATH, "//img[@alt='SteadyMouse Cover']"))))

main_text = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.XPATH, "//div[@class='main_inner_box']/h1[1]"))))
assert main_text.text == "The SteadyMouse Project"

sub_text = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.XPATH, "//div[@class='main_inner_box']/div[@class='tiny_centered_text' and 1]"))))
assert sub_text.text == "Go steady with your mouse again!"

learn_more_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button-blue-sharp']")))
learn_more_btn.click()

home_pg_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[1]/a[1]/span[1]")))
home_pg_btn.click()

buy_now_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button-red-sharp']")))
buy_now_btn.click()

driver.quit()
