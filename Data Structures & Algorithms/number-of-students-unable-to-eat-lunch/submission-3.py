class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studs = deque(students)
        n = len(students)

        res = n

        for sandwhich in sandwiches:
            count = 0
            while studs[0] != sandwhich and count < n: 
                curr = studs.popleft()
                studs.append(curr)
                count += 1
            if studs[0] == sandwhich:
                studs.popleft()
                res -= 1
                
            else:
                break
        return res