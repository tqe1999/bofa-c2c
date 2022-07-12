import sys
import xml.etree.ElementTree as ET

from lib.models import db

# get command line args
input_file = sys.argv[1]

# parse xml
mytree = ET.parse('input.xml')
myroot = mytree.getroot()
print(myroot)

