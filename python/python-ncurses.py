#!/usr/bin/env python
import curses, os, traceback

class CursedMenu(object):
    '''A class which abstracts the horrors of building a curses-based menu system'''

    def __init__(self):
        '''Initialization'''
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.screen.keypad(1)

        # Highlighted and Normal line definitions
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.highlighted = curses.color_pair(1)
        self.normal = curses.A_NORMAL


    def show(self, options, title="Title", subtitle="Subtitle"):
        '''Draws a menu with the given parameters'''
        self.set_options(options)
        self.title = title
        self.subtitle = subtitle
        self.selected = 0
        self.draw_menu()

    def set_options(self, options):
        '''Validates that the last option is "Exit"'''
        if options[-1] is not 'Exit':
            options.append('Exit')
        self.options = options

    def draw_menu(self):
        '''Actually draws the menu and handles branching'''
        request = ""
        try:
            while request is not "Exit":
                self.draw()
                request = self.get_user_input()
                self.handle_request(request)
            self.__exit__()

        # Also calls __exit__, but adds traceback after
        except Exception as exception:
            self.__exit__()
            traceback.print_exc()

    def draw(self):
        '''Draw the menu and lines'''
        self.screen.border(0)
        self.screen.addstr(2,2, self.title, curses.A_STANDOUT) # Title for this menu
        self.screen.addstr(4,2, self.subtitle, curses.A_BOLD) #Subtitle for this menu

        # Display all the menu items, showing the 'pos' item highlighted
        for index in range(len(self.options)):
            textstyle = self.normal
            if index == self.selected:
                textstyle = self.highlighted
            self.screen.addstr(5+index,4, "%d - %s" % (index+1, self.options[index]), textstyle)

        self.screen.refresh()

    def get_user_input(self):
        '''Gets the user's input and acts appropriately'''
        user_in = self.screen.getch() # Gets user input

        '''Enter and Exit Keys are special cases'''
        if user_in == 10:
            return self.options[self.selected]
        if user_in == 27:
            return self.options[-1]

        # This is a number; check to see if we can set it
        if user_in >= ord('1') and user_in <= ord(str(min(9,len(self.options)+1))):
            self.selected = user_in - ord('0') - 1 # convert keypress back to a number, then subtract 1 to get index
            return

        # Increment or Decrement
        if user_in == curses.KEY_DOWN: # down arrow
            self.selected += 1
        if user_in == curses.KEY_UP: # up arrow
            self.selected -=1
        self.selected = self.selected % len(self.options)
        return

    def handle_request(self, request):
        '''This is where you do things with the request'''
        if request is None: return

    def __exit__(self):
        curses.endwin()
        os.system('clear')


'''demo'''
cm = CursedMenu()
result = cm.show(['First','2nd','#3'], title='Demo Menu', subtitle='Options')
print result
#!/usr/bin/python
#
# Adapted from:
# http://blog.skeltonnetworks.com/2010/03/python-curses-custom-menu/
#
# Goncalo Gomes
# http://promisc.org
#

import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)

import os
import sys
import curses
import traceback
import atexit
import time

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class cmenu(object):
    datum = {}
    ordered = []
    pos = 0

    def __init__(self, options, title="python curses menu"):
        curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.curs_set(0)
        self.screen = curses.initscr()
        self.screen.keypad(1)

        self.h = curses.color_pair(1)
        self.n = curses.A_NORMAL

        for item in options:
            k, v = item.items()[0]
            self.datum[k] = v
            self.ordered.append(k)

        self.title = title

        atexit.register(self.cleanup)

    def cleanup(self):
        curses.doupdate()
        curses.endwin()

    def upKey(self):
        if self.pos == (len(self.ordered) - 1):
            self.pos = 0
        else:
            self.pos += 1

    def downKey(self):
        if self.pos <= 0:
            self.pos = len(self.ordered) - 1
        else:
            self.pos -= 1

    def display(self):
        screen = self.screen

        while True:
            screen.clear()
            screen.addstr(2, 2, self.title, curses.A_STANDOUT|curses.A_BOLD)
            screen.addstr(4, 2, "Please select an interface...", curses.A_BOLD)

            ckey = None
            func = None

            while ckey != ord('\n'):
                for n in range(0, len(self.ordered)):
                    optn = self.ordered[n]

                    if n != self.pos:
                        screen.addstr(5 + n, 4, "%d. %s" % (n, optn), self.n)
                    else:
                        screen.addstr(5 + n, 4, "%d. %s" % (n, optn), self.h)
                screen.refresh()

                ckey = screen.getch()

                if ckey == 258:
                    self.upKey()

                if ckey == 259:
                    self.downKey()

            ckey = 0
            self.cleanup()
            if self.pos >= 0 and self.pos < len(self.ordered):
                self.datum[self.ordered[self.pos]]()
                self.pos = -1
            else:
                curses.flash()



