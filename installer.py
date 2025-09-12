import curses
import os
import time

def clear_screen(stdscr):
    stdscr.clear()
    stdscr.refresh()

def print_centered(stdscr, text, row):
    # Texti terminalde ortalayarak yazdırır.
    cols = curses.COLS
    x = cols // 2 - len(text) // 2
    stdscr.addstr(row, x, text)

def install_package(stdscr):
    clear_screen(stdscr)
    print_centered(stdscr, "Installing package...", 1)
    stdscr.refresh()
    time.sleep(2)  # Simulate installation time
    stdscr.clear()
    print_centered(stdscr, "Package installed successfully!", 1)
    stdscr.refresh()
    time.sleep(2)

def show_main_menu(stdscr):
    clear_screen(stdscr)
    print_centered(stdscr, "Welcome to Spy in Cigarette Installer", 0)
    print_centered(stdscr, "Select an option:", 2)
    
    options = ["Install", "Exit"]
    
    for i, option in enumerate(options, start=4):
        print_centered(stdscr, f"{i}. {option}", i)
    
    while True:
        key = stdscr.getch()
        
        if key == ord('1'):  # Install option
            install_package(stdscr)
            return
        elif key == ord('2'):  # Exit option
            break

def main(stdscr):
    curses.curs_set(0)  # Cursor'ü gizler
    stdscr.timeout(100)  # Timeout'u ayarlayarak hızlı bir şekilde hareket etmeyi sağlar
    show_main_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
