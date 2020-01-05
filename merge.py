import curses

numrow = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def rowget(index):
    return numrow[index]

class Merge:

    def __init__(self, seperate_files, merge_file):

        self.slists = []
        for f in seperate_files:
            self.slists.append(f.readlines())
        
        self.merge_file = merge_file

        self.mlist = []
        self.ops = []
        self.written_ops = 0
    
    def main_loop(self, stdscr):
        while True:
            options = self.draw(stdscr)
            if not self.get_input(stdscr):
                break

    def draw(self, stdscr):
        stdscr.clear()
        height,width = stdscr.getmaxyx()
        
        stdscr.addstr(height - len(self.slists) - 2, 0, 'Which item goes next?  [u] undo  [q] quit  [w] write')
        stdscr.addstr(height - 1, width - 25, self.get_status())

        options = self.get_options()
        for i in range(len(self.slists)):
            y = height - len(self.slists) - 1 + i
            if i in options:
                stdscr.addstr(y, 2, '[%d] %s' % (numrow[i], self.slists[i][0]))
            else:
                stdscr.addstr(y, 2, '~%d~' % numrow[i])

        for i in range(len(self.mlist)):
            stdscr.addstr(height - len(self.slists) - 4 - len(self.mlist) + i, 0, '%d. %s' % (i + 1, self.mlist[i]))

        stdscr.refresh()

        return options

    def get_input(self, stdscr):
        c = stdscr.getch()
        options = self.get_options()
        cont = True
        if c == ord('q'):
            cont = False
        elif c == ord('u'):
            self.undo()
        elif c == ord('w'):
            self.write()
        elif c in list(map(ord, map(str, map(rowget, options)))):
            self.choose(numrow.index(int(chr(c))))
        return cont

    def get_options(self):
        options = []
        for i in range(len(self.slists)):
            if len(self.slists[i]) > 0:
                options.append(i)

        return options

    def get_status(self):
        stati = ['-Unsaved changes', '-No changes since save']
        return stati[len(self.ops) == self.written_ops]

    def choose(self, c):
        self.mlist.append(self.slists[c].pop(0))

        def inverse():
            self.slists[c].insert(0, self.mlist.pop())
        self.ops.append(inverse)
    
    def undo(self):
        if len(self.ops) > 0:
            self.ops.pop()()

    def write(self):
        self.merge_file.writelines(self.mlist)
        self.written_ops = len(self.ops)
