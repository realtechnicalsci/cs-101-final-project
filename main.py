import json

# You do not need to worry about reading data from files. Reading in all of the data to the
# maui_high, maui_waena_intermediate, and lokelani_intermediate lists is handled for you.
maui_high = []
with open("MauiHigh.csv") as maui_high_file: # opens the file with data on Maui High
    for student in maui_high_file: # this goes through the file one line at a time
        student = student.split(",") # this splits the line of data into a list
        student[-1] = student[-1].strip() # this removes the "\n" from the end of the last item
        maui_high.append(student) # this adds the item to the list

maui_waena_intermediate = []
with open("MauiWaenaIntermediate.csv") as maui_waena_intermediate_file:
    for student in maui_waena_intermediate_file:
        student = student.split(",")
        student[-1] = student[-1].strip()
        maui_waena_intermediate.append(student)

lokelani_intermediate = []
with open("LokelaniIntermediate.csv") as lokelani_intermediate_file:
    for student in lokelani_intermediate_file:
        student = student.split(",")
        student[-1] = student[-1].strip()
        lokelani_intermediate.append(student)

class Student:
    #TODO: Complete this class. You will need to add additional methods.
    def __init__(self, student_data):
      if len(student_data) == 5:
        #TODO: Complete this method to initialize student data. Be sure to use the variables outlined here (also seen in the __repr__ method)
        # student_data should be a list with containing:
        # name at index 0 (make this a string)
        self.name = str(student_data[0])
        # grade at index 1 (make this an int)
        self.grade = int(student_data[1])
        # graduation_requirements at index 2 (make this a boolean - True if they've been met, False if they haven't)
        self.graduation_requirements = student_data[2]
        if self.graduation_requirements == "met" or self.graduation_requirements == "True":
            self.graduation_requirements = True
        elif self.graduation_requirements == "not met" or self.graduation_requirements == "False":
            self.graduation_requirements = False
        # credits at index 3 (make this an int)
        self.credits = int(student_data[3])
        # transferring at index 4 (make this a boolean - True if they're transferring, False if they're not)
        self.transferring = student_data[4]
        if self.transferring == "transferring" or self.transferring == "True":
            self.transferring = True
        elif self.transferring == "not transferring" or self.transferring == "False":
            self.transferring = False
      
      elif len(student_data) == 3:
        self.name = str(student_data[0])
        self.grade = int(student_data[1])
        #self.high_school = str(student_data[2])
        self.graduation_requirements = False
        self.credits = 0
        self.transferring = False
        
        
        

        
    
    # defines the "less than" method for students (for sorting purposes)
    def __lt__(self, other):
        # This method has already been completed for you. Do NOT mess with it (for grading reasons).
        return self.name < other.name

    # provides a string representation of a student
    def __repr__(self):
        # This method has already been completed for you. Do NOT mess with it (for grading reasons).
        return self.name + "," + str(self.grade) + "," + str(self.graduation_requirements) + "," + str(self.credits) + "," + str(self.transferring)

# new_maui_high is a list for next year's student data. When you're finished, it should contain
# a list of Student objects updated for next school year.
graduating = 0
freshmen = 0
sophomores = 0
juniors = 0
seniors = 0
total_seniors = 0
waena = 0
loke = 0

new_maui_high = []
for student in maui_high:
  new_student = Student(student)
  if new_student.grade == 12:
    total_seniors += 1
    
  if new_student.grade == 9 and new_student.credits < 13 and new_student.transferring == False:
    freshmen += 1
    new_maui_high.append(new_student)

  if new_student.grade == 10 and new_student.credits < 26 and new_student.transferring == False:
    sophomores += 1
    new_maui_high.append(new_student)

  if new_student.grade == 11 and new_student.credits < 39 and new_student.transferring == False:
    juniors += 1
    new_maui_high.append(new_student)

  if new_student.grade == 12 and (new_student.credits < 52 or new_student.graduation_requirements == False) and new_student.transferring == False:
    seniors += 1
    new_maui_high.append(new_student)
    
  if new_student.grade == 9 and new_student.credits > 12 and new_student.transferring == False:
    new_student.grade = 10
    sophomores += 1
    new_maui_high.append(new_student)
    
  if new_student.grade == 10 and new_student.credits > 25 and new_student.transferring == False:
    new_student.grade = 11
    juniors += 1
    new_maui_high.append(new_student)
    
  if new_student.grade == 11 and new_student.credits > 38 and new_student.transferring == False:
    new_student.grade = 12
    seniors += 1
    new_maui_high.append(new_student)
    
  if new_student.grade == 12 and new_student.credits > 51 and new_student.graduation_requirements:
    graduating += 1
    new_student.grade += 1

