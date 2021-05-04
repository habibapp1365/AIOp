import subprocess
from configparser import ConfigParser


path={
    "sshd"      : "/home/hbb/workspace/AIO/AIOp/core/config.ini",
    "apache2"   : "/home/hbb/workspace/AIO/AIOp/core/apache2.ini",
    }


def getStatus(service):
    bashCommand = "systemctl status "+service+".service"
    cmd = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    for line in cmd.stdout:
        if b"Active" in line:
            output = li.decode('UTF-8')
    ls = output.split()
    print(ls[1])
    return(ls[1])

def isActive(service):
    return(subprocess.call(["systemctl", "is-active", "--quiet", service]))

def parseConfig(service, old, new):
    config = open(path[service])
    tmp = config.readlines()
    config.close()
    for line in tmp:
        if (line.split(' ')[0]).strip('#') == old:
            tmp[tmp.index(line)] = line.replace(line, new+'\n')
    config = open(path[service],"w")
    config.write("".join(tmp))
    config.close()

def readConfig(service, params):
    config = open(path[service])
    tmp = config.readlines()
    config.close()
    for param in params:
        for line in tmp:
            if (line.split(' ')[0]).strip('#') == param:
                return line.split(' ')[1]
    return 0



if __name__ == "__main__":
    readConfig("sshd", ["Port"])
