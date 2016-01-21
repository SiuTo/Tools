#! /usr/bin/env python3

import urllib.request
import re
import datetime
import smtplib
from email.mime.text import MIMEText

Home = "http://www.jwc.fudan.edu.cn"
Page_URL = Home+"/9397/list.htm"
SMTP_server = "mail.fudan.edu.cn"
Email_addr = "xtliang13@fudan.edu.cn"
Password = "*********"

response = urllib.request.urlopen(Page_URL)
html = response.read().decode()

articles = re.findall("<td align=\"left\"><a href=\'(.*)\' target=\'_blank\' title=\'(.*)\' alt=\'.*\'>.*</a>\s*</td>\s*<td align=\"right\">(\d{4})-(\d{2})-(\d{2})\s*</td>", html)

yesterday = datetime.date.today()-datetime.timedelta(days=1)
content = ""
for (url, title, year, month, day) in articles:
	if datetime.date(int(year), int(month), int(day))==yesterday:
		content += title+"    "+Home+url+"\n"
if not content:
	exit()
content = yesterday.isoformat()+"\n\n"+content

msg = MIMEText(content, "plain", "utf-8")
msg["Subject"] = "New Messages from JWC"

server = smtplib.SMTP_SSL(SMTP_server)
server.login(Email_addr, Password)
server.send_message(msg, Email_addr, Email_addr)
server.quit()