for student in maui_waena_intermediate:
  if student[2] != "Maui High":
    continue
  new_student = Student(student)
  if new_student.grade == 8:
    new_student.grade = 9
    freshmen += 1
    waena += 1
    new_maui_high.append(new_student)
  if new_student.grade == 7:
    continue

for student in lokelani_intermediate:
  if student[2] != "Maui High":
    continue
  new_student = Student(student)
  if new_student.grade == 8:
    new_student.grade = 9
    loke += 1
    freshmen += 1
    new_maui_high.append(new_student)
  if new_student.grade == 7:
    continue
    
#print(str(new_maui_high))
# stats is a dictionary. It has already been created for you with all of the data that you need.
# All you need to take care of is updating these values. This is easy to do. If you'd like to
# set "graduating" to 74, for instance, all you have to do is:
# stats["graduating"] = 74
stats = {
		"graduating":0, # the number of students who will be graduating this year
		"graduation_rate":0.0, # the number of students graduating divided by the total number of seniors this year (NOT next year's seniors)
		"maui_waena_incoming":0, # the number of students coming to Maui High from Maui Waena Intermediate
		"lokelani_incoming":0, # the number of students coming to Maui High from Lokelani Intermediate
		"freshmen":0, # the number of freshman for next year
		"sophomores":0, # the number of sophomores for next year
		"juniors":0, # the number of juniors for next year
		"seniors":0 # the number of seniors for next year
}

#TODO: Write the rest of your code
stats["graduating"] = graduating
#print(str(stats["graduating"]))

stats["graduation_rate"] = graduating / total_seniors
#print(str(stats["graduation_rate"]))

stats["maui_waena_incoming"] = waena
#print(str(stats["maui_waena_incoming"]))

stats["lokelani_incoming"] = loke
#print(str(stats["lokelani_incoming"]))

stats["freshmen"] = freshmen
#print(str(stats["freshmen"]))

stats["sophomores"] = sophomores
#print(str(stats["sophomores"]))

stats["juniors"] = juniors
#print(str(stats["juniors"]))

stats["seniors"] = seniors
#print(str(stats["seniors"]))




def add_student():
  name = input("Enter student name:")
  current_credits = input("Current credits:")
  new_grade = input("New grade: ")
  student_data = [name, new_grade, False, current_credits, False]
  new_student = Student(student_data)
  new_maui_high.append(new_student)




def look_up_student():
  nameornumber = input("Are you searching by name?: ").lower()
  if "y" in nameornumber:
    name = input("What student are you trying to look up?: ").lower()
    z = -1
    for student in new_maui_high:
      z += 1
      #new_student = Student(student)
      if name in str(student.name).lower():
        print(str(z) + ": " + str(student))
  
    #pass
  if "n" in nameornumber:
    number = int(input("What number are they?: "))
    z = -1
    for student in new_maui_high:
      z+= 1
      if number == z:
        print(str(z) + ": " + str(student))






def update_student():
  name = input("What student do you want to change?:")
  z = -1
  for student in new_maui_high:
    z += 1
    #new_student = Student(student)
    if name == student.name:
      print(str(z) + ": " + str(student))
  student_number = int(input("Select the number of the person you would like to use: "))
  print("Time to enter some new information")
  new_grade = input("Enter their updated grade: ")
  can_graduate = input("Can they graduate (True/False): ")
  updated_current_credits = input("Enter their updated amount of credits: ")
  updated_transfer = input("Is this student transfering? (True/False): ")
  #print(new_maui_high[student_number])
  name_new = new_maui_high[student_number].name
  #print(name_new)
  #new_name = name_new[0] + " " + name_new[1]
  #print(new_name)
  student_data = [name_new, str(new_grade), str(can_graduate), str(updated_current_credits), str(updated_transfer)]
  new_maui_high[student_number] = Student(student_data)



while True:
  print("Options")
  print("Add New Student: 'a'")
  print("Student Look Up: 'b'")
  print("Student Update: 'c'")
  print("Finish: 'x'")
  option = input("Enter your option: ")
  print("")
  if option == 'a':
    add_student()
  if option == 'b':
    look_up_student()
  if option == 'c':
    update_student()
  elif option == 'x':
    break









# Keep all of the following code at the BOTTOM of the file (after all of the code you add).
# Sorting and writing your updated new_maui_high data to a file is taken care of for you here.
new_maui_high.sort()
with open("MauiHighUpdated.csv", "w") as maui_high_updated_file:
    for student in new_maui_high:
        maui_high_updated_file.write(repr(student) + "\n")

# Writing your stats to a file is taken care of for you here.
with open("Stats.json", "w") as stats_file:
    json.dump(stats, stats_file, indent=4)

# After running this file, run CS 101 Final Project Checker.py to see if you got everything right!