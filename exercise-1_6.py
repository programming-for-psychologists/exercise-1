import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

square.draw()
win.flip()
core.wait(1.0)
square.setOri(45)
square.draw()
win.flip()
core.wait(1.0)


win.close()
sys.exit()

#------------------------------------------------------------------------------
# 1 Make the square red instead of blue
# 2 Make the square appear for 1.5 secs.
# 3 Show a red square for 1 s, then switch it to blue and show it for 1 s
# 4 Make the square appear for 1.5 secs, then show a blank screen for 1 sec, then flash the square 3 times for 30 ms each.
# 5 Show the following sequence: blue, red, blue, red, blue, red (with each square appearing for 1 s with a 50 ms blank screen in the middle).
# 6 Show a red square for 1 s then change its orientation by 45-deg
# 7 Now make a square rotate continuously, one full revolution (360 degrees) per second
# 8 Make a rotating square stop rotating when you press the 's' key
# 9 Make a square stop rotating when you press 's' and then start rotating again when you press 'r'
# 10 Display a blue square and increase its width (making it a rectangle) by 10 pixels whenever the user presses the left-arrow key. Decrease the width by 10 pixels when the user presses the right-arrow key
# 11 Make the rectangle decrease/increase its width by 10% of its current width with each keypress instead of 10 pixels
# 12 Show two rotating squares simultaneously, one left of center rotating clockwise, the other right of center, rotating counterclockwise
# 13 As time allows, do something that's not listed here (e.g., make it a pentagon instead of a square, make it pulsate, play a sound as it moves, bounce off walls.. be creative.
#------------------------------------------------------------------------------


