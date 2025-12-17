class Car:
    car_sales =0 

    def __init__(self , brand , model):
        self.__brand=brand
        self.model=model
        Car.car_sales +=1

    def get_brand(self):
        return self.__brand

    def carDetails(self):
        print(f"Brand : {self.__brand} | Model : {self.model}")

    def fuel_type(self):
        return "Petrol"
    
    @staticmethod
    def generic_Car():
        print("There is a 40% sale in cars ")

# class ElectricCar(Car):

#     def __init__(self, brand, model , batterySize):
#         super().__init__(brand, model)
#         self.batterySize = batterySize  

#     # def carDetails(self):
#     #     print(f"Brand : {self.get_brand()} | Model : {self.model} | Battery Size : {self.batterySize} ")
    
#     def fuel_type(self):
#         return "Battery"
    

# car1 = Car("Mahendra" , "XUV700")
# # car1.__brand = "Tata" 

# # print(car1.__brand)
# car1.carDetails()
# print(f"The car fueled by  {car1.fuel_type()}")

# car2 = ElectricCar("Tesla" , "cybertruck" , "80kwh")
# car2.carDetails()
# print(f"The car fueled by  {car2.fuel_type()}")

# print(f"Total No. of Car Sold : {Car.car_sales}")

# Car.generic_Car()


# print(isinstance(car1 , Car))
# print(isinstance(car1 , ElectricCar))

class Battery:
    def battery_info(self):
        print("The car has battery")

class Engine:
    def engine_info(self):
        print("Engine is very good")

class ElectricCar(Battery , Engine):
    pass


ecar1=ElectricCar()
ecar1.battery_info()
ecar1.engine_info()


