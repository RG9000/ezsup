import curses

class App:

    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)  # hide cursor
        self.stdscr.clear()
        self.stdscr.refresh()
        
        # A longer list of options for demonstration purposes
        self.options = ["Option " + str(i) for i in range(1, 100)]
        self.selected_options = []
        self.current_option_idx = 0
        self.top_visible_idx = 0

        # Create left panel window with border
        self.left_win_height = curses.LINES - 4  # minus borders and title
        self.left_win = curses.newwin(self.left_win_height + 2, 38, 1, 1)
        self.left_win.box()
        self.left_win.addstr(0, 2, 'Select log files for inclusion')

        # Create right panel window with border
        self.right_win = curses.newwin(curses.LINES - 2, 38, 1, 40)
        self.right_win.box()
        self.right_win.addstr(0, 10, 'Selected files')

    def draw(self):
        # Clear the windows
        self.left_win.clear()
        self.right_win.clear()
        self.left_win.box()
        self.right_win.box()
        self.left_win.addstr(0, 2, 'Select log files for inclusion')
        self.right_win.addstr(0, 10, 'Selected files')

        # Draw options on the left panel
        for idx in range(self.top_visible_idx, min(self.top_visible_idx + self.left_win_height, len(self.options))):
            mode = curses.A_REVERSE if idx == self.current_option_idx else curses.A_NORMAL
            self.left_win.addstr(idx - self.top_visible_idx + 1, 2, self.options[idx], mode)

        # Draw selected options on the right panel
        for idx, option in enumerate(self.selected_options):
            self.right_win.addstr(idx + 1, 2, option)

        self.left_win.refresh()
        self.right_win.refresh()

    def run(self):
        while True:
            self.draw()

            # Wait for user input
            key = self.stdscr.getch()

            if key == curses.KEY_DOWN and self.current_option_idx < len(self.options) - 1:
                self.current_option_idx += 1
                if self.current_option_idx >= self.top_visible_idx + self.left_win_height:
                    self.top_visible_idx += 1
            elif key == curses.KEY_UP and self.current_option_idx > 0:
                self.current_option_idx -= 1
                if self.current_option_idx < self.top_visible_idx:
                    self.top_visible_idx -= 1
            elif key == ord('\n'):  # Enter key
                if self.options[self.current_option_idx] not in self.selected_options:
                    self.selected_options.append(self.options[self.current_option_idx])
            elif key == ord('q'):
                break

def main(stdscr):
    app = App(stdscr)
    app.run()

if __name__ == "__main__":
    curses.wrapper(main)

