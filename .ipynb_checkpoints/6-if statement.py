#Write a program that ask user to entera number. Program should tell them if number is odd and even.
# num = input("Enter a number : ")
# num = int(num)
# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd ")


#oprators
# 4==4
# 4!=4
# 2>1
# 2<1
# 2>=1
# 2<=4
# 3>2 and 4>7
# 4>5 or 6>1
#not 4==4


#Write a program that ask user to enter dish name and itshould print which cuisine is that dish.
indain = ["samosa","dall","naan"]
pakistani = ["chawal","baryani","lasi"]
italin = ["piza","pasta","risotto"]

dish = input("Enter a dish name : ")
if dish in indain:
    print("indain")
elif dish in pakistani:
    print("pakistan")
elif dish in italin:
    print("italian")
else:
    print("Based on my knowledge i do not know from which this cosin is",dish)