#problen
#Store monthly expenses in a list and find out total expenses for all months

# #not good method
exp =[2340,4566,5444,2333,7876]
# total = exp[0] + exp[1] + exp[2] + exp[3]
# print(total)

#Good Method
# total = 0
# for items in exp:
#     total = total + items
# # print(total)
#
# for i in range(10,20):
#     print(i*i)

#problem
#Calculate monthly expenses of each month
total = 0
for i in range(len(exp)):
    # print("Month:",(i+1),'Expenses:',exp[i])
    total = total + exp[i]
# print("Total Expenses is:",total)


#problem
#Search for lost car keys in home and when found stop searching

# key_location = "chair"
# Locations = ["garge","living room","chair","closet"]
# for i in Locations:
#     if i==key_location:
#         print("key is found in",i)
#         break
#     else:
#         print("Keys not found in ",i)


#When we require to skip something from a klarge dataset
for i in range(1,6):
    if i%2==0:
        continue
    # print(i*i)


i = 0
#whlipe loop
while i < 9:
    print(i)
    i = i+1