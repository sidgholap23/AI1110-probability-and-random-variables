import random
import pygame


def play_songs(songs):
    pygame.mixer.init()

    while True:
        # Shuffle the songs list in a random order
        random.shuffle(songs)

        for song in songs:
            print("Now playing:", song)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                user_input = input("Press 'n' to play the next song: ")
                if user_input.lower() == 'n':
                    pygame.mixer.music.stop()
                    break

        # Ask the user to play the songs again
        input("Press Enter to play the songs again...")


# List of song file paths
songs = [
    "/home/siddhesh/Desktop/ringtones/audio1.mp3",
    "/home/siddhesh/Desktop/ringtones/audio2.mp3",
    "/home/siddhesh/Desktop/ringtones/audio3.mp3",
    "/home/siddhesh/Desktop/ringtones/audio4.mp3",
    "/home/siddhesh/Desktop/ringtones/audio5.mp3",
    "/home/siddhesh/Desktop/ringtones/audio6.mp3",
    "/home/siddhesh/Desktop/ringtones/audio7.mp3",
    "/home/siddhesh/Desktop/ringtones/audio8.mp3",
    "/home/siddhesh/Desktop/ringtones/audio9.mp3",
    "/home/siddhesh/Desktop/ringtones/audio10.mp3",
    "/home/siddhesh/Desktop/ringtones/audio11.mp3",
    "/home/siddhesh/Desktop/ringtones/audio12.mp3",
    "/home/siddhesh/Desktop/ringtones/audio13.mp3",
    "/home/siddhesh/Desktop/ringtones/audio14.mp3",
    "/home/siddhesh/Desktop/ringtones/audio15.mp3",
    "/home/siddhesh/Desktop/ringtones/audio16.mp3",
    "/home/siddhesh/Desktop/ringtones/audio17.mp3",
    "/home/siddhesh/Desktop/ringtones/audio18.mp3",
    "/home/siddhesh/Desktop/ringtones/audio19.mp3",
    "/home/siddhesh/Desktop/ringtones/audio20.mp3"
]

# Play the songs infinitely
while True:
    play_songs(songs)

