import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the Speed Typing Test!')
    stdscr.addstr('\nPress any key to begin!')
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(0, 0, f"WPM: {wpm}")
    stdscr.addstr(2, 0, target)

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # Green for correct
        if char != correct_char:
            color = curses.color_pair(2)  # Red for incorrect
        stdscr.addstr(2, i, char, color)

def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text = []
    start_time = time.time()
    stdscr.nodelay(True)  # Non-blocking input mode

    while True:
        # Calculate elapsed time and WPM
        time_elapsed = max(time.time() - start_time, 1)  # Avoid divide by zero
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Check if the user has completed the text
        if ''.join(current_text) == target_text:
            stdscr.nodelay(False)  # Re-enable blocking input
            stdscr.addstr(4, 0, "You completed the text! Press any key to continue...")
            stdscr.refresh()
            stdscr.getkey()
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # ESC key to exit
            break

        if key in ('KEY_BACKSPACE', '\b', '\x7f'):  # Backspace keys
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            # Append valid characters to the current text
            current_text.append(key)

def main(stdscr):
    # Initialize color pairs for text display
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Correct input
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Incorrect input
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default text

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(6, 0, "Press ESC to quit or any other key to restart...")
        key = stdscr.getkey()
        if ord(key) == 27:  # ESC key to quit
            break

wrapper(main)
