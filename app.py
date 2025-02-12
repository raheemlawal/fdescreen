# checks
def sort(width, height, length, mass):
    temp = 0
    # non-positive dimension or mass is impossible
    if (width <= 0 or height <= 0 or length <= 0 or mass <=0):
        return 'error' 
    if width * height * length >= 1000000 or width>=150 or height>=150 or length>=150:
        temp = temp + 1
    if mass >= 20:
        temp = temp + 1
    return dispatch(temp)

# helper function
def dispatch(t):
    if t == 0:
        stack = 'standard'
    if t == 1:
        stack = 'special'
    if t == 2:
        stack = 'rejected'
    return stack

#print(sort(1,1,1,1))