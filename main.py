import sys


input_file = sys.argv[1]
output_file = sys.argv[2]
print(input_file, output_file)

data = open(input_file, 'r')
lines = data.readlines()
data.close()

file = open(output_file, "a")

# 0 = opening tag, 1 = closing tag
person = ['<person>\n', '</person>\n']
firstname = ['<firstname>', '</firstname>\n']
surname = ['<surname>', '</surname>\n']

family = ['<family\n', '</family>\n']
born = ['<born>', '</born>\n']
name = ['<name>', '</name>\n']

address = ['<address>\n', '</address>\n']
phone = ['<phone>\n', '</phone>\n']
mobile = ['<mobile>', '</mobile>\n']
homephone = ['<homephone>', '</homephone>\n']


street = ['<street>', '</street>\n']
city = ['<city>', '</city>\n']
zipcode = ['<zipcode>', '</zipcode>\n']


indent = ["", "  ", "    ", "      ", "         "]


c = 1  # counter/index for indentation
queue = []  # for closing opened person/family bracket
lines = map(lambda s: s.strip(), lines)  # removing whitespace from all strings

file.write("<people>\n")
for l in lines:
    split = l.split('|')
    if split[0] == 'P':
        c = 1
        if len(queue) == 1:
            file.write(indent[c] + queue.pop())
        queue.append(person[1])
        file.write(indent[c] + person[0])
        c += 1

        # First name
        file.write(indent[c] + firstname[0] + split[1] + firstname[1])

        # Surname
        file.write(indent[c] + surname[0] + split[2] + surname[1])

    elif split[0] == 'F':
        c = 1
        if len(queue) == 1:
            file.write(indent[1] + queue.pop())
        queue.append(family[1])

        file.write(indent[c] + family[0])
        c += 1

        # name
        file.write(indent[c] + name[0] + split[1] + name[1])
        c += 1

        # born
        file.write(indent[c] + born[0] + split[2] + born[1])

    if split[0] == 'T':
        # phone
        file.write(indent[c] + phone[0])
        c += 1

        for p in split[1:]:
            if len(p) > 9:
                # # mobile
                file.write(indent[c] + mobile[0] + p + mobile[1])
            else:
                file.write(indent[c] + homephone[0] + split[2] + homephone[1])

        c -= 1
        file.write(indent[c] + phone[1])

    if split[0] == 'A':
        # address
        file.write(indent[c] + address[0])
        c += 1

        # street
        file.write(indent[c] + street[0] + split[1] + street[1])

        # city
        file.write(indent[c] + city[0] + split[2] + city[1])

        # zipcode
        if len(split) > 3:
            file.write(indent[c] + zipcode[0] + split[3] + zipcode[1])
        c -= 1
        file.write(indent[c] + address[1])
file.write(indent[c] + queue.pop())
file.write("</people>\n")
file.close()
