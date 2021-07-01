print('into file - work with try except \n')
'''
try
except
exepet NameError
else
finally


ERROR TYPE:
NameError - name 'var_name' is defined
ZeroDivisionError - try division by zero
TypeError - have problem with the type 
ValueError - have problem with the value

'''

# print(first)  # NameError: name 'x' is not defined

print("****** demo1 -  try + except ******")
try:
    print(first)  # try print first, but first is not defined
except:
    print("BOOM!!! some problem with action..")


print("\n****** demo2_a - except NameError ******")
try:
    print(first)
except NameError:  # run ONLY if have problem with NameError
    print("BOOM!!! run this line if have problem with NameError")
except:  # run if have problem in any other case
    print("BOOM!!! some problem with action..")

print("\n****** demo2_b - except TypeError ******")
x = 10
try:  # if have 2 excepts will take ONLY one..
    print('hola from ' + x)
except NameError:  # run ONLY if have problem with NameError
    print("BOOM!!!  run this line if have problem with **NameError**")
except TypeError:  # run ONLY if have problem with TypeError
    print("BOOM!!!  run this line if have problem with **TypeError**")
except:  # run if have problem in any other case
    print("BOOM!!! some problem with action..")



print("\n****** demo3 - else ******")
try:
    print(first)
except:  # run if have problem
    print("BOOM!!! some problem with action..")
else:  # run ONLY if NO have problem
    print('OK!! run this line ONLY if no have problem.. ')


print("\n****** demo4 - finally ******")
try:
    print(first)
except:  # run if have problem
    print("BOOM!!! some problem with action..")
finally:  # run anyway in the end of code..
    print('FINISH!!! run this line anyway when will finish action')



print("\n****** demo5 - try with input.. :)  ******")
try:
    x = int(input("Please enter a number: "))  # 1. try input 'Gal' try input 10
except ValueError:
    print("BOOM!!! NO number.  Try again...")
finally:
    print('finish!!!')



print("\n****** demo6 - all in one.. :)  ******")
try:
    print(first)
except NameError:
    print("BOOM!!! run this line if have problem with NameError")
except:
    print("BOOM!!!  some problem with action..")
else:
    print('OK!!! run this line ONLY if no have problem.. ')
finally:
    print('FINISH!! run this line anyway when will finish action')


