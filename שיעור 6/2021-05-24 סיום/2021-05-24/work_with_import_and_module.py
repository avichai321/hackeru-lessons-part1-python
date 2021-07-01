print("into work_with_module.py ")


import demo_gil as fabi

fabi.sayHolala()

print(fabi.x)



import work_with_import_and_module_1

work_with_import_and_module_1.say_hola()
print( work_with_import_and_module_1.x ) # 10

work_with_import_and_module_1.x = 100
print( work_with_import_and_module_1.x )  # 100


import work_with_import_and_module_2 as gal

gal.plus()

x = gal.plus()
print("x = ", x)
