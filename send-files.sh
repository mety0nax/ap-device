#!/bin/bash

if [ -f '/tmp/rsync-sending' ]; then
  echo '[*] Rsync task already running'
  exit 0
else
  touch /tmp/rsync-sending
fi

if [ -z ${1} ]; then
  echo '[*] Please, provide a path to send in 1st argument'
  rm -rf /tmp/rsync-sending
  exit 1
elif ! ([ -f ${1} ] || [ -d ${1} ]); then
  echo '[*] Specified path does not exist'
  rm -rf /tmp/rsync-sending
  exit 1
fi

if [ -z ${2} ]; then
  bandwidth_lim='20m'
else
  bandwidth_lim=${2}
fi

python3 /home/pi/apDevice/prepExcludeList.py /home/pi/apDevice/data_*

# Private key for password-less SSH connection ...
path_to_private_key='/home/pi/apDevice/ssh-keys/id_rsa'

# Necessary to access RSync daemons module on server ...
export RSYNC_PASSWORD='RSYNC_USER_PASSWORD'

# Specifies SSH command which RSync will be using for data transfer ...
export RSYNC_CONNECT_PROG="ssh -i ${path_to_private_key} -p <SSH_PORT> <SSH_USER>@<SSH_SERVER>"

# Specifies Rsync credentials
remote_dir=<RSYNC_USER>@<RSYNC_SERVER>::<RSYNC_MODULE>

# Paths to log files ...
rsync_log_file='/home/pi/apDevice/logs/rsync.log'

timeout 4m rsync \
  --log-file=${rsync_log_file} \
  --bwlimit=${bandwidth_lim} \
  --recursive \
  --exclude-from='/tmp/excludeList.txt' \
  --exclude '.gitkeep' \
  --remove-source-files \
  --compress-level=9 \
  --partial \
  ${1} ${remote_dir} > /dev/null 2>&1

if [ $? -eq 0 ]; then
  echo '[*]' $(date) 'Complete successfully ...'
else
  echo '[*]' $(date) 'Complete with error ...'
fi

rm -rf /tmp/rsync-sending