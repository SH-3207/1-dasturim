from colorama import Fore, Back, Style, init
import pyfiglet
init(autoreset=True)
l=1
while True:
  if l==1:
   with open("SH_3207.txt","w") as file:
    matn=input(Fore.RED + Style.BRIGHT+"Faylga saqlash uchun matn kiritishingz mumkin -")
    file.write(f"{matn}\n")
    l=0  
  if input(Fore.YELLOW + """Faylga yozishni davom etaszmi [1]\nYoki tugatmoqchimisiz [0]\nKiriting -> """) =="1":
       with open("SH_3207.txt","a") as file:
         matnn=input(Fore.RED + Style.BRIGHT+ "Faylga saqlash uchun matn kiritishingiz mumkin: ")
         file.write(f"{matnn}\n")
  else:
       break
with open ("SH_3207.txt") as file:
    natija=file.read()
    natija=natija.rstrip()
    banner = pyfiglet.figlet_format("SH_3207")
    print(Fore.GREEN + Style.BRIGHT + banner + natija)

