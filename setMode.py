import os

# wlanList = ['wlan1', 'wlan2', 'wlan3']
wlanList = ['wlan1']

for i in wlanList:
    os.system("ifconfig %s down" % i)
    print("%s down" % i)
    os.system("iwconfig %s mode monitor" % i)
    print("set %s mode monitor" % i)
    os.system("ifconfig %s up" % i)
    print("%s up" % i)