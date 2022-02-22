def check(string):
    return len(set(string.lower()))

print(check('helo'))

def longest(a1, a2):
    a3 = []
    a4 = []
    a3.extend(a1)
    a3.extend(a2)
    a4.extend(set(a3))
    a4.sort()
    return ''.join(a4)
print(longest('abcc', 'def'))

def remove_char(s):
    return s[1:len(s)-1]
print(remove_char('country'))

def mygcd(x, y):
    list = []
    for i in x, y:
        if x % 2 == 0 and y % 2 == 0:
            list.append(int(i))
    return list[-1]
print(mygcd(30,12))