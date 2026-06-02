import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 



# Fetch initial admin list
ADMIN = []  # TemporLoad admins when the bot starts

TOKEN_VERIFY=False
API = environ.get("API", "5a7508a173d6462e4cd4b723766b92541c389a6b") # shortlink api
URL = environ.get("URL", "arolinks.com") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/+Gt55OVP7VTAyNmNl") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "GiRenamerRobot") # bot username without @
VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.
USER_LIMIT_TIME = int(os.environ.get("USER_LIMIT_TIME", "1"))#enter time based on hours

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "14909835")
    API_HASH  = os.environ.get("API_HASH", "384e6e7c78a80b808955af7e48458863")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8791853317:AAHFwDTL8al_aFbwCQnF1QerSixw1uPI-p8") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","hdhub4net")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://aman:hdhub4net@cluster0.f6fbxm4.mongodb.net/?retryWrites=true&w=majority")
    PORT = os.environ.get("PORT", "8050")
    OWNER = int(os.environ.get("OWNER", "1781188088"))
    PRIVATE_USE = False #If Bot is private use set True otherwise False
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', "").split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003742433308"))
    DUMB_CHANNEL = os.environ.get("DUMB_CHANNEL", "100426639554")
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<b>Hello {} 👋 

I Am Powerful And Advance Auto Rename Bot of Gi Cartoons Network!⚡️

To Know More Click Help Button! 😊

Made By - @GI_CARTOONS_OFFICIAL</b>"""

    ABOUT_TXT = f"""
○ Creator: @GiToonsOwner
○ Language: Python3
○ Library: <a href='https://docs.pyrogram.org/'>Pyrogram 2.0.106</a>
○ Channel: @GI_CARTOONS_OFFICIAL
    
Made By - @GI_CARTOONS_OFFICIAL"""

    HELP_TXT = """
<b>➻ Using This Bot You Can Able to Rename Your Files one by one or multi.

➻ You Can Also Select the file type is need to upload.

➻ This Bot is only for Admin use other can use with low limitation </b>

🌌 <b><u>How To Set Thumbnail?</u>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail
➪ /settings - Set Queue, Upload type and metadata 
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail
➪ /view_thumb - Use This Command To View Your Current Thumbnail</b>

📑 <b><u>How To Set Custom Caption?</u>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption</b>
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

</blockquote>"""

    PROGRESS_BAR = """In Progress...\n<blockquote>
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
</blockquote>"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

contact Me:@GiToonsOwner For 🛍 UPI ID</b>"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA?</u>

For Example :

<code>@GI_CARTOONS_OFFICIAL</code>

💬 For Any Help Contact: @GiToonsOwner</b>"""





