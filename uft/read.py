file = open("index.uft",'r')
######## process1
try:
    p1 = []
    for each in file:
        a = each
        p1.append(a)
except:
    print("error:p1")
######## process2
try:
    p2 = "".join(p1)
    p2 = p2.split(',')
except:
    print("error:p2")
#########################################################################PART 1
