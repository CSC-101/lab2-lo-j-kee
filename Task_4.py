from typing import Optional

def checked_access(l, idx) -> Optional[int]:
    test = idx >= 0 ^ idx < len(l)
    # This test prevents returning and index that doesn't exist within the list.
    if test:
        return l[idx]
    else:
        return None

first = checked_access([1,0,1],9)
# The index value called for in first does not exist, therefore it returns None.
second = checked_access([1,0,1],2)
# The value of second is the third element in the list, which is 1.
print("Index Check 1 =",first)
print("Index Check 2 =",second)



def length_sum(x):
    if len(x)>2:
# Evaluated for "first", returning the total character length of the first three elements from the list.
        return len(x[0])+len(x[1])+len(x[2])
    elif len(x)>1:
# Evaluated for "third", returning the total character length of the first two elements from the list.
        return len(x[0])+len(x[1])
    elif len(x)>0:
# Evaluated for "second", returning the character length of the only element in the list.
        return len(x[0])
    else:
        return 0

first = length_sum(["this","is","the","first","call"])
second = length_sum(["second call"])
third = length_sum(["another","call"])
print("Character Length 1 =",first)
print("Character Length 2 =",second)
print("Character Length 3 =",third)



def surprising(x, other):
    x.append(other.upper())
    return x
#

words = ["this","is","confusing","code"]
first = surprising(words,"Avoid")
# The value of words after first is ["this","is","confusing","code","AVOID"].
second = surprising(words,"such.")
# The value of words after second is ["this","is","confusing","code","AVOID","SUCH."].
print(words)
# Since lists are mutable, first and second are aliases for words and change when second changes.