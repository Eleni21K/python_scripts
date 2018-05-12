"""
Destination prices
"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475

Every day you rent the car costs $40.
if you rent the car for 7 or more days, you get $50 off your total.
Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
You cannot get both of the above discounts.
"""

CODE :
def hotel_cost(nights):
  """Caclulate hotel cost
  Args:
    nights (int): number of nights at the hotel
  Returns:
    cost (int): hotel cost
  """
  cost = 140 * nights
  return cost

def plane_ride_cost(city):
  """Calculate plane ride cost
  Args:
    city (str): name of city
  Returns:
    cost (int): flight cost
  """
  if city == "Charlotte":
    cost = 183
  	return cost
  elif city == "Tampa":
    cost = 220
  	return cost
  elif city == "Pittsburgh":
    cost = 222
  	return cost
  elif city == "Los Angeles":
    cost = 475
  	return cost

 def rental_car_cost(days):
  """Calculate plane ride cost.
  Args:
    days (int): number of days
  Returns:
    cost (int): rental car cost
  """
  cost = 40*days
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city,days):
  """Calculate plane ride cost.
  Args:
    days (int): number of days
    city (str): name of city
  Returns:
    full_cost (int): full trip cost
  """
  full_cost = rental_car_cost(days)+hotel_cost(days-1)+plane_ride_cost(city)
  return full_cost
