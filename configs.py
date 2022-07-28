# (c) @RoyalKrrishna

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "0")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
        START_PHOTO = int(os.environ.get("START_PHOTO"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**I Am Permanent File Store Bot 🤖
Send me any file and I will save it in my Database.\n\nI'm Also works for channel, Add me to your channel as Admin with Edit Permission and I will Save all your Uploaded File in Channel and add Sharable Button Link.🔗**

🤖 **My Name: [Doluram](https://t.me/{BOT_USERNAME})**

🧑‍🍼 **My Father: @RoyalKrrishna**
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer: @RoyalKrrishna**

Developer is Super Noob 😒. He's Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive 🤪.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

💰 **Donate Now** - krrishnabaaghi@paytm (UPI)
"""
	HOME_TEXT = """
**Hey, [{}](tg://user?id={}) 😀\n\nThis is Doluram The Permanent File Store Bot.🤖

Send me any file And I will give you a permanent Sharable Link. I Support Channel Also! Check About Bot Button.

Note❗
Don't upload any adult content otherwise you will be ban.🚫**
"""
