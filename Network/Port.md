
端口号的范围是从1～65535。
其中1～1024是被RFC 3232规定好了的，被称作“众所周知的端口”(Well Known Ports)；
从1025～65535的端口被称为动态端口（Dynamic Ports），可用来建立与其它主机的会话，也可由用户自定义用途。


app-protocols|   port  | protocols | description
-------------|---------|-----------|--------------------------
ftp-data     |      20 | tcp       | FTP, data
ftp          |      21 | tcp       | FTP. control
telnet       |      23 | tcp       |
smtp         |      25 | tcp       | Simple Mail Transfer Protocol
time         |      37 | tcp       | timserver 
time         |      37 | udp       | timserver 
domain       |      53 | tcp       | Domain Name Server
domain       |      53 | udp       | Domain Name Server
tftp         |      69 | udp       | Trivial File Transfer
gopher       |      70 | tcp       | 
http         |      80 | tcp       | www-http World Wide Web
pop3         |     110 | tcp       | Post Office Protocol-Version 3
nntp         |     119 | tcp       | Network News Transfer Protocol
netbios-ns   |     137 | tcp       | NETBIOS Name Service
netbios-ns   |     137 | udp       | NETBIOS Name Service
netbios-dgm  |     138 | udp       | NETBIOS Datagram Service
netbios-ssn  |     139 | tcp       | NETBIOS Session Service
imap         |     143 | tcp       | Internet Message Access Protocol
snmp         |     161 | udp       | SNMP
snmptrap     |     162 | udp       | SNMP trap
irc          |     194 | tcp       | Internet Relay Chat Protocol
ipx          |     213 | udp       | IPX over IP
ldap         |     389 | tcp       | Lightweight Directory Access Protocol
https        |     443 | tcp       | 
https        |     443 | udp       | 
uucp         |     540 | tcp       | 
ldaps        |     636 | tcp       | LDAP over TLS / SSL
doom         |     666 | tcp       | Doom Id Software
doom         |     666 | udp       | Doom Id Software
phone        |    1167 | udp       | Conference calling
ms-sql-s     |    1433 | tcp       | Microsoft-SQL-Server
ms-sql-s     |    1433 | udp       | Microsoft-SQL-Server
ms-sql-m     |    1434 | tcp       | Microsoft-SQL-Monitor
ms-sql-m     |    1434 | udp       | Microsoft-SQL-Monitor
wins         |    1512 | tcp       | Microsoft Windows Internet Name Service
wins         |    1512 | udp       | Microsoft Windows Internet Name Service
l2tp         |    1701 | udp       | Layer Two Tunneling Protocol
             |    1720 | tcp       | 
QICQ         |    4000 | udp       | 
QICQ         |    8000 | udp       | 
QQ           |    1080 | udp       | Socks 代理《木马的常用连接端口》
