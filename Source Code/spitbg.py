import subprocess
from datetime import datetime
import time
import json
import platform
from colorama import init, Fore, Back, Style
import os
import argparse

# background class
class Background:
    def __init__(self, filename: str, directory: str, start: str, end: str) -> None:
        self.filename = filename
        self.directory = directory
        self.start = start
        self.end = end

# method to read configuration from conf.json
def read_configuration(file_path: str) -> tuple[list[Background], str]:
    backgrounds = []
    check = ""
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
            if "backgrounds" in config:
                for bg in config["backgrounds"]:
                    backgrounds.append(Background(bg["filename"], bg["directory"], bg["start"], bg["end"]))
            if "check" in config:
                check = config["check"]
    except FileNotFoundError:
        pass
    return backgrounds, check

# method to change background spesific time
def set_background_at_time(backgrounds: list[Background]) -> None:
    now = datetime.now().time()
    for item in backgrounds:
        start_time = datetime.strptime(item.start, "%H:%M").time()
        end_time = datetime.strptime(item.end, "%H:%M").time()

        if start_time < end_time:
            if start_time <= now < end_time:
                set_background(item.directory + item.filename)
                break
        else:
            if now >= start_time or now < end_time:
                set_background(item.directory + item.filename)
                break

# method to change background
def set_background(image_path):
    command = ["feh", "--bg-fill", image_path]
    subprocess.run(command)

# method to check if conf.json is properly configured
def check_configuration(check: str) -> None:
    if check.upper() != "Y":
        print(Fore.RED + "❌ Please config the conf.json file as needed and update the 'check' value to 'Y'" + Style.RESET_ALL)
        print("Config File:    ~/.config/spitbg/conf.json")
        sys.exit(1)

# main loop
def main() -> None:
    conf_file = "~/.config/spitbg/conf.json"
    backgrounds, check = read_configuration(conf_file)
    check_configuration(check)

    while True:
        # check now
        now = datetime.now()

        # set background according to configured times
        set_background_at_time(backgrounds)

        # check every minute
        time.sleep(60)

if __name__ == '__main__':
    main()
