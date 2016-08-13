"""

    SrvFilter - free server filtering software
    Software version: 0.1
    
    Copyright (C) 2016 Arseny Denisov
    Email: nullbytes0x00@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
"""

#!/usr/bin/env python

import sys

try:

    import tkinter as tk
    import tkinter.scrolledtext as tkst
    from tkinter import filedialog
    from tkinter import ttk
    
except ImportError:

    raise
    sys.exit("Python 3 is required!")

from .cgui import *
    

class MainGUI:

    def __init__(self):
        
        self.title = "SrvFilter v0.1"
        self.proxy_list = None
        self.timeout = 3
        
        self.export_file = None
        self.checking_class = None
        
        self.x = 50
        self.y = 50

        self.pad = 12
        
        self.__root = tk.Tk()
        self.__root.configure()
        self.__root.resizable(0, 0)
        self.__root.wm_title(self.title)

        
        self.__ScrolledText1 = tkst.ScrolledText(self.__root, height = 13, width = 25)
        self.__ScrolledText1.grid(row = 0, column = 0, padx = (self.pad, 0), pady = 15)
        

        self.__LabelFrame1 = ttk.LabelFrame(self.__root, text = "Settings", padding = (5, 5))
        self.__LabelFrame1.grid(row = 0, column = 1, padx = self.pad, pady = self.pad, sticky = tk.N)

        self.__Label1 = tk.Label(self.__LabelFrame1, text = "Country")
        self.__Label1.grid(row = 0, column = 0, sticky = tk.N + tk.W)

        self.__Label2 = tk.Label(self.__LabelFrame1, text = "Locality")
        self.__Label2.grid(row = 0, column = 1, sticky = tk.N + tk.W)

        self.__Entry1 = tk.Entry(self.__LabelFrame1)
        self.__Entry1.grid(row = 2, column = 0, padx = (0, 5), pady = (2, 0), sticky = tk.N + tk.W)
        
        self.__Entry2 = tk.Entry(self.__LabelFrame1)
        self.__Entry2.grid(row = 2, column = 1, pady = (2, 0), sticky = tk.N + tk.W)

        self.__Label3 = tk.Label(self.__LabelFrame1, text = "Timeout")
        self.__Label3.grid(row = 3, column = 0, pady = (5, 0), sticky = tk.N + tk.W)

        self.__Label4 = tk.Label(self.__LabelFrame1, text = "Working")
        self.__Label4.grid(row = 3, column = 1, pady = (5, 0), sticky = tk.N + tk.W)

        self.__Spinbox1 = tk.Spinbox(self.__LabelFrame1, from_=0, to=10, width=5)
        self.__Spinbox1.grid(row = 4, column = 0, pady = (2, 0), sticky = tk.N + tk.W)
        self.__Spinbox1.delete(0, "end")
        self.__Spinbox1.insert(0, self.timeout)

        self.__Spinbox2 = tk.Spinbox(self.__LabelFrame1, values= ("Yes", "No"), width=5)
        self.__Spinbox2.grid(row = 4, column = 1, pady = (2, 0), sticky = tk.N + tk.W)


        self.importing = tk.IntVar()


        self.__Checkbutton1 = tk.Checkbutton(self.__LabelFrame1, text="Enable importing", onvalue = 1, offvalue = 0, variable = self.importing)
        self.__Checkbutton1.grid(row = 5, column = 0, pady = (5, 0), sticky = tk.N + tk.W)


        def on_import():
            
            if self.importing.get() == 1:
            
                f = filedialog.askopenfile(parent = self.__root, mode = "r", title = "Open server list")
                
                if f != None:
                    try:
                        self.proxy_list = str(f.read()).split()
                    except:
                        print("Incorrect server format.")
                        
                    f.close()
                
                print("On import")


        self.__Button1 = tk.Button(self.__LabelFrame1, text = "Browse", command = on_import)
        self.__Button1.grid(row = 5, column = 1, pady = (5, 0), sticky = tk.N + tk.W)


        self.exporting = tk.IntVar()

                            
        self.__Checkbutton2 = tk.Checkbutton(self.__LabelFrame1, text="Export server list", onvalue = 1, offvalue = 0, variable = self.exporting)
        self.__Checkbutton2.grid(row = 6, column = 0, pady = (5, 0), sticky = tk.N + tk.W)


        def on_export():
            
            if self.exporting.get() == 1:
            
                self.export_file = filedialog.asksaveasfilename(defaultextension='.txt',
                                            filetypes=[('Text file', '.txt')])
                print("On export")


        self.__Button2 = tk.Button(self.__LabelFrame1, text = "Browse", command = on_export)
        self.__Button2.grid(row = 6, column = 1, pady = (5, 0), sticky = tk.N + tk.W)


        def on_check():
            
            if (self.importing.get() == 0) and self.proxy_list is not None:

                try:
                    self.proxy_list = str(self.__ScrolledText1.get('1.0', tk.END+'-1c')).split()
                except:
                    print("Incorrect server format.\n")
                    
            elif (self.importing.get() == 1) and self.proxy_list is None:
                
                print("Select a server list.")
                
            elif self.proxy_list is None:
                self.proxy_list = str(self.__ScrolledText1.get('1.0', tk.END+'-1c')).split()

            try:

                if (self.exporting.get() == 1) and self.export_file is None:
                    print("You must select an export file.")
                    return
                    
                self.checking_class = CheckGUI(self.proxy_list, self.__Entry1.get(), self.__Entry2.get(), int(self.timeout), self.export_file, self.__Spinbox2.get())
                
            except:
                print("Incorrect server format.\n")
                

        
        self.__Button3 = tk.Button(self.__root, text = "Check", command = on_check, width = 10)
        self.__Button3.grid(row = 0, column = 1, pady = (0, self.pad), sticky = tk.S)
                   
        self.__root.geometry("+%d+%d" % (self.x, self.y))
        self.__root.mainloop()
