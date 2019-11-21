#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Change interface MAC Address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC Address")
    #(options, arguments) = parser.parse_args()
    return parser.parse_args()


def change_mac(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])



#interface = options.interface
#mac = options.mac

(options, arguments) = get_arguments()
change_mac(options.interface, options.mac)