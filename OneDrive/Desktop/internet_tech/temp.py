

'''
CS352 Assignment 1: Network Time Protocol
You can work with 1 other CS352 student

DO NOT CHANGE ANY OF THE FUNCTION SIGNATURES BELOW
'''

from socket import socket, AF_INET, SOCK_DGRAM
import struct
from datetime import datetime

def getNTPTimeValue(server="time.apple.com", port=123) -> (bytes, float, float):
    # Create an NTP packet (request) as bytes
    ntp_packet = b'\x1b' + 47 * b'\0'
    
    # Create a UDP socket
    client = socket(AF_INET, SOCK_DGRAM)
    client.sendto(ntp_packet, (server, port))
    
    # Receive the response packet
    response_packet, server_address = client.recvfrom(48)
    
    # Close the socket
    client.close()
    
    # Extract T1 and T4 timestamps
    T1 = datetime.utcnow().timestamp()
    T4 = datetime.utcnow().timestamp()
    
    return (response_packet, T1, T4)

def ntpPktToRTTandOffset(pkt: bytes, T1: float, T4: float) -> (float, float):
    # Extract T2 and T3 timestamps from the packet
    T2 = struct.unpack('!Q', pkt[16:24])[0] / 2**32 - 2208988800.0
    T3 = struct.unpack('!Q', pkt[24:32])[0] / 2**32 - 2208988800.0

    # Compute RTT and offset
    RTT = (T4 - T1) - (T3 - T2)
    offset = ((T2 - T1) + (T3 - T4)) / 2.0

    return (RTT, offset)

def getCurrentTime(server="time.apple.com", port=123, iters=20) -> float:
    offsets = []

    for _ in range(iters):
        # Get (pkt, T1, T4) from getNTPTimeValue
        pkt, T1, T4 = getNTPTimeValue(server, port)
        
        # Get (RTT, offset) from ntpPktToRTTandOffset
        RTT, offset = ntpPktToRTTandOffset(pkt, T1, T4)
        
        # Get current time with microsecond granularity
        timeNow = datetime.now().microsecond
        
        # Append timeNow + offset + RTT to times
        offsets.append(timeNow + offset + RTT)

    # Compute currentTime as the average of times
    currentTime = sum(offsets) / len(offsets)

    return currentTime

if __name__ == "__main__":
    print(getCurrentTime())
