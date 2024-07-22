from User import Users
from Course import Courses
from assignments import Assignment
class Student(Users):
    student_info={
        "name":["hussien samy","ashraf sayed","mostafa hussien","ali mohamed","hani sayed"],
        "password":["123","1234","12345","123456", "1234567"],
        "id":["00102345","00204690","00307035","00409380","00501725"],
        "courses":[
            ["CS111","CS112","CS333","CS136","CS240","CS350"],
            ["CS111","CS112","CS123","CS333","CS136","CS240","CS350"],
            ["CS112","CS123","CS333","CS136"],
            ["CS111","CS112","CS123","CS333","CS136","CS350"],
            ["CS111","CS112","CS123","CS333","CS136","CS240"]
        ],
        "email":["hussiensamy@gmail.com","ashrafsayed@gmail.com","mostafahussien@gmail.com","alimohamed@gmail.com","hanisayed@gmail.com"],
    }
    
    assignment_info={
        "course_code":["CS111","CS112","CS123","CS333","CS136","CS240","CS350"],
        "assignment":["task111","task112","task123","task333","task136","task240","task350"]
    }

    def init(self, userName, password):
        super().init(userName, password)
      
        

        
    def logIn(self, userName, password):
       
        for i,j in zip(self.student_info["name"] , self.student_info["password"]):
            if(i==userName and j==password):
                return f"Welcome {userName}.you are logged in"
        
        return f"fail log in"

    def signUp(self,username,password):
        self.student_info["name"].append(username)
        self.student_info["password"].append(password)
        return f"sign up successfully"
    
    def display_std_info(self):
         for name, std_id, courses in zip(self.student_info["name"], self.student_info["id"], self.student_info["courses"]):
            print(f"Student {name} with ID {std_id} registered in {len(courses)} courses.")
            print(f"Courses list: {' '.join(courses)}\n")
    
    def register_in_course(self):
        pass

    def list_my_courses(self):
         index = self.student_info["name"].index(self.userName)
         registered_courses = self.student_info["courses"][index]
         print("My Course List: ")
         for idx, course_code  in enumerate(registered_courses):
            course_name = Courses.get_course_name(course_code)
            if course_name:
                print(f"{idx + 1}) Course {course_name} - code {course_code}")
            else:
                print(f"not found.")

    def display_courses(self):
         index = self.student_info["name"].index(self.userName)
         registered_courses = self.student_info["courses"][index]
         print("My Course List: ")
         for idx, course_code  in enumerate(registered_courses):
            course_name = Courses.get_course_name(course_code)
            if course_name:
                print(f"{idx + 1}) Course {course_name} - code {course_code}")
            else:
                print(f"not found.")      
         choice = int(input(f"Which ith [1 - {len(registered_courses)}] course to view? ").strip())
         if 1 <= choice <= len(registered_courses):
            self.view_course_details(registered_courses[choice - 1])

    
    def view_course_details(self, course_code):
        course_name = Courses.get_course_name(course_code)
        assignments = Assignment.get_assignments_by_course(course_code)

        print(f"Course {course_name} with Code {course_code} - taught by Doctor {Courses.get_doctor_name(course_code)}")
        print(f"Course has {len(assignments)} assignment(s):")

        for idx, assignment in enumerate(assignments):
            status = "submitted" if self.userName in assignment['solutions'] else "NOT submitted"
            grade = assignment['grades'].get(self.userName, "NA")
            print(f"Assignment {idx + 1}: {assignment['title']} {status} - Grade: {grade} / {assignment.get('total_marks', 'NA')}")

        self.course_actions_menu(course_code)

    def course_actions_menu(self, course_code):
        while True:
            print("\nPlease make a choice:")
            print("1 - UnRegister from Course")
            print("2 - Submit solution")
            print("3 - Back")
            choice = input("Enter Choice: ").strip()
            
            if choice == '1':
                self.unregister_from_course(course_code)
                break
            elif choice == '2':
                self.submit_solution(course_code)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    
    def unregister_from_course(self, course_code):
        index = self.student_info["name"].index(self.userName)
        self.student_info["courses"][index].remove(course_code)
        print(f"Successfully unregistered from course {course_code}.")

    def submit_solution(self, course_code):
        assignments = self.assignment_manager.get_assignments_by_course(course_code)
        print("Assignments:")
        for idx, assignment in enumerate(assignments):
            print(f"{idx + 1}. {assignment['title']} (Due: {assignment['due_date']})")
        
        assignment_choice = int(input("Select assignment number to submit: ").strip()) - 1
        if 0 <= assignment_choice < len(assignments):
            assignment_id = assignments[assignment_choice]['assignment_id']
            solution = input("Enter your solution: ").strip()
            self.assignment_manager.submit_solution(assignment_id, self.userName, solution)
            print(f"Solution submitted for assignment {assignment_choice + 1}.")
        else:
            print("Invalid choice.")


    
         
        


    def std_mainMenu(self):
        while True:
            print("Please make a choice: ")
            print("         1-Register in Course")
            print("         2-List My Courses")
            print("         3-View Course")
            print("         4-Grades Report")
            print("         5-Log Out")
            choice=input("         Enter Choice: ").strip()
            if choice=='1':
                pass
            elif choice=='2':
                self.list_my_courses()
            elif choice=='3':
                self.display_courses()
                break
            elif choice=='4':
                pass
            elif choice=='5':
                break


        
        



        


    
