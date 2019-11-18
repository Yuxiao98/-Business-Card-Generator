name = input ("Enter name :")

if len(name) >= 30 or len(name) == 0:
    print("Ooops! That's not good for piggy!>_<")
    exit()

name = name.center(30)

print('   M_________________________')
print("  /                          \\")
print(" /   .                        \\")
print(f"O{name}Q")
print(" \\                            /")
print("  \\  ______________________  / ")
print("    W                       W")
