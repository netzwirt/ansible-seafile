#Seafile server

Install seafile fileserver.

##Role Variables


@see defaults/main.yml

##Init database

When is `seafile_create_database` set to True, database is initialized after it's created.
To initialize manualy use extra vars:
 
     ansible-playbook ../../path/to/playbook.yml --extra-vars '{"seafile_init_database": True}'

##Misc
Sometimes you need to restart memcached, when assets not loading properly.

     service memcached restart

##Dependencies

None

Example Playbook
----------------

    - hosts: seafile
      become: True
      roles:
         - netzwirt.seafile

# License

BSD

# Author Information

[netzwirt](https://github.com/netzwirt)).
