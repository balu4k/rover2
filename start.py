# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import motorcontrol as motorcontrol

# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
dc = 50  # set dc variable to 0 for 0%

motorcontrol.start(GPIO, dc)
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break

        elif char == curses.KEY_UP:
            motorcontrol.forward(GPIO)
            print "up"

        elif char == curses.KEY_DOWN:
            motorcontrol.reverse(GPIO)
            print "down"

        elif char == curses.KEY_RIGHT:
            motorcontrol.right(GPIO)
            print "right"

        elif char == curses.KEY_LEFT:
            motorcontrol.left(GPIO)
            print "left"

        elif char == 10:
            motorcontrol.stop(GPIO)
            print "stop"

        elif char == 275:
            dc = dc + 5
            motorcontrol.changespeed(GPIO, dc)
            print "speeding up" , dc

        elif char == 276:
            dc = dc - 5
            motorcontrol.changespeed(GPIO, dc)
            print "speeding down" , dc

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
