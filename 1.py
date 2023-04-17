number=int(input("Введите трехзначное число:"))
sum=0
if number<100:
   print("Число не трехзначное")

if number>=100 and number<=999:
    while(number>0):
      x=number%10
      print(x)
      sum=sum+x
      number=number//10
print(sum)

