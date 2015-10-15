#! /bin/bash

echo "Starting server. Logging to prost_log.log"
echo "ctrl-c to stop"
python src/pysrc/server.py > prost_log.log
