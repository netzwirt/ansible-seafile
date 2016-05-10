#!/bin/bash
#
# {{ ansible_managed }}
#
# Create seafile user from shell
# Usage: ./init_admin.sh <username> <password>
#
#

cd {{ seafile_home_path }}

source env.sh

/usr/bin/env python {{ seafile_installation_path }}/init_admin.py $1 $2
