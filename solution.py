# Kiera McCabe
# Computer Networking Web Server Python Program


# import socket module
from socket import *
import sys # In order to terminate the program

#host='127.0.0.1' #provided host from assignment

def webServer(port=13331): #start of function header, use 13331 else assumes port 80 and returns 404 not found
	serverSocket = socket(AF_INET, SOCK_STREAM) #serversocket is welcoming socket

	#Prepare a server socket
	serverSocket.bind(("", port)) #binding to (host, port)
	#Fill in start DONE
	serverSocket.listen(1) #parameter 1 sets max
	#Fill in end DONE
	

	while True:
		print('PRINT STATEMENT: Ready to serve...') #uncommented provided line
		#Establish the connection
		connectionSocket, addr = serverSocket.accept() #Fill after '='

		try:
			print('PRINT STATEMENT: Try 1') 
			try:
				message = connectionSocket.recv(1024).decode() #Fill after '='
				filename = message.split()[1]
				f = open(filename[1:])
				outputdata = f.read() #Fill after '='

				#Send one HTTP header line into socket.
				#Fill in start
				connectionSocket.send('HTTP/1.1 200 OK'.encode())
				print('PRINT STATEMENT: HTTP Header Line 200 OK')
				#Fill in end

				#Send the content of the requested file to the client
				for i in range(0, len(outputdata)):
					connectionSocket.send(outputdata[i].encode())
				connectionSocket.send("\r\n".encode())
				connectionSocket.close()


			except IOError:
				#Fill in start DONE

				# Send response message for file not found (404)
				connectionSocket.send('HTTP/1.1 404 Not Found'.encode())
				print('PRINT STATEMENT: 404 Not Found response')

				#Close client socket
				connectionSocket.close()

				#Fill in end DONE

		except (ConnectionResetError, BrokenPipeError):
			pass


	serverSocket.close()
	sys.exit()  # Terminate the program after sending the corresponding data
	print('PRINT STATEMENT: Outside of While Loop, exited')


if __name__ == "__main__":
	webServer(13331)