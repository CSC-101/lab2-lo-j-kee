def smallest(n:float,m:float)->float:
    if n<m:
        return n # This statement is not evaluated for either calls.
    else:
        return m

first = smallest(3,2) # The value of first is 2.
second = smallest(2,2) # The value of second is 2.
print("first =",first)
print("second =",second)

def func2(a:int,b:int,c:int)->int:
    if a>b and a>c:
        return a-b # A call will only evaluate this statement when variable a is the largest integer.
    elif b>c:
        return b+c # A call will only evaluate this statement when variable b is the largest integer.
    else:
        return 2*c # A call will only evaluate this statement when variable c is the largest integer.

answer1 = func2(3,2,1) # The value of answer1 is 1.
answer2 = func2(2,3,1) # The value of answer2 is 4.
answer3 = func2(2,1,3) # The value of answer3 is 6.
print("answer1 =",answer1)
print("answer2 =",answer2)
print("answer3 =",answer3)