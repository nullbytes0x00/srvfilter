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
import threading

try:

    import tkinter as tk
    import tkinter.scrolledtext as tkst
    from tkinter import ttk
    
except ImportError:

    raise
    sys.exit("Python 3 is required!")


from .parse import * 
from .proxy import *
   

class CheckGUI:

    def proxy_status_check(self, input_list, input_country, input_local, input_timeout, export_file, working):

        #print("Thread started")
        self.export_file = export_file
        self.proxy_list_final_text = ""        
        self.proxy_ipport = []

        self.proxy_ipport = parse_ipport(input_list)

        for v in self.proxy_ipport:
            
            if self.stopped is True or self.stopped is None:
                break
                
            c = Proxy(v[0], v[1])
            geoinfo = c.geoinfo()
            
            def proxy_accept():
                
                proxy_processed = [v[0], v[1], geoinfo]
                self.proxy_list_final_text += parse_totext(proxy_processed)                        
                self.update(parse_totext(proxy_processed), export_file)
                self.update("-"*9, export_file)
                    
    
            if working == "Yes":
                #if no proxy location is provided by the user
                if not input_country and not input_local: 
                    if c.up(input_timeout):
                        #the proxy is up
                        proxy_accept()
                    else:
                        #the proxy is down
                        pass
                #if rpoxy location is provided by the user
                else:
                    #if the proxy passes through the location filter
                    if geofilter_proxy(geoinfo, input_country, input_local):
                        if c.up(input_timeout):
                            #the proxy is up
                            proxy_accept()
                        else:
                            #the proxy is down
                            pass
                    else:
                        #the location isn't matched
                        pass
            else:
                if not input_country and not input_local:
                    proxy_accept()
                else:
                    if geofilter_proxy(geoinfo, input_country, input_local):
                        proxy_accept()
                    else:
                        pass
                    
            if self.proxy_ipport[int(len(self.proxy_ipport))-1] is v:
                self.update("\n\nProxy checking is complete.", export_file)
                self.Label1.config(text = "Status: Complete")
                self.Progressbar1.config(mode="determinate")
                self.Progressbar1.stop()

                self.switch_state()
            
        #print("Stopping thread...")
        
    def __init__(self, input_list, input_country, input_local, input_timeout, export_file, working):
    
        self.title = "SrvFilter v0.1: Filtering"

        self.stopped = False
        
        self.x = 50
        self.y = 50

        self.pad = 12
        
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.wm_title(self.title)
        
        def on_quit():
            self.stopped = True
            self.root.destroy()
            
        self.root.protocol("WM_DELETE_WINDOW", on_quit)
        
        self.ScrolledText1 = tkst.ScrolledText(self.root, height = 12, width = 40)
        self.ScrolledText1.grid(row = 0, column = 0, padx = self.pad, pady = (self.pad, 5))
        self.ScrolledText1.insert(tk.INSERT, "Filtering servers...\n\n")        
        self.ScrolledText1.config(state = tk.DISABLED)

        self.Label1 = tk.Label(self.root, text = "Status: Checking")
        self.Label1.grid(row = 1, column = 0, padx = self.pad, pady = (0, 5))

        self.Progressbar1 = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=200, mode='indeterminate')
        self.Progressbar1.grid(row=2, column=0, padx=(self.pad, self.pad), pady = (0, 7))
        self.Progressbar1.start()


                
        self.Button1 = tk.Button(self.root, text = "Stop", width=7, command = self.switch_state)
        self.Button1.grid(row = 3, column = 0, padx = self.pad, pady = (0, self.pad))
        
        self.root.geometry("+%d+%d" % (self.x, self.y))

        self.checking_thread = threading.Thread(None, self.proxy_status_check, None, (input_list, input_country, input_local, input_timeout, export_file, working, ), None)
        self.checking_thread.start()

        self.root.mainloop()

    def switch_state(self):
        if self.stopped is False:
            self.stopped = True
            self.Button1.config(state = tk.DISABLED)
            self.Label1.config(text = "Status: Completed")
            self.Progressbar1.config(mode="determinate")
            self.Progressbar1.stop()
            
    def update(self, text, file):
        if file:
            f = open(file, "a")
            f.write(str(text))
            f.close()
            
        self.ScrolledText1.config(state = tk.NORMAL)
        self.ScrolledText1.insert(tk.INSERT, str(text))        
        self.ScrolledText1.config(state = tk.DISABLED)
