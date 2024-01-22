from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "27188054"))
API_HASH = getenv("API_HASH", "03cf971d70a86171fffa0eb22227849c")
BOT_TOKEN = getenv("BOT_TOKEN", "6846020310:AAEo32SBlIyjmR2nwg8Suk_0wpDYl_Mghpw")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuzn-29_uM4SNenapGZ_58du8oKBfi-m_LHBWdhjjmELAIJ-f4_uFH8u51EHayUGcbMvr6WCe6F4oqtnxwgvZnRVsD67X7lItgtAX_790uNzHHYpC5WA-ekeTTEMRbGgLVmI7PQ7nGfRwH5QceYmz63RoaGrOM05cJ6DV6aDBAs66r7Z9YdIAMIUTo6TDdJ-wCMBTYAimSYYmGzN6RHxPYorXt0-GkAdeiXFdRHWdRv9Y0k3Ag1y4AHvAUPqixJKOdLH7h8m3aaTnCw6SWS4yzLqsvIaUt6LCkq1fzpG8ccaaUlMqeqITXpDTl2ZBkui6sca-QDMLxHnnHQjcmhKBVEU=)

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xs_ub")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "W7MBoT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rr8r9")
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
