import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "23554959")) #optional
API_HASH = getenv("API_HASH", "cad04ad7178d62f5d50b2a37fb32ff51") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5887336213", "5919535585").split()))
OWNER_ID = int(getenv("OWNER_ID", "5887336213"))
MONGO_URL = getenv("MONGO_URL", "mongodb://ud7kcz6totsvepy86bb2:d4gmTfoBbpzDmNLzItwG@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/b0ojwj6pcvvj30u?replicaSet=rs0")
BOT_TOKEN = getenv("BOT_TOKEN", "5944740729:AAEYsqcrzsvn3evjSPQsPtKqcgVbuZuTEKk")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/e8048f405cdccc7ac8e86.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAX3OTkva_PCoGHEiGGl8JYXyk2ehEMESC1NXrJv-YUY_HfApiq4atDnC_Nl5UeDJhAFUk42_l5k-0an40mdnvh99Vvv4pTJtBeVPJTla8608vxmLVHPkNqin5VB0mhVaPqlle2YndTj8LOWQ5ZLOxXWn_ueZi8S4XaoJrKetKUe-JDT3mAhJdbrIXFGnXfqkizeG-nlA61FFjKcEg390gNo5k27YF-vv9cpNuSRHYHtm6rQxbuNEkjr92YEXJOPMAfkXq4_NWOLKrCsZBWWKsUava40xvq7b_A7fc-XsVv12iCOJEJkUAdYZuF7E_f90Kp6ASY3eDDFNclEhNG-H9pAAAAAFe6Z8VAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
