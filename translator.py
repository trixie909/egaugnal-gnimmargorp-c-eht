def reverse(string):
    string = string[::-1]
    return string
input = open('egaugnal-gnimmargorp-c-eht.c', 'rt')
output = open('translated.c', 'wt')

for line in input:
    output.write(reverse(line))