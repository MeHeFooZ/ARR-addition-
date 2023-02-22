dict={
    "username":"20A31A4459",
    "password":"M@5194",
}
m=input('enter the userrname')
n=input("enter the password:")
if m==dict['username']:
    if n==dict["password"]:
        print("given passowrd is correct")
    else:
        print("enter the valid password")
else:
    print('enter the valid username')