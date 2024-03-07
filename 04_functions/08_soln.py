def sum_of_any_nums (**kwargs):
    # print(sum(args))
    print(kwargs)
    for key , value in kwargs.items():
        print (f"key : {key} | value : {value}")
    # result=0
    # for i in args :
    #     result= sum( result , i)
    # print(result)

# sum_of_any_nums(1,2,3,3,4)
sum_of_any_nums(a=1,b=-1)