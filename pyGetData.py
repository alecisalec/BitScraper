#####BitScrape##########
####Alec Graham 7.2.2021

#### impert Libraries
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import sys


#Call from comand line as follows:

#python3 pyGetData.py BTC > outputFile.csv
#or
#python3 pyGetData.py BTC >> outputFile.csv

## use the >> to append to outfile, us eht > to overwrite outfile

###if you want headless or not  edit options.headless (True or False)
### fun to watch, maybe not as performative tho

### options and variables
options = Options()
options.headless = False  # edit here to see browswer or not

#name for coin passed into the commandline
flags = sys.argv[1]

#### time between collections
interval = 5


#Init web driver
driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://robinhood.com/crypto/'+flags)
## loads the page
time.sleep(5)

####locates the element based on it XPATH 
PriceXPATH =['/html/body/div[1]/div[1]/div[2]/main/div/div/div/div/section/header/div[1]/h2/span/div/div[1]',
'/html/body/div[1]/div[1]/div[2]/main/div/div/div/div/section/header/div[1]']
priceContainer= driver.find_element(By.XPATH, PriceXPATH[0])


while True:
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    ### print out in csv format / can be modified to export to DB SQLite3 etc
    print(date_time_str, ","+priceContainer.text)
    ### set the interval between collection above
    time.sleep(interval)


#I disabled driver.close becuase this runs all day collecting data
## for a ML project
##driver.close()
### will run until you stop it
## make sure you check your process 
# ##manager to avoid Zombies even after you exit out.

