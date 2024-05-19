#!/bin/bash

sudo wget -O /usr/local/bin/spitbg https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg
sudo wget -O /usr/local/bin/config_gui.py https://github.com/TurkishLinuxUser/spitbg/raw/main/config_gui.py
sudo wget -O /usr/local/bin/spitbg_conf.json https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg_conf.json

# Dosyaları çalıştırılabilir hale getirme
sudo chmod +x /usr/local/bin/spitbg /usr/local/bin/spitbg_conf.json /usr/local/bin/config_gui.py

# Güncelleme tamamlandıktan sonra update.sh dosyasını silme
rm update_wget.sh