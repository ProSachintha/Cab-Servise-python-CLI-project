import Variable
scode=""
print("\t--------------------------")
print("\tWelcome TO SSG Cab service")
print("\t--------------------------\n")

type=int(input(" \t-----------------\n\tvehical type\n\t----------------- \n01\tCar\n02\tVan\n03\tThree Weal\n04\tTruck\n05\tLorry\nEnter Your Choice"))



if type==1:
    orner_name = input(" Enter Your Name :- ")
    orner_nic = input(" Enter Your NIC :- ")
    id = input(" Enter Your Vehicle registation number :- ")
    model=int(input("Please enter Your Vehicle Type\n 01\tAC\n 02\tNon AC\nEnter Your Choice :-"))
    if model==1:
        Variable.car_type.append("AC")
    elif model==2:
        Variable.car_type.append("Non AC")
    else:
        print("Please enter valid choice")


    pas = int(input("Please enter Your Vehicle Type\n 01\t3 Passenger\n 02\t4 Passenger\nEnter Your Choice :- "))

    if pas==1:
        Variable.car_pass.append("03 passenger")
    elif pas==2:
        Variable.car_pass.append("04 passenger")
    else:
        print("Please enter valid choice")

    Variable.car.append(id)
    Variable.passcode+=1
    scode="C"+str(Variable.passcode)

    print("Your Vehical Add Successfuly and pember this coad ",scode)


elif type==2:
    orner_name = input(" Enter Your Name :- ")
    orner_nic = input(" Enter Your NIC :- ")
    id = input(" Enter Your Vehicle registation number :- ")

    model = int(input("Please enter Your Vehicle Type\n 01\tAC\n 02\tNon AC\nEnter Your Choice :-"))
    if model == 1:
        Variable.van_type.append("AC")
    elif model == 2:
        Variable.van_type.append("Non AC")
    else:
        print("Please enter valid choice")

    pas = int(input("Please enter Your Vehicle Type\n 01\t6 Passenger\n 02\t8 Passenger\nEnter Your Choice :-"))

    if pas == 1:
        Variable.van_pass.append("06 passenger")
    elif pas == 2:
        Variable.van_pass.append("08 passenger")
    else:
        print("Please enter valid choice")

    Variable.van.append(id)
    Variable.passcode += 1
    scode = "V" + str(Variable.passcode)

    print("Your Vehical Add Successfuly and pember this coad ", scode)



elif type==3:
    orner_name = input(" Enter Your Name :- ")
    orner_nic = input(" Enter Your NIC :- ")
    id = input(" Enter Your Vehicle registation number :- ")

    Variable.tree_weal.append(id)

    Variable.passcode += 1
    scode = "TV" + str(Variable.passcode)

    print("Your Vehical Add Successfuly and pember this coad ", scode)


elif type==4:
    orner_name = input(" Enter Your Name :- ")
    orner_nic = input(" Enter Your NIC :- ")
    id = input(" Enter Your Vehicle registation number :- ")

    model = int(input("Please enter Your Vehicle Type\n 01\t7 Feet\n 02\t12 Feet\nEnter Your Choice :- "))
    if model == 1:
        Variable.truck_type.append("07 Feet")
    elif model == 2:
        Variable.truck_type.append("12 Feet")
    else:
        print("Please enter valid choice")

    Variable.truck.append(id)

    Variable.passcode += 1
    scode = "TR" + str(Variable.passcode)

    print("Your Vehical Add Successfuly and pember this coad ", scode)
elif type==5:
    orner_name = input(" Enter Your Name :- ")
    orner_nic = input(" Enter Your NIC :- ")
    id = input(" Enter Your Vehicle registation number :- ")

    model = int(input("Please enter Your Vehicle Type\n 01\t2500Kgt\n 02\t3500Kg\nEnter Your Choice :-"))
    if model == 1:
        Variable.truck_type.append("2.5t")
    elif model == 2:
        Variable.truck_type.append("3.5t")
    else:
        print("Please enter valid choice")

    Variable.lorry.append(id)
    Variable.passcode += 1
    scode = "L" + str(Variable.passcode)

    print("Your Vehical Add Successfuly and pember this coad ", scode)
else:
    print("Please Enter Valid Choice")

import main
