# pycecast-radio

Python code I use to stream .mp3 files from specified directory to icecast using [python-shout](https://github.com/yomguy/python-shout) library

<p align="center">
  <img src="https://img.shields.io/github/workflow/status/bastakka/pycecast-radio/Pylint?style=for-the-badge" alt="Build"/>
  <img src="https://img.shields.io/github/license/bastakka/pycecast-radio?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge" alt="Python"/>
  <img src="https://img.shields.io/badge/code%20style-black-black?style=for-the-badge" alt="Black" />
</p>

## Instalation

- Clone this repository preferebly to `/srv`

```
cd /srv
git clone https://github.com/bastakka/pycecast-radio.git && cd pycecast-radio
```

- Install apt & pip requiremenets (venv recommended)

```
apt install libshout3-dev
pip install -r requirements.txt
```

- Run radio localy in terminal

```
python3 radio.py
```

or

- Run radio as a systemd service. Service is configurated to /srv/pycecast-radioradio path with python venv called venv and to run after and with icecast service.

```
sudo cp resources/radio.service /etc/systemd/system/
sudo systemctl enable radio
```

## Icecast instalation

To install icecast follow [this](https://www.atlantic.net/dedicated-server-hosting/how-to-install-icecast-audio-streaming-server-on-ubuntu-20-04/).

## Configuration

In order for pycecast to work correctly you will need to make its configuration file. There is an example included.

### pycecast

Edit file `config/config-example.json` to your liking and rename it to `config.json`. Be sure to fill same values for hostname, port and password as in Icecast config, pycecast will use source password from icecast configuration.

## Read the docs

* [Icecast](https://icecast.org/docs/)

## License

This project is licensed under the GNU GPL v.3 License.
