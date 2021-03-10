# LVM_Commands

#### To Install LVM

 yum install lvm2

pvcreate — This command converts the attached Disk or external disk into physical volume.

vgcreate — This command creates the volume groups for all the specified physical volumes.

vgdisplay — This command displays all the available or created volume groups.

lvcreate — This command creates the logical volume from the volume group.

lvdisplay — This command displays all the available or created logical volumes from the volume groups.

lvextend — This command extends the current logical volume size from the available space of the volume group.

resize2fs — This command extends the unallocated space of the partition without formatting it.


### Steps

1. pvcreate /dev/sdb

'/dev/sdb' is the Volume attached.

2. vgcreate tk7 /dev/sdb 

 'tk7' - is the name of Volume Group
 'dev/sdb' - pv name

3. lvcreate --size +4G tk7 -n tk7lv

'tk7' - vg name
'tk7lv' - lv name

4. mkfs.ext4 /dev/tk7/tk7lv

It will format the storage.

5. mount and enjoy..!!
