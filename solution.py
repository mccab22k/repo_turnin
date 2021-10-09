#Kiera McCabe
#NYU Cyberfellow
#Computer NEtworking Assignment 3
from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope


   # Fill in start
   print('Attempt to establish mailserver / port connection')

   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientSocket = socket(AF_INET, SOCK_STREAM) #???
   clientSocket.connect((mailserver,port))
   print('Established mailserver / port connection')
   # Fill in end

   recv = clientSocket.recv(1024).decode()
   print('recv print: ' + recv)
   #you should receive 220 reply from server after TCP connection is established
   if recv[:3] != '220':
       print('220 reply not received from server.')
   # clientSocket.close()
   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   print(heloCommand)
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print('recv1 print: ' + recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   # Fill in start
   mailFromCommand = "MAIL FROM: < kmm9497@nyu.edu >\r\n" # <36287726+mccab22k@users.noreply.github.com>'
   print(mailFromCommand)
   clientSocket.send(mailFromCommand.encode())
   recv2 = clientSocket.recv(1024).decode()
   print('recv2 print: ' + recv2)
   # Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start
   rcptToCommand= "RCPT TO: < kmm9497@nyu.edu > \r\n" #<36287726+mccab22k@users.noreply.github.com>'
   print(rcptToCommand)
   clientSocket.send(rcptToCommand.encode())
   recv3 = clientSocket.recv(1024).decode()
   print('recv3 print statement: ' + recv3)
   # Fill in end

   # Send DATA command and print server response.
   # Fill in start
   dataCommand = 'DATA'
   print(dataCommand)
   clientSocket.send(dataCommand.encode())
   recv4 = clientSocket.recv(1024).decode()
   print('recv4 print statement: ' + recv4)
   # Fill in end

   # Send message data.
   # Fill in start
   messageData = msg
   print(messageData)
   clientSocket.send(messageData.encode())
   recv5 = clientSocket.recv(1024).decode()
   print('recv5 print statement: ' + recv5)
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   messageEnd=endmsg
   print(messageEnd)
   clientSocket.send(messageEnd.encode())
   recv6=clientSocket.recv(1024).decode()
   print('recv6 print statement: ' + recv6)
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   quitCommand = 'QUIT'
   print(quitCommand)
   clientSocket.send(quitCommand.encode())
   recv7=clientSocket.recv(1024).decode
   print('recv7 print statement: ' + recv7)
   # Fill in end
   # clientSocket.close()
   # serverSocket.close()


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')


