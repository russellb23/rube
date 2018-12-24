#!/usr/bin/env python3.6
###############################################################################
# Play songs in a directory using 'mplayer'                                   #
# Manual: Choose songs one by one                                             #
# Automatic: Plays sequentially in the order present in the directory         #
# Shuffle: Plays song in random order                                         #
# Choose: TODO: Create the song order in which chosen songs will be played    #
# Author: Russell Bert (C) Dec 2018                                           #
###############################################################################
# Import required modules
import os, subprocess, sys, random
## Source directory of songs
src = sys.argv[1]
songs = os.listdir(str(src))
# Prompt user for the mode of play
mode = input("[M]anual/[A]utomatic/[S]huffle:\n")
# Playing logic
if mode.lower() == 'm':
    count = 1
    while count <= len(songs):
        for idx, song in enumerate(songs):
            print('['+(str(idx)+']'+':\t'+song))
        song_id = input("Song ID: ")
        if song_id.lower() == 'q':
            sys.exit(0)
        song_play = subprocess.Popen(['mplayer', str(src)+songs[int(song_id)]])
        song_play.wait()
        count += 1
elif mode.lower() == 'a':
    for song in songs:
        song_play = subprocess.Popen(['mplayer', str(src)+'/'+str(song)])
        song_play.wait()
elif mode.lower() == 's':
    count = 1
    while count <= len(songs):
        song = random.choice(songs)
        song_play = subprocess.Popen(['mplayer', str(src)+'/'+str(song)])
        song_play.wait()
        count += 1
else:
    print("Please choose a mode")
# Logic execution
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting")
        sys.exit(0)
