

print("\t--------------------------")
print("\tWelcome TO SSG Cab service")
print("\t--------------------------\n")
print("What Are You Looking For ?\n")
print("\t 01\t Hire A Vehical ")
print("\t 02\t Finish My Hire ")
print("\t 03\t Add A Vehical ")
print("\t 04\t Remove A Vehical ")

x=int(input(" Enter Your Choice :- "))

if x==1:

    import Heir
elif x==2:

    from Remove import finish
elif x==3:

    import Add
elif x==4:

    from Remove import remove
else:

    print("please enter valid number!!!")
    import __main__
