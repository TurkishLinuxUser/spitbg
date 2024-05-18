# SpitBG
SpitBG is a simple but very functional tool for automatically making backgrounds out of the photos you specify at the times you previously saved in the config file. For example, you have 2 photos of a mountain taken at sunrise and sunset. You may want to have the sunrise photo in the background from sunrise to sunset and the sunset photo in the background after sunset until sunrise. With this tool you can do it easily.

![My background photo at sunrise](/src/1.png)
![My background photo at noon](/src/2.png)
![My background photo in the evening](/src/3.png)

## Requirements:
- Python >=3.9
  - PyQt5
- Curl or Wget (Only for Fedora and Others)
## Installation
### Linux

**Fedora and Others:**

Download Python3 and PyQt5 first:
```
sudo dnf install python3
sudo dnf install python3-pip
sudo dnf install PyQt5

or

sudo yum install python3
sudo yum install python3-pip
sudo yum install PyQt5
```
Then download Curl or Wget:
```
For Wget:
sudo dnf install wget
or
sudo dnf install wget

For Curl:
sudo yum install curl
or
sudo dnf install curl
```

Then you can download SpitBG:

Download with Curl:
```
sudo curl -o /usr/local/bin/spitbg https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg && sudo curl -o /usr/local/bin/config_gui.py https://github.com/TurkishLinuxUser/spitbg/raw/main/config_gui.py && sudo curl -o /usr/local/bin/spitbg_conf.json https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg_conf.json && sudo chmod +x /usr/local/bin/spitbg /usr/local/bin/spitbg_conf.json /usr/local/bin/config_gui.py
```

Download with Wget:
```
sudo wget -O /usr/local/bin/spitbg https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg && sudo wget -O /usr/local/bin/config_gui.py https://github.com/TurkishLinuxUser/spitbg/raw/main/config_gui.py && sudo wget -O /usr/local/bin/spitbg_conf.json https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg_conf.json && sudo chmod +x /usr/local/bin/spitbg /usr/local/bin/spitbg_conf.json /usr/local/bin/config_gui.py
```

**Ubuntu/Debian:**

Download Python3 and PyQt5 first:
```
sudo apt install python3
sudo apt install python3-pip
sudo apt install PyQt5
```

You should know that you can download SpitBG without typing the following commands. You can download the .deb file from the [Github Releases Page](https://github.com/TurkishLinuxUser/spitbg/releases) :))

or

Curl:
```
sudo apt install curl
```

Wget:
```
sudo apt install wget
```

Then you can download SpitBG:

Download with Curl:
```
sudo curl -o /usr/local/bin/spitbg https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg && sudo curl -o /usr/local/bin/config_gui.py https://github.com/TurkishLinuxUser/spitbg/raw/main/config_gui.py && sudo curl -o /usr/local/bin/spitbg_conf.json https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg_conf.json && sudo chmod +x /usr/local/bin/spitbg /usr/local/bin/spitbg_conf.json /usr/local/bin/config_gui.py
```

Download with Wget:
```
sudo wget -O /usr/local/bin/spitbg https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg && sudo wget -O /usr/local/bin/config_gui.py https://github.com/TurkishLinuxUser/spitbg/raw/main/config_gui.py && sudo wget -O /usr/local/bin/spitbg_conf.json https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg_conf.json && sudo chmod +x /usr/local/bin/spitbg /usr/local/bin/spitbg_conf.json /usr/local/bin/config_gui.py
```

## Usage:

Usage: spitbg

Options:
  
  -h, --help    Show help message and exit
  
  -c, --config  Opens config file editor in GUI mode to easily edit your config file

