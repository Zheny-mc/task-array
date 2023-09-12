from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum([abs(students[i] - seats[i]) for i in  range(len(seats))])

print( Solution().minMovesToSeat(seats = [3,1,5], students = [2,7,4]) )