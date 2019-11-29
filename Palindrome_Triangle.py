N = int(input("enter the triangle size"))
for row in range(1,(N+1)):
    line = ""
    for col in range(1,(row+1)):
        line = line + str(col)
    for x in range(int(line[-1])):
        line = line + str(int(line[-1]) - 1)
    print(int(line)//10)
