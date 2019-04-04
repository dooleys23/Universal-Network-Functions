import requests, re
oui_master_dic = {}

r = requests.get('http://standards-oui.ieee.org/oui.txt')
oui_html_list = r.text.split('\n')

for row in oui_html_list:
  if re.match(r'\s', row):
    continue
  else:
    try:
      if row.split(' ')[0][2] == '-':
        oui_master_dic[row.split(' ')[0][:8]] = row.split('\t',2)[2]
    # EOL hit, expected behavior
    except IndexError as e:
      continue

with open('./path_to_file.txt', 'w+') as cisco_oui_file:
  for row in oui_master_dic:
    if 'cisco' in  oui_master_dic[row].lower():
      cisco_oui_file.write('{0},{1}'.format(row, oui_master_dic[row]))
      
'''
EX: Looking for Cisco MAC's
>>> for row in oui_master_dic:
...   if 'cisco' in  oui_master_dic[row].lower():
...     print row, oui_master_dic[row]


EX Output:
00-0A-41 Cisco Systems, Inc
00-0A-42 Cisco Systems, Inc
00-B0-C2 Cisco Systems, Inc
00-50-3E Cisco Systems, Inc
00-13-80 Cisco Systems, Inc
2C-01-B5 Cisco Systems, Inc
F8-7B-20 Cisco Systems, Inc
08-96-AD Cisco Systems, Inc
...
'''
