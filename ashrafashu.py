'''''
    name["syed","aashif","hii""queen"]
rollno=[1,2,3,4]
present=[3,4]
roll=int(input("enter roll mun"))
if roll in rollno:
    if roll in present:
        print("present")
    else:
        print("present")
else:
    print("roll number is not found")
'''''



'''''''''''
t=("syed","asif","hi")
p=list(t)
p[2]="ashu"
r=tuple(p)
print(r)
'''''''''''




'''
t=("syed","asif","hi")
print(t[0:2])
print(t[1:3])
print(t[:2])
print(t[1:])
print(t[::-1])
'''




'''
fruits = {"Apple", "Banana", "Mango"}
print("Original Set:", fruits)
fruits.add("Orange")
print("After Adding Orange:", fruits)
fruits.remove("Banana")
print("After Removing Banana:", fruits)
'''




'''
a ={1,2,3,4}
b ={4,5,6,7}
print("union value:",a | b)
print("set diff:",a-b)
print("same value:",a&b)
'''
    



'''    
a={"name":"syed","age":20}
print(((a["name"])))
'''




'''
q={"name":"munni","age":19}
a["ashu"]="ashu"
print((a["name"]))
print((a["age"]))
print(a)
'''





'''
print("welcome to the cart")
cart={}
while true:
p=input(yujk'"1.enter the product name")
p=input("2.enter the product name")
p=input("3.display the total value")
p=input("enter the choice:")
if p == 1:
    name=(input("enter the product name:"))
    price=(float(input("enter the price:")))
    count=(int(input("enter the quantity:")))
    cart[name]=price,count
    print("cart")
'''    





'''
def profile(name,hobby):
    print(f"name:{name}")
    print(f"hobby:{hobby}")
n=input("enter name:")
b=input("enter hobby:")
profile(n,b)
'''




'''
def add(a,b):
    return a+b
def get():
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    return a,b
c,d=get()
r=add(c,d)
print("sum:",r)
'''




'''
def square(n):
    return n*n
y=square(4)print(y)
'''





'''
def cube(n):
    return n*n*n
y=cube(4)
print(y)
'''





'''
def multiply(a,b):
    return a*b
product=multiply(5,4)
print(product)
'''




'''
def grade_profile(username,status,role):
    print("Username:",username)
    print("Status:",status)
    print("Role:",role)
grade_profile("Ali","Active","Student")
'''





'''
c={}
def add():
    n=input("enter name:")
    p=int(input("enter phonenumber:"))
    c[n]=p
    print("successfully added number")
def view():
    n=input("enter name to view:")
    if n in c:
        print(f"name:{n},phone:{c[n]}")
    else:
        print("contact not found")
def delete():
     n=input("enter name to delete:")
     if n in c:
         del c[n]
         print("successfully deleted")
     else:
        print(" contact not found")
def display():
    if c:
        for n,p in c.items():
            print(f"name:{n},phone:{c[n]}")
    else:
        print("no contacts are there")
def main():
    choice=""
    while choice !="6":
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice=int(input("enter choice(1-5):"))
        if choice==1:
            add()
        elif choice==2:
            view()
        elif choice == 3:
            delete()
        elif choice ==4:
            display()
        elif choice==5:
            print("thanks for visiting")
            break
        else:x
            ("invalid choice try again")
main()

'''






'''
u={}
def signin():
    user=input("enter username:")
    if user in u:
        print("choose another name that name is already exist")
    else:
            ame=input("enter name:")
            password=int(input("enter pass:"))
            u[name]=password
def login():
    name=input("enter name:")
    password=int(input("enter pass:"))
    if name in u and u[name]== password:
        print(f"successfully login,welcome {name}")
    else:
        print("enter pass or username wrong")
def main():
    choice=""
    while choice!="3":
        print("\n===== Login System =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice=int(input("enter your choice :"))
        if choice==1:
            signin()
        elif choice==2:
            login()
        elif choice==3:
            print("thanks for visiting!")
            break
        else:
            print("enter choice is wrong :")
main()
'''










