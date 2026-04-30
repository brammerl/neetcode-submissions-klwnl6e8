class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        qeue = deque(students)
        n = len(students)

        res = n

        for sandwich in sandwiches:
            count = 0
            while count < n and qeue[0] != sandwich: 
                student = qeue.popleft()
                qeue.append(student)
                count += 1
            if qeue[0] == sandwich: 
                qeue.popleft()
                res -= 1
            else:
                break
        return res