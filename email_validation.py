import re 
  
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def Validate_email(N):
    l2=[]
    for email in N:
        if(re.search(regex,email)):  
            l2.append(email)
    return l2



N=int(input("enter the number of emails"))

l1=[]

for i in range(N):
    l1.append(input("enter email : "))


print(Validate_email(l1))



