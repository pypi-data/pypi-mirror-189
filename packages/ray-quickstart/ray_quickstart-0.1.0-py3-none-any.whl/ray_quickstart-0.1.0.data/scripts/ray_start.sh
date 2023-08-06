#!/bin/bash

cd ~/git/ai || exit

ip_address=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)
~/.local/share/virtualenvs/ai-lw7wTiLA/bin/ray start --head --node-ip-address $ip_address --port 6380 --ray-client-server-port 10001 --num-gpus 1 --dashboard-host 0.0.0.0 --dashboard-port 8265 --disable-usage-stats
