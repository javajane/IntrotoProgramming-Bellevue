#Author: Pinaki Vazarkar
#Professor: Jordan Moline
"""
create class Vehicle with attributes: make, model,color, fuelType,options and
methods:getMake,getModel,getColor,getFuelType,getOptions
power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, navigation, heated seats, heated steering wheel).

Create a Car class as a child of the Vehicle class with attributes engineSize, numDoors and
methods: getEngineSize(), getNumDoors()

Create a Pickup class as a child of the Vehicle class with attributes cabStyle and bedLength
methods: getCabStyle(), getBedLength()

"""

import sys

class Vehicle:

    def __init__(self, make, model, color, fuelType, optionslist):
        self.make=make
        self.model=model
        self.color=color
        self.fuelType=fuelType

        self.power_mirrors=optionslist[0]
        self.power_locks=optionslist[1]
        self.remote_start=optionslist[2]
        self.backup_camera=optionslist[3]
        self.bluetooth=optionslist[4]
        self.cruise_control=optionslist[5]
        self.navigation=optionslist[6]
        self.heated_seats=optionslist[7]
        self.heated_steering=optionslist[8]


    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getFuelType(self):
        return self.fuelType

    def getColor(self):
        return self.color

    def getOptions(self):
        myreturnstr="Power Mirrors: "+self.power_mirrors+ " Power Locks: "+self.power_locks
        myreturnstr+=" Remote Start: "+self.remote_start + " Backup Camera: "+self.backup_camera
        myreturnstr+=" Bluetooth: "+self.bluetooth+" Cruise Control: "+self.cruise_control
        myreturnstr+=" Navigation: "+self.navigation+" Heated Seats: "+self.heated_seats
        myreturnstr+=" Heated Steering: "+self.heated_steering

        return myreturnstr


class Car(Vehicle):

    def __init__(self, make, model, color, fuelType,engineSize, numDoors, options):
        Vehicle.__init__(self,make, model, color, fuelType, options)
        self.engineSize = engineSize
        self.numDoors = numDoors
        self.type='Car'

    def getEngineSize(self):
        return self.engineSize

    def getNumDoors(self):
        return self.numDoors

    def __str__(self):
        return(self.make+" "+self.model+" "+self.color+" "+self.fuelType+" "+self.engineSize+" "+self.numDoors)


class Pickup(Vehicle):

    def __init__(self, make, model, color, fuelType,cabStyle, bedLength, options):
        Vehicle.__init__(self,make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength
        self.type='Pick-Up'

    def getCabStyle(self):
        return self.cabStyle

    def getBedLength(self):
        return self.bedLength

def printMainMenu():

    print ("Please enter a Car or Pickup to start building your vehicle")
    print ("You will need to add at least one Car and one Pickup to your garage\n")
    print("The following will be required to build your vehicle: Make, Model, Color, FuelType, ")

def buildOptions():
    print("Please select additional options")
    optionsdict={'power mirrors':'No',
                 'power locks':'No',
                 'remote start':'No',
                 'backup camera':'No',
                 'bluetooth':'No',
                 'cruise control':'No',
                 'navigation':'No',
                 'heated seats':'No',
                 'heated steering':'No'
    }

    for k in optionsdict.keys():
        ans='something'
        while ans.lower() not in ['yes', 'no', '']:
            if ans=='':
                ans='No'
            ans = input("Please enter Yes or No for {}: ".format(k))
        optionsdict[k]=ans.title()

    return optionsdict


def builduservehicle():

    build_a_vehicle=False
    attribarray=['make', 'model', 'color', 'fueltype']
    descdict = {}

    while not build_a_vehicle:
        type=input("Please enter a Vehicle type: Car or Pickup: ")
        type=type.lower()
        if type not in ['car', 'pickup']:
            continue
        if type=='car':
            attribarray.extend(['enginesize', 'numdoors'])
        else:
            attribarray.extend(['cabstyle', 'bedlength'])

        for input_type in attribarray:
            ans=""
            while ans=="":
                ans=input("Please enter {i} for your {v} ".format(i=input_type, v=type))

            descdict[input_type]=ans

        build_a_vehicle=True

    #get options from the user
    optionsdict=buildOptions()
    # attribarray.append(optionsdict.values())
    # print("OPTIONS VALUES ", optionsdict.values().to_list())

    if type=='car':
        print("ATTRIB ", attribarray)
        #vehicle=Car(attribarray)
        vehicle=Car(descdict['make'],descdict['model'],descdict['color'], descdict['fueltype'], descdict['enginesize'], descdict['numdoors'], list(optionsdict.values()))
    if type=='pickup':
        vehicle=Pickup(descdict['make'],descdict['model'],descdict['color'], descdict['fueltype'], descdict['cabstyle'], descdict['bedlength'], list(optionsdict.values()))

    return vehicle


def printInventory(inventory):
    print("\n*****Here are the vehicles in your Pink's Virtual Garage*****\n")
    counter=1
    for item in inventory:
        print("Vehicle #{}".format(counter))
        if isinstance(item, Car):
            print(item.type + " " + item.getMake() + " ", item.getModel() + " " + item.getFuelType() + " " + item.getColor() + " " + item.getEngineSize() + " " + item.getNumDoors() + " "+ item.getOptions())
        else:
            print(item.type + " " + item.getMake() + " ", item.getModel() + " " + item.getFuelType() + " " + item.getColor() + " " + item.getCabStyle() + " " + item.getBedLength()+ " "+ item.getOptions())
        print("---------------------------------------\n")
        counter+=1

    return

if __name__=='__main__':

    vehicles=[]

    #welcome user and prompt user to pick a car or a pickup
    print("**************Hello!  Welcome to Pink's virutal garage!*******************\n")

    garagebuilt=False
    carcounter=0
    pickupcounter=0

    while not garagebuilt:

        printMainMenu()

        while True:
            vehicle=builduservehicle()
            if isinstance(vehicle, Car):
                carcounter+=1
            elif isinstance(vehicle, Pickup):
                pickupcounter+=1

            print("You have added a {} in your garage \n".format(vehicle.type))

            vehicles.append(vehicle)

            if carcounter>=1 and pickupcounter>=1:
                print("Great work!  You have at least one car and one pick-up in your garage \n")
                ans=input("If you would like to quit, please enter q quit or c to continue adding to your garage\n")
                if ans.lower()[0]=='q':
                    garagebuilt=True
                    break


        print("Thank you for visiting Pink's Virtual Garage\n")
        #print("Here is what your garage currently has ", vehicles)
        printInventory(vehicles)
        sys.exit()






