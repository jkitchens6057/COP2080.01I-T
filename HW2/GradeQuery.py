grades = {}

choice = 'T'

while (choice != 'Q'):
  
  choice = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()

  if choice == 'A':
    name = input("Enter the student's name: ")
    if name in grades:
      print("Sorry, that student is already present")
      continue
    grade = int(float(input("Enter the student's grade: ")))
    while not (grade >= 0 and grade <= 100):
      grade = int(float(input("Please enter the grade as a number 0-100: ")))
    grades[name] = grade
  elif choice == 'R':
    student = input("What student do you want to remove? ")
    if (student not in grades):
      print("Sorry, that student doesn't exist and couldn't be removed")
    else:
      grades.pop(student)
  elif choice == 'M':
    student = input("Enter the name of the student to modify: ")
    if (student not in grades):
      print("Sorry, that students doesn't exist and couldn't be modified")
      continue
    print("The old grade is", grades[student])
    grade = int(float(input("Enter the new grade: ")))
  elif choice == 'P':
    avg = 0;
    for student in grades:
      avg += grades[student]
    avg = avg / len(grades)
    print("The average grade is", avg)
    for student in grades:
      print(f"{student}: {grades[student]}")
  elif choice == 'Q':
    print("Goodbye!")

  else:
    print("Sorry that wasn't a valid choice.")