#!/bin/bash

if [ -z ${1} ]; then
  echo '[*] Please, provide a path to send in 1st argument'
  exit 1
elif ! ([ -f ${1} ] || [ -d ${1} ]); then
  echo '[*] Specified path does not exist'
  exit 1
fi

if [ -z ${2}]; then
  bandwidth_lim='20m'
else
  bandwidth_lim=${2}
fi

# Private key for password-less SSH connection ...
path_to_private_key='./ssh-keys/id_rsa'

# Necessary to access RSync daemons module on server ...
export RSYNC_PASSWORD='PASSWORD HERE'

# Specifies SSH command which RSync will be using for data transfer ...
export RSYNC_CONNECT_PROG="ssh -i ${path_to_private_key} -p <PORT> <SSH_USER>@<SSH_SERVER>"

# Specifies Rsync credentials
remote_dir=<RSYNC_USER>@<RSYNC_SERVER>::<RSYNC_MODULE_NAME>

# Paths to log files ...
rsync_log_file='./rsync.log'

timeout 4m rsync \
  --log-file=${rsync_log_file} \
  --bwlimit=${bandwidth_lim} \
  --recursive \
  --delete-after \
  --compress-level=9 \
  --partial \
  ${1} ${remote_dir} > /dev/null 2>&1

if [ $? -eq 0 ]; then
  echo '[*] Complete successfully ...'
else
  echo '[*] Complete with error ...'
fi