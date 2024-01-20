from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID"27188054))
API_HASH = getenv("API_HASH"03cf971d70a86171fffa0eb22227849c)
BOT_TOKEN = getenv("BOT_TOKEN"6846020310:AAEo32SBlIyjmR2nwg8Suk_0wpDYl_Mghpw)
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuzn-29_uM4SNenapGZ_58du8oKBfi-m_LHBWdhjjmELAIJ-f4_uFH8u51EHayUGcbMvr6WCe6F4oqtnxwgvZnRVsD67X7lItgtAX_790uNzHHYpC5WA-ekeTTEMRbGgLVmI7PQ7nGfRwH5QceYmz63RoaGrOM05cJ6DV6aDBAs66r7Z9YdIAMIUTo6TDdJ-wCMBTYAimSYYmGzN6RHxPYorXt0-GkAdeiXFdRHWdRv9Y0k3Ag1y4AHvAUPqixJKOdLH7h8m3aaTnCw6SWS4yzLqsvIaUt6LCkq1fzpG8ccaaUlMqeqITXpDTl2ZBkui6sca-QDMLxHnnHQjcmhKBVEU=")

# mandatory vars
OWNER_USERNAME = getenv("@Xs_UB")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_جيمثون")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")

# language
LANGUAGE = getenv("BOT_LANGUAGE", "en")
