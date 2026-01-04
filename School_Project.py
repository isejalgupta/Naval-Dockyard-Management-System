import mysql.connector
from mysql.connector.cursor import MySQLCursor

# Admin credentials for database intialization
MASTER_ADMIN_USERNAME = "master_admin"
MASTER_ADMIN_PASSWORD = 990099

## Verification Of ship
def Shipverify():
    Shipsid = int(input("Enetr teh ship id"))
    cursor.execute("SELECT shipid FROM ships")
    new = cursor.fetchall()
    print(new)
    if (Shipsid,) in new:
        cursor.execute("SELECT * FROM ships WHERE shipid = %s",(Shipsid,),)
        row3 = cursor.fetchall()
        for row in row3:

            print('Ship ID:              ',row[0])
            print('Ship Name:            ',row[1])
            print('Ship Import From:     ',row[2])
        cursor.execute("SELECT destination,timeofarrival FROM shipdestination WHERE shipid = %s",(Shipsid,),)
        row4 = cursor.fetchall()
        for i in row4:
            print('Ship ID:              ',i[0])
            print('Ship Estimated TOA:   ',i[1])
        return(True)        
    else:
        return(False)
            
        
            
# Function to insert data into the Ships table
def insert_ship_data():
    while True:
        if Shipverify() == True:
            print("The ship already Exist and is on voyage")
            exit
        else:
            print("The ship is currently not in voyage and changes can be done")
            break

        
    qn = ["Britain","China","Malaysia","Thailand","Russia"]
    shipid = int(input("enter the ship id no.:"))
    ship_name = input("enter the name of the ship:")
    #country = input("enter the country from where the ship is coming in:")
    #destination = input("enter the destination:[Britain,India,Thailand,Malaysia,China]")
    while True:
        destination = input("enter the destination:[Britain,India,Thailand,Malaysia,China]")
        if destination not in qn:
            print("Destination not in database")
            continue
        else:
            break
    while True:
        print(["Britain","India","Thailand","Malaysia","China"])
        country = input("enter the country from where the ship is coming in:")
        if country not in qn:
            print("Country Not in database")
            continue
        if country in qn and country != destination:
            rn = destination
            break

    captain_name = input("name of the person driving the ship:")
    cursor.execute(
        "INSERT INTO ships (shipid, shipName, countryOfOrigin, captainName) VALUES (%s, %s, %s, %s)",
        (shipid, ship_name, rn, captain_name),
    )
    conn.commit()

# Function to insert data into the ShipDestinations table
def insert_destination_data():
    while True:
        if Shipverify() == False:
            print("The ship already Exist and is on voyage")
            exit
        else:
            print("The ship is currently not in voyage and changes can be done")
            break
    q = ["Britain","China","Malaysia","Thailand","Russia"]
    #country = input("enter the country from where the ship is coming in:")
    while True:
        country = input("enter the country from where the ship is coming in:")
        print(["Britain","India","Thailand","Malaysia","China"])
        if country not in q:
            print("Country Not in database")
            continue
        else:
            break
    ship_id = int(input("enter the id of the ship you want to add:"))
    #destination = input("enter the destination:[Britain,India,Thailand,Malaysia,China]")
    while True:
        destination = input("enter the destination:[Britain,India,Thailand,Malaysia,China]")
        if destination not in q:
            continue
        if destination in q and destination != country:
            r = destination
            break

        
    time_of_arrival = input("enter the time of arrival as per IST:")
    time_of_departure =input("enter the time of departure as per IST:")
    cursor.execute(
        "INSERT INTO shipDestination (shipid, destination, timeOfArrival , timeofdeparture) VALUES (%s, %s, %s, %s)",
        (ship_id, r, time_of_arrival, time_of_departure),
    )
    conn.commit()


# Function to insert data into the shipcargo table
def insert_cargo_data():
   while True:
        if Shipverify() == True:
            print("The ship already Exist and is on voyage")
            break
        else:
            print("The ship is currently not in voyage and changes can be done")
            exit
   ship_id = int(input("Enter the ship: "))
   cargo_name = input("what is in the cargo?:")
   cargoname = ["Weapons","Food","Commodities like Oil and Petrol"]
   print(cargoname)
   cargo_weight = int(input("what is the weight in kgs?:"))
   while True:
    if cargo_name in cargoname:
        if cargo_name == "Weapons":
            cargocost = cargo_weight*1000
        elif cargo_name == "Food":
            cargocost = cargo_weight*800
        elif cargo_name == "Commodities":
            cargocost = cargo_weight*1200
        break
    else:
        continue
   crew_count = int(input("how many people required to handle that cargo?:"))
   car = f"INSERT INTO shipCargo VALUES ({ship_id},'{cargo_name}',{cargo_weight},{crew_count},{cargocost})"
   cursor.execute(car)
   conn.commit()


# Function to insert new Admin, Captain or Crew
def insert_admin_data():
    username = input("Enter new admin username:")
    password = int(input("Enter password for new admin:"))

    cursor.execute('INSERT INTO admins (username, password) VALUES (%s, %s)', (username, password),)
    conn.commit()


# function to ship table's row data
def update_ship_data():
    while True:
        if Shipverify() == False:
            print("The ship already Exist and is on voyage")
            continue
        else:
            print("The ship is currently not in voyage and changes can be done")
            break
    qn = ["Britain","India","Thailand","Malaysia","China"]
    ship_id = int(input("enter ship id: "))
    ship_name = input("enter the name of the ship: ")
    print(["Britain","India","Thailand","Malaysia","China"])
    ##country = input("enter the country from where the ship is coming in: ")
    print(["Britain","India","Thailand","Malaysia","China"])
    #destination = input("enter the destination:")
    while True:
        destination = input("enter the destination:[Britain,India,Thailand,Malaysia,China]")
        if destination not in qn:
            print("Destination not in database")
        else:
            xn = destination
            break
    while True:
        print(["Britain","India","Thailand","Malaysia","China"])
        country = input("enter the country from where the ship is coming in:")
        
        if country not in qn:
            print("Country Not in database")
        if country in qn and country != destination:
            rn = country
            break
    captain_name = input("name of the person driving the ship: ")
    a = f"UPDATE ships SET shipName='{ship_name}', countryOfOrigin='{rn}', captainName='{captain_name}' WHERE shipid={ship_id}"
    cursor.execute(a)
    conn.commit()


# function  to shipDestination table's row data
def update_destination_data():
    while True:
        if Shipverify() == False:
            print("The ship already Exist and is on voyage")
            continue
        else:
            print("The ship is currently not in voyage and changes cannot be done")
            break
            
    ship_id = int(input("enter the id of the ship you want to update:"))
    #destination = input("enter the destination: ")
    q = ["Britain","India","Thailand","Malaysia","China"]
    while True:
        print(["Britain","India","Thailand","Malaysia","China"])
        country = input("enter the country from where the ship is coming in:")
       
        if country not in q:
            print("Country Not in database")
            continue
        else:
            break
    while True:
        destination = input("enter the destination:[Britain,India,Thailand,Malaysia,China]")
        if destination not in q:
            continue
        if destination in q and destination != country:
            r = destination
            break
    time_of_arrival = input("enter the time of arrival: ")
    time_of_departure = input("enter the time of departure")
    n = f"UPDATE shipDestination SET destination='{r}', timeOfArrival='{time_of_arrival}',timeofDeparture = '{time_of_departure}' WHERE shipid={ship_id}"
    cursor.execute(n)
    conn.commit()


# function  to shipCargo table's row data
def update_cargo_data():
    while True:
        if Shipverify() == False:
            print("The ship already Exist and is on voyage")
            continue
        else:
            print("The ship is currently not in voyage and changes cannot be done")
            break
  
    ship_id = int(input("enter the shipid you want to update: "))
    cargo_name = input("what is in the cargo? ")
    cargo_weight = int(input("what is the weight in kgs? "))
    crew_count = int(input("how many people required to handle that cargo? "))
    while True:
        if cargo_name in cargo_name:
            if cargo_name == "Weapons":
                cargocost = cargo_weight*1000
            elif cargo_name == "Food":
                cargocost = cargo_weight*800
            elif cargo_name == "Commodities":
                cargocost = cargo_weight*1200
            break
        else:
            continue

    q = f"UPDATE shipcargo SET CargoName='{cargo_name}', CargoWeight={cargo_weight}, CrewCount={crew_count}, Bill = {cargocost} WHERE shipid={ship_id}"
    cursor.execute(q)
    conn.commit()



# function to initiate the database if it doesn't already exists
def init_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS NavalDockyard")
    conn.commit()
    cursor.execute("USE NavalDockyard")
    conn.commit()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS captains (username varchar(30),password int)"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ships (shipid INT AUTO_INCREMENT PRIMARY KEY, shipName VARCHAR(25), countryOfOrigin VARCHAR(25), captainName VARCHAR(20))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS shipDestination (shipid INT, destination VARCHAR(25), timeOfArrival VARCHAR(15), timeofDeparture VARCHAR(15), FOREIGN KEY (shipid) REFERENCES ships(shipid))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS shipCargo (shipid INT, cargoName VARCHAR(25), cargoWeight INT, crewCount INT, Bill INT, FOREIGN KEY (shipid) REFERENCES ships(shipid))"
    )

    cursor.execute(""" CREATE TABLE IF NOT EXISTS admins (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50) NOT NULL,password VARCHAR(255) NOT NULL,role VARCHAR(50))""")

    # unlike "IF NOT EXISTS", here we need to manually check whether the admin was already added
    cursor.execute("SELECT * FROM admins WHERE username = %s", (MASTER_ADMIN_USERNAME,))
    result = cursor.fetchone()
    if result is None:
        cursor.execute(
            "INSERT INTO admins (username,password) VALUES (%s,%s)",
            (MASTER_ADMIN_USERNAME, MASTER_ADMIN_PASSWORD),
        )
    conn.commit()


# loop that adds new ship data
def add_data():
    
    print(
        """Which data would you like to insert records for?:
          1-New ship
          2-Ship voyage
          3-New ship cargo
          4-quit"""
    )
    n = input("Enter:")

    if n == "1":
        print("insert data in ships table")
        insert_ship_data()
    elif n == "2":
        print("insert destination data")
        insert_destination_data()
    elif n == "3":
        print("insert cargo information")
        insert_cargo_data()
    
    conn.commit()

# loop that is used to update existing data
def update_data():
    print(
        """Enter the table you wish to edit:
          1-ship
          2-ship destination
          3-ship cargo
          4-quit"""
    )

    n = input("Enter:")

    if n == "1":
        print("update data in ships table")
        update_ship_data()
    elif n == "2":
        print("update destination data")
        update_destination_data()
    elif n == "3":
        print("update cargo information")
        update_cargo_data()

    conn.commit()

def view_data():
    n = int(input("Enter the Shipid"))
    #cursor.execute("select * from ships natural join shipDestination natural join shipCargo where shipid = %s",(n,)
    #master               )
    cursor.execute("Select * from ships where shipid = %s",(n,))
    rows = cursor.fetchall()
    for row in rows:
        print('shipid:              ',row[0])
        print('shipname:            ',row[1])
        print('ship import from:    ',row[2])
        print('ship driver:         ',row[3])
        print("-"*20)
    cursor.execute("Select * from shipdestination where shipid = %s",(n,))
    row1 = cursor.fetchall()
    for row in row1 :
        print('shipid:              ',row[0])
        print('ship est. TOA:       ',row[1])
        print('ship cargo contains: ',row[2])
        print('ship est. TOD:       ',row[3])
        print("-"*20)
    cursor.execute("Select * from shipCargo where shipid = %s",(n,))
    row2 = cursor.fetchall()
    for row in row2:
        print('shipid:              ',row[0])
        print('ship cargo contains: ',row[1])
        print('the weight in kgs:   ',row[2])
        print('no. of men needed    ',row[3])
        print('BILL Amount          ',row[4])
        print("-"*20) # for data separation

# MAIN FUNCTION
# Connect to the MySQL server
conn = mysql.connector.connect(host="localhost",user="root",password="sejal")
# conn = mysql.connector.connect(host="127.0.0.1", user="root", password="secretpassword")

# quit program if unsuccessful in connection
if conn.is_connected() == False:
    print("error!")
    exit(1)

# Create a cursor to execute SQL queries
cursor = conn.cursor()
init_database()


# Checking if the user has proper autherization to execute commands otherwise exiting the program
username = input("Enter admin username:")
password = int(input("Enter password:"))
cursor.execute(
    "select * from admins WHERE username = %s AND password = %s",
    (username, password),
)
data = cursor.fetchone()
if data is not None:
    print("Successful authentication!")
else:
    print("Authentication failed, exiting program!")
    if conn.is_connected():
        cursor.close()
    conn.close()
    exit()

# Main Loop of the program to perform all the actions after authentication
while True:
    print(
        """Select an option no.:
          1. view data
          2. add new data
          3. update existing data
          4. quit"""
    )
    n = input("Enter:")
    if n == "1":
        view_data()
    elif n == "2":
        add_data()
    elif n == "3":
        update_data()
    elif n == "4":
        break


# Commit changes and close the connection
conn.commit()
if conn.is_connected():
    cursor.close()
    conn.close()
