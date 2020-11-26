

for i in range(5):
    ''' FOR N'''
    for n in range(4):
        if i==n or n==0 or n==3:
            print('N', end=' ')
        else:
            print( "  ", end='')

        print(end = ' ')
    print(end = ' ')
    

    ''' FOR A '''
    for a in range(4):
        if i==0 or i==2 or a==0 or a==3:
            print('A', end=' ')
        else:
            print( "  ", end='')
        print(end = ' ')
    print(end = ' ')


    ''' FOR R '''
        
    for r in range(4):
        if i==2 and r==3:
            print( ' ',end=' ')
        elif i==0 or i==2 or r==0 or r==3:
            print('R', end=' ')
     
        else:
            print( "  ", end='')
        print( end = ' ')
    print(end = ' ')

    ''' FOR E '''
    for e in range(4):
        if i==2 and e==3:
            e =' '
            print(' ',end= ' ')
        elif i==0 or i ==2 or i==4 or e==0 :
            print('E', end=' ')
        else:
            print( "  ", end='')
        print(end = ' ')
    print(end = ' ')


    ''' FOR S '''

    for s in range(4):
        if i == 1 and s==3 or i==3 and s==0 :
            s = ' '
            print(end= '')
        if i==0 or i==2 or i==4 or s==0 or s==3:
            print('S', end=' ')
        else:
            print( "  ", end='')
        print(end = ' ')
    print(end = ' ')


    ''' FOR H '''

    for h in range(4):
        if i==2 or h==0 or h==3:
            print('H', end=' ')
        else:
            print( "  ", end='')
        print(end = ' ')
    print(end = ' ')

    print()



# for k 

# for i in range(7):
#     for j in range(4):
#         if j==0 or i-j==3  or i+j==3:
#             print("*" ,end='')
#         else:
#             print(end =' ')
#     print()








            # N        N   A  A  A  A   R  R  R  R   E  E  E  E   S  S  S  S   H        H   
            # N  N     N   A        A   R        R   E            S            H        H   
            # N     N  N   A  A  A  A   R  R  R      E  E  E      S  S  S  S   H  H  H  H   
            # N        N   A        A   R        R   E                     S   H        H   
            # N        N   A        A   R        R   E  E  E  E   S  S  S  S   H        H   