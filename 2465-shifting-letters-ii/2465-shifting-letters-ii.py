class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        line = [0] * len(s)

        for shift in shifts:
            start, end, direction = shift

            if direction == 0:
                line[start] -= 1
            
                if end+1 < len(s):
                    line[end+1] += 1
            
            else:
                line[start] += 1

                if end+1 < len(s):
                    line[end+1] -= 1

        print(line)

        for i in range(1, len(line)):
            line[i] += line[i - 1]

        result = []
        for i, char in enumerate(s):
            new_char = chr((ord(char) - ord('a') + line[i]) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)