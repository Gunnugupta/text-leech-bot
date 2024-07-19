import os

API_ID    = os.environ.get("API_ID", "29626867")
API_HASH  = os.environ.get("API_HASH", "82b19751497d00e47c3032409d130423")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6502406090:AAFIBYUGLSYxBgZAS4M8v14-Rw7fGNS_xuk") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8800))  # Default to 8000 if not set
