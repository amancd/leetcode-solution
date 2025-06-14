class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        maximum = 0
        minimum = 0

        st = ''
        word = str(num)

        count = 0
        for ch in word:
            if ch!='9':
                st += ch
                count += 1
                break
        
        if count == 0:
            return num
        print(st)

        maximum = word.replace(st, '9')

        st = ''
        for ch in word:
            if ch!='0':
                st += ch
                break
        
        minimum = word.replace(st, '0')


        return int(maximum) - int(minimum)