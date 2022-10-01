class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        answers = []
        new_answers = []
        for i in digits:
            mapping = digit_map[i]
            new_answers = []
            for char in mapping:
                for item in answers:
                    new_answers.append(item + char)
            
            if(len(answers) == 0):
                item = ""
                for char in mapping:
                    new_answers.append(item + char)
            
            answers = new_answers.copy()
        return answers
