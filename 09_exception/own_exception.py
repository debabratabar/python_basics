class valueExacceptionhandle (Exception):
    pass


def prepareChai(milk , sugar):
    if milk ==0 and sugar ==0:
        # raise  valueExacceptionhandle('Mising milk or sugar')
        raise ValueError('Error, milk and sugar both needed')
    print('chai is ready')


prepareChai(0,1)