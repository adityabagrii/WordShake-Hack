wordlist = []
with open('wordlist.txt', 'r') as f:
    for line in f:
        wordlist.append(line.strip())

def backtrack(i, j, mat, word, visited, s, lst):
    if len(word) == s:
        if word.lower() in wordlist:
            lst.append(word)
        return
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            ni, nj = i + x, j + y
            if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]) and not visited[ni][nj]:
                visited[ni][nj] = True
                backtrack(ni, nj, mat, word + mat[ni][nj], visited, s, lst)
                visited[ni][nj] = False

def generateWords(word_length):
    lst = []
    # Type in the word grid here
    mat = [['Y', 'N', 'C', 'H'], ['O', 'S', 'O', 'R'], ['N', 'I', 'N', 'I'], ['A', 'T', 'A', '']]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
            visited[i][j] = True
            backtrack(i, j, mat, mat[i][j], visited, word_length, lst)
    lst = list(set(lst))
    print(" ".join(lst))

# type in the range of word length you want to generate: 3-8 for example
for i in range(3,9):
    generateWords(i)