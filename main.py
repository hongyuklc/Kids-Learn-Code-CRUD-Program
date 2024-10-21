import pickle
class car: #Defining Class
    def __init__(self, model, brand, year): #First/Last Name and NRIC Parameters
        self.model = model #Storing data from instance into object
        self.brand = brand    #Storing data from instance into object
        self.year = year    #Storing data from instance into object
    def displayName(self):
        return(self.brand + " " + self.model)
    def getFullInfo(self):
        return(f"Name: {self.brand} {self.model}|Year: {self.year}")
class EV(car):
    def __init__(self, model, brand, year, batteryCapacity):
        super().__init__(model, brand, year) #Initialising the parent class parameters
        self.batteryCapacity = batteryCapacity #Intialising child class parameters
    def update(self, field, newValue):
        if field == 1:
            self.model = newValue
        if field == 2:
            self.batteryCapacity = newValue
        if field == 3:
            self.year = newValue
        if field == 4:
            self.brand = newValue
class gasCar(car):
    def __init__(self, model, brand, year, tankCapacity):
        super().__init__(model, brand, year)
        self.tankCapacity = tankCapacity
    def update(self, field, newValue):
        if field == 1:
            self.model = newValue
        if field == 2:
            self.tankCapacity = newValue
        if field == 3:
            self.year = newValue
        if field == 4:
            self.brand = newValue
def add(currentMode):
    if currentMode == 1:
        year = input("What is the year of produce?")
        model = input("What is the model?")
        brand = input("What is the brand?")
        batteryCapacity = input("What is the battery capacity?")
        EVLIST.append(EV(model, brand, year, batteryCapacity))
    else:
        year = input("What is the year of produce?")
        model = input("What is the model?")
        brand = input("What is the brand?")
        gasCapcity = input("What is the tank capicty?")
        GASCARLIST.append(gasCar(model, brand, year, gasCapcity))
def read(currentMode):
    if currentMode == 1:
        if (len(EVLIST) != 0):
            for i in range(0, len(EVLIST)):
                print(str(i+1)+")"+EVLIST[i].getFullInfo()+"|Battery Capacity: "+str(EVLIST[i].batteryCapacity))
        else:
            print("No items in EV List")
    if currentMode == 2:
        if (len(GASCARLIST) != 0):
            for i in range(0, len(GASCARLIST)):
                print(str(i+1)+")"+GASCARLIST[i].getFullInfo()+"|Tank Capacity: "+str(GASCARLIST[i].tankCapacity))
        else:
            print("No items in GAS CAR List")
def delete(currentMode):
    if currentMode == 1:
        if (len(EVLIST) != 0):
            read(1)
            try:
                index = int(input("What is the index of the item you would like to delete?"))
                EVLIST.pop(index-1)
            except ValueError:
                print("Please enter a valid index")
        else:
            print("No items in EV List to be deleted")
    else:
        if (len(GASCARLIST) != 0):
            read(2)
            try:
                index = int(input("What is the index of the item you would like to delete?"))
                GASCARLIST.pop(index-1)
            except ValueError:
                print("Please enter a valid index")
        else:
            print("No items in GASCAR List to be deleted")
def update(currentMode):
    if currentMode == 1:
        if (len(EVLIST) != 0):
            read(1)
            indexToUpdate = int(input("What is the index of the item you would like to update?"))
            while not (1 <= indexToUpdate <= len(EVLIST)):
                print("Please enter a valid index")
                indexToUpdate = int(input("What is the index of the item you would like to update?"))
            fieldToUpdate = int(input("""===What would you like to update?===
            1) Model
            2) Battery Capacity
            3) Year
            4) Brand
            """))
            while not (1 <= fieldToUpdate <= 4):
                print("Please enter a valid index")
                fieldToUpdate = int(input("What is the index of the item you would like to update?"))
            newValue = input("What is the new value?")
            EVLIST[indexToUpdate-1].update(fieldToUpdate, newValue)
        else:
            print("No items in EV List to be updated")
    if currentMode == 2:
        if (len(GASCARLIST) != 0):
            read(2)
            indexToUpdate = int(input("What is the index of the item you would like to update?"))
            while not (1 <= indexToUpdate <= len(GASCARLIST)):
                print("Please enter a valid index")
                indexToUpdate = int(input("What is the index of the item you would like to update?"))
            fieldToUpdate = int(input("""===What would you like to update?===
            1) Model
            2) Tank Capacity
            3) Year
            4) Brand
            """))
            while not (1 <= fieldToUpdate <= 4):
                print("Please enter a valid index")
                fieldToUpdate = int(input("What is the index of the item you would like to update?"))
            newValue = input("What is the new value?")
            GASCARLIST[indexToUpdate-1].update(fieldToUpdate, newValue)
        else:
            print("No items in EV List to be updated")
#Main Program
filename="cars.txt"
#Try and open the file, to load your list
try:
  f=open(filename,"rb")
  EVLIST=pickle.load(f)
  GASCARLIST=pickle.load(f)
  f.close()
  print("Data loaded...")
#if file don't exist, create 2 new lists
except:
  EVLIST=[]
  GASCARLIST=[]
  print("Creating new data...")
currentMode = 0
#The start of the while loop
while True:
    print()
    try:
        mode = int(input("""===You are in the main menu===
    EV(1)
    GASCAR(2)
    EXIT(3)
    What would you like to access?"""))
    except ValueError:
        print("Please enter a number")
        continue
    if mode == 1:
        currentMode = 1
    elif mode == 2:
        currentMode = 2
    else:
        f = open(filename, "wb")
        pickle.dump(
            EVLIST, f)
        pickle.dump(GASCARLIST, f)
        f.close()
        print("File Saved...Closing program")
        print("Bye Bye!")
        break
    while currentMode == 1:
        try:
            event = int(input(""""===You are in the EV List===
                    - Add EV (1)
                    - Read EV List (2)
                    - Update EV List (3)
                    - Delete EV (4)
                    - Exit (5)"""))
        except ValueError:
            print("Please enter a number")
        if event == 1:
            add(1)
        if event == 2:
            read(1)
        if event == 4:
            delete(1)
        if event == 3:
            update(1)
        if event ==  5:
            currentMode = 0
    while currentMode == 2:
        try:
            event = int(input(""""===You are in the Gas Car List===
                    - Add Gas Car (1)
                    - Read Gas Car List (2)
                    - Update Gas Car List (3)
                    - Delete Gas Car (4)
                    - Exit (5)"""))
        except ValueError:
            print("Please enter a number")
        if event == 1:
            add(2)
        if event == 2:
            read(2)
        if event == 4:
            delete(2)
        if event == 3:
            update(2)
        if event ==  5:
            currentMode = 0


