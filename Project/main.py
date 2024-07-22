from User import Users
from Doctors import Doctor
from Students import Student

def main_menu():
    while True:
        print("Please make a choice: ")
        print("         1-Login")
        print("         2-Sign Up")
        print("         3-Shutdown system")
        choice=input("         Enter Choice: ").strip()
        #LogIn
        if(choice=='1'):
            print("Please Enter username and password: ")
            role=input("Enter Student/Doctor  ").lower().strip()
            name=input("user Name: ").lower().strip()
            password=input("Password: ").strip()
            if role=="doctor":
                dr=Doctor(name,password)
                loginResult=dr.logIn(name,password)
                print(loginResult)
            elif role=="student":
                std=Student(name,password)
                loginResult=std.logIn(name,password)
                print(loginResult)
                if "Welcome" in loginResult:
                    std.std_mainMenu()  # Call the student main menu
                    break 
                
               
            else:
                print("Invalid role. Please enter 'doctor' or 'student'.")
        #SignUp
        elif choice=='2':
            print("Please Enter username and password to sign up: ")
            role=input("Enter Student/Doctor  ").lower().strip()
            name=input("user Name: ").lower().strip()
            password=input("Password: ").strip()
            if role=="doctor":
                dr=Doctor(name,password)
                signup=dr.signUp()
                print(signup)
            elif role=="student":
                std=Student(name,password)
                signup=std.signUp(name,password)
                print(signup)
               
        
        elif choice=='3':
            print("Shutting down the system...")
            break
                

    

 
if __name__ == "__main__":
     main_menu()
     










