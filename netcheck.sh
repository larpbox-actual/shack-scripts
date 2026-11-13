#!/bin/sh
# quick and dirty link check. run it before you ring me.
# usage: ./netcheck.sh [hostfile]

HOSTS="${1:-hosts.txt}"

if [ ! -f "$HOSTS" ]; then
    echo "no host file. make one, one host per line."
    exit 1
fi

down=0
while read -r h; do
    case "$h" in ''|\#*) continue ;; esac
    if ping -c 2 -W 2 "$h" >/dev/null 2>&1; then
        echo "ok    $h"
    else
        echo "DOWN  $h"
        down=$((down+1))
    fi
done < "$HOSTS"

# TODO mail this somewhere instead of just printing it
[ "$down" -gt 0 ] && echo "$down down. have you tried the power cable"
exit 0
