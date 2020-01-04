import curses

numrow = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def ordchr(num):
    return ord(str(num))

class Merge:

    def __init__(self, seperate_files, merge_file):

        self.slists = []
        for f in seperate_files:
            self.slists.append(f.readlines())
        
        self.mlist = []
        self.ops = []
    
    def main_loop(self, stdscr):
        while True:
            stdscr.clear()
            height,width = stdscr.getmaxyx()
            
            available = []
            for i in range(len(self.slists)):
                y = height - len(self.slists) - 1 + i
                if len(self.slists[i]) > 0:
                    stdscr.addstr(height - len(self.slists) - 1 + i, 2, '[%d] %s' % (numrow[i], self.slists[i][0]))
                    available.append(numrow[i])
                else:
                    stdscr.addstr(y, 2, '~%d~' % numrow[i])
            stdscr.addstr(height - len(self.slists) - 2, 0, 'Which item goes next?  [u] undo  [q] quit')
        
            for i in range(len(self.mlist)):
                stdscr.addstr(height - len(self.slists) - 4 - len(self.mlist) + i, 0, self.mlist[i])
        
            stdscr.refresh()

            c = stdscr.getch()
            if c == ord('q'):
                break
            elif c == ord('u'):
                self.undo()
            elif c in list(map(ordchr, available)):
                self.choose(numrow.index(int(chr(c))))


    def choose(self, c):
        self.mlist.append(self.slists[c].pop(0))
        self.ops.append(c)
    
    def undo(self):
        if len(self.ops) > 0:
            self.slists[self.ops.pop()].insert(0, self.mlist.pop())
