import pygame
import os
import random
from pathlib import Path

class MusicPlayer:
    def __init__(self, music_dir="music"):
        pygame.mixer.init()
        self.music_dir = self.__create_music_folder(music_dir)
        self.tracks = list(self.music_dir.glob("**/*.mp3"))
                    #   list(self.music_dir.glob("**/*.flac")) + \
                    #   list(self.music_dir.glob("**/*.wav"))
        self.current = 0
        self.is_playing = False

    def play(self, query=None):
        if not self.tracks:
            return "Музыка не найдена"
        
        if query:
            # Поиск по названию
            query = query.lower()
            found = [t for t in self.tracks if query in t.name.lower()]
            if found:
                track = random.choice(found)
            else:
                track = random.choice(self.tracks)
        else:
            track = random.choice(self.tracks)
            
        pygame.mixer.music.load(str(track))
        pygame.mixer.music.play()
        self.is_playing = True
        return f"Играю: {track.name}"

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def pause(self):
        pygame.mixer.music.pause()
        self.is_playing = False

    def unpause(self):
        pygame.mixer.music.unpause()
        self.is_playing = True

    def next(self):
        self.stop()
        self.current = (self.current + 1) % len(self.tracks)
        pygame.mixer.music.load(str(self.tracks[self.current]))
        pygame.mixer.music.play()
        return f"Следующий: {self.tracks[self.current].name}"

    def volume(self, level):  # 0.0 - 1.0
        pygame.mixer.music.set_volume(level)

    @staticmethod
    def __create_music_folder(folder_name: str) -> Path:
        os.makedirs(folder_name, exist_ok=True)
        return Path(folder_name)