#! /bin/bash
for ip in `cat $1`; do
	avgtime=`ping -c 3 -W 1 $ip 2>null | grep rtt | awk -F / '{ print $5 }'`
	if test -z $avgtime; then
		printf '%s    no\n' $ip
	else
		printf '%s    %s ms\n' $ip $avgtime
	fi
done
