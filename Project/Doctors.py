from User import Users
class Doctor(Users):
    doctors_info={
        "name":["ali","mostafa","hani","mohamed","ashraf","samy","morad","sayed","hussien"],
        "password":["123","1234","12345","123456", "1234567","111","222","333","444"],
        "courses":[
            [],
            [],
            ["Cs333"],
            [],
            ["CS123"],
            ["CS111"],
            ["CS112","CS350"],
            ["CS136"],
            ["CS240"]
        ]

    }
    
    
    def __init__(self, userName, password):
        super().__init__(userName, password)
        
    def logIn(self, userName, password):
       
        for i,j in zip(self.doctors_info["name"] , self.doctors_info["password"]):
            if(i==userName and j==password):
                return f"Welcome Dr {userName}.you are logged in"
        
        return f"fail log in"
    
   



    def display_doctors_info(self):
         for name,courses in zip(self.doctors_info["name"],self.doctors_info["courses"]):
            if len(courses) !=0 :
                print(f"Doctor {name} is teaching {len(courses)} courses. Courses Codes: {' '.join(courses)}\n")
            else:
                print(f"Doctor {name} is teaching {len(courses)} courses.\n")



# Dr=Doctor("","")
# Dr.display_doctors_info()