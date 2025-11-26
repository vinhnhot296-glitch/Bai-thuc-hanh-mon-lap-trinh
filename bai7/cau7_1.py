input_file = open('a.txt', 'r')
for line in input_file:
    line = line.rstrip('\n')
    s = ''
    l = len(line)
    while(l >= 1):
        s = s + line[l-1]
        l = l-1
    print(s)
input_file.close()
