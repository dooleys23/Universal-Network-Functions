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
