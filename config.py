from os import getenv
from 

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "27188054"))
API_HASH = getenv("API_HASH", "03cf971d70a86171fffa0eb22227849c")
BOT_TOKEN = getenv("BOT_TOKEN", "6900102201:AAHZ-0tkXuqjq4G8sfiQTuxQJ0TUTjOfrBA")
SESSION_NAME = getenv("SESSION_NAME", "AgGe21YARdrzgt9FTzfgplJNV0tAkvKhLuy60k8rgMqT0sp96b_aU5Yi6uiTr0-YxHJkr858ztQy8RmVV9v30CkwrVShnUQdQ8rYoKNWDEN0ukO8CabAZG6UxKLyen6l5_Lc8zmHyhAjHhpaOCTPgoVHP5PazRg-wWz61c_BoGOdoYnmDv30KrvUTad9XgziNY4SA49nnx5jQoAKSmxMAWOQbY1xdPPTKyEZnRd5J4DAdFlrypFD0NoVxymOc_mU2wXpXB-km9aEbyWz2Uo1GIRdB8GlO4tY0MGEPcZNN0SnZCjsYnDuuJ_zUlHu8i119uyTTbYlo_Yd8UQdXgcQZOV6boVTewAAAAFw6QsnAA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xs_UB")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "W7MBoT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Xs_UB")
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
