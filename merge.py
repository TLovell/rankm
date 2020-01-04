import curses

class Merge:
        
    slists = []
    mlist = []
    ops = []

    def __init__(seperate_files, merge_file):
        self.scr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        scr.keypad(True)

        self.slists = []
        for f in seperate_files:
            self.slists.append(f.readlines())
        
        self.mlist = []
        self.ops = []
    
    def main_loop():
        scr.clear()
        scr.addstr(1, len(slists) + 1, 'Which item goes next?')
        for i in range(len(slists)):
            scr.addstr(1, len(slists) - i, '[%d] %s' % (i, slists[i][0]))
    
        for i in range(len(mlist)):
            scr.addstr(1, len(slists) + 2 + len(mlist) - i, mlist[i])
    
        scr.refresh()

        


    def choose():
        pass
    
    def undo():
        pass
    
    def close()
        curses.nocbreak()
        scr.keypad(False)
        curses.echo()
        curses.endwin()
