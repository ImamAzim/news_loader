News Loader
============
a daemon to install on a raspberry pi. Once you connect your ereader, it will automatically fetch news and transfer them to ereader

Status
======
on developpement.

Installlation
==============
#. clone project
#. run install.sh
#. set device id and manuf id in udev rules (udevadm info -d /dev/sda)
#.  udevadm control --reload
#. uid (blkid) in disk-uuid.json
#. change password and username in reveil.recipe
#. reboot

customization
==============
you can change the recipes, remove or add some. if necessary create a .credential file with the same structure as the current one.
