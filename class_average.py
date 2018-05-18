
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):
  """Calculate average grade.
  Args:
    numbers (float): grade number
  Returns:
    average_grade (float): the average of grades for each subject
  """
  total = sum(numbers)
  total = float(total)
  average_grade = total/len(numbers)
  
  return average_grade

def get_average(student):
  """Calculate student average.
  Args:
    student ():
  Returns:
   student_average ():
  """
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  student_average = 0.1 * homework + 0.3 * quizzes + 0.6 * tests
  
  return student_average

def get_class_average(class_list):
  """Calculate class average.
  Args:
    class_list (list):
  Returns:
    student_avg ():
  """
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
    
  return average(results)


students = [lloyd, alice, tyler]
print get_class_average(students)
