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

- Run radio as a systemd service (configurated to /srv/pycecast-radioradio path with venv called venv)

```
sudo cp resources/radio.service /etc/systemd/system/
sudo systemctl enable radio
```

## Icecast instalation

To install icecast follow [this](https://github.com/xiph/Icecast-Server#buildinstall). Included directory `resources/radio` is used by default for icecast, in order to run it either:

- Run icecast localy in terminal

```
icecast -c /srv/pycecast-radio/resources/radio/conf/icecast.xml
```

or

- Run icecast as a systemd service (configurated to /srv/pycecast-radioradio path) as well

```
sudo cp resources/icecast.service /etc/systemd/system/
sudo systemctl enable icecast
```

## Configuration

In order for both to work correctly you will need to make their configuration files. There are examples included.

### Icecast

Edit file `resources/radio/conf/icecast-example.xml` to your liking and rename it to `icecast.xml`. Set `hostname` depending on if you are gonna use some reverse proxy like nginx to either `127.0.0.1` or the real access IP address.

### pycecast

Edit file `config/config-example.json` to your liking and rename it to `config.json`. Be sure to fill same values for hostname, port and password as in Icecast config, pycecast will use source password from icecast configuration.

### accounts

Both service file use the account `icecast` for their work. It is recommended to make that account with for example following command

```
sudo useradd -m icecast -s /usr/sbin/nologin -g icecast
```

You will have to then change ownership of icecast directory to this account with

```
sudo chown -R icecast:icecast resources/radio
```

be sure that audio files used by python process are accessible from this account. You can make them accessible just for the icecast group.

## Read the docs

* [Icecast](https://icecast.org/docs/)

## License

This project is licensed under the GNU GPL v.3 License.
