def hello(*variable):
    print(variable)
    sum=0
    for i in variable:
        sum=sum+i
    print(sum)

hello(12,13,14,15)
hello(12,14, )