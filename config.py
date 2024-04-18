# Don't Remove Credit @Filethumbnailbot
# Subscribe Instagram page For Amazing Bot @silent_jethalal_back
# Ask Doubt on telegram @movie4hollywood


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("28416899", "")

API_HASH = os.environ.get("18216e288ed0676fc986abc1526c1358", "")

BOT_TOKEN = os.environ.get("7030179376:AAHsOLxufrDUslwe0T5uTztChV2FBikrTgs", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "silent_jethalal_back") 

             # Don't Remove Credit @Filethumbnailbot
             # Subscribe YouTube Channel For Amazing Bot @Filethumbnailbot
             # Ask Doubt on telegram @movie4hollywood
DB_NAME = os.environ.get("DB_NAME", "renamefilethumbnailbot")     

DB_URL = os.environ.get("mongodb+srv://kajalagarwal12334321:FQeRWyY1aK7c5qJR@cluster0.pjkymxu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7030179376').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit  @Filethumbnailbot
# Subscribe Instagram page For Amazing Bot @silent_jethalal_back
# Ask Doubt on telegram @movie4hollywood
