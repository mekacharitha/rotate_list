import functions
k = int(input("Enter number of times to rotate"))
lis=list(map(int , input().split()))
print(functions.rotate(k,lis))
