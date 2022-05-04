import scapy.all
import threading
import time
# dmac = '24:31:54:ee:32:76'
dmac = 'a0:57:e3:01:65:16'
wLs1 = []
wLs2 = []
wLs3 = []


def callbackw1(packet):
    global wLs1
    if packet.subtype != 8 and packet.addr2 == dmac:
        wLs1.append([packet.addr2, time.time(), packet.dBm_AntSignal])
    # Address 1 代表接收端， Address 2 代表传送端， Address 3 为被接收端拿来过虑地址。
    '''
    if packet.subtype != 8:
        print('1', int(time.time()))

    if packet.subtype != 8 and packet.addr2 == dmac:
        print(packet.timestamp)
        print(packet.dBm_AntSignal)
        print(packet.addr2)
        print('以上来自wlan1---------------------------------')
    '''
    
def callbackw2(packet):
    global wLs2
    if packet.subtype != 8 and packet.addr2 == dmac:
        wLs2.append([packet.addr2, time.time(), packet.dBm_AntSignal])
    # Address 1 代表接收端， Address 2 代表传送端， Address 3 为被接收端拿来过虑地址。
    '''
    if packet.subtype != 8:
        print('2', int(time.time()))
    
    if packet.subtype != 8 and packet.addr2 == dmac:
        print(packet.timestamp)
        print(packet.dBm_AntSignal)
        print(packet.addr2)
        print('以上来自wlan2---------------------------------')
    '''

def callbackw3(packet):
    global wLs3
    if packet.subtype != 8 and packet.addr2 == dmac:
        wLs3.append([packet.addr2, time.time(), packet.dBm_AntSignal])
    # Address 1 代表接收端， Address 2 代表传送端， Address 3 为被接收端拿来过虑地址。
    '''
    if packet.subtype != 8:
        print('2', int(time.time()))
    
    if packet.subtype != 8 and packet.addr2 == dmac:
        print(packet.timestamp)
        print(packet.dBm_AntSignal)
        print(packet.addr2)
        print('以上来自wlan3---------------------------------')
    '''
    

def trdw1():
    scapy.all.sniff(prn=callbackw1, iface='wlan1', count=0)

def trdw2():
    scapy.all.sniff(prn=callbackw2, iface='wlan2', count=0)

def trdw3():
    scapy.all.sniff(prn=callbackw3, iface='wlan3', count=0)

def trdBr():
    # while 1:
        time.sleep(60)
        for i in wLs1:
            print(i)
        # print('', len(wLs1), wLs1, '\n',len(wLs2), wLs2, '\n', len(wLs3), wLs3)
        print('------wLs1',len(wLs1))
        for i in wLs2:
            print(i)
        print('++++++wLs2',len(wLs2))
        for i in wLs3:
            print(i)
        print('======wLs3',len(wLs3))
# def call(p):
#     print(p.show())
# scapy.all.sniff(prn=call, iface='wlan3', count=1)
trd0 = threading.Thread(target=trdw1)
trd1 = threading.Thread(target=trdw2)
trd2 = threading.Thread(target=trdw3)
trd3 = threading.Thread(target=trdBr)
trd0.start()
trd1.start()
trd2.start()
trd3.start()
trd0.join()
trd1.join()
trd2.join()
trd3.join()