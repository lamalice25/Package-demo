from Instructions import Pybot2
from Instructions import Pybot1
from Instructions.voice import droid

exec_code = input("quel code voulais vous executer  : ")

if "pybot1" in exec_code:
    Pybot1.Pybot_chat()

elif "pybot2" in exec_code:
    Pybot2.pybot2()
    

else:
    droid.say("Nous arrivons pas a ouvrir les données")
    droid.runAndWait()
    print("rtfm : read the fucking manuel, voir readme")