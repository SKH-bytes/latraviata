# # # # # # # # # # # # # Import # # # # # # # # # # # # # # # # # # # # # # # # # # #
from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# # # # # # # # # # # # # Import # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # Intro # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Start the session
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'none'
driver = webdriver.Firefox()
time.sleep(1)
print("Ouverture de session : réussie")

# Page de connexion 

def connect():
	driver.get("https://ts2.x1.europe.travian.com/")
	driver.find_element(By.NAME,"name").send_keys("")
	driver.find_element(By.NAME,"password").send_keys("")
	driver.find_element(By.TAG_NAME,"button").click()
	time.sleep(1)
	print("Connexion : réussie")
connect()

# # # # # # # # # # # # # Intro # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # General Quest choose # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Retrieve object class to make decision

quest_master_path = "//button[@id='questmasterButton']"
data_quest_master = driver.find_element(By. XPATH, quest_master_path)
retrieve_quest_master = data_quest_master.get_dom_attribute("class")

time.sleep(1)

	# Determine if go to the collect or not

def quest_test():
	if retrieve_quest_master == "vid_3 ":
		print("Quêtes : Rien à collecter")
		pass
	else:
		print("Quêtes : Quelque(s) chose(s) à collecter")
		data_quest_master.click() #rentre dans le menu
quest_test()

time.sleep(1)

# # # # # # # # # # # # # General Quest choose # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # Journeys choose # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 	# Retrieve journeys data to make decision

# journeys_path = "div.content:nth-child(1)"
# data_journeys = driver.find_element(By. CSS_SELECTOR, journeys_path)
# retrieve_journeys = data_journeys.get_dom_attribute("class")

# data_journeys.click()

# time.sleep(2)

# go_journey_path = "//div[@id='contentOuterContainer']/div[@class='contentContainer']/div[@id='content']/div[@id='heroAdventure']/table[@class='borderGap adventureList']/tbody/tr[1]/td[5]"
# data_go_journey = driver.find_element(By. XPATH, go_journey_path)
# retrieve_go_journey = data_go_journey.get_dom_attribute("class")

# data_go_journey.click()

# continue_journey_path = ".textButtonV2 > div:nth-child(1)"
# data_continue_journey = driver.find_element(By. CSS_SELECTOR, continue_journey_path)
# retrieve_continue_journey = data_continue_journey.get_dom_attribute("class")

# data_continue_journey.click()

# # # # # # # # # # # # # Journeys choose # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # Heros status FAILED # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 	# Retrieve data to ensure Heros levelUp - Ok

# heros_levelUP_path = ".levelUp"
# data_heros_levelUP = driver.find_element(By. CSS_SELECTOR, heros_levelUP_path)
# retrieve_heros_levelUP = data_heros_levelUP.get_dom_attribute("class")

# 	# If Heros levelUP, acess Heros status - Ok

# heros_attributaccess_path = "#heroImageButton"
# data_heros_attributaccess = driver.find_element(By. CSS_SELECTOR, heros_attributaccess_path)
# retrieve_heros_attributaccess = data_heros_attributaccess.get_dom_attribute("class")

# data_heros_attributaccess.click()

# 	# Count how many points we have - Impossible to access the right path

# heros_countpoint_path = "//div[@id='background']/div[@id='center']/div[@id='contentOuterContainer']/div[@class='contentContainer']/div[@id='content']/div[@id='heroV2']"
# data_heros_countpoint = driver.find_element(By. CSS_SELECTOR, heros_countpoint_path)
# retrieve_heros_countpoint = data_heros_countpoint.text
# print(data_heros_countpoint)

# 	# Use points to increase abbility - Impossible to access the right path

# heros_increaseabbility_path = "/html/body/div[3]/div[3]/div[3]/div[2]/div/div/div[4]/div/div/div[5]/button[1]"
# data_heros_increaseabbility = driver.find_element(By. XPATH, heros_increaseabbility_path)
# retrieve_heros_increaseabbility = data_heros_increaseabbility.get_dom_attribute("class")

# for use in range(4):
# 	data_heros_increaseabbility.click()

# 	# Save abbilities which are increased

# heros_saveabbilities_path = "#savePoints > div:nth-child(1)"
# data_heros_saveabbilities = driver.find_element(By. CSS_SELECTOR, heros_saveabbilities_path)
# retrieve_heros_saveabbilities = data_heros_saveabbilities.get_dom_attribute("class")

# data_heros_saveabbilities.click()

# # # # # # # # # # # # # Heros status FAILED # # # # # # # # # # # # # # # # # # # # # # # # # # #


# driver.quit()
