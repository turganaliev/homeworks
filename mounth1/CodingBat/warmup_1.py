def sleep_in(weekday, vacation):
  if weekday:
    if vacation:
      return True
    else:
      return False
  else:
    return True

def diff21(n):
  if n <= 21:
    diff = 21 - n
    return diff
  if n > 21:
    diff1 = n - 21
    return diff1*2

def near_hundred(n):
  if n in range(90, 111):
    return True
  elif n in range(190, 211):
    return True
  else:
    return False

def missing_char(str, n):
  new = str.replace(str[n], "")
  return new


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if a_smile or b_smile:
        return False
    else:
        return True

def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
    else:
      return False
  else:
    return False

def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if a > 0 and b < 0:
      return True
    if a < 0 and b > 0:
      return True
    else:
      return False

def front_back(str):
  if len(str) > 1:
    first = str[0]
    last = str[-1]
    return last + str[1:-1] + first
  else:
    return str

def sum_double(a, b):
  if a == b:
    return (a + b)*2
  else:
    return a + b

def makes10(a, b):
  return ((a == 10 or b == 10) or (a + b == 10))

def not_string(str):
  if str[0:3] == "not":
    return str
  return ("not " + str)

def front3(str):
  return (str[:3]*3)
