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

import ipwhois
from ipwhois.utils import get_countries
countries = get_countries()

def convert_string(info_string):
    
    outstr = str(info_string)
    outstr = outstr[0].upper() + outstr[1:]
    outstr = outstr.replace("_", " ")
    
    return outstr


def parse_totext(proxy):
     
    info_string = "\nIP: %s:%s\n" % (str(proxy[0]), str(proxy[1]))

    for k, v in proxy[2].items():

        if k == "country":
            newv = countries[v]
            v = newv
            
        info_string += convert_string(k) + ": " + str(v) + "\n"

    return info_string


#inputs a ["proxy:ip"] list of strings, outputs ["proxy", ip]
def parse_ipport(ipport_list):

    proxy_list = []
    proxy_list = [proxy.split(":") for proxy in ipport_list]
    
    for i in range(0, len(proxy_list)):
        proxy_list[i][1] = int(proxy_list[i][1])
        
    return proxy_list

	
#filter outputs
def geofilter_proxy(geoinfo, country, locality):

    if geoinfo is None:
        return False
    
    if not country and not locality:
        return False
    
    for k, v in geoinfo.items():

        if (country) and (v is not None) and (k == "country"):
            
            newv = countries[v]
            v = newv
            
            if country.lower() in v.lower():
                return True
                break
                        
        elif (locality) and (v is not None) and ((k == "state") or (k == "city") or (k == "postal_code")):
            
            if (locality.lower() in v.lower()):
                return True
                break
                
    return False
