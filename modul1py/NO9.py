def mencetak(a):
    for i in range(a):
        if(i<=0):
            pass
        elif(i%3==0 and i%5==0):
            print("Phyton UMS")
        elif(i%3==0):
            print("Phyton")
        elif(i%5==0):
            print("UMS")
        else:
            print(i)
