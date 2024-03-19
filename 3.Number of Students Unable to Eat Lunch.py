class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = Counter(students)
        sandwich_count = Counter(sandwiches)
        
        for sandwich in sandwiches:
            if student_count[sandwich] > 0 and sandwich_count[sandwich] > 0:
                student_count[sandwich] -= 1
                sandwich_count[sandwich] -= 1
            else:
                break
        
        return sum(student_count.values())