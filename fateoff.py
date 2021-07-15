import os


def lvmcreate():
  lvminput = input("You want to create lvm y/n? :")
  if lvminput == 'y':
    os.system("fdisk -l") 
    print()
    pv = input("Enter your Disks name for creating PV:") 
        
    os.system("pvcreate {}".format(pv))
    os.system("pvdisplay {}".format(pv))
    print("=============================================================================")
    vgname = input("Enter VG Name:")
    os.system("vgcreate {} {}".format(vgname, pv)) 
    os.system("vgdisplay {}".format(vgname))
    print(vgname)
    print("=============================================================================")

    lvsize = input("Enter size of LV in {K,M,G}: ")
    lvname = input("Enter LV Name: ")
    os.system("lvcreate --size {} -n {} {} ".format(lvsize, lvname, vgname))
    os.system("lvdisplay")
    print("=============================================================================")

    path = input("Enter path of disk :")
    os.system("mkfs.ext4 {}".format(path))
    print("=============================================================================")



  elif lvminput == 'n':
    print("Try Again!!")
  else:
    print("Select available optins")
print("================================================================================")


print("\t\t\tWelcome to LVM Automation")
print("\t\t********************************************")

while True:
    print("""

    1. display all available PV,LV,LG 

    2. Create PV,VG,LV in one go

    3. to create PV 
    
    4. to create VG from available PV
    
    5. to create LV from available VG
    
    6. to mount LV to DataNode
    
    7. to Extend LV
    
    8. to Reduce LV
    
    """)
    val = input("Enter your choice 0-6 : " )
    if val=='1':
        os.system("df -h")
        print("\t\t\tPhysical Volume")
        print("\t\t********************************************")
        os.system("pvdisplay")
        print("\t\t\tVolume Group")
        print("\t\t********************************************")
        os.system("vgdisplay")
        print("\t\t\tLogical Volume")
        print("\t\t********************************************")
        os.system("lvdisplay")
         
    elif val=='2':
        lvmcreate()
    elif val=='3':
         pv_m = input("Enter your Disks name for creating PV:") 
         os.system("pvcreate {}".format(pv_m))
         os.system("pvdisplay {}".format(pv_m))
         print("=============================================================================")
    elif val=='4':
        vgname_m = input("Enter VG Name:")
        os.system("vgcreate {} {}".format(vgname_m, pv_m)) 
        os.system("vgdisplay {}".format(vgname_m))
        print(vgname_m)
        print("=============================================================================")
    elif val=='5':
        lvsize_m = input("Enter size of LV : ")
        lvname_m = input("Enter LV Name: ")
        os.system("lvcreate --size {} -n {} {} ".format(lvsize_m, lvname_m, vgname_m))
        os.system("lvdisplay")
        print("=============================================================================")
    elif val=='6':
        path = input("Enter path of disk :")
        os.system("mkfs.ext4 {}".format(path))
        print("=============================================================================")
        dirname = input("Enter directory name: ")
        os.system("mkdir {}".format(dirname))
        os.system("mount {} {}".format(path, dirname))

    elif val=='7':

        break
    else:
        print("select from the given options")

