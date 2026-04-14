class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for n in operations: 
            if n == "+":
                newScore = record[-1] + record[-2]
                record.append(newScore)
            elif n == "D":
                doubledScore = record[-1] * 2
                record.append(doubledScore)
            elif n == "C":
                record.pop()
            else: 
                record.append(int(n))
        return sum(record)
