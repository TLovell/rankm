import curses

class Merge:


    def __init__(self, seperate_files, merge_file):

        self.slists = []
        for f in seperate_files:
            self.slists.append(f.readlines())
        
        self.mlist = []
        self.ops = []
    
    def main_loop(self, scr):
        while True:
            scr.clear()
            scr.addstr(1, len(self.slists) + 1, 'Which item goes next?')
            for i in range(len(self.slists)):
                scr.addstr(1, len(self.slists) - i, '[%d] %s' % (i, self.slists[i][0]))
        
            for i in range(len(self.mlist)):
                scr.addstr(1, len(self.slists) + 2 + len(self.mlist) - i, self.mlist[i])
        
            scr.refresh()

            c = scr.getch()
            if c == ord('q'):
                break


    def choose(self):
        pass
    
    def undo(self):
        pass
