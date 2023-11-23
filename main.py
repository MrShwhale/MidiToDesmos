import mido
import sys

# Function from https://github.com/AlexApps99/MIDI2Desmos/blob/master/graph.py
def mid_to_hz(d):
	# Formula from Wikipedia
	return (2 ** ((d - 69) / 12)) * 440

def main(input_file: str, output_file: str):
    midi = mido.MidiFile(input_file, clip=True)

    print(f"Tracks: {len(midi.tracks)}")
    # Create a list of notes for each track, with the second they are played and the length
    song = []
    for track in midi.tracks:
        song_track = [[] for _ in range(0,16)]
        on_notes = [False for _ in range(0,16)]
        starts = [0 for _ in range(0,16)]
        notes = [0 for _ in range(0,16)]
        velocities = [0 for _ in range(0,16)]
        time = 0
        tempo = 500000
        # For the purposes of this:
        # Ignore different instruments. This will be bad, since no variety, but idc its hard
        # Velocity should be converted to the gain value
        
        print(midi.ticks_per_beat)

        # For now, just try to get something that will play the notes with no fancy stuff
        print("Starting new track")
        for message in track:
            if isinstance(message, mido.MetaMessage):
                if message.type == "set_tempo":
                    print(f"Changing tempo from {tempo} to {message.tempo}")
                    tempo = message.tempo
                continue

            time += message.time
            if message.type == "sysex":
                continue

            channel = message.channel
            # Go through each channel
            if message.type == "note_off" or (message.type == "note_on" and message.velocity == 0):
                on_notes[channel] = False
                song_track[channel].append((mido.tick2second(starts[channel], midi.ticks_per_beat, tempo), mido.tick2second(time, midi.ticks_per_beat, tempo), notes[channel], velocities[channel]))
            elif message.type == "note_on":
                on_notes[channel] = True
                notes[channel] = message.note
                starts[channel] = time
                velocities[channel] = message.velocity

        song.append(song_track)

    table_string = ""

    for track in song:
        for channel in track:
            if len(channel) > 1:
                print("New Channel")
            for note in channel:
                # Ideal form: start time (s), end time (s), pitch (hz), volume (0-1)
                table_string += f"{note[0]}\t{note[1]}\t{mid_to_hz(note[2])}\t{note[3]/127}\n"
                 
    with open(output_file, "w") as f:
        f.write(table_string)


if __name__ == "__main__":
    midi_arg = sys.argv[1]
    output_arg = sys.argv[2]
    main(midi_arg, output_arg)
