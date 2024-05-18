import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QTimeEdit, QComboBox, QGroupBox
from PyQt5.QtCore import QTime


class ConfigEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Config Editor")
        self.layout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.backgrounds = []
        self.check = ""

        self.loadConfig()

        self.addBackgrounds()

        self.check_label = QLabel("Check:")
        self.check_combobox = QComboBox()
        self.check_combobox.addItems(["X", "Y"])
        self.layout.addWidget(self.check_label)
        self.layout.addWidget(self.check_combobox)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.saveConfig)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def loadConfig(self):
        try:
            with open("spitbg_conf.json", "r") as f:
                config = json.load(f)
                self.backgrounds = config.get("backgrounds", [])
                self.check = config.get("check", "")
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "Config file not found!")
        except Exception as e:
            QMessageBox.warning(self, "Warning", f"Error loading config: {e}")

    def addBackgrounds(self):
     for i, background in enumerate(self.backgrounds):
        background_layout = QHBoxLayout()  # Yatay bir düzen oluşturuyoruz
        self.addBackground(background, i, background_layout)
        self.layout.addLayout(background_layout)  # Ana düzene yatay düzeni ekliyoruz

    def addBackground(self, background, index, layout):
    # Arka planı eklemek için bu sefer ana düzene değil, verilen yatay düzene ekliyoruz
     filename_label = QLabel("Filename:")
     filename_edit = QLineEdit(background.get("filename", ""))
     layout.addWidget(filename_label)
     layout.addWidget(filename_edit)

     directory_label = QLabel("Directory:")
     directory_edit = QLineEdit(background.get("directory", ""))
     directory_button = QPushButton("Select Directory")
     directory_button.clicked.connect(lambda checked, directory_edit=directory_edit: self.selectDirectory(directory_edit))
     layout.addWidget(directory_label)
     layout.addWidget(directory_edit)
     layout.addWidget(directory_button)

     start_label = QLabel("Start Time:")
     start_edit = QLineEdit(background.get("start", ""))
     layout.addWidget(start_label)
     layout.addWidget(start_edit) 

     end_label = QLabel("End Time:")
     end_edit = QLineEdit(background.get("end", ""))
     layout.addWidget(end_label)
     layout.addWidget(end_edit)


    def selectDirectory(self, directory_edit):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            directory_edit.setText(directory + "/")

    def saveConfig(self):
     try:
        backgrounds = []
        for i in range(self.layout.count()):
            background_group_h = self.layout.itemAt(i)
            if background_group_h and isinstance(background_group_h, QHBoxLayout):
                background_group = background_group_h.layout()
                background = {}
                for j in range(background_group.count()):
                    widget = background_group.itemAt(j).widget()
                    if isinstance(widget, QLineEdit):
                        label_text = background_group.itemAt(j - 1).widget().text()  # Get label text
                        if label_text == "Filename:":
                            background["filename"] = widget.text()
                        elif label_text == "Directory:":
                            background["directory"] = widget.text()
                        elif label_text == "Start Time:":
                            background["start"] = widget.text()
                        elif label_text == "End Time:":
                            background["end"] = widget.text()
                backgrounds.append(background)

        check = self.check_combobox.currentText()

        config = {"backgrounds": backgrounds, "check": check}
        with open("spitbg_conf.json", "w") as f:
            json.dump(config, f, indent=4)
        QMessageBox.information(self, "Success", "Config file saved successfully!")
     except Exception as e:
        QMessageBox.warning(self, "Warning", f"Error saving config: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfigEditor()
    window.show()
    sys.exit(app.exec_())
