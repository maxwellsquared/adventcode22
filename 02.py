# A/X rock, B/Y paper, C/Z scissors

def resolve(theirs, mine):
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

print(resolve('A', 'Y'))
print(resolve('B', 'X'))
print(resolve('C', 'Z'))