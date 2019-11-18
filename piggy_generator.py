name = input ("Enter name :")

if len(name) >= 30 or len(name) == 0:
    print("Ooops! That's not good for piggy!>_<")
    exit()

elif len(name)%2 == 0:
    add_spaces = 30 - len(name)
    name_length=len(name)+add_spaces  
    name=name.center(name_length)

else:
    front_spaces = (30 - len(name))//2
    back_spaces = front_spaces + 1
    back_length=len(name)+back_spaces
    name=name.ljust(back_length)
    front_length=len(name)+front_spaces
    name=name.rjust(front_length)

print('   M_________________________')
print("  /                          \\")
print(" /   .                        \\")
print(f"O{name}Q")
print(" \\                            /")
print("  \\  ______________________  / ")
print("    W                       W")
