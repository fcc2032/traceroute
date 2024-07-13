#!/usr/bin/python3
from scapy.all import *
ttl = 1
maxttl = 25
while True:
    a = IP(dst='8.8.8.8', ttl = ttl)
    b = ICMP()
    p = a/b
    pkt = sr1(p, timeout = 2,verbose = 0)
 
    
    if pkt == None:
        print('TTL: %d, Source *' %ttl)
        ttl += 1
    elif (maxttl - ttl) == 0:
        print("Max TTL reached")
        break
    elif pkt[IP].src == a.dst:
        print ("TTL: %d, Complete" %ttl, pkt[IP].src)
        break
    elif pkt != None:
        print('TTL: %d, Source ' %ttl , pkt[IP].src)
        ttl += 1
