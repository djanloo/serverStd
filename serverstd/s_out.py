import shutil
from datetime import datetime
import sys

SERVER_FOLDER = "/var/www/lowtiers.xyz"
FILE = f"{SERVER_FOLDER}/index.html"

body_string = '<html>\n<head><link rel="stylesheet" href="style.css">\n</head>\n<body>\n<center><h3>server stdout</h3><h4>session started at {startsession}</h4></center></br><p style="font-family:\'Lucida Console\', monospace">\n{content}\n</p>\n</body>\n</html>'
body_string = body_string.format(
    startsession=datetime.now().strftime("%H:%M:%S"), content="{content}"
)

img_string = '<div class="outblock"><div><div class="out">img[<span style="color:green;">{img_counter}</span>]</div><div class="content"><img src={file} /></div></div><div class="datetime">{time}</div></div>'
outblock_string = '<div class="outblock"><div><div class="out">out[<span style="color:green;">{msg_counter}</span>]</div><div class="content">{content}</div></div><div class="datetime">{time}</div></div>'
errblock_string = '<div class="err"><div><div class="out">err[<span style="color:red;">{msg_counter}</span>]</div><div class="content">{content}</div></div><div class="errdatetime">{time}</div></div>'

current_msg = ""

img_counter = 0
msg_counter = 0
err_counter = 0 

def sprint(string):
    string = str(string)
    global current_msg, msg_counter
    current_msg += outblock_string.format(
        msg_counter=msg_counter,
        content=string,
        time=datetime.now().strftime("%H:%M:%S"),
    )
    with open(FILE, "w") as f:
        f.write(body_string.format(content=current_msg))
    msg_counter += 1


def sperr(string):
    string = str(string)
    global current_msg, err_counter
    current_msg += errblock_string.format(
        msg_counter=err_counter,
        content=string,
        time=datetime.now().strftime("%H:%M:%S"),
    )
    with open(FILE, "w") as f:
        f.write(body_string.format(content=current_msg))
    err_counter += 1


def splot(figure):
    global current_msg, img_counter
    figure.savefig(f"{SERVER_FOLDER}/images/image_{img_counter}.png")
    current_msg += img_string.format(
        img_counter=img_counter,
        file=f"/images/image_{img_counter}.png",
        time=datetime.now().strftime("%H:%M:%S"),
    )
    with open(FILE, "w") as f:
        f.write(body_string.format(content=current_msg))
    img_counter += 1


def color_str(string, color):
    return f'<span style="color:{color}">{str(string)}</span>'


class ServerStderr:
    """A wrapper for sys.stderr"""

    def __init__(self):
        self.old_stderr = sys.stderr

    def write(self, data):
        if data.replace(" ", "") != "" and data != "\n" and data != ": ":
            sperr(color_str(data, "red"))
            self.old_stderr.write(f"{data}\n")


class ServerStdout:
    """A wrapper for sys.stderr"""

    def __init__(self):
        self.old_stdout = sys.stdout

    def write(self, data):
        if data.replace(" ", "") != "" and data != "\n":
            sprint(data)
            self.old_stdout.write(f"{data}\n")

    def flush(*args):
        pass
