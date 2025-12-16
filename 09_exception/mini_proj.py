class userCustomException(Exception) : pass


def bill ( tea_type , cups ):
    try:
        chai_varity = {'masala':20 , 'herbal' : 50 }
        if tea_type not in chai_varity:
            raise userCustomException("Error !! this tea type isn't in the menu ")
        
        if not isinstance(cups , int) :
            raise TypeError('please give the cup in integer')
        
        total_price  = cups * chai_varity[tea_type]

        print(f'your total bill for {cups} of {tea_type} tea is {total_price} ')
    except Exception as e :
        print('Exception',e)
    finally:
        print('Visit Again')

    


bill('mint' ,10)
bill('herbal' , 'three')
bill('masala' , 3)

