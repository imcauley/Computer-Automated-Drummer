from midiutil import MIDIFile

degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
track    = 0
channel  = 10
time     = 0   # In beats
duration = 0.0625   # In beats
tempo    = 140  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,time, tempo)

hat = 44
for time_step in range (0,64):
    MyMIDI.addNote(track, channel, hat, (time_step*0.25), duration, volume)

duration = 0.125
kick = 36
for time_step in range (0,16, 2):
    MyMIDI.addNote(track, channel, kick, (time_step), duration, volume)

kick = 38
for time_step in range (1,18, 2):
    MyMIDI.addNote(track, channel, kick, (time_step), duration, volume)

with open("major-scale3.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
