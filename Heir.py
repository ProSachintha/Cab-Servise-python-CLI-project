print("\t--------------------------")
print("\tWelcome TO SSG Cab service")
print("\t--------------------------\n")
print("What Are You Looking For ?\n")
print("\t 01\t Car")
print("\t 02\t Van ")
print("\t 03\t Three Weel")
print("\t 04\t Truck ")
print("\t 05\t Lorry ")

x=int(input(" Enter Your Choice :- "))

if x==1:
    import Car
elif x==2:
    import Van
elif x==3:
    import Three_Weel
elif x==4:
    import Truck
elif x==5:
    import Lorry