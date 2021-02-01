n = int(input("Enter the times you want the loop to run.."))

for i in range(1,n):                                   #First for loop..
                                                        #Second for spacing..
      for j in range(n , i , -1):
            print(" " , end = "")
      for k in range(1,(2*i-1)+1):                      #Third for printing ..
            print("*" , end = "")
      print()
for i in range(n , 0 , -1):
      for j in range(1,n+1-i):
            print(" " , end = "")
      for k in range(1,(2*i-1)+1):
            print("*" , end="")
      print()
