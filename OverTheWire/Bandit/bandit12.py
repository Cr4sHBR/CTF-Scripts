#!/usr/bin/python

from paramiko import SSHClient
import paramiko
import sys



server = "bandit.labs.overthewire.org"
port = "2220"
username = "bandit12"
password = "5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu"


class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=server ,port=port ,username=username,password=password)

    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            print "The password for next level is -> "+stdout.read()


if __name__ == '__main__':
    ssh = SSH()
    ssh.exec_cmd("cd /tmp/tste")
    stdin.flush()
    ssh.exec_cmd("xxd -r data.txt > xxd_reverse")
    stdin.flush()
    ssh.exec_cmd("zcat tmp/tste/xxd_reverse > tmp/tste/data_zcat")
    stdin.flush()
    ssh.exec_cmd("bzip2 -d tmp/tste/data_zcat")
    stdin.flush()
    ssh.exec_cmd("zcat tmp/tste/data_zcat.out > tmp/tste/data_zcat_2")
    stdin.flush()
    ssh.exec_cmd("tar xvf tmp/tste/data_zcat_2")
    stdin.flush()
    ssh.exec_cmd("tar xvf tmp/tste/data5.bin")
    stdin.flush()
    ssh.exec_cmd("bzip2 -d tmp/tste/data6.bin")
    stdin.flush()
    ssh.exec_cmd("tar xvf tmp/tste/data6.bin.out")
    stdin.flush()
    ssh.exec_cmd("zcat tmp/tste/data8.bin > tmp/tste/data8_zcat")
    stdin.flush()
    ssh.exec_cmd("cat tmp/tste/data8_zcat")
