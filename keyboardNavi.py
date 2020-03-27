# import curses
import curses

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
print "waiting for keyboard"

try:
    while True:
        char = screen.getch()
        print char
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print "up"
        elif char == curses.KEY_DOWN:
            print "down"
        elif char == curses.KEY_RIGHT:
            print "right"
        elif char == curses.KEY_LEFT:
            print "left"
        elif char == 10:
            print "stop"
        elif char == 275:
            print "speeding up"
        elif char == 276:
            print "speeding down"


finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
