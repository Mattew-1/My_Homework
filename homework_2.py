def a():
    ev3.speaker.set_speech_options("en")
    ev3.speaker.say("melodies №1")
    ev3.speaker.play_notes(["G4/4",'E4/2','E4/4','B4/4','B4/4','B4/4','B4/4','D4/8','D4/4','D4/4','D4/4','E4/4'])
def b(num):
    ev3.speaker.set_speech_options("en")
    ev3.speaker.say("melodies №2")
    for i in range(num)
        ev3.speaker.play_notes(["G4/4","E4/4",'G4/4','B4/4','E4/4','B4/4','G4/4','E4/4','G4/4','B4/4','E4/4','B4/4',"G4/4"])
a()
b(2)
