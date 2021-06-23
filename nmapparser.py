import sys
import json
import xmltodict

if len(sys.argv) == 3 :
	with open(sys.argv[1]) as f:
		filecontent = f.read()
		nmdict = xmltodict.parse(filecontent)
		for host in nmdict['nmaprun']['host']:
			if 'script' in host['ports']['port']:
				if '@output' in host['ports']['port']['script']:
					if host['ports']['port']['script']['@id'] == sys.argv[2]:
						print(host['address']['@addr'])
						print(host['ports']['port']['script']['@id'])
						print(host['ports']['port']['@portid'])
						print(host['ports']['port']['script']['@output'])
else:
	print('usage : ' + sys.argv[0] + ' nmapscanoutput.xml CVE-Number')