def top():
    os.system("top")

def exit():
    sys.exit(1)

def submenu():
    # c.screen.clear()     # nope
    # c.cleanup()          # nope
    submenu_list = [{"first": exit}, {"second": exit}, {"third": exit}]
    submenu = cmenu(submenu_list)
    submenu.display()

try:

    list = [{ "top": top }, {"Exit": exit}, {"Another menu": submenu}]

    c = cmenu(list)

    c.display()

except SystemExit:
    pass
else:
    #log(traceback.format_exc())
    c.cleanup()
#!/usr/bin/python
import time
import sys

def print_there(x, y, text):
  sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
  sys.stdout.flush()

while True:
    try:
        print_there(40, 20, str(time.time()))
    except KeyboardInterrupt: break

#!/usr/bin/python
import sys

try: 
  import npyscreen
except: 
  print "Missing npyscreen module. Do 'sudo pip install npyscreen' to install it."
  sys.exit(1)

class myEmployeeForm(npyscreen.Form):
  def afterEditing(self):
    self.parentApp.setNextForm(None)

  def create(self):
    self.myName       = self.add(npyscreen.TitleText, name='Name')
    self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
    self.myDate       = self.add(npyscreen.TitleDateCombo, name='Date Employed')

class MyApplication(npyscreen.NPSAppManaged):
  def onStart(self):
    self.addForm('MAIN', myEmployeeForm, name='Create Stack')
    # A real application might define more forms here.......


def main (args):
  TestApp = MyApplication().run()


if __name__ == '__main__':
  main(sys.argv)
#!/usr/bin/env python
# cm13

import npyscreen

class entryForm(npyscreen.NPSApp):
  def __init__(self, title, msg):
    self.title = title
    self.msg   = msg

  def main(self):
    F = npyscreen.Popup(name=self.msg)
    response = F.add(npyscreen.TitleText,name=self.title)
    F.edit()                            # Allow user to edit the form
    self.value = response.get_value()

class selectForm(npyscreen.NPSApp):
  def __init__(self, title, msg, optvals, defval):
    self.title   = title
    self.msg     = msg
    self.optvals = optvals
    self.defval  = defval

  def main(self):
    F = npyscreen.Popup(name=self.msg)
    response = F.add(
      npyscreen.TitleCombo,
      name   = self.title,
      values = self.optvals,
      value  = self.defval,
    )
    F.edit()                            # Allow user to edit the form
    self.value = response.get_value()


entry = entryForm("Stack Name","Enter stack name, no leading digits.")
entry.run()
print entry.value

entry = selectForm("InstanceType","Select instance type", ['t2.terminator','x1.cray','z4.ibm'], 0)
entry.run()
print entry.value

#!/usr/bin/env python                                                       

import curses                                                                
from curses import panel                                                     

