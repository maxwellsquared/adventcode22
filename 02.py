import data02


# A/X rock, B/Y paper, C/Z scissors

# resolve a list of pairs
def resolve_list(input_list):
    return_list = []
    for line in input_list:
        return_list.append(resolve_pair(line))
    return return_list

# return a score when given [theirs, mine] - e.g. ["A", "Y"]
def resolve_pair(input_pair):
    theirs = input_pair[0]
    mine = input_pair[1]
    score = 0
    if mine == 'X':
        score += 1
    if mine == 'Y':
        score += 2
    if mine == 'Z':
        score += 3
    if (mine == 'X' and theirs == 'A') or (mine == 'Y' and theirs == 'B') or (mine == 'Z' and theirs == 'C'):
        score += 3
    if (mine == 'X' and theirs == 'C') or (mine == 'Y' and theirs == 'A') or (mine == 'Z' and theirs == 'B'):
        score += 6
    return score

def add_list(input_list):
    to_return = 0
    for elem in input_list:
        to_return += int(elem)
    return to_return

def parse_string(input):
    games = input.split('\n')
    to_return = []
    for line in games:
        to_return.append([line[0], line[2]])
    return to_return


pairs = parse_string(data02.input_string)

print(str(len(pairs)))
print("adding...")
print(add_list(resolve_list(pairs)))