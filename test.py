
#i = 1
#while i < 5:
#    j = 1
 #   while j <= 4:
  #      print("Rocks", end="")
   #     j += 1
    #i+=1
    #print()

for i in range(1,9):
    print(i,end=" ")
    for j in range(2,9-i):
        print(j,end=" ")
    print()
