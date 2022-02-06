import random
import sys
import shout
from threading import Thread
from glob import glob
from random import shuffle

from core.config import get_config
from core.logger import get_logger


class StreamThread(Thread):
    def __init__(
        self,
        stream_index,
        music_directory,
        station_url,
        genre,
        name,
        description
    ):
        # connection to icecast
        self.shout = shout.Shout()
        self.shout.audio_info = {
            shout.SHOUT_AI_BITRATE: "128",
            shout.SHOUT_AI_SAMPLERATE: "44100",
            shout.SHOUT_AI_CHANNELS: "5",
        }
        self.shout.format = "mp3"  # using mp3 but it can also be ogg vorbis
        self.shout.genre = genre
        self.ogv = 0

        self.config = get_config()
        self.shout.host = self.config.hostname
        self.shout.port = self.config.port
        self.shout.password = self.config.password
        self.shout.mount = stream_index

        self.logger = get_logger(name)

        self.shout.name = name
        self.shout.url = station_url
        self.music_directory = music_directory
        self.shout.description = description
        self.song_conter = 0

        self.shout.open()
        Thread.__init__(self)

    # checking directories for files to stream
    def scan_directories(self):
        self.files_array = glob(self.music_directory + "/*.[mM][Pp]3")
        if len(self.files_array) == 0:
            self.logger.error("Found %i audio files. Exiting.", len(self.files_array))
            sys.exit(1)
        else:
            self.logger.info("Found %i audio files", len(self.files_array))
        shuffle(self.files_array)  # randomize playlist

        self.info_spots = glob(self.music_directory + "/spots/*.[mM][Pp]3")
        self.logger.info("Found %i info spot files", len(self.info_spots))

        self.adverts = glob(self.music_directory + "/adverts/*.[mM][Pp]3")
        self.logger.info("Found %i advert files", len(self.adverts))

    def run(self):
        while True:  # infinity
            self.scan_directories()  # rescan dir, maybe in time you add some new songs
            self.song_counter = 0
            for audio_file in self.files_array:
                self.sendaudio(audio_file)
                if len(self.info_spots) > 0:
                    self.sendaudio(random.choice(self.info_spots))
                if len(self.adverts) > 2 and self.song_conter % 5 == 0:
                    sent = []
                    for i in range(0, 3):
                        advert = random.choice(self.adverts)
                        while advert in sent:
                            advert = random.choice(self.adverts)
                        self.sendaudio(advert)
                        sent.append(advert)
                    self.sendaudio(random.choice(self.info_spots))
                self.song_counter += 1
                    
    def format_songname(self, song):
        """
        Format song name from filename
        strips "mp3" and changes _ to " "
        Used for metadata
        """
        result = song.split("/")[-1].split(".")
        result = (
            ".".join(result[:len(result) - 1]).replace("_", " ").replace("-", " - ")
        )
        return result

    def sendaudio(self, audio_file):
        self.logger.info("Playing file %s" % str(audio_file))
        temp = open(audio_file, "rb")
        self.shout.set_metadata({"song": self.format_songname(audio_file)})
        new_buffer = temp.read(4096)
        while len(new_buffer) != 0:
            buffer = new_buffer
            new_buffer = temp.read(4096)
            self.shout.send(buffer)
            self.shout.sync()
        temp.close()
