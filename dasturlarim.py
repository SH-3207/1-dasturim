
import json

# 1 Masala: 

# with open("filelar.json") as f:
#     data = json.load(f)

# if isinstance(data, list):
#     data = data[0]

# for branch in data['branches']:
#     print(branch['name'])


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 2 Masala: 

# with open("filelar.json") as f:
#     data = json.load(f)
# asosiy_lugat = data[0]

# for branch in asosiy_lugat['branches']:
    
#     for teacher in branch['teachers']:
        
#         if teacher['subject'] == "Python":
#             print(f"Ismi: {teacher['name']}")
#             print(f"Filial: {branch['name']}")
#             print(f"Tajribasi: {teacher['experience']} yil")
#             print("-" * 20)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 3 Masala: 

# with open("filelar.json") as f:
#     data= json.load(f)
#     asos=data[0]
#     count=0
#     for i in asos['branches']:
#      f_nomi=i["name"]
#      sh_soni=len(i["students"])
#      print(f"{f_nomi} Filialida: {sh_soni} ta oquvchi bor:")
         
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 4 Masala: 

# with open("filelar.json") as f:
#     data = json.load(f)

# asosiy_lugat = data[0]

# max_tulov = 0
# eng_zort_oquvchi = None

# for branch in asosiy_lugat['branches']:
    
#     for student in branch['students']:
         
#         if student['payment'] > max_tulov:
#             max_tulov = student['payment']
#             eng_zort_oquvchi = student['name']

# print(f"Eng ko'p to'lov qilgan o'quvchi: {eng_zort_oquvchi}")
# print(f"To'lov miqdori: {max_tulov} so'm")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 5 Masala: 

# with open("filelar.json") as f:
#     data = json.load(f)

# asosiy_lugat = data[0]

# print("-Filiallar bo'yicha umumiy tushum:")

# for branch in asosiy_lugat['branches']:
#     filial_tushumi = 0  
    
#     for student in branch['students']:
#         filial_tushumi += student['payment']
#     print(f"{branch['name']} filiali: {filial_tushumi} so'm")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 6 Masala: 

# with open("filelar.json") as f:
#     data = json.load(f)

# asosiy_lugat = data[0]

# print("-Tajribasi 5 yildan ko'p bo'lgan o'qituvchilar:")

# for branch in asosiy_lugat['branches']:

#     for teacher in branch['teachers']:
        
#         if teacher['experience'] > 5:
#             print(f"Ismi: {teacher['name']}")
#             print(f"Fani: {teacher['subject']}")
#             print(f"Tajribasi: {teacher['experience']} yil")
#             print(f"Filial: {branch['name']}\n")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 7 Masala: 

# with open("filelar.json") as f:
#     data = json.load(f)

# asosiy_lugat = data[0]

# print("-Python kursi mavjud filiallar:")

# for branch in asosiy_lugat['branches']:
#     python_bor = False 

#     for teacher in branch['teachers']:
#         if teacher['subject'] == "Python":
#             python_bor = True
#             break 
            
#     if python_bor:
#         print(f"Filial nomi: {branch['name']}")


