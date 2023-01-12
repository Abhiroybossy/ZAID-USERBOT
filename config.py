import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "23554959")) #optional
API_HASH = getenv("API_HASH", "cad04ad7178d62f5d50b2a37fb32ff51") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5919535585").split()))
OWNER_ID = int(getenv("OWNER_ID", "5634468517"))
MONGO_URL = getenv("MONGO_URL", "mongodb://ud7kcz6totsvepy86bb2:d4gmTfoBbpzDmNLzItwG@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/b0ojwj6pcvvj30u?replicaSet=rs0")
BOT_TOKEN = getenv("BOT_TOKEN", "5897828783:AAGvabF1w7zwspVLHCXvDKWHHmWu439Hygo")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/e8048f405cdccc7ac8e86.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "+CBhcdLPU_HFhYzll")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAwso_Aok1DYq82Qyly7LiGiFzoMpW8IcEEwaFySWeNyArzCxhxCQySLae_U3C2W90JUH7Db7ObtKvIE2XTQCaVD3Kljvw6q1U_xEcZw0FPSIvKixw0v3oR6xsPgWiwD3txZg6ztY--PHK94YR07ZrFPdCJXqXxaABzbe1sQ9sZ3Ufd_K5hWMN0b1Fgwzav0zNdReklXzSBU26c4fX1433HJqMDStBHD1Ks64ChtbhLcuq46DsDu53ImgsLsBeDqMoxkC9fKhNw4f43MvWtvlzyBPLXwvA3xxYcIadQJrYOQIC2GCu7y-JDKO0gdZJCO1myjMypklul2pTmeQC2UgCqwAAAAFP1yqlAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
