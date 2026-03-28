from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def analyze_packet(packet):
    print("\n--- Packet Captured ---")

    # Check if IP layer exists
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol       : {ip_layer.proto}")

    # Check for TCP
    if packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        print("Protocol Name  : TCP")
        print(f"Source Port    : {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")

    # Check for UDP
    elif packet.haslayer(UDP):
        udp_layer = packet[UDP]
        print("Protocol Name  : UDP")
        print(f"Source Port    : {udp_layer.sport}")
        print(f"Destination Port: {udp_layer.dport}")

    # Check for ICMP
    elif packet.haslayer(ICMP):
        print("Protocol Name  : ICMP")

    # Payload (Raw Data)
    if packet.haslayer(Raw):
        payload = packet[Raw].load
        print(f"Payload        : {payload[:50]}")  # Show first 50 bytes

def start_sniffing():
    print("Starting packet capture... Press Ctrl+C to stop.")
    
    # Capture packets
    sniff(prn=analyze_packet, count=20)  # capture 20 packets

if __name__ == "__main__":
    start_sniffing()
