# 	BLOCKED TABLE
#  _______________
# |ID | IP | PORT |
# -----------------
# 	FLAG TABLE
#  ___________________________________________________________________
# | ICMP | TCP | ARP | UDP | BACKGROUND | AUTOBLOCKING | NOTIFICATION |
# ---------------------------------------------------------------------

import sqlite3


def add_ip_port_to_block(ip, port):
    file = sqlite3.connect('sfile.db')
    try:
        query="INSERT INTO BLOCKED (IP,PORT) VALUES ('" + str(ip) + "'," + str(port) + ");"
        file.execute(query)
        file.commit()
    except:
        print 'invalid ip,port'
        return False
    file.close()
    return True


def new_change_flag(string, state):
    file = sqlite3.connect('sfile.db')
    query = "UPDATE FLAG SET " + str(string) + " = '" + str(state)+"' ;"
    print(query)
    file.execute(query)
    file.commit()

    fetch = "SELECT ICMP, TCP, ARP, UDP, BACKGROUND, AUTOBLOCKING, NOTIFICAIION FROM FLAG;"
    status = file.execute(fetch)
    file.commit()
    print(status)

    #dict = {"ICMP":status[0], "TCP": status[1], "ARP":status[2], "UDP":status[3], "BACKGROUND":status[4], "AUTOBLOCKING":status[5], "NOTIFICAIION":status[6]}

    #print(dict)

    for row in status:
        print ("ICMP = ", row[0])
        print ("TCP = ", row[1])
        print ("ARP = ", row[2])
        print ("UDP = ", row[3])
        print ("BACKGROUND = ", row[1])
        print ("AUTOBLOCKING = ", row[2])
        print ("NOTIFICATION = ", row[3])

    file.close()



def change_flag(icmp, tcp, arp, udp, background, autoblocking, notification):
    file = sqlite3.connect('sfile.db')
    query = "UPDATE FLAG SET ICMP='" + str(icmp) + "',TCP='" + str(tcp) + "',ARP='" + str(arp) + "',UDP='" + str(
        udp) + "',BACKGROUND='" + str(background) + "',AUTOBLOCKING='" + str(autoblocking) + "',NOTIFICAIION='" + str(
        notification) + "'"
    file.execute(query)
    file.commit()
    file.close()


def add_ip_mac(ip, mac):
    file = sqlite3.connect('sfile.db')
    file.execute("INSERT INTO MACIP (IP,MAC) VALUES ('" + ip + "','" + str(mac) + "');")
    file.commit()
    file.close()


def add_logdata(text):
    file = open('logfile', 'a')
    file.write(text)
    file.close()


def flush_tables():
    open('logfile','w').write('')
    file = sqlite3.connect('sfile.db')
    file.execute("delete from macip;")
    file.execute("delete from blacklist;")
    file.commit()
    file.close()

def get_flags():
    file = sqlite3.connect('sfile.db')
    data=file.execute("SELECT * FROM FLAG").fetchall()[0]
    file.commit()
    file.close()
    n=['icmp','tcp','arp','udp','imt','background','autoblocking','notification']
    fdata=dict()
    for i in range(len(n)):
        if data[i]==u'True':
            fdata[n[i]]=True
        else:
            fdata[n[i]]=False
    return fdata