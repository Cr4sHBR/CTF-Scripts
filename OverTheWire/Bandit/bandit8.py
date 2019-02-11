#!/usr/bin/python

from paramiko import SSHClient
import paramiko


server = "bandit.labs.overthewire.org"
port = "2220"
username = "bandit8"
password = "cvX2JJa4CFALtqS87jk27qwqGhBM9plV"


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
    ssh.exec_cmd("cat data.txt | sort | uniq -u")
