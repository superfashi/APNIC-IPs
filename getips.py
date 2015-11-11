import ftplib
import sys
from math import log
from os import path

if not path.exists('delegated-apnic-latest'):
	apnicip = ftplib.FTP('ftp.apnic.net')
	apnicip.login()
	apnicip.cwd('/public/apnic/stats/apnic')
	ipfile = open('delegated-apnic-latest', 'w')
	print('start retriving!')
	apnicip.retrbinary('RETR delegated-apnic-latest', ipfile.write)
	ipfile.close()

ipfinal = open('ipfinal.txt', 'w')
ipfile = open('delegated-apnic-latest', 'r')

needcountry = sys.argv[1]
ipori = ipfile.readlines()
print('Start grabbing!')
for ips in ipori:
	try:
		if ips.split('|')[2] == 'ipv4':
			pass
		else:
			continue
	except IndexError:
		continue
	if ips.split('|')[1] == needcountry or needcountry == 'all':
		ip = ips.split('|')[3]
		netmask = str(int(32 - log(int(ips.split('|')[4]), 2)))
		ipfinal.writelines(ip + '/' + netmask + '\n')
print('Grab complete!')
ipfinal.close()