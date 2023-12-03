schematic = []
f = open('test_aoc03.txt','rt')
for line in f:
    schematic += ['.' + line[:-1] + '.']
f.close()
line_length = len(schematic[0])
schematic = ['.' * line_length] + schematic
print()