def cigar_party(cigars, is_weekend):
    if is_weekend:
        if cigars >= 40:
            return True
        else:
            return False
    else:
        if cigars in range(40, 61):
            return True
        else:
            return False

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
        if speed <= 60:
            return 0
        if speed in range(61, 81):
            return 1
        if speed >= 81:
            return 2
    else:
        if speed <= 60:
            return 0
        if speed in range(61, 81):
            return 1
        if speed >= 81:
            return 2

def love6(a, b):
  if a == 6 or b == 6:
    return True
  if a + b == 6 or a - b == 6 or b - a == 6:
    return True
  else:
    return False

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    else:
        return 1

def sorta_sum(a, b):
  if a + b in range(10, 20):
    return 20
  else:
    return a + b

def in1to10(n, outside_mode):
    if outside_mode:
        if n <= 1 or n >= 10:
            return True
        else:
            return False
    else:
        if n in range(1, 11):
            return True
        else:
            return False

def squirrel_play(temp, is_summer):
    if is_summer:
        if temp in range(60, 101):
            return True
        else:
            return False
    else:
        if temp in range(60, 91):
            return True
        else:
            return False

def alarm_clock(day, vacation):
    if vacation:
        if day in range(1, 6):
            return "10:00"
        elif day == 0 or day == 6:
            return "off"
    else:
        if day in range(1, 6):
            return "7:00"
        elif day == 0 or day == 6:
            return "10:00"

def near_ten(num):
    remainder = num % 10
    if remainder <= 2 or remainder >= 8:
        return True
    else:
        return False



