s_diff ,k_order = input("").split()

print(s_diff, k_order)
PN_List = []

def CreateHex(s,k):
    if s == 1:
        for i in k:
            temp = 0x0000000
            PN_List.append(temp)
            temp += 0x1
    else:
        return
        

CreateHex(s_diff,k_order)
print(PN_List[0])

for i in PN_List:
    print("%x"%PN_List[i])
    

# def CompareHex():

# def sorting():  
