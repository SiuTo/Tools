#! /usr/bin/env python3

import urllib.request
import re
import datetime
import smtplib
from email.mime.text import MIMEText

URL = "http://www.jwc.fudan.edu.cn/9397/list.htm"
SMTP_server = "mail.fudan.edu.cn"
Email_addr = "xtliang13@fudan.edu.cn"
Password = "123456789"

response = urllib.request.urlopen(URL)
html = response.read().decode()

articles = re.findall("<td align=\"left\"><a href=\'(.*)\' target=\'_blank\' title=\'(.*)\' alt=\'.*\'>.*</a>\s*</td>\s*<td align=\"right\">(\d{4})-(\d{2})-(\d{2})\s*</td>", html)

today = datetime.date.today()
content = ""
for (url, title, year, month, day) in articles:
	if datetime.date(int(year), int(month), int(day))==today:
		content += title+"\t"+home+url+"\n"
if not content:
	exit()
content += today.strftime("%Y-%m-%d")+"\n"

msg = MIMEText(content, "plain", "utf-8")
msg["Subject"] = "New Messages from JWC"

server = smtplib.SMTP()
server.connect(SMTP_server)
server.login(Email_addr, Password)
server.sendmail(Email_addr, Email_addr, msg.as_string())
server.quit()