'''
def summm(a):
    if a%2==0:
        print("even")
    else:
        prinr("odd")
        return a
def summ():
    a=int(input("number:"))
    return a
b=summ()
t=summm(b)
'''








'''
import math
print(math.sqrt(64))
print(math.factorial(5))
'''








'''
import ashrafashu
print(cal.add_(2,3))
'''








'''
try:
    num=100000000000000000000
    n=int(input("enter:"))
    print(1%num)
    print(n)
except(ZeroDivisionError,ValueError):
    print("Zer0")
    print("enter number")
'''









'''
class book:
    def display(self):
        print("my name is syed")
s1=book()
s1.display()
'''







'''
calss dog:
    def bark(self):
        return "woof! woof!"
dog=dog()
print(dog.bark())
'''








'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1 = Student("Syed", 20)
s1.show()
'''








'''
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def show(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
c1 = Car("Audi", "Black")
c1.show()
'''







'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance: ₹", self.balance)
account = BankAccount("Ashraf", 10000000000000000000000000000000000000000)
account.show_balance()
'''







'''
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def result(self):
        if self.marks > 50:
            return "Pass"
        else:
            return "Fail"
    def display(self):
        print("Student Name :", self.name)
        print("Roll Number  :", self.roll_no)
        print("Marks        :", self.marks)
        print("Result       :", self.result())
        print("__detail__")
student1 = Student("syed", "101", 85)
student2 = Student("Ashraf", "102", 45)
student1.display()
student2.display()
'''








'''
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
    def display(self):
        print("Employee ID :", self.emp_id)
        print("Employee Name :", self.name)
        print("Basic Salary :", self.basic_salary)
    def bonus(self):
        if self.basic_salary >= 50000000000000000:
            bonus = self.basic_salary * 0.10
        else:
            bonus = self.basic_salary * 0.05
        print("Bonus Amount :", bonus)
        print("-" * 30)
e1 = Employee(101, "Ashraf", 60000000)
e2 = Employee(102, "syed", 450000000)
e3 = Employee(103, "ali", 750000000)
e4 = Employee(104, "Kavin", 30000000)
e5 = Employee(105, "Anitha", 50000000)
employees = [e1, e2, e3, e4, e5]
for emp in employees:
    emp.display()
    emp.bonus()
'''









'''
class Movie:
    def __init__(self, movie_name, director_name, rating):
        self.movie_name = movie_name
        self.director_name = director_name
        self.rating = rating
    def display(self):
        print("Movie Name :", self.movie_name)
        print("Director   :", self.director_name)
        print("Rating     :", self.rating)
        print()
movie1 = Movie("Leo", "Lokesh Kanagaraj", 4.8)
movie2 = Movie("RRR", "S.S.Rajamouli", 4.9)
movie1.display()
movie2.display()
'''





'''
class Laptop:
    def __init__(self, brand, ram)://///////
        self.brand = brand
        self.ram = ram
    def display(self):
        print("Brand :", self.brand)
        print("RAM   :", self.ram)
        print()
laptop1 = Laptop("Dell", "8 GB")
laptop2 = Laptop("HP", "16 GB")
laptop1.display()
laptop2.display()
'''





'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
name = input("Enter Name: ")
age = int(input("Enter Age: "))
s = Student(name,age)
s.display()
'''





'''
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
    def display(self):
        print("\nEmployee Details")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("Salary      :", self.salary)
n=int(input("Enter the number of employees: "))
employees=[]
for i in range(n):
    print(f"\nEnter details for Employee {i+1}")
    emp_id=input("Enter Employee ID: ")
    name=input("Enter Name: ")
    department=input("Enter Department: ")
    salary=float(input("Enter Salary: "))
'''



'''
def find_topper(data):
    if data:
        topper = max(data, key=data.get)
        print("Topper:", topper)
        print("Marks:", data[topper])
    else:
        print("No valid records found.")
students = {}
try:
    with open("students.txt", "r") as file:
        for line in file:
            try:
                name, marks = line.strip().split(",")
                students[name] = int(marks)
            except ValueError:
                print("Invalid Record:", line.strip())
    print("Student Dictionary:")
    print(students)
    find_topper(students)
except FileNotFoundError:
    print("students.txt file not found.")
'''


'''
calss Animal:
    def eat(self):
        print("Animal is eating"
class car(Animal):
    def cat(self):
        print("cat is sleeping")
c=cat()
c.eat()
c.cat()
'''



'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name :", self.name)
        print("Age  :", self.age)
class Student(Person):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
    def display_student(self):
        self.display_person()
        print("Weight :", self.weight)
name = input("Enter Name: ")
age = int(input("Enter Age: "))
weight = float(input("Enter Weight: "))
s = Student(name, age, weight)
print("\nStudent Details")
s.display_student()
'''


'''
class vehicle:
    def __init__(self,  brand, model):
        self.brand = brand
        self.model = model
    def display_vehicle(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
class car(vehicle):
    def __init__(self, brand, model, fuel_type, seating):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.seating = seating
    def display_car(self):
        self.display_vehicle()
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Seating Capacity: {self.seating}")
s1 = car("Toyota", "Camry", "Petrol", 5)
s1.display_car()
s1.display_vehicle()
'''



'''
class securebank:
    def __init__(self, username, password, balance):
        self.username=username
        self.password=password
        self.balance=balance
        self.otp=1234  
        
    def login(self, u, p):
        if u==self.username and p==self.password:
            print("login succes")
            return True
        else:
            print("wrong pass and name")
            return False
            
    def verify_otp(self, otp):
        if otp == self.otp:
            print("otp verified")
            return True
        else:
            print("wrong otp")
            return False
            
    def show_balance(self):
        print("your balanace", self.balance)
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("withdraw", amount)
            print("balance", self.balance)
        else:
            print("no balance")
# User kitta input vaanguren
u = input("Enter username: ")
p = input("Enter password: ")
bal = int(input("Enter balance: "))
bank=securebank(u, p, bal)
if bank.login(input("Login username: "), input("Login password: ")):
    if bank.verify_otp(int(input("Enter OTP: "))):
        bank.show_balance()
        bank.withdraw(int(input("Enter amount to withdraw: ")))
'''


'''
class Customer:
    def __init__(self, customer_name, mobile_number):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
    def customer(self):
        print("Customer Name :", self.customer_name)
        print("Mobile Number :", self.mobile_number)
class Order(Customer):
    def __init__(self, customer_name, mobile_number, product_name, quantity, price):
        super().__init__(customer_name, mobile_number)
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.total = 0
    def calculate_total(self):
        self.total = self.quantity * self.price
        print("Product Name :", self.product_name)
        print("Quantity     :", self.quantity)
        print("Price        :", self.price)
        print("Total Amount :", self.total)
'''



'''
class Customer:
    def __init__(self, customer_name, mobile_number):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
    def customer(self):
        print("Customer Name :", self.customer_name)
        print("Mobile Number :", self.mobile_number)
class Order(Customer):
    def __init__(self, customer_name, mobile_number, product_name, quantity, price):
        super().__init__(customer_name, mobile_number)
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.total = 0
    def calculate_total(self):
        self.total = self.quantity * self.price
        print("Product Name :", self.product_name)
        print("Quantity     :", self.quantity)
        print("Price        :", self.price)
        print("Total Amount :", self.total)
'''








'''
class Customer:
    def __init__(self, customer_name, mobile_number):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
    def customer(self):
        print("Customer Name :", self.customer_name)
        print("Mobile Number :", self.mobile_number)
class Order(Customer):
    def __init__(self, customer_name, mobile_number, product_name, quantity, price):
        super().__init__(customer_name, mobile_number)
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.total = 0
    def calculate_total(self):
        self.total = self.quantity * self.price
        print("Product Name :", self.product_name)
        print("Quantity     :", self.quantity)
        print("Price        :", self.price)
        print("Total Amount :", self.total)
class Payment(Order):
    def make_payment(self):
        if self.total > 0:
            print("Payment Status : Payment Successful")
        else:
            print("Payment Status : Payment Failed")
name = input("Enter Customer Name: ")
mobile = input("Enter Mobile Number: ")
product = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price: "))
p = Payment(name, mobile, product, quantity, price)
print("\nCustomer Details")
p.customer()
print("\nOrder Details")
p.calculate_total()
print("\nPayment Details")
p.make_payment()
'''










'''
class UserLogin:
    def __init__(self):
        self.username = "customer"
        self.password = "123"
    def login(self, uname, pwd):
        if uname == self.username and pwd == self.password:
            print("Login Successful")
            return True
        else:
            print("Login Failed")
            return False
class FoodOrder:
    def __init__(self):
        self.menu = {
            "pizza": 250,
            "burger": 150,
            "vegroll": 100
        }
    def place_order(self, food_name, quantity):
        food_name = food_name.lower()
        if food_name in self.menu:
            total = self.menu[food_name] * quantity
            return food_name, quantity, total
        else:
            print("Food item are unailable.")
            return None, None, None
class FoodDelivery(UserLogin, FoodOrder):
    def __init__(self):
        UserLogin.__init__(self)
        FoodOrder.__init__(self)
    def generate_bill(self):
        uname = input("Enter Username: ")
        pwd = input("Enter Password: ")
        if self.login(uname, pwd):
            food = input("Enter Food Name: ")
            qty = int(input("Enter Quantity: "))
            item, quantity, total = self.place_order(food, qty)
            if item:
                print("\n ORDER BILL ")
                print("Food Name :", item)
                ("Quantity  :", quantity)
                print("Total Amt :", total)
                print("Order Confirmed")
        else:
            print("Cannot place order.")
obj = FoodDelivery()
obj.generate_bill()
'''





'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Doctor(Person):
    def __init__(self, name, age, department):
        Person.__init__(self, name, age)
        self.department = department
    def doctor_info(self):
        print("\nDoctor Details")
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Department :", self.department)
class Patient(Person):
    def __init__(self, name, age, disease):
        Person.__init__(self, name, age)
        self.disease = disease
    def patient_info(self):
        print("\nPatient Details")
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Disease :", self.disease)
class MedicalInfo(Doctor, Patient):
    def __init__(self, name, age, department, disease, internet_id):
        Doctor.__init__(self, name, age, department)
        Patient.__init__(self, name, age, disease)
        self.internet_id = internet_id
    def internet_info(self):
        print("Internet ID :", self.internet_id)
name = input("Enter Name: ")
age = int(input("Enter Age: "))
department = input("Enter Department: ")
disease = input("Enter Disease: ")
internet_id = input("Enter Internet ID: ")
obj = MedicalInfo(name, age, department, disease, internet_id)
obj.doctor_info
obj.patient_info()
obj.internet_info()
'''





'''
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_user(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.post_name = ""
    def enroll_post(self):
        self.post_name = input("Enter post name: ").strip()
        if self.post_name:
            print("Enrollment successful!")
        else:
            print("Please enter a post name.")
class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.course_name = ""
    def create_course(self):
        self.course_name = input("Enter course name: ").strip()
        if self.course_name:
            print("Course creation successful!")
        else:
            print("Course name cannot be empty.")
if __name__ == "__main__":
    print("--- STUDENT DETAILS ---")
    student1 = Student("Alice", "alice@example.com")
    student1.display_user()
    student1.enroll_post()
    print("\n" + "=" * 30 + "\n")
    print("--- INSTRUCTOR DETAILS ---")
    instructor1 = Instructor("Dr. Smith", "smith@example.com")
    instructor1.display_user()
    instructor1.create_course()
'''







class BankAccount:
    def __init__(self):
        self.__balance = 0   # Private variable
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited Successfully")
        else:
            print("Invalid Deposit Amount")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")
    def getBalance(self):
        print("Current Balance:", self.__balance)
account = BankAccount()
while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. See Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter withdraw amount: "))
        account.withdraw(amount)
    elif choice == 3:
        account.getBalance()
    elif choice == 4:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
