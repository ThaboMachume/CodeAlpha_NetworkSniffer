from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        proto_name = {6: "TCP", 17: "UDP"}.get(proto, str(proto))
        
        print(f"Source: {src_ip} -> Destination: {dst_ip} | Protocol: {proto_name}")

print("Starting packet capture...")
sniff(prn=packet_callback, count=10) # Just capture 10 packets for testing