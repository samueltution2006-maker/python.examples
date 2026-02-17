import sys
def validatedigits(phone):    # callee
    for digit in phone:
        if digit.isalpha():
            print("the given field cannot contain alphabetical values")
            sys.exit(1)

cphone = "2756789"
pnum = "600054"

validatedigits(cphone)   # caller
validatedigits(pnum)     # caller