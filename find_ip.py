import os

subnet = "192.168.1."

for i in range (1,256):
    ip = ("%s%s" % (subnet, i))
    #print (ip)
    cmd = ("ping -n 2 -w 1 %s%s" % (subnet, i))
    output = os.popen(cmd).read()
    #print(i)
    if (output.find("Reply",0) > 0):
        print(ip)

print ("ok")
