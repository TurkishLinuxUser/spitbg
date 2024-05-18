# SpitBG
SpitBG is a simple but very functional tool for automatically making backgrounds out of the photos you specify at the times you previously saved in the config file. For example, you have 2 photos of a mountain taken at sunrise and sunset. You may want to have the sunrise photo in the background from sunrise to sunset and the sunset photo in the background after sunset until sunrise. With this tool you can do it easily.

## Installation
### Linux

Download Curl or Wget first

**Fedora and Others:**

Curl:
```
sudo yum install curl

or

sudo dnf install curl
```

Wget:
```
sudo yum install wget

or

sudo dnf install wget
```

**Ubuntu/Debian**

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
sudo curl -o /usr/bin/spitbg https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg && sudo mkdir -p ~/.config/spitbg && sudo curl -o ~/.config/spitbg/conf.json https://github.com/TurkishLinuxUser/spitbg/raw/main/conf.json && sudo chmod +x /usr/bin/spitbg ~/.config/spitbg/conf.json
```

Download with Wget:
```
sudo wget -O /usr/bin/spitbg https://github.com/TurkishLinuxUser/spitbg/raw/main/spitbg && sudo mkdir -p ~/.config/spitbg && sudo wget -O ~/.config/spitbg/conf.json https://github.com/TurkishLinuxUser/spitbg/raw/main/conf.json && sudo chmod +x /usr/bin/spitbg ~/.config/spitbg/conf.json
```

