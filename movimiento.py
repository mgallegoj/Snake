def up(t):
    if t[0][0]-1 < 0:
        return False
    return (t[0][0]-1, t[0][1])

def left(t):
    if t[0][1]-1 < 0:
        return False
    return (t[0][0], t[0][1]-1)

def down(t):
    if t[0][0]+1 > 12:
        return False
    return (t[0][0]+1, t[0][1])

def right(t):
    if t[0][1]+1 > 12:
        return False
    return (t[0][0], t[0][1]+1)

