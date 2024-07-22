class Assignment:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code
        self.solutions = {}
        self.grades = {}

    def submit_solution(self, student_id, solution_text):
        self.solutions[student_id] = solution_text
        print(f"Solution submitted for student {student_id}: {solution_text}")

    def set_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def view_grades_report(self):
        for student_id, grade in self.grades.items():
            print(f"Student ID: {student_id}, Grade: {grade}")
       

