class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        
        
    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"
           
        
class Vehicle:
    total_vehicles = 0
    
    def __init__(self, brand : str , model : str , engine :Engine ):
        self.brand = brand
        self.model = model
        self._rental_price = 0
        Vehicle.total_vehicles+=1
        self.eng_obj = engine
        
    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"
        
    @classmethod
    def get_total_vehicles():
        return Vehicle.total_vehicles
        
    @property
    def rental_price(self ):
        return self._rental_price
        
    @rental_price.setter
    def rental_price(self , rental_price):
        if rental_price >0:
            self._rental_price = rental_price
            
            
    def get_details(self):
        return f' {self.brand} , {self.model} , {self.eng_obj.get_engine_info()} '
        
        
class Car(Vehicle):
    def __init__(self , brand , model , engine ,  seats):
        super(brand , model , engine )
        self.seats = seats
        
    def get_details(self):
        return f'{super().get_details()} Seats: {self.seats}'
    

        
    
        
    
    
        
        