class ChaiClass:
    # def __init__(self , tea_type , price , cup_size):
    #     self.tea_type  = tea_type
    #     self.price  = price
    #     self.cup_size  = cup_size


    def __init__(self ,  **kwargs):
        self.tea_type  = kwargs.get('tea_type' , 'Normal')
        self.price  = kwargs.get('price' , 50)
        self.cup_size  = kwargs.get('cup_size' , 'small')


    @classmethod
    def from_dict(cls , chai_dict):
        # print(chai_dict)

        return cls( tea_type = chai_dict['tea_type'] ,price= chai_dict['price'] , cup_size = chai_dict['cup_size'])
    
    @classmethod
    def from_str(cls , chai_str):

        chai_arr = chai_str.split('-')

        return cls( tea_type = chai_arr[0] ,price =chai_arr[1] , cup_size=chai_arr[2]) 
    


obj_masala = ChaiClass.from_dict({'tea_type' : 'masala' , 'price' : '100' , 'cup_size' : 'small'})
print(obj_masala.__dict__)

obj_herbal = ChaiClass.from_str('herbal-150-medium')
print(obj_herbal.__dict__)

obj_kulhad = ChaiClass( tea_type='kulhad' , price='50' , cup_size='small')
print(obj_kulhad.__dict__)
    







# obj_masala= ChaiClass('Masala' , 100 , 'small')



