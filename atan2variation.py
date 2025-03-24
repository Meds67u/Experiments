def atan2(y,x):
    if y == 0 and x == 0:
        return float(0) 
    elif y == 0 and x == -1:
        return pi
    elif y == 0 and x == 1:
        return float(0)
    else:
        return atan(y/x) - pi * sign(y) * sign(min(0,x))
#It is important to consider when a function with a single argument atan : x = 0 when division by zero occurs
