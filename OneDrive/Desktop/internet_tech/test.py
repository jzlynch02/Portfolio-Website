from socket import socket, AF_INET, SOCK_DGRAM
import struct
from datetime import datetime

def getNTPTimeValue(server="time.apple.com", port=123) -> (bytes, float, float):
    # Create an NTP packet (48 bytes)
    # fill in your code here
# make an NTP packet
# take a timestamp, T1 = current_time
# send packet to the server,port address
# receive the response packet
# take a timestamp, T4 = current_time
# return a 3-tuple:
# return (pkt, T1, T4)
    ntp_packet = bytearray(48)
    ntp_packet[0] = 0x1B
    
    # Take a timestamp, T1 = current_time
    T1 = datetime.now().timestamp()

    # Create a UDP socket
    client = socket(AF_INET, SOCK_DGRAM)
    
    
    client.sendto(ntp_packet, (server, port))

        # Receive the response packet
    response, _ = client.recvfrom(48)

        # Take a timestamp, T4 = current_time
    T4 = datetime.now().timestamp()
   
    client.close()

    return (response, T1, T4)


def ntpPktToRTTandOffset(pkt: bytes, T1: float, T4: float) -> (float, float):
    # Extract T2 and T3 from the NTP packet
    # fill in your code here
# foreach of the 2 timestamps (T2,T3) in the packet do:
# get the bytes for the seconds part and convert to a
# floating point number
# get the bytes for the fraction part and convert to
# a floating point number
# combine the seconds and fraction into 1 number
# compute the RTT by: (T4-T1) - (T3-T2)
# compute the offset by: ((T2-T1) + (T3-T4))/2
# return a 2-tuple containing the RTT and offset as Python floats
# return (RTT, offset)
    T2 = struct.unpack('!Q', pkt[32:40])[0] / 2.0**32 
    T3 = struct.unpack('!Q', pkt[40:48])[0] / 2.0**32
    
    # Calculate RTT and offset
    RTT = (T4 - T1) - (T3 - T2)
    offset = ((T2 - T1) + (T3 - T4)) / 2
    
    return (RTT, offset)
def getCurrentTime(server="time.apple.com", port=123, iters=20) -> float:
    offsets = []

    for _ in range(iters):
        pkt, T1, T4 = getNTPTimeValue(server, port)
        RTT, offset = ntpPktToRTTandOffset(pkt, T1, T4)
        offsets.append(offset)

    # Calculate the average offset
    average_offset = sum(offsets) / len(offsets)

    current_time = datetime.now().microsecond + average_offset

    return current_time 

if __name__ == "__main__":
    print(getCurrentTime())
