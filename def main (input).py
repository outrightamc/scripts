#!/usr/bin/python3

#def checkName(name):
import re
import os
import json
import logging
logger = logging.getLogger(__name__)

# stored = input("Enter Filename:") 

for filename in os.listdir('//Users//outright//Downloads'):
    if re.match('^.*$', filename):
        try:
            if not filename == 'CVS' and not filename == '.cvsignore' and not filename.endswith('.new'):

                filepath = '//Users//outright//Downloads//'+filename
                read_file = open(filepath, "r")

            for line in read_file.readlines():
                if re.match(r'(IP)\s\s\s\s\s\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line):
                    saved = re.match(r'(IP)\s\s\s\s\s\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line).group(2)
            for match in saved:
                print(match)

# WRITE RESULTS
        except IOError:
            print ("I/O error {}".format(filepath))

#logger.debug('\n- dump data.json')
#with open(localpath+'data.json', 'w') as data_json:
#    json.dump(d, data_json, indent=4)
#data_json.close()