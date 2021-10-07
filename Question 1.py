def sol(n):
   #add code here
   num2=round(n/3)
   num1=n-(2*num2)
   print(num1+num2)

# do not edit below code
def main():
    n=int(input())
    print(sol(n))

if __name__ == '__main__':
    main()
