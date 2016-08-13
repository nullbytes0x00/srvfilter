#SrvFilter

![Example of use 1](https://raw.githubusercontent.com/nullbytes0x00/srvfilter/master/sfuse3.png)

SrvFilter is a program which filters a list of IP addresses and ports based on the criteria specified by the user.
It can be used in a number of ways. A good example is filtering proxy servers by their precise location information (city, region/state, country) - upon the filtering process, you will obtain a list of proxy servers only in the precise location which you desire (if such were present in the proxy list you inputed).

This program was created by NullBytes0x00 (Arseny Denisov), and it's licensed under the GPLv3. It is therefore free software.

Please note that this program is in its early stages of development, so the code is rather messy, and there are most likely
some unresolved bugs. Contact me if you wish to report any bugs or to make suggestions.


##Dependencies
The ipwhois package, as well as Python 3 are all required to run this program.


##Usage
First, import a server list you want to filter. This can be done by either entering the list into the field on the left, or by
importing a file with your server list (in this case, you have to enable importing).

The format has to be IP:PORT, with each server being placed on a new line.

If you want to export the results to a file, enable exporting, and specify the file name (it can be a new file, or an existing one; the data is appended to the end of the file).

Adjust the filtering settings as they suit you (please note that you can enter either the state/region, the city, or the postal
code in the locality), and click the "Check" button. The filtering should then start.

##Future updates
A Windows executable version of the program will be released in the future.

##Contact
You can contact me at nullbytes0x00@gmail.com.
