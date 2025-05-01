import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

#Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7644552445:AAGuO66qTGANJYBEITAxOF8kHyyzYG50Vio")
APP_ID = int(os.environ.get("APP_ID", "20697474"))
API_HASH = os.environ.get("API_HASH", "1acf41c146d578a57741ab0760208eb4")

##---------------------------------------------------------------------------------------------------

#Main 
OWNER_ID = int(os.environ.get("OWNER_ID", "5851158054"))
PORT = os.environ.get("PORT", "8080")

##---------------------------------------------------------------------------------------------------

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jetoj55421:8MVPDRNIxwJen7Vf@cluster0.uyyl02b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "links")

##---------------------------------------------------------------------------------------------------

#Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "") #No Need keep it blank
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5851158054 1885113059").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

##---------------------------------------------------------------------------------------------------        

#Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = None

##---------------------------------------------------------------------------------------------------

#Admin == OWNERID
ADMINS.append(OWNER_ID)
ADMINS.append()

##---------------------------------------------------------------------------------------------------

#Default
LOG_FILE_NAME = "links-sharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
##---------------------------------------------------------------------------------------------------
