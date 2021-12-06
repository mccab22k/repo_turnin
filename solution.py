from socket import *
from statistics import *
import os
import sys
import struct
import time
import select
# import binascii

# Should use stdev
# you will need to add a few lines of code in order to calculate minimum time, average time, maximum time, and stdev time and print the results like in the operating system.

ICMP_ECHO_REQUEST = 8

#no change
def checksum(string):
	csum = 0
	countTo = (len(string) // 2) * 2
	count = 0

	while count < countTo:
		thisVal = (string[count + 1]) * 256 + (string[count])
		csum += thisVal
		csum &= 0xffffffff
		count += 2

	if countTo < len(string):
		csum += (string[len(string) - 1])
		csum &= 0xffffffff

	csum = (csum >> 16) + (csum & 0xffff)
	csum = csum + (csum >> 16)
	answer = ~csum
	answer = answer & 0xffff
	answer = answer >> 8 | (answer << 8 & 0xff00)
	return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
	timeLeft = timeout

	while 1:
		startedSelect = time.time()
		whatReady = select.select([mySocket], [], [], timeLeft)
		howLongInSelect = (time.time() - startedSelect)
		if whatReady[0] == []:  # Timeout
			return "Request timed out."

		timeReceived = time.time()
		recPacket, addr = mySocket.recvfrom(1024)

		# Fill in start
		# Fetch the ICMP header ICMP_ECHO_REPLY from the IP packet
		icmph = recPacket[20:28]
		icmpt, code, checksum, pckID, sq = struct.unpack("bbHHh", icmph)

		# In the “receiveOnePing” method, you need to receive the structure ICMP_ECHO_REPLY and fetch the information you need, such as checksum, sequence number, time to live (TTL), etc. Study the “sendOnePing” method before trying to complete the “receiveOnePing” method.
		# The echo reply is an ICMP message generated in response to an echo request, and is mandatory for all hosts and routers.
		# • Type and code must be set to 0.
		# • The identifier and sequence number can be used by the client to determine which echo requests are associated with the echo replies.
		# • The data received in the echo request must be entirely included in the echo reply.

		if icmpt != 0:
			return "type should be 0 in echo but was {}".format(icmpt)
		if code != 0:
			return "code should be 0 in echo but was {}".format(code)	
		if pckID != ID:
			return "packet ID and ID should match"
		else:
			double = struct.calcsize("d")
			timeSent = struct.unpack("d", recPacket[28:28 + double])[0]
			difference=timeReceived-timeSent
			return difference

		# Fill in end

		timeLeft = timeLeft - howLongInSelect
		if timeLeft <= 0:
			return "Request timed out."

#do not change
def sendOnePing(mySocket, destAddr, ID):
	# Header is type (8), code (8), checksum (16), id (16), sequence (16)
	
	myChecksum = 0
	# Make a dummy header with a 0 checksum
	# struct -- Interpret strings as packed binary data
	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
	data = struct.pack("d", time.time())
	# Calculate the checksum on the data and the dummy header.
	myChecksum = checksum(header + data)

	# Get the right checksum, and put in the header
	
	if sys.platform == 'darwin':
		# Convert 16-bit integers from host to network  byte order
		myChecksum = htons(myChecksum) & 0xffff
	else:
		myChecksum = htons(myChecksum)

	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
	packet = header + data

	mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str
	# Both LISTS and TUPLES consist of a number of objects
	# which can be referenced by their position number within the object.

# array = []

#no change
def doOnePing(destAddr, timeout):
	icmp = getprotobyname("icmp")
	# SOCK_RAW is a powerful socket type. For more details:   http://sockraw.org/papers/sock_raw
	mySocket = socket(AF_INET, SOCK_RAW, icmp)
	myID = os.getpid() & 0xFFFF  # Return the current process i
	sendOnePing(mySocket, destAddr, myID)
	delay = receiveOnePing(mySocket, myID, timeout, destAddr)

	# array.append(delay)

	mySocket.close()
	return delay

#add in min, max, avg, stdv
def ping(host, timeout=1):
	# timeout=1 means: If one second goes by without a reply from the server,      # the client assumes that either the client's ping or the server's pong is lost
	dest = gethostbyname(host)
	print("Pinging " + dest + " using Python:")
	print("")
	# print(array)

	array=[]
	# Send ping requests to a server separated by approximately one second
	for int(i) in [0,1,2,3,4]:
		delay = doOnePing(dest, timeout)*1000
		print(delay)
		time.sleep(1)  # one second
		# array=[i]
		array[i]=delay #first loop at 1, then 2, then 3 ...
		# array.insert(i,int(delay*1000))
		# array.append(delay)
	# Calculate vars values and return them
	print("printing array: " + array)
	packet_min = (min(array)) 
	packet_max = (max(array)) 
	packet_avg = (mean(array)) 
	stdev_var = (stdev(array)) 
	vars = [str(round(packet_min, 2)), str(round(packet_avg, 2)), str(round(packet_max, 2)),str(round(stdev(stdev_var), 2))]
	print("printing vars: " + vars)
	return vars
	# return delay

if __name__ == '__main__':
		ping("google.co.il")

