from scapy.all import Ether,ARP,srp
target_ip = input("target ip>>")
arp_header = Ether(dst="ff:ff:ff:FF:FF:FF")
arp_options = ARP(pdst=target_ip)


arp_packet = arp_header / arp_options

ans , unans = srp(arp_packet,timeout=2)

for send , recive in ans:
    print(recive[Ether].psrc,recive[Ether].hwsrc)