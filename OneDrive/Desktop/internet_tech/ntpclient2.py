#!/usr/bin/env python
'''
CS352 Assignment 1: Network Time Protocol
You can work with 1 other CS352 student
DO NOT CHANGE ANY OF THE FUNCTION SIGNATURES BELOW
'''
from socket import socket, AF_INET, SOCK_DGRAM
import struct
from datetime import datetime

def getNTPTimeValue(server="time.apple.com", port=123) -> (bytes, float, float):
# add your code here
# make an NTP packet
    ntp_packet = bytearray(48)
    ntp_packet[0] = 0x1B
# take a timestamp, T1 = current_time
    T1 = datetime.now().timestamp()
# send packet to the server,port address
    client = socket(AF_INET,SOCK_DGRAM)
    client.sendto(ntp_packet,(server,port))
# receive the response packet
    pkt = socket.recvfrom(48)
# take a timestamp, T4 = current_time
    T4 = datetime.now().timestamp()
    client.close()
# return a 3-tuple:
# return (pkt, T1, T4)
    return (pkt, T1, T4)

def ntpPktToRTTandOffset(pkt: bytes, T1: float, T4: float) -> (float, float):
# add your code here
# foreach of the 2 timestamps (T2,T3) in the packet do:
# get the bytes for the seconds part and convert to a floating point number
# get the bytes for the fraction part and convert to a floating point number
# combine the seconds and fraction into 1 number
    T2 = struct.unpack('!Q', pkt[32:40])[0] / 2.0**32 
    T3 = struct.unpack('!Q', pkt[40:48])[0] / 2.0**32   
# compute the RTT by: (T4-T1) - (T3-T2)
    rtt = (T4-T1) - (T3-T2)
# compute the offset by: ((T2-T1) + (T3-T4))/2
    offset = ((T2-T1)+(T3-T4))/2

    return (rtt, offset)

def getCurrentTime(server="time.apple.com", port=123, iters=20) -> float:
# add your code here
# offsets = empty list
    offsets = []
#for _ in range(iters):
    for _ in range(iters):
# call (pkt,T1,T4) = getNTPTimeValue(server, port)
        pkt, T1, T4 = getNTPTimeValue(server,port)
# call (RTT,offset) = ntpPktToRTTandOffsett(pkt,T1,T4)
        RTT, offset = ntpPktToRTTandOffset(pkt,T1,T4)
# append offset to offsets
        offsets.append(offset)
# currentTime = average of offsets + current time with microsecond granularity
    timeNow = datetime.utcnow().timestamp
    currentTime = ((sum(offsets))/len(offsets)) + timeNow
# return currentTime in Unix time as a Python float
    return currentTime

if __name__ == "__main__":
    print(getCurrentTime())
