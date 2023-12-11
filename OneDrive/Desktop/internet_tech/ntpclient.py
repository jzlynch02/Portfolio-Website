'''
CS352 Assignment 1: Network Time Protocol
You can work with 1 other CS352 student
DO NOT CHANGE ANY OF THE FUNCTION SIGNATURES BELOW
'''
from socket import socket, AF_INET, SOCK_DGRAM
import struct
from datetime import datetime
def getNTPTimeValue(server="time.apple.com", port=123) -> (bytes, float, float):
# fill in your code here
# make an NTP packet
    pkt = bytearray(48)
    pkt[0] = 0b00100011
    client = socket(AF_INET,SOCK_DGRAM)
# take a timestamp, T1 = current_time
    T1 = datetime.now().timestamp()
# send packet to the server,port address
    client.sendto(pkt, (server, port))
# receive the response packet
    response,_ = client.recvfrom(48)
    
# take a timestamp, T4 = current_time
    T4 = datetime.now().timestamp()
# return a 3-tuple:
# return (pkt, T1, T4)
    client.close()
    return (response, T1, T4)

def ntpPktToRTTandOffset(pkt: bytes, T1: float, T4: float) -> (float, float):
# fill in your code here
# foreach of the 2 timestamps (T2,T3) in the packet do:
# get the bytes for the seconds part and convert to a
# floating point number
    T2_seconds = struct.unpack("!I", pkt[32:36])[0]
    T2_fraction = struct.unpack("!I", pkt[36:40])[0] / 2**32

    T3_seconds = struct.unpack("!I", pkt[40:44])[0]
    T3_fraction = struct.unpack("!I", pkt[44:48])[0] / 2**32

    T2 = (T2_seconds + T2_fraction) - 2208988800.0
    T3 = (T3_seconds + T3_fraction) - 2208988800.0
# get the bytes for the fraction part and convert to a floating point number
# combine the seconds and fraction into 1 number
# compute the RTT by: (T4-T1) - (T3-T2)
# compute the offset by: ((T2-T1) + (T3-T4))/2
    rtt = (T4 - T1) - (T3 - T2)
    offset = ((T2 - T1) + (T3 - T4)) / 2.0
# return a 2-tuple containing the RTT and offset as Python floats
# return (RTT, offset)
    return (rtt, offset)

def getCurrentTime(server="time.apple.com", port=123, iters=20) -> float:
# fill in your code here
# Computing the current time in Unix time format (seconds with microsecond fractions since 00:00:00 UTC on 1 January 1970)
    offsets = []
    for _ in range(iters):
        pkt,T1,T4 = getNTPTimeValue(server,port)
        rtt,offset = ntpPktToRTTandOffset(pkt,T1,T4)
        offsets.append(offset)
    average_offsets = (sum(offsets)/len(offsets))
    currentTime = datetime.utcnow()
    currentTime = currentTime.timestamp()
# call (pkt,T1,T4) = getNTPTimeValue(server, port)
# call (RTT,offset) = ntpPktToRTTandOffsett(pkt,T1,T4)
# append offset to offsets
# currentTime = average of offsets + current time with
# microsecond granularity
# return currentTime in Unix time as a Python float
    return currentTime

if __name__ == "__main__":
    print(getCurrentTime())