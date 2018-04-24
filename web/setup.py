import os

try:
    os.environ['BOT_SCRIPT_PATH'] = "~/scripts"
    script_path =os.environ['BOT_SCRIPT_PATH']
except Exception as exp:

    script_path =os.environ['BOT_SCRIPT_PATH']
