#!/usr/bin/env python

import re
import socket

#initializing the tcp socket
TCP_IP = '127.0.0.1'                                    
TCP_PORT = 6666
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
loop == 1
while loop == 1 :
        input = raw_input('\n')
        out = ''
        input = input.replace(' ','') #stripping all the spaces to prevent errors in match
        match = re.match(r'(\D+)\((\d+),(\d+)(\D+)', input)
        matchexit = re.match(r'\D+',input)
       
        if match.group(1) == 'quit'
                break;

        if match.group(1)=='dio.set' :
                out += 'SET DIO['
        elif match.group(1)=='pwm.set' :
                out += 'SET PWM['
        else :
                print "syntax error"
                continue

        if match.group(2) >= 0:
                out += (str(match.group(2)) + ']')
        else :
                print "enter valid pin numbers"
                continue


        if match.group(1) =='dio.set' :
                if match.group(3) == 0 or match.group(3) == 1 :
                        out += (',' + str(match.group(3)))
        elif match.group(1) =='pwm.set':
                if match.group(3 )>= 0 or match.group(3) <=100:
                        out += (',' + str(match.group(3)))
        else :
                print "invalid value"
                continue

        print out


        MESSAGE = out


        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        print "received data:", data


s.close()
