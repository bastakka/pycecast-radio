# pycecast-radio
Python code I use to stream .mp3 files from specified directory to icecast using [python-shout](https://github.com/yomguy/python-shout) library

<p align="center">
  <img src="https://img.shields.io/github/workflow/status/bastakka/pycecast-radio/Pylint?style=for-the-badge" alt="Build"/>
  <img src="https://img.shields.io/github/license/bastakka/pycecast-radio?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge" alt="Python"/>
  <img src="https://img.shields.io/badge/code%20style-black-black?style=for-the-badge" alt="Black" />
</p>

## Instalation

- Clone this repository
```
git clone https://github.com/bastakka/pycecast-radio.git && cd Coco-bot
```
- Install pip requiremenets (venv recommended)
```
pip install -r requirements.txt
```
- Run radio localy in terminal
```
python3 radio.py
```
or
- Run radio as a systemd service (configurated to /srv/radio path with venv called venv)
```
sudo cp resources/radio.service /etc/systemd/system/
sudo systemctl enable radio
```
## License
This project is licensed under the GNU GPL v.3 License.