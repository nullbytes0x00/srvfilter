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

import socket
import ipwhois
from ipwhois import IPWhois

class Proxy:
    
    def __init__(self, ip, port):
        
        self.ip = ip
        self.port = port

    def up(self, timeout):
        
        try:
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            
            res = s.connect_ex((self.ip, self.port))
            
            if res == 0:
                return True
            else:
                return False
            
            s.close()
            
        except:
            
            #raise
            return False

    def geoinfo(self):
        
        try:
            data = IPWhois(self.ip)
            return data.lookup(False)['nets'][0]   
        except:
            #raise
            return None
    
