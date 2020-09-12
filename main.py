from app import app
import io, sys, os, webbrowser, time
from multiprocessing import Process
import subprocess
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValue

if __name__ == '__main__':
    #disable text logging from app
    """
    text_trap = io.StringIO()
    sys.stdout = text_trap
    """


    app.run(host="0.0.0.0", port=app.config["PORT"])