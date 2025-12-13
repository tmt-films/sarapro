import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8163907060:AAEbMLWLiLW-MgLlqrw041OdYvKP0TQXEkQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9698652"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b354710ab18b84e00b65c62ba7a9c043")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002568581749"))

MIN_ID = int(os.getenv("MIN_ID", 1))
MAX_ID = int(os.getenv("MAX_ID", 150))

VIDEOS_RANGE = list(range(MIN_ID, MAX_ID + 1))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "8454765899"))

#Port
PORT = os.environ.get("PORT", "3435")
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sarra:sarra@cluster0.va2usbg.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "sara")

IS_VERIFY = os.environ.get("IS_VERIFY", "false")

TUT_VID = os.environ.get("TUT_VID", "https://t.me/delight_link/2")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/604716a0e6cf18f715701-c68e4f9aa382c8b69e.jpg")

FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/d351fccfbe3abaf29ac46-c0db9c0cd3e9720242.jpg")

QR_PIC = os.environ.get("QR_PIC", "https://graph.org/file/894fef0a8b13ab4e46117-75da0530835c83d498.jpg")

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links

PICS = (os.environ.get("PICS", "https://graph.org/file/1fc526b363c759f2a154a-84319e90b899344ca1.jpg https://graph.org/file/081e39049f441e33600d7-714ddb2b2b37e0563b.jpg https://graph.org/file/604716a0e6cf18f715701-c68e4f9aa382c8b69e.jpg https://graph.org/file/d351fccfbe3abaf29ac46-c0db9c0cd3e9720242.jpg")).split() #Required

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>ʙʏ @Javpostr</b>")


#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("True", True) == 'True'


#==========================(BUY PREMIUM)====================#

PREMIUM_BUTTON = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
)
PREMIUM_BUTTON2 = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
) 

OWNER_TAG = os.environ.get("OWNER_TAG", "rohit_1888")

#UPI ID
UPI_ID = os.environ.get("UPI_ID", "rohit23pnb@axl")

#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://t.me/paymentbot6/2")

#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/rohit_1888")

#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "0 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "199 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "349 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "599 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "1999 rs")
#===================(END)========================#

#==========================(REFERRAL SYSTEM)====================#
# Referral system settings
# How many referrals needed to get premium
REFERRAL_COUNT = int(os.environ.get("REFERRAL_COUNT", "5"))  # Default: 5 referrals
# How many days of premium to give for referrals
REFERRAL_PREMIUM_DAYS = int(os.environ.get("REFERRAL_PREMIUM_DAYS", "7"))  # Default: 7 days
#===================(END)========================#

#==========================(USER REPLY TEXT)====================#
# Reply text for unnecessary messages from non-admin users
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "⚠️ Pʟᴇᴀsᴇ ᴜsᴇ ᴛʜᴇ ᴘʀᴏᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴏʀ ʙᴜᴛᴛᴏɴs ᴛᴏ ɪɴᴛᴇʀᴀᴄᴛ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ.\n\nUse /help to see available commands.")
#===================(END)========================#
LOG_FILE_NAME = "testingbot.txt"
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









