import sys

import sys
import getopt
input_file = sys.argv[1]
output_file = sys.argv[2]
print(input_file, output_file)

data = open(input_file, 'r')
lines = data.readlines()
data.close()
tab1 = "    "
tab2 = tab1 + tab1
tab3 = tab1 + tab2

f = open("outputfile", "a")
f.write("<people>\n")

lines = map(lambda s: s.strip(), lines)
for idx, l in enumerate(lines):
    split = l.split('|')
    if split[0] == 'P':
        f.write(tab1 + "<person>\n")
        f.write(tab2 + "<firstname>"),
        f.write(split[1])
        f.write("</firstname>\n")
        f.write(tab2 + "<lastname>")
        f.write(split[2])
        f.write("</lastname>\n")
        if split[3]:

    elif split[0] == 'F':
        f.write(tab1 + "<family>\n")
        f.write(tab2 + "<name>"),
        f.write(split[1])
        f.write("</name>\n")


f.write("</people>\n")
f.close()
