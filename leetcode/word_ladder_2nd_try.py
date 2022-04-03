from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def BFS(beginWord, endWord, wordList):
            queue = []
            queue.append([beginWord, 1])
            wordList = set(wordList)
            lenWord = len(beginWord)
            while len(queue) > 0:
                cur, count = queue.pop(0)
                if cur == endWord:
                    return count
                for index in range(lenWord):
                    for i in range(26):
                        newChar = chr(ord('a') + i)
                        newWord = str(cur[:index] + newChar + cur[index + 1:])
                        # print(f'{newWord}')
                        if newWord in wordList:
                            queue.append([newWord, count + 1])
                            wordList.remove(newWord)
            return 0
        ans = BFS(beginWord, endWord, wordList)
        # print(f'{ans}')
        return ans
sol = Solution()
assert sol.ladderLength("qa",
"sq",
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]) == 5
