import math
def circle_values(radious):
    area =  round( ( math.pi * (radious ** 2 )) , 2 )
    circumstance = round((2 * math.pi * radious),2 )

    return area , circumstance

area , circumstance = circle_values(4)

print(f"Area : {area} , Circumstance : {circumstance}")