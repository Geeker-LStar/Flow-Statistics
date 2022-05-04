import scapy.all
import threading
import time
# from app import main as webMode
from solve import Solve

class Main(Solve):
    def __init__(self):
        self.wLs1 = []
        self.fshts = 300
        # self.lens = len(self.wLs1)
        
    def callbackw1(self, packet):
        if packet.subtype != 8:
            self.wLs1.append([time.time(), packet.dBm_AntSignal, packet.addr2])# 时间戳，强度，MAC
        # Address 1 代表接收端， Address 2 代表传送端， Address 3 为被接收端拿来过虑地址。

    def trdw1(self):
        scapy.all.sniff(prn=self.callbackw1, iface='wlan1', count=0)

    def trdBr(self):
        while 1:
            time.sleep(1)
            now = time.time()
            for i in self.wLs1:
                if now-i[0] >= self.fshts:
                    self.wLs1.remove(i)
            # self.lens = len(self.wLs1)

    # def trdShow(self):
    #     webMode()

    def main(self):
        self.trd0 = threading.Thread(target=self.trdw1)
        # self.trd1 = threading.Thread(target=self.trdShow)
        self.trd2 = threading.Thread(target=self.trdBr)
        self.trd0.start()
        # self.trd1.start()
        self.trd2.start()
        # self.trd0.join()
        # self.trd1.join()
        # self.trd2.join()

if __name__ == '__main__':
    a = Main()
    a.main()