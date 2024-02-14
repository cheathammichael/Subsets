import os
import re
import sys
import fileinput
import ipaddress

ips = [

]

subnets = [

]

notCovered = [

]

covered = [

]

covSub = [

]

print("Input your subnet list filename (followed by .txt):")
input1 = input()

file1 = open(input1, 'r')
Lines = file1.readlines()
file1.close()

for line in Lines:
    string = line.strip()
    subnets.append(string)

print("Input your IP list filename (followed by .txt):")
input2 = input()

file2 = open(input2, 'r')
Lines1 = file2.readlines()
file2.close()

for line in Lines1:
    string1 = line.strip()
    ips.append(string1)

x = 0
sub = ''

for ip in ips:
	for subnet in subnets:	
		if (ipaddress.ip_address(ip) in ipaddress.ip_network(subnet)):
			sub = subnet
			x = 1
			break
		else:
			x = 0
	if (x==0):
		notCovered.append(ip)
		x = 0
	else:
		covSub.append(sub)
		covered.append(ip)

with open('Not-Covered.txt', 'a+') as file_object:
		file_object.write('IPs in ' + input2 + ' not covered by subnets in ' + input1 + ':')
		file_object.write('\n')
		file_object.close()

for ip in notCovered:
	with open('Not-Covered.txt', 'a+') as file_object:
		file_object.write('\n')
		file_object.write(ip)
		file_object.close()

y=0

for ip in covered:
	with open('Covered.txt', 'a+') as file_object:
		file_object.write('\n')
		file_object.write(ip + ' covered by ' + covSub[y])
		file_object.close()
	y = y + 1

print('')
print('Run complete.')
print('')
print(os.system('cat Not-Covered.txt'))
print('')
print('Results stored in "Not-Covered.txt".')