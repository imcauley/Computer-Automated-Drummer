#!/usr/bin/env python3

from midiutil import MIDIFile
import sys
import highhat
import kick
import snare
import clap

track    = 0
channel  = 10
tempo    = 140  # In BPM

MyMIDI = MIDIFile(1, adjust_origin=False) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,0, tempo)

instruments = []
instruments.append(highhat.Highhat())
instruments.append(kick.Kick())
instruments.append(snare.Snare())
instruments.append(clap.Clap())


time = 0
while(time < 4):
    for instrument in instruments:
        if(instrument.play(time)):
            MyMIDI.addNote(track, channel, instrument.sound,
            time, instrument.duration, instrument.volume)

    time = time + 0.25

if(sys.argv[1] != ""):
    with open(sys.argv[1], "wb") as output_file:
        MyMIDI.writeFile(output_file)