class Menu(object):                                                          

    def __init__(self, items, stdscreen):                                    
        self.window = stdscreen.subwin(0,0)                                  
        self.window.keypad(1)                                                
        self.panel = panel.new_panel(self.window)                            
        self.panel.hide()                                                    
        panel.update_panels()                                                

        self.position = 0                                                    
        self.items = items                                                   
        self.items.append(('exit','exit'))                                   

    def navigate(self, n):                                                   
        self.position += n                                                   
        if self.position < 0:                                                
            self.position = 0                                                
        elif self.position >= len(self.items):                               
            self.position = len(self.items)-1                                

    def display(self):                                                       
        self.panel.top()                                                     
        self.panel.show()                                                    
        self.window.clear()                                                  

        while True:                                                          
            self.window.refresh()                                            
            curses.doupdate()                                                
            for index, item in enumerate(self.items):                        
                if index == self.position:                                   
                    mode = curses.A_REVERSE                                  
                else:                                                        
                    mode = curses.A_NORMAL                                   

                msg = '%d. %s' % (index, item[0])                            
                self.window.addstr(1+index, 1, msg, mode)                    

            key = self.window.getch()                                        

            if key in [curses.KEY_ENTER, ord('\n')]:                         
                if self.position == len(self.items)-1:                       
                    break                                                    
                else:                                                        
                    self.items[self.position][1]()                           

            elif key == curses.KEY_UP:                                       
                self.navigate(-1)                                            

            elif key == curses.KEY_DOWN:                                     
                self.navigate(1)                                             

        self.window.clear()                                                  
        self.panel.hide()                                                    
        panel.update_panels()                                                
        curses.doupdate()

class MyApp(object):                                                         

    def __init__(self, stdscreen):                                           
        self.screen = stdscreen                                              
        curses.curs_set(0)                                                   

        submenu_items = [                                                    
                ('beep', curses.beep),                                       
                ('flash', curses.flash)                                      
                ]                                                            
        submenu = Menu(submenu_items, self.screen)                           

        main_menu_items = [                                                  
                ('beep', curses.beep),                                       
                ('flash', curses.flash),                                     
                ('submenu', submenu.display)                                 
                ]                                                            
        main_menu = Menu(main_menu_items, self.screen)                       
        main_menu.display()                                                  

if __name__ == '__main__':                                                       
    curses.wrapper(MyApp) 
#!/usr/bin/env python

from os import system
import curses

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print ""
     if a == 0:
          print "Command executed correctly"
     else:
          print "Command terminated with error"
     raw_input("Press enter")
     print ""

x = 0

while x != ord('4'):
     screen = curses.initscr()

     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, "Please enter a number...")
     screen.addstr(4, 4, "1 - Add a user")
     screen.addstr(5, 4, "2 - Restart Apache")
     screen.addstr(6, 4, "3 - Show disk space")
     screen.addstr(7, 4, "4 - Exit")
     screen.refresh()

     x = screen.getch()

     if x == ord('1'):
          #username = get_param("Enter the username")
          #homedir = get_param("Enter the home directory, eg /home/nate")
          #groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
          #shell = get_param("Enter the shell, eg /bin/bash:")
          curses.endwin()
          #execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
          print chr(x)
          break
     if x == ord('2'):
          curses.endwin()
          print chr(x)
          break
          #execute_cmd("apachectl restart")
     if x == ord('3'):
          curses.endwin()
          print chr(x)
          break
          #execute_cmd("df -h")

curses.endwin()
#!/usr/bin/env python
# From https://github.com/NikolaiT/Scripts/blob/master/scripts/python/curses/text_selector.py
import sys, curses

# Author: Nikolai Tschacher
# Date: 02.06.2013

