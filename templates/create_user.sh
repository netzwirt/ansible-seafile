#!/bin/bash
#
# {{ ansible_managed }}
#
# Create seafile user from shell
# Usage: ./create_user.sh <username> <password>
#
#

cd {{ seafile_home_path }}

source env.sh

/usr/bin/env python {{ seafile_installation_path }}/create_user.py $1 $2
