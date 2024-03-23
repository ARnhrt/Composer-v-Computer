"""Random Music Generator 
Author: Addison Rinehart
Date: 3/20/24
Description: program will randomly generate a song by picking the
 -Key
      -Starting Note
      -Major/Minor
      -Sharp/Flat/Neutral
 -Chord Progression
      -Numeric Value (in scale)
      *Major/Minor is not generated, but displayed according to a selection structure
 -Notes
      -Numeric Value (in scale)
      -Length
Theoretically, this could be more random, but I don't know how to do that."""

#random.randint(x,y)
import random

#Variables
MEASURES = 4
COUNTS = 3
BEATS = MEASURES * COUNTS #constant

#Functions
def chordChooser(): 
    print("\nChord Progression:")
    j = 0
    chordChoice = [1, 2, 3, 4, 5, 6, 7, 8]

    for j in range(MEASURES):
        chord = random.choice(chordChoice)
        print(chord, end = " ")
        if (mm == "Major"):
            if (chord == 1)or(chord == 4) or(chord == 5):
                print("Major")
            elif (chord == 7):
                print("Diminished")
            else:
                print("Minor")
        else:
            if (chord == 1) or (chord == 4) or(chord == 5):
                print("Minor")
            elif (chord == 2):
                print("Diminished")
            else:
                print("Major")

def melody():
    #Melody Sequence
    more = "yes"
    while (more == "yes"):
        beats = BEATS #changing
        
        #rhythm
        rhythmChoice = [0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0]
        totals = []
        iterations = 0 
        
        count = 0
        print("\n\nNote length: ")
        while (0 < beats):
            temp = random.choice(rhythmChoice)
            beats -= temp
            count +=temp
            totals.append(count)
            if (count > BEATS):
                temp = BEATS - totals[iterations-1]
                count = BEATS
                beats = 0
            print(temp, end="; ")
            iterations +=1
        
        
        
        #sequence
        i = 0
        print("\n\nNote Sequence: ")
        for i in range(iterations):
            #notes
            scalePos = [0,1,2,3,4,5,6,7,8] #position in scale. 0 = rest
            note = random.choice(scalePos)
            print(note, end="; ")
            
            
            
        more = input("\n\nGenerate another measure? ").lower()

#Print starting text
input("***Welcome to Random Music Generator(working title)!*** \nPress anything to start!")
print()

#Key
##starting note
snChoice = ["A", "B", "C", "D", "E", "F", "G"]
startingNote = random.choice(snChoice)

##M/m
mmChoice = ["Major", "Minor"]
mm = random.choice(mmChoice)

##accidentals
accChoice = ["Sharp", "Flat", "Natural"]
accidental = random.choice(accChoice)

print("Key:", startingNote, accidental, mm)

##Menu
choice = ""
while (choice != "quit"):
    print()
    choice = input("Type 'Chords' to generate a random chord progression \nType 'Melody' to generate a random melody \nType 'Quit' to end program\n").lower()
    if (choice == "chords"):
        chordChooser()
        
    elif (choice=="melody"):
        melody()
    
    elif (choice == "quit"):
        break
    
    else:
        print("Invalid input. Please try again.")



print("\nfine")
    

