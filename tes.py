tme = [0] * 5
i = 0
e = 0
while(1):
    
    print(e, '1')
    
    if(e >= len(tme)):
        break

    if(i == e):
        e+=1
        continue
    else:
        tme[e] += 20
        tme[e] += 5
        e+=1              