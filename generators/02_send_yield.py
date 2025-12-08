def send_yield():

    print('Ready to take your order !')
    order = yield 

    while True :
        print(f'Preparing order : {order}')
        order = yield 


stall = send_yield()
next(stall)

stall.send("masala chai")


