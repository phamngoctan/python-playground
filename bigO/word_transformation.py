import queue


def BFS(orgWord, transformWord, dictionary):
    q = queue.Queue()
    q.put(orgWord)
    dict = {}
    dict[orgWord] = 0

    while not q.empty():
        word = q.get()
        level = dict[word]

        if word == transformWord:
            break

        for i in range(len(word)):
            char = word[i]

            for asciiValue in range(97, 122):
                if ord(char) == asciiValue:
                    continue

                newV = word[:i] + chr(asciiValue) + word[i + 1:]

                if newV in dict:
                    continue

                if newV in dictionary:
                    q.put(newV)
                    dict[newV] = level + 1

    return dict[transformWord]


def solve(orgWord, transformWord):
    global dictionary
    step = BFS(orgWord, transformWord, dictionary)
    print(orgWord, transformWord, step)


T = int(input())
for _ in range(T):
    blank = input()
    dictionary = []

    while True:
        word = input()
        if word == '*':
            break
        dictionary.append(word)

    try:
        while True:
            ins = input()
            if ins == '':
                break
            orgWord, transformWord = ins.split()
            solve(orgWord, transformWord)
    except EOFError:
        break
