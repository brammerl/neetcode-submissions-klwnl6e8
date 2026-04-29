class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for operation in operations:
            if operation == 'D':
                newScore = score[-1] * 2
                score.append(newScore)
            elif operation == 'C':
                score.pop()
            elif operation == '+':
                newScore = score[-1] + score[-2]
                score.append(newScore)
            else:
                newScore =  int(operation)
                score.append(newScore)
        return sum(score)
                

    def is_number(val):
        try:
            float(val)
            return True
        except ValueError:
            return False