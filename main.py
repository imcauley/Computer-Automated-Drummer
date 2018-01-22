from midiutil import MIDIFile
import highhat
import kick
import snare
import clap

track    = 0
channel  = 10
tempo    = 140  # In BPM

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,0, tempo)

hh = highhat.Highhat()
kc = kick.Kick()
sn = snare.Snare()
cp = clap.Clap()

time = 0
while(time < 4):
    if(hh.play(time)):
        MyMIDI.addNote(track, channel, hh.sound, time, hh.duration, hh.volume)
    if(kc.play(time)):
        MyMIDI.addNote(track, channel, kc.sound, time, kc.duration, kc.volume)
    if(sn.play(time)):
        MyMIDI.addNote(track, channel, sn.sound, time, sn.duration, sn.volume)
    if(cp.play(time)):
        MyMIDI.addNote(track, channel, cp.sound, time, cp.duration, cp.volume)

    time = time + 0.25

with open("test1.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
