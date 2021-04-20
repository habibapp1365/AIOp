import subprocess


def getStatus(service):
    bashCommand = "systemctl status "+service+".service"
    cmd = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    for line in cmd.stdout:
        if b"Active" in line:
            output = line.decode('UTF-8')
    ls = output.split()
    print(ls[1])
    return(ls[1])

if __name__ == "__main__":
    getStatus("apache2")
