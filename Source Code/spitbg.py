import subprocess
from datetime import datetime
import time
import json
import platform
from colorama import init, Fore, Back, Style
import os
import sys
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Spit Background Configuration")

    parser.add_argument("-c", "--config", action="store_true", help="Opens config file editor in GUI mode to easily edit your config file")

    return parser.parse_args()

class Background:
    def __init__(self, filename: str, directory: str, start: str, end: str) -> None:
        self.filename = filename
        self.directory = directory
        self.start = start
        self.end = end

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

def set_background(image_path):
    command = ["feh", "--bg-fill", image_path]
    subprocess.run(command)
    
def check_configuration(check: str) -> None:
    if check.upper() != "Y":
        print(Fore.RED + "❌ Please configure the spitbg_conf.json file as needed by typing spitbg -c or spitbg --config and update the 'check' value to 'Y'" + Style.RESET_ALL)
        sys.exit(1)

# main loop
def main() -> None:
    args = parse_arguments()
    
    if args.config:
     subprocess.run(["python3", "/usr/local/bin/config_gui.py"])
    else:
     conf_file = "spitbg_conf.json"
     backgrounds, check = read_configuration(conf_file)
     check_configuration(check)

     while True:
        now = datetime.now()
        set_background_at_time(backgrounds)
        time.sleep(60)

if __name__ == '__main__':
    main()
