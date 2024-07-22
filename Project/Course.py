
class Courses:
    courses_info={
        "course_name":["prog1","prog2","math1","math2","prog3","stat1","stat2"],
        "course_code":["CS111","CS112","CS123","CS333","CS136","CS240","CS350"],
        "doctors":["samy","morad","ashraf","hani","sayed","hussien","morad"],
        "students": [
            ["01402830", "00204690", "00706415", "01003450", "01105795", "01607520"],
            ["00604070", "01105795", "02006900", "00204690", "01802210", "00102345"],
            ["00501725", "02006900", "01607520", "00204690", "01709865", "00307035"],
            ["00808760", "01709865", "01802210", "00204690", "00501725", "01904567"],
            ["00501725", "01402830", "00409380", "00901105", "01208140", "01802210"],
            ["00501725", "02006900", "01208140", "00204690", "01709865", "01904567"],
            ["01208140", "01003450", "00102345", "00808760", "01402830", "02006900"]
        ]
    }

    def display_courses_info(self):
         for name, code, doctor, std in zip(self.courses_info["course_name"], self.courses_info["course_code"], self.courses_info["doctors"], self.courses_info["students"]):
            print(f"Course name = {name} \t Code = {code} \t Taught by Dr: {doctor}")
            print(f"Registered students ID: {' '.join(std)}\n")
    
    @classmethod
    def get_course_name(cls, course_code):
            index = cls.courses_info["course_code"].index(course_code)
            return cls.courses_info["course_name"][index]
    
        

# c=Courses()
# c.display_courses_info()