import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QComboBox


class ConfigEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Config Editor")
        self.layout = QVBoxLayout()
        self.background_layouts = []
        self.initUI()

    def initUI(self):
        self.backgrounds = []
        self.check = ""

        self.loadConfig()

        # Check bölümünü önceden tanımlayalım
        self.check_label = QLabel("Check:")
        self.check_combobox = QComboBox()
        self.check_combobox.addItems(["X", "Y"])
        self.check_combobox.setCurrentText(self.check)

        # Check ve Save düğmelerini layout'a ekleyelim
        self.layout.addWidget(self.check_label)
        self.layout.addWidget(self.check_combobox)

        self.add_button = QPushButton("+ Add Background")
        self.add_button.clicked.connect(self.addBackgroundButtonClicked)
        self.layout.addWidget(self.add_button)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.saveConfig)
        self.layout.addWidget(self.save_button)

        # Arka planları ekleyelim
        self.addBackgrounds()
        link_layout = QHBoxLayout()
        link_layout.addStretch()

        link1_label = QLabel("<a href='https://github.com/TurkishLinuxUser/spitbg/releases'>Github</a>")
        link1_label.setOpenExternalLinks(True)
        link_layout.addWidget(link1_label)
        link_layout.addStretch()

        self.layout.addLayout(link_layout)
        self.adjustSize()
        self.setLayout(self.layout)

    def loadConfig(self):
        try:
            with open("/usr/local/bin/spitbg_conf.json", "r") as f:
                config = json.load(f)
                self.backgrounds = config.get("backgrounds", [])
                self.check = config.get("check", "")
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "Config file not found!")
        except Exception as e:
            QMessageBox.warning(self, "Warning", f"Error loading config: {e}")

    def addBackgrounds(self):
        for i, background in enumerate(self.backgrounds):
            self.addBackground(background, i)

    def addBackgroundButtonClicked(self):
        if len(self.background_layouts) < 10:
            self.addBackground({}, len(self.background_layouts))
            if len(self.background_layouts) >= 10:
                self.add_button.setEnabled(False)
        else:
            self.add_button.setEnabled(False)
        self.adjustSize()

    def addBackground(self, background, index):
        background_layout = QHBoxLayout()
        self.background_layouts.append(background_layout)
        
        file_label = QLabel("File:")
        file_edit = QLineEdit(background.get("filename", ""))
        file_edit.setMinimumWidth(200)  # File QLineEdit'inin minimum genişliğini ayarla
        background_layout.addWidget(file_label)
        background_layout.addWidget(file_edit)

        file_button = QPushButton("Select File")
        file_button.clicked.connect(lambda checked, file_edit=file_edit: self.selectFile(file_edit))
        background_layout.addWidget(file_button)

        start_label = QLabel("Start Time:")
        start_edit = QLineEdit(background.get("start", ""))
        background_layout.addWidget(start_label)
        background_layout.addWidget(start_edit)

        end_label = QLabel("End Time:")
        end_edit = QLineEdit(background.get("end", ""))
        background_layout.addWidget(end_label)
        background_layout.addWidget(end_edit)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda checked, layout=background_layout: self.deleteBackground(layout))
        background_layout.addWidget(delete_button)

        self.layout.insertLayout(self.layout.indexOf(self.check_label), background_layout)

    def selectFile(self, file_edit):
        filename, _ = QFileDialog.getOpenFileName(self, "Select File")
        if filename:
            file_edit.setText(filename)

    def deleteBackground(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        self.layout.removeItem(layout)
        self.background_layouts.remove(layout)
        if len(self.background_layouts) < 10:
            self.add_button.setEnabled(True)
        self.adjustSize()

    def saveConfig(self):
        try:
            backgrounds = []
            for background_layout in self.background_layouts:
                background = {}
                for i in range(background_layout.count()):
                    widget = background_layout.itemAt(i).widget()
                    if isinstance(widget, QLineEdit):
                        label_text = background_layout.itemAt(i - 1).widget().text()
                        if label_text == "File:":
                            background["filename"] = widget.text()
                        elif label_text == "Start Time:":
                            background["start"] = widget.text()
                        elif label_text == "End Time:":
                            background["end"] = widget.text()
                backgrounds.append(background)

            check = self.check_combobox.currentText()

            with open("/usr/local/bin/spitbg_conf.json", "r") as f:
                config = json.load(f)

            config["backgrounds"] = backgrounds
            config["check"] = check

            with open("/usr/local/bin/spitbg_conf.json", "w") as f:
                json.dump(config, f, indent=4)

            QMessageBox.information(self, "Success", "Config file saved successfully!")
        except Exception as e:
            QMessageBox.warning(self, "Warning", f"Error saving config: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfigEditor()
    window.show()
    sys.exit(app.exec_())
