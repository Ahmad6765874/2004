from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "27188054"))
API_HASH = getenv("API_HASH", "03cf971d70a86171fffa0eb22227849c")
BOT_TOKEN = getenv("BOT_TOKEN", "6900102201:AAHZ-0tkXuqjq4G8sfiQTuxQJ0TUTjOfrBA")
SESSION_NAME = getenv("SESSION_NAME", "AgGe21YAVIcXSH9v5RwDJZ3oO9K7golaAehVP8kn7KXIapSlBsenTxo9ToYEY8u02ddY8GfEu8HPliIRvuDVR8VlqKw8bdVBq2HOE2PcAaUNmHNHsJQ3vcr72n49zTKSNrHHqn2GB4F6isCFV8oJJjheo5uHSXdLihYxr2xVr8qtdqL0otmWu3G04u00XPYfHDWKWIKWsO-yWSbNchphz05EcdkLvmEu_FT9RuaD6gHjEnkGhgiUQ1QQsAj97LzOYRr0ugEVQ_9hGrV7ATgHWxsiJFTi3fCOG2sD41Xvdlvw9JFXuvdOKYyTSbDhYQCGVyoHX9nwoWPd8mf2V00a1winbbBXCwAAAAFw6QsnAA=)

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xs_ub")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "W7MBoT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "XS_UB")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
