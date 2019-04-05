# Author: Shawn Dooley
# Date 20190405
# Program that watches network devices, alerts on new devices which are connected.
# Will produce html for GUI, will also create alrtered version for cron-emailing.

import os


def netwatch_full_scan():
    host_dic = {}
    f_list = read_file()

    ip = ''
    mac = ''
    switch = False

    # F-List is output of nmap -sv x.x.x.x/subnet.
    # Can be swapped out for f_list= os.popen(' nmap -sv x.x.x.x/subnet.').read()

    for row in f_list:
        if row.lower().startswith('nmap scan report for'):
            ip = row.split(' ')[4]

        elif row.lower().startswith('mac address:'):
            try:
                mac = row.split(' ')[2]
                host_dic[ip] = mac
            except:
                host_dic[ip] = mac
    return host_dic


def netwatch_host_scan(host_dic):
    for row in host_dic:
        os.popen('nmap -v -A -SV {}'.format(row))


def read_file():
    f_list =[]
    with open('net_watch.txt', 'r') as f:
        f = f.read().split('\n')
        for row in f:
            f_list.append(row)
    return f_list


def find_owner(host_dic):
    owner_dic = {}
    with open('host_owner.txt', 'r') as f:
        f = f.read().split('\n')
        for row in f:
            row = row.split(',',1)
            # owner = hosts
            owner_dic[row[0]]  = row[1]

    for ip in host_dic:
        new_phone_switch = True
        for owner in owner_dic:
            if host_dic[ip] in owner_dic[owner].split(','):
                new_phone_switch = False

        if new_phone_switch == True:
            print(host_dic[ip])

# netwatch_host_scan(netwatch_full_scan())
find_owner(netwatch_full_scan())
code.interact(local=locals())
