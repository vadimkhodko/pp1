def f(x,bool):
    my_int=(x)
    my_list=[] #создаём пустой лист для инта, чтобы потом добавить в него x

    for x in str(my_int):
        my_list.append(int(x)) #добавляем инт в лист

    if (bool==True):
        result=0
        for i in range(0,len(my_list)):
            if(my_list[i] %2 == 0):
                result +=  my_list[i]
        print(result, end='')
            
    if (bool==False):
        result=0
        for i in range(0,len(my_list)):
            if(my_list[i] %2 == 1):
                result += my_list[i]
            print(result, end='')

        
f(1241526,True)

