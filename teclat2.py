
import winsound
import keyboard
import time 

octava1 = {                                          # Frequencies
    "A": 261, #DO
    "S": 293, #RE
    "D": 329, #MI
    "F": 349, #FA
    "G": 393, #SOL
    "H": 440, #LA
    "J": 493  #SI
}


estat = {t: False for t in octava1}

print("tecles: A S D F G H J")

while True:                                           # Key Down
    for tecla in octava1:
        premuda = keyboard.is_pressed(tecla)
         
         
        if premuda and not estat[tecla]:
            winsound.Beep(octava1[tecla], 500)
            estat[tecla] = True
                                                       # Key Up
        elif not premuda and estat[tecla]:
            estat[tecla] = False

    time.sleep(0.1)                                   