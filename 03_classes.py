class Vehicle:
    def __init__(self,brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print("gas is now full")

    def drive(self):
        print(f'The {self.brand} is driving now')

    #define a method to update attribute value
    def update_fuel_level(self,new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
        else:
            print("Excedded Capacity")

    #Define a method to increment an attribute’s value
    #tank cant contain more than gas_tank_size i.e 14 litre
    def get_gas(self,amount):
        if self.fuel_level + amount <= self.gas_tank_size:
            self.fuel_level += amount
        else:
            print("the tank cant hold that much")


vehicle_object = Vehicle("honda","Ridgeline","truck")
#access attribute values
print(vehicle_object.brand)
#print(vehicle_object.model)
#print(vehicle_object.type)
vehicle_object.drive()

vehicle_object.fuel_up()
vehicle_object.update_fuel_level(8) # now tank contain 8 litre
#print(vehicle_object.fuel_level)
#print(vehicle_object.fuel_level)
#vehicle_object.fuel_up()
print(vehicle_object.fuel_level)
vehicle_object.get_gas(3) #cant increase that 14 litre
print(vehicle_object.fuel_level)

