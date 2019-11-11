print ("Hello world!")

def icmp2echo(data):

    # if len(sys.argv) != 2:
    #     print ("Usage: icmp2echo <IP or hostname>\n  eg: icmp2echo 192.168.1.1")
    #     sys.exit(1)

    from scapy.all import sr1, IP, ICMP

    #packet = sr1(IP(dst=sys.argv[1])/ICMP())
    packet = sr1(IP(dst=data)/ICMP())
    if packet:
        packet.show()