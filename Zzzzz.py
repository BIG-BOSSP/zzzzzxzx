import requests,json,os,sys
os.system("clear")
os.system("xdg-open https://facebook.com/groups/711929427000456")
logo="""
print \033[1;32m

   ██████  ██       █████   ██████ ██   ██ 
   ██   ██ ██      ██   ██ ██      ██  ██  
   ██████  ██      ███████ ██      █████   
   ██   ██ ██      ██   ██ ██      ██  ██  
   ██████  ███████ ██   ██  ██████ ██   ██ 

\033[1;33m××××××××××××××××××××××××××××××××××××××××××××××
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m CREATED BY\033[1;33m     ☞  \033[1;32mPROKASH ROY      \033[1;33m  |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m FACEBOK\033[1;33m        ☞  \033[1;32mPROKASH TECH 24  \033[1;33m  |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m GITHUB\033[1;33m         ☞  \033[1;32mBLACK-TEAM-24   \033[1;33m   |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m TEAM\033[1;33m           ☞  \033[1;32mBLACK           \033[1;33m   |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m TOOLS NAME\033[1;33m     ☞  \033[1;32mIP ADDRESS       \033[1;33m  |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m TOOLS VERSION\033[1;33m  ☞  \033[1;32m0.4             \033[1;33m   |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m SERVER\033[1;33m         ☞  \033[1;32mDATA WORKING       \033[1;33m   |
×××××××××××××××××××××××××××××××××××××××××××××

"""

print(logo)
#Note=input("\033[1;32mThis Tool Create By BLACK-TEAM")
victim=input(' \033[1;36mVICTIM IP ADDRESS : ')
url="http://ip-api.com/json/"+victim
ip=requests.get(url).json()

print("""\n
 \033[1;33m×××××××××××××××××××××××××××××××××××××××××××××××××××
×             \033[1;36mYOUR VICTIM INFORMATION             ×
×××××××××××××××××××××××××××××××××××××××××××××××××××

""")

print(" \033[1;31mVICTIM IP : \033[1;32m "+ip['query'])
print(" \033[1;31mIP STATUS : \033[1;32m "+ip['status'])
print(" \033[1;31mCOUNTRY : \033[1;32m "+ip['country'])
print(" \033[1;31mCOUNTRY CODE : \033[1;32m "+ip['countryCode'])
print(" \033[1;31mDIVISION : \033[1;32m "+ip['regionName'])
print(" \033[1;31mCITY : \033[1;32m "+ip['city'])
#print("DISTRICT : "+ip['district'])
print(" \033[1;31mNETWORK SERVICE : \033[1;32m "+ip['isp'])
print(" \033[1;31mTIMEZONE : \033[1;32m "+ip['timezone'])


  

