#!/bin/bash

set -e


NAME="sensor-arduino-collector"


DAEMON_RUNTIME="/home/pi/Python-3.6.3/bin/python"
DAEMON_SCRIPT="/home/pi/bin/sensor-arduino-collector.py"
DAEMON_OPTS=""
DAEMON_USER="pi"
DAEMON_PID="/var/run/$NAME.pid"


export PATH="${PATH:+$PATH:}/usr/sbin:/sbin"


case "$1" in
  start)
        echo -n "Starting daemon: $NAME"
        start-stop-daemon --start --background --chuid $DAEMON_USER  --quiet --pidfile $DAEMON_PID --exec $DAEMON_RUNTIME $DAEMON_SCRIPT -- $DAEMON_OPTS
        echo "."
     ;;
  stop)
        echo -n "Stopping daemon: $NAME"
        start-stop-daemon --stop --quiet --oknodo --pidfile $DAEMON_PID
        echo "."
     ;;
  restart)
        echo -n "Restarting daemon: $NAME"
     $0 stop
     $0 start
     echo "."
     ;;

  *)
     echo "Usage: "$0" {start|stop|restart}"
     exit 1
esac

exit 0