class BoxSelector:
    """ Originally designed for accman.py.
        Display options build from a list of strings in a (unix) terminal.
        The user can browser though the textboxes and select one with enter.
    """
    
    def __init__(self, L):
        """ Create a BoxSelector object. 
            L is a list of strings. Each string is used to build 
            a textbox.
        """
        self.L = L
        # Element parameters. Change them here.
        self.TEXTBOX_WIDTH = 50
        #self.TEXTBOX_HEIGHT = 6
        self.TEXTBOX_HEIGHT = 3

        self.PAD_WIDTH = 400
        self.PAD_HEIGHT = 10000
        
    def pick(self):
        """ Just run this when you want to spawn the selction process. """
        self._init_curses()
        self._create_pad()
        
        windows = self._make_textboxes()
        picked = self._select_textbox(windows)
        
        self._end_curses()
        
        return picked
        
    def _init_curses(self):
        """ Inits the curses appliation """
        # initscr() returns a window object representing the entire screen.
        self.stdscr = curses.initscr()
        # turn off automatic echoing of keys to the screen
        curses.noecho()
        # Enable non-blocking mode. Keys are read directly, without hitting enter.
        curses.cbreak()
        # Disable the mouse cursor.
        curses.curs_set(0)
        self.stdscr.keypad(1)
        # Enable colorous output.
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.stdscr.bkgd(curses.color_pair(2))
        self.stdscr.refresh()

    def _end_curses(self):
        """ Terminates the curses application. """
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()
        
    def _create_pad(self):
        """ Creates a big self.pad to place the textboxes in. """
        self.pad = curses.newpad(self.PAD_HEIGHT, self.PAD_WIDTH)
        self.pad.box()
        
    def _make_textboxes(self):
        """ Build the textboxes in the pad center and put them in the 
            horizontal middle of the pad. """
        # Get the actual screensize.
        maxy, maxx = self.stdscr.getmaxyx()
        
        windows = []
        i = 1
        for s in self.L:
            windows.append(self.pad.derwin(self.TEXTBOX_HEIGHT,
                    self.TEXTBOX_WIDTH, i, self.PAD_WIDTH//2-self.TEXTBOX_WIDTH//2))
            i += self.TEXTBOX_HEIGHT
            
        for k in range(len(windows)):
            windows[k].box()
            windows[k].addstr(4, 4, '0x{0:X} - {1}'.format(k, self.L[k]))
            
        return windows

    def _center_view(self, window):
        """ Centers and aligns the view according to the window argument given. 
            Returns the (y, x) coordinates of the centered window. """
        # The refresh() and noutrefresh() methods of a self.pad require 6 arguments
        # to specify the part of the self.pad to be displayed and the location on
        # the screen to be used for the display. The arguments are pminrow,
        # pmincol, sminrow, smincol, smaxrow, smaxcol; the p arguments refer
        # to the upper left corner of the self.pad region to be displayed and the
        # s arguments define a clipping box on the screen within which the
        # self.pad region is to be displayed.
        cy, cx = window.getbegyx()
        maxy, maxx = self.stdscr.getmaxyx()
        self.pad.refresh(cy, cx, 1, maxx//2 - self.TEXTBOX_WIDTH//2, maxy-1, maxx-1)
        return (cy, cx)
        
    def _select_textbox(self, windows):
        # See at the root textbox.
        topy, topx = self._center_view(windows[0])
        
        current_selected = 0
        last = 1
        top_textbox = windows[0]
        
        while True:
            # Highligth the selected one, the last selected textbox should
            # become normal again.
            windows[current_selected].bkgd(curses.color_pair(1))
            windows[last].bkgd(curses.color_pair(2))
            
            # While the textbox can be displayed on the page with the current 
            # top_textbox, don't alter the view. When this becomes impossible, 
            # center the view to last displayable textbox on the previous view.
            maxy, maxx = self.stdscr.getmaxyx()
            cy, cx = windows[current_selected].getbegyx()
            
            # The current window is to far down. Switch the top textbox.
            if ((topy + maxy - self.TEXTBOX_HEIGHT) <= cy):
                top_textbox = windows[current_selected]
            
            # The current window is to far up. There is a better way though...
            if topy >= cy + self.TEXTBOX_HEIGHT:
                top_textbox = windows[current_selected]
            
            if last != current_selected:
                last = current_selected
                
            topy, topx = self._center_view(top_textbox)
            
            c = self.stdscr.getch()
            
            # Vim like KEY_UP/KEY_DOWN with j(DOWN) and k(UP).
            if c == ord('j'):
                if current_selected >= len(windows)-1:
                    current_selected = 0 # wrap around.
                else:
                    current_selected += 1
            elif c == ord('k'):
                if current_selected <= 0:
                    current_selected = len(windows)-1 # wrap around.
                else:
                    current_selected -= 1
            elif c == ord('q'): # Quit without selecting.
                break
            # At hitting enter, return the index of the selected list element.
            elif c == curses.KEY_ENTER or c == 10:
                return int(current_selected)


def main (argv):
  choices = ['one','two','three','four','five']
  choice = BoxSelector(choices).pick()
  print "choices", choices
  print "choice", choice
  print "Your choice was %s" % (choices[choice])


if __name__ == '__main__':
  main(sys.argv)
#!/usr/bin/env python
import sys, curses, curses.textpad

def maketextbox(h,w,y,x,value="",deco=None,underlineChr=curses.ACS_HLINE,textColorpair=0,decoColorpair=0):
    nw = curses.newwin(h,w,y,x)
    txtbox = curses.textpad.Textbox(nw)
    if deco=="frame":
        screen.attron(decoColorpair)
        curses.textpad.rectangle(screen,y-1,x-1,y+h,x+w)
        screen.attroff(decoColorpair)
    elif deco=="underline":
        screen.hline(y+1,x,underlineChr,w,decoColorpair)

    nw.addstr(0,0,value,textColorpair)
    nw.attron(textColorpair)
    screen.refresh()
    return txtbox

foo = maketextbox(1,40, 10,20,"foo",deco="underline",textColorpair=curses.color_pair(0),decoColorpair=curses.color_pair(1))
text = foo.edit()
#!/usr/bin/env python

import curses
import curses.textpad as textpad

try:
    mainwindow = curses.initscr()
    # Some curses-friendly terminal settings
    curses.cbreak(); mainwindow.keypad(1); curses.noecho()
    textpad.Textbox(mainwindow).edit()
finally:
    # Reverse curses-friendly terminal settings
    curses.nocbreak(); mainwindow.keypad(0); curses.echo()
    curses.endwin()
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import curses 
import curses.textpad
import cmd

def maketextbox(h,w,y,x,value="",deco=None,textColorpair=0,decoColorpair=0):
    # thanks to http://stackoverflow.com/a/5326195/8482 for this
    nw = curses.newwin(h,w,y,x)
    txtbox = curses.textpad.Textbox(nw,insert_mode=True)
    if deco=="frame":
        screen.attron(decoColorpair)
        curses.textpad.rectangle(screen,y-1,x-1,y+h,x+w)
        screen.attroff(decoColorpair)
    elif deco=="underline":
        screen.hline(y+1,x,underlineChr,w,decoColorpair)

    nw.addstr(0,0,value,textColorpair)
    nw.attron(textColorpair)
    screen.refresh()
    return nw,txtbox

class Commands(cmd.Cmd):
    """Simple command processor example."""
        
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro  = "Welcome to console!"  ## defaults to None
	
    def do_greet(self, line):
	self.write("hello "+line)

    def default(self,line) :
	self.write("Don't understand '" + line + "'")

    def do_quit(self, line):
	curses.endwin()
        return True

    def write(self,text) :
        screen.clear()
	textwin.clear()
        screen.addstr(3,0,text)
        screen.refresh()


if __name__ == '__main__':
    screen = curses.initscr() 	
    curses.noecho()
    textwin,textbox = maketextbox(1,40, 1,1,"")
    flag = False
    while not flag :
        text = textbox.edit()
	curses.beep()
        flag = Commands().onecmd(text)
#!/usr/bin/env python
import curses 
from curses import panel 
def main(stdscr): 
  pad = curses.newpad(100, 100) 
  pad.bkgd('x',0) 
  pad.refresh( 0,0, 5,5, 15,15) 
  pad.getch() 

def main_1(stdscr): 
  win=curses.newpad(0,0) 
  pad=win.subpad(100,100) #<--- error 
  my_pan=panel.new_panel(win) 
  pad.bkgd('x',0) 
  pad.refresh( 0,0, 5,5, 15,15) 
  panel.update_panels() 
  curses.doupdate() 
  pad.getch() 

def main_2(stscr): 
  pad = curses.newwin(100, 100) 
  a_panel= panel.new_panel(pad) #<--- error 
  pad.bkgd('x',0) 
  pad.refresh( 0,0, 5,5, 15,15) 

  panel.update_panels() 
  curses.doupdate() 
  pad.getch() 

if __name__=='__main__': 
  curses.wrapper(main) 
  #curses.wrapper(main_1) 
  #curses.wrapper(main_2) 
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import curses 

screen = curses.initscr() 
curses.noecho() 
curses.curs_set(0) 
screen.keypad(1) 

screen.addstr("This is a Sample Curses Script\n\n") 
while True: 
   event = screen.getch() 
   if event == ord("q"): break 
    
curses.endwin()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Topmenu and the submenus are based of the example found at this location http://blog.skeltonnetworks.com/2010/03/python-curses-custom-menu/
# The rest of the work was done by Matthew Bennett and he requests you keep these two mentions when you reuse the code :-)
# Basic code refactoring by Andrew Scheller

from time import sleep
import curses, os #curses is the interface for capturing key presses on the menu, os launches the files
screen = curses.initscr() #initializes a new window for capturing key presses
curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
curses.start_color() # Lets you use colors when highlighting selected menu option
screen.keypad(1) # Capture input from keypad

# Change this to use different colors when highlighting
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background
h = curses.color_pair(1) #h is the coloring for a highlighted menu option
n = curses.A_NORMAL #n is the coloring for a non highlighted menu option

MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"

menu_data = {
  'title': "Program Launcher", 'type': MENU, 'subtitle': "Please select an option...",
  'options':[
    { 'title': "XBMC", 'type': COMMAND, 'command': 'xbmc' },
        { 'title': "Emulation Station - Hit F4 to return to menu, Esc to exit game", 'type': COMMAND, 'command': 'emulationstation' },
        { 'title': "Ur-Quan Masters", 'type': COMMAND, 'command': 'uqm' },
        { 'title': "Dosbox Games", 'type': MENU, 'subtitle': "Please select an option...",
        'options': [
          { 'title': "Midnight Rescue", 'type': COMMAND, 'command': 'dosbox /media/samba/Apps/dosbox/doswin/games/SSR/SSR.EXE -exit' },
          { 'title': "Outnumbered", 'type': COMMAND, 'command': 'dosbox /media/samba/Apps/dosbox/doswin/games/SSO/SSO.EXE -exit' },
          { 'title': "Treasure Mountain", 'type': COMMAND, 'command': 'dosbox /media/samba/Apps/dosbox/doswin/games/SST/SST.EXE -exit' },
        ]
        },
        { 'title': "Pianobar", 'type': COMMAND, 'command': 'clear && pianobar' },
        { 'title': "Windows 3.1", 'type': COMMAND, 'command': 'dosbox /media/samba/Apps/dosbox/doswin/WINDOWS/WIN.COM -conf /home/pi/scripts/dosbox2.conf -exit' },
        { 'title': "Reboot", 'type': MENU, 'subtitle': "Select Yes to Reboot",
        'options': [
          {'title': "NO", 'type': EXITMENU, },
          {'title': "", 'type': COMMAND, 'command': '' },
          {'title': "", 'type': COMMAND, 'command': '' },
          {'title': "", 'type': COMMAND, 'command': '' },
          {'title': "YES", 'type': COMMAND, 'command': 'sudo shutdown -r -time now' },
          {'title': "", 'type': COMMAND, 'command': '' },
          {'title': "", 'type': COMMAND, 'command': '' },
          {'title': "", 'type': COMMAND, 'command': '' },
        ]
        },

  ]
}



# This function displays the appropriate menu and returns the option selected
def runmenu(menu, parent):

  # work out what text to display as the last menu option
  if parent is None:
    lastoption = "Exit"
  else:
    lastoption = "Return to %s menu" % parent['title']

  optioncount = len(menu['options']) # how many options in this menu

  pos=0 #pos is the zero-based index of the hightlighted menu option. Every time runmenu is called, position returns to 0, when runmenu ends the position is returned and tells the program what opt$
  oldpos=None # used to prevent the screen being redrawn every time
  x = None #control for while loop, let's you scroll through options until return key is pressed then returns pos to program

  # Loop until return key is pressed
  while x !=ord('\n'):
    if pos != oldpos:
      oldpos = pos
      screen.border(0)
      screen.addstr(2,2, menu['title'], curses.A_STANDOUT) # Title for this menu
      screen.addstr(4,2, menu['subtitle'], curses.A_BOLD) #Subtitle for this menu

      # Display all the menu items, showing the 'pos' item highlighted
      for index in range(optioncount):
        textstyle = n
        if pos==index:
          textstyle = h
        screen.addstr(5+index,4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
      # Now display Exit/Return at bottom of menu
      textstyle = n
      if pos==optioncount:
        textstyle = h
      screen.addstr(5+optioncount,4, "%d - %s" % (optioncount+1, lastoption), textstyle)
      screen.refresh()
      # finished updating screen

    x = screen.getch() # Gets user input

    # What is user input?
    if x >= ord('1') and x <= ord(str(optioncount+1)):
      pos = x - ord('0') - 1 # convert keypress back to a number, then subtract 1 to get index
    elif x == 258: # down arrow
      if pos < optioncount:
        pos += 1
      else: pos = 0
    elif x == 259: # up arrow
      if pos > 0:
        pos += -1
      else: pos = optioncount

  # return index of the selected item
  return pos

# This function calls showmenu and then acts on the selected item
def processmenu(menu, parent=None):
  optioncount = len(menu['options'])
  exitmenu = False
  while not exitmenu: #Loop until the user exits the menu
    getin = runmenu(menu, parent)
    if getin == optioncount:
        exitmenu = True
    elif menu['options'][getin]['type'] == COMMAND:
      curses.def_prog_mode()    # save curent curses environment
      os.system('reset')
      if menu['options'][getin]['title'] == 'Pianobar':
        os.system('amixer cset numid=3 1') # Sets audio output on the pi to 3.5mm headphone jack
      screen.clear() #clears previous screen
      os.system(menu['options'][getin]['command']) # run the command
      screen.clear() #clears previous screen on key press and updates display based on pos
      curses.reset_prog_mode()   # reset to 'current' curses environment
      curses.curs_set(1)         # reset doesn't do this right
      curses.curs_set(0)
      os.system('amixer cset numid=3 2') # Sets audio output on the pi back to HDMI
    elif menu['options'][getin]['type'] == MENU:
          screen.clear() #clears previous screen on key press and updates display based on pos
          processmenu(menu['options'][getin], menu) # display the submenu
          screen.clear() #clears previous screen on key press and updates display based on pos
    elif menu['options'][getin]['type'] == EXITMENU:
          exitmenu = True

# Main program
processmenu(menu_data)
curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
os.system('clear')
#!/usr/bin/env python

import npyscreen as np

class myPop(np.NPSApp):

    def setopt(self, title, oList):
        self.title = title
        self.options = oList

    def main(self):
        F = np.Popup(name="Choose an option")
        opt = F.add(np.TitleSelectOne, name=self.title, max_height=len(self.options), values=self.options, scroll_exit=True)
        F.edit()
        self.return_this = opt.get_selected_objects()

def ChooseOption(title, oList):

    a = myPop()
    a.setopt(title, oList)
    a.run()
    return a.return_this

print ChooseOption('fadsfas', ['qwqwqe', 'asdadd', 'zczczcx'])
#!/usr/bin/env python

import npyscreen as np

class StackCreationFormHandler (np.NPSAppManaged):
  keypress_timeout_default = 2

  def __init__(self, title):
    self.title = title

  def onStart(self):
    self.Form = np.Form(name=self.title,minimum_lines=22,minimum_columns=80,lines=22,columns=110)
    ApplicationName = self.Form.add(np.TitleText,name="ApplicationName",begin_entry_at=28,)

Form = StackCreationFormHandler("Title")
Form.run()
#!/usr/bin/env python
import npyscreen 
from datetime import datetime 

class StackCreationEntryForm(npyscreen.Form): 
  def while_waiting(self): 
    self.date_widget.value = datetime.now() 
    self.display() 

  def create(self): 
    self.date_widget = self.add(npyscreen.FixedText, value=datetime.now(), editable=False) 

class StackCreationApp(npyscreen.NPSAppManaged): 
  keypress_timeout_default = 10 
  def onStart(self): 
    self.addForm("MAIN", StackCreationEntryForm, name="Time", minimum_lines=22,minimum_columns=80,lines=22,columns=110) 

if __name__ == '__main__': 
  App = StackCreationApp()
  App.run()
