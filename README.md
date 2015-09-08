# Tools
Some little tools.

## Documentation

### ping.sh

#### Description
Ping a list of IPs or domain names in a file and return the time.

#### Usage
Write down all IPs or domain names in a file:
```
192.30.252.128
www.google.com
www.wikipedia.org
```

```
bash ping.sh [FILE]
```

### scan.py

#### Description
Check new messages from a website every day and seng a email to yourself if there are some new messages.

#### Usage
Add a line to `/etc/crontab`:
```
55 23   * * *   [USER]  python3 [PATH]/scan.py
```
Replace [USER] and [PATH] with proper values.

Modify the variables used for configuration and the related code in `scan.py`:
```
URL, SMTP_server, Email_addr, Password
```

