import sqlite3

print("initiate.py called")

connection = sqlite3.connect('sfile.db')

connection.execute("""
	DROP TABLE IF EXISTS BLOCKED;
	""")

connection.execute("""
	DROP TABLE IF EXISTS FLAG;
	""")

connection.execute("""
	DROP TABLE IF EXISTS MACIP;
	""")

connection.execute("""
	DROP TABLE IF EXISTS BLACKLIST;
	""")

connection.execute("""
	CREATE TABLE BLOCKED
	(
	IP AUTOCHAR(20) DEFAULT "",
	PORT INTEGER DEFAULT NONE);
	""")
connection.execute("""
	CREATE TABLE FLAG
	(ICMP BOOLEAN DEFAULT TRUE,
	TCP BOOLEAN DEFAULT TRUE,
	ARP BOOLEAN DEFAULT TRUE,
	UDP BOOLEAN DEFAULT TRUE,
	IMP BOOLEAN DEFAULT TRUE,
	BACKGROUND BOOLEAN DEFAULT TRUE,
	AUTOBLOCKING BOOLEAN DEFAULT TRUE,
	NOTIFICAIION BOOLEAN DEFAULT TRUE
	);
	""")
connection.execute("""
	CREATE TABLE MACIP
	(
	MAC AUTOCHAR(50) DEFAULT '',
	IP AUTOCHAR(50) DEFAULT ''
	);
	""")
connection.execute("""
	CREATE TABLE BLACKLIST 
	(
	MAC	AUTOCHAR(50) DEFAULT '',
	IP	AUTOCHAR(50) DEFAULT ''
	);
	""")

connection.execute("""
     INSERT INTO FLAG ( ICMP,TCP,ARP,UDP,BACKGROUND,AUTOBLOCKING,NOTIFICAIION )
     VALUES ('True', 'True', 'True', 'True', 'True', 'True', 'True');
""")

connection.commit()

connection.close()
