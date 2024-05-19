import subprocess
from datetime import datetime
import time
import json
import platform
from colorama import init, Fore, Back, Style
import os
import sys
import argparse

class Background:
    def __init__(self, filename: str, start: str, end: str) -> None:
        self.filename = filename
        self.start = start
        self.end = end

    def full_path(self, directory: str) -> str:
        return os.path.join(directory, self.filename)

def read_configuration(file_path: str) -> tuple[list[Background], str]:
    backgrounds = []
    check = ""
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
            if "backgrounds" in config:
                for bg in config["backgrounds"]:
                    backgrounds.append(Background(bg["filename"], bg["start"], bg["end"]))
            if "check" in config:
                check = config["check"]
    except FileNotFoundError:
        pass
    return backgrounds, check

def set_background_at_time(backgrounds: list[Background]) -> None:
    now = datetime.now().time()
    for item in backgrounds:
        start_time = datetime.strptime(item.start, "%H:%M").time()
        end_time = datetime.strptime(item.end, "%H:%M").time()

        if start_time < end_time:
            if start_time <= now < end_time:
                set_background(item.filename)
                break
        else:
            if now >= start_time or now < end_time:
                set_background(item.filename)
                break

def set_background(image_path):
    command = ["feh", "--bg-fill", image_path]
    subprocess.run(command)
    
def check_configuration(check: str) -> None:
    if check.upper() != "Y":
        print(Fore.RED + "❌ Please configure the spitbg_conf.json file as needed by typing spitbg and update the 'check' value to 'Y'" + Style.RESET_ALL)
        sys.exit(1)

# main loop
def main() -> None:
    conf_file = "/usr/local/bin/spitbg_conf.json"
    backgrounds, check = read_configuration(conf_file)
    check_configuration(check)

    while True:
        now = datetime.now()
        set_background_at_time(backgrounds)
        time.sleep(5)

if __name__ == '__main__':
    main()
