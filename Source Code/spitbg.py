import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
import subprocess
import webbrowser
import requests
import json
import os
import argparse

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpitBG Tool")
        self.resize(230, 50)

        layout = QVBoxLayout()

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop)
        layout.addWidget(self.stop_button)

        self.config_edit_button = QPushButton("Config Edit", self)
        self.config_edit_button.clicked.connect(self.edit_config)
        layout.addWidget(self.config_edit_button)

        self.check_updates_button = QPushButton("Check Updates", self)
        self.check_updates_button.clicked.connect(self.check_updates)
        layout.addWidget(self.check_updates_button)

        self.setLayout(layout)

    def start(self):
        subprocess.Popen(["python3", "/usr/local/bin/spitbg_bd.py"])

    def stop(self):
        subprocess.Popen(["pkill", "-f", "spitbg_bd.py"])

    def edit_config(self):
        subprocess.Popen(["python3", "/usr/local/bin/config_gui.py"])

    def check_updates(self):
        current_version = self.get_current_version_from_config()
        latest_version = self.get_latest_version_from_github()

        if latest_version and latest_version != current_version:
            self.show_update_notification()
        else:
            QMessageBox.information(self, "No Updates", "No updates available.")

    def get_current_version_from_config(self):
        try:
            with open("spitbg_conf.json", "r") as f:
                config_data = json.load(f)
                current_version = config_data["version"]
                return current_version
        except Exception as e:
            print("Error reading current version from config:", e)
            return None

    def get_latest_version_from_github(self):
        try:
            response = requests.get("https://raw.githubusercontent.com/TurkishLinuxUser/spitbg/main/version/check_updates.txt")
            latest_release = response.text.strip() 
            return latest_release
        except Exception as e:
            print("Error fetching latest version from GitHub:", e)
            return None

    def show_update_notification(self):
        update_dialog = QMessageBox(self)
        update_dialog.setWindowTitle("Update Available")
        update_dialog.setText("An update is available!")

        update_button = QPushButton("Update", update_dialog)
        update_button.clicked.connect(self.update_tool)

        update_dialog.addButton(update_button, QMessageBox.ActionRole)

        update_dialog.exec_()

    def update_tool(self):
            webbrowser.open("https://github.com/TurkishLinuxUser/spitbg/blob/main/README.md")
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
