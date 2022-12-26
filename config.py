import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "18971757")

API_HASH = os.environ.get("API_HASH", "9395187b26708c27d80fb81f3d75a3bb")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5984317959:AAFDLuGol21E0cmmXEv8AKFagLoqlBXLxjI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001836916053") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/0ca538210e8b4af835339.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
