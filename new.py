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

file = open(output_file, "a")


address = ['<street>', '<city>', '<zipcode>']
p = ['<person>\n', '</person>\n']
f = ['<family\n', '</family>\n']
a = ['<address>\n', '</address>\n']
ph = ['<phone>\n', '</phone>\n']
fn = ['<firstname>', '</firstname>\n']
sn = ['<surname>', '</surname>\n']
mobile = ['<mobile>', '</mobile>\n']
homephone = ['<homephone>', '</homephone>\n']
born = ['<born>', '</born>\n']
name = ['<name>', '</name>\n']

street = ['<street>', '</street>\n']
city = ['<city>', '</city>\n']
zipcode = ['<zipcode>', '</zipcode>\n']


tab = ["", "  ", "    ", "      ", "         "]

idx = 0
isFamily = False

c = 0
queue = []
lines = map(lambda s: s.strip(), lines)
file.write("<people>\n")
c += 1
for l in lines:
    split = l.split('|')
    if split[0] == 'P':
        if len(queue) == 1:
            file.write(tab[1] + queue.pop())
        queue.append(p[1])
        file.write(tab[c] + p[0])

        # First name
        file.write(tab[2] + fn[0])
        file.write(split[1])
        file.write(fn[1])

        # Surname
        file.write(tab[2] + sn[0])
        file.write(split[2])
        file.write(sn[1])

    elif split[0] == 'T':
        # phone
        file.write(tab[2] + ph[0])
        # mobile
        file.write(tab[3] + mobile[0])
        file.write(split[1])
        file.write(mobile[1])

        # homephone
        if len(split) > 2:
            file.write(tab[3] + homephone[0])
            file.write(split[2])
            file.write(homephone[1])

        file.write(tab[2] + ph[1])

    elif split[0] == 'F':
        if len(queue) == 1:
            file.write(tab[1] + queue.pop())
        queue.append(f[1])
        file.write(tab[1] + f[0])
        file.write(tab[2] + name[0] + split[1] + name[1])
        file.write(tab[3] + born[0] + split[2] + born[1])

    if split[0] == 'A':
        # address
        extraTab = 0
        if queue[0] == f[1]:
            extraTab = 1

        file.write(tab[2 + extraTab] + a[0])

        # street
        file.write(tab[3 + extraTab] + street[0] + split[1] + street[1])

        # city
        file.write(tab[3 + extraTab] + city[0] + split[2] + city[1])

        # zipcode
        if len(split) > 3:
            file.write(tab[3 + extraTab] + zipcode[0] + split[3] + zipcode[1])
        file.write(tab[2 + extraTab] + a[1])

file.write(tab[1] + queue.pop())
file.write("</people>\n")
file.close()
