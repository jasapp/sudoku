def empty_board():
    a = [0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0]
    return a

def empty_spots(a):
    a = [i for i,x in enumerate(a) if x == 0]
    return a

def offset(a, b):
    a = [x + b for x in a]
    return a
