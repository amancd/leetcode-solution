class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res = sentence.split(" ")
        n = len(searchWord)
        print(res)

        for i in range(len(res)):
            temp = res[i]
            if searchWord in temp[0:n]:
                return i+1
        

        return -1