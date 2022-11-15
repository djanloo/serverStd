import os
import json

old_dir = os.getcwd()
packageDir = os.path.dirname(__file__)
os.chdir(packageDir)

is_configured = False

with open("conf.cf", "r") as conf:
    try:
        conf_data = json.load(conf)
        is_configured = True
    except json.decoder.JSONDecodeError:
        is_configured = False

if not is_configured:
    with open("conf.cf", "w") as conf:
        print("serverstd is not configured yet. Enter server root folder path:")
        SERVER_FOLDER = input()
        if not os.path.exists(SERVER_FOLDER):
            print("Error: path does not exist.")
            exit()
        else:
            json.dump(SERVER_FOLDER, conf)
            import shutil

            print("style sheet copied.")
            shutil.copy("style.css", f"{SERVER_FOLDER}/style.css")
            os.mkdir(f"{SERVER_FOLDER}/images")


from .s_out import ServerStderr as serverStderr
from .s_out import ServerStdout as serverStdout
from .s_out import sprint, sperr, splot
