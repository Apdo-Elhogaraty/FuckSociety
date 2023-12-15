from scapy.all import ICMP, IP
from scapy.all import sr1

while True:
    try:
        src_ip = input("Source ip>")
        des_ip = input("Destination ip>")
        ip_head = IP(src=src_ip,dst=des_ip)

        icmp_option = ICMP(id=100)
        full_packet = ip_head / icmp_option

        packet_sender = sr1(full_packet)
        if packet_sender:
            print(packet_sender.show())
        user_answer = input("Continue ??")
        if user_answer.lower() == "y" or user_answer.lower() == "yes":
            continue
        else:
            break
    except Exception:
        print("There is error")
        continue
