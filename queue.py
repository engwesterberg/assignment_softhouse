
import sys
import json
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

f = open(output_file, "a")


address = ['<street>', '<city>', '<zipcode>']

stack = []


lines = map(lambda s: s.strip(), lines)
f.write("<people>\n")
for l in lines:
    split = l.split('|')
    if split[0] == 'P':
        stack.append(tab1 + "<person>\n")
        stack.append(tab2 + "<firstname>")
        stack.append(split[1])
        stack.append("</firsname>\n")
        stack.append(tab2 + "<lastname >")
        stack.append(split[2])
        stack.append("</lastname>\n")
    elif split[0] == 'T':
        stack.append(tab2 + "<phone>\n")
        for nr in split[1:]:
            stack.append(tab3 + "<mobile>")
            stack.append(nr)
            stack.append("</mobile>\n")
        stack.append(tab2 + "</phone>\n")
    elif split[0] == 'A':
        stack.append(tab2 + "<address>\n")
        for idx, nr in enumerate(split[1:]):
            stack.append(tab3 + address[idx])
            stack.append(nr)
            stack.append("</" + address[idx][1:] + "\n")
        stack.append(tab2 + "</address>\n")
    elif split[0] == 'F':
        stack.append(tab1 + '<family>')
        stack.append(split[1])
        stack.append('t</name>')


for obj in stack:
    f.write(obj)
