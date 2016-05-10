#!/usr/bin/env python
#
# {{ ansible_managed }}

from check_init_admin import rpc
import os
import subprocess
import sys

def main():
    
    subprocess.call(["{{ seafile_installation_path }}/seafile.sh", "start"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if len(sys.argv) == 3:
        check = rpc.rpc_client.add_emailuser(sys.argv[1],sys.argv[2], 0, 1)
        if check == -1:
            print "changed=False"
        sys.exit(0)
    else:
        print
        print "Usage: create_client.py <username> <password>"
        print 
        sys.exit(1)


if __name__ == '__main__':
    
    try:
        main()
    except KeyboardInterrupt:
        print '\n\n\n'
        print 'Aborted.'
        print
        sys.exit(1)
    except Exception, e:
        print
        print 'Error happened during creating seafile user:'
        print e
        print
        sys.exit(1)
