# arr=[1,2, 2,1,1,3]
# dct={}
# for i in arr:
#     if i not in dct:
#         dct[i]=1

#     else:
#         dct[i]+=1

# for i , q in dct.items():
#     print(f"{i} dan {q} marta ")

# qiymatlar=list(dct.values())
# if len(qiymatlar)==len(set(qiymatlar)):
#     print("True")
# else:
#     print("False")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# word = "a123bc34d8ef34"
# temp = ""
# for i in word:

#     if i.isdigit():
#         temp += i
#     else:
#         temp += " "
# nums = temp.split()

# print(nums)         
# print(set(nums))     
# print(len(set(nums))) 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# nums=[8,1,2,2,3]
# new_lst=[]
# for i in nums:
#     count=0
#     for x in nums:
#         if i>x:
#             count+=1
#     new_lst.append(count)
# print(new_lst)       

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# text="Maktabimizda 4 -'a' snifdagi 17 tadan ortiq o'quvchilar imtixondan 86 balldan yuqori ball oldi. "
# sonlar=[]
# for i in text.split():
#     if i.isdigit():
#         sonlar.append(int(i))
# print(sonlar)
# s=sorted(sonlar)
# text="Maktabimizda 99 -'a' snifdagi 17 tadan ortiq o'quvchilar imtixondan 86 balldan yuqori ball oldi."
# sonlar=[]
# for i in text.split():
#     if i.isdigit():
#         sonlar.append(int(i))

# s = sorted(sonlar)
# if sonlar == s:
#     print("True")
# else:
#     print("False")

# print("Matndagi sonlar:", end=" ")

# for i in range(len(sonlar)):
#     print(sonlar[i], end=" ")
    
#     if i < len(sonlar)-1:
#         if sonlar[i] > sonlar[i+1]:
#             print(">", end=" ")
#         elif sonlar[i] == sonlar[i+1]:
#             print("=", end=" ")
#         else:
#             print("<", end=" ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>












