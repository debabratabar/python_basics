def sum_of_any_nums (*args):
    print(sum(args))
    print(*args)
    print(args)
    # result=0
    # for i in args :
    #     result= sum( result , i)
    # print(result)

sum_of_any_nums(1,2,3,3,4)
sum_of_any_nums(1,-1)