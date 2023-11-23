# MidiToDesmos
Python script to convert MIDI files to Desmos tables for use with the new "tone" function.
# Use
Download and the script (make sure the mido python library is installed), passing in the .mid file as the first argument and the output text file as the second (this file does not have to exist, and will otherwise be overwritten)
Then, copy and paste the text file into Desmos. This will create a table, with the rows being as follows:
| x1                   | y1                 | z1             | u1                       |
| -------------------- | ------------------ | -------------- | ------------------------ |
| start time (seconds) | end time (seconds)  | pitch (hertz) | volume (between 0 and 1) |

To test this out with a simple player, and to see what mechanism may be used play these notes, check out this simple music player I made: https://www.desmos.com/calculator/v5pfuqawlc.
There are some more instructions in the "Player" folder on that. 

Alternatively, use this script to put music into this rythm game I made on Desmos: https://www.desmos.com/calculator/rhdkqxxk4v.
This uses a very similar player, this time in the "Music" folder.

# Notes
Since there are not distinctive instruments, this version may sound very bad depending on what instruments are used. Drums do not fare well.
The script may break when drums without "end" commands are loaded, or may not include them at all
