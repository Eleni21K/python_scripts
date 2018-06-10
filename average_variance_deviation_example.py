# Find how the grades varied against the average. This is called computing the variance.

# Listof grades:
grades_input = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  """Print the list of grades.
  Args:
    grades_input (list): list of grades
  """
  for grade in grades_input:
    print grade

def grades_sum(grades_input):
  """Get sum of grades.
  Args:
    grades_input (list): list or grades
  Returns:
    total (float): sum of the grades
  """
  total = 0
  for score in scores: 
    total += score

  return total
    
def grades_average(grades_input):
  """Get average of grades.
  Args:
    grades_input (list): list or grades
  Returns:
    average (float): average of the grades
  """
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))

  return average

def grades_variance(scores):
  """
  Args:

  Returns:
    result ():
  """
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average-score)**2
  result = variance/len(scores)
  
  return result


def grades_std_deviation(variance):
  result = variance**0.5
  return result

variance = grades_variance(grades)
print grades_std_deviation(variance)

print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
