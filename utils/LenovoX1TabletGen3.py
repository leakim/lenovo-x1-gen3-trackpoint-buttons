#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# https://www.beyondlogic.org/usbnutshell/usb4.shtml#Control
#


import sys
import usb1
import time


__maintainer__ = 'Mikael Wikström'
__email__ = '<leakim.wikstrom@gmail.com>'
__url__ = 'https://github.com/leakim/lenovo-x1-gen3-trackpoint-buttons'


VENDOR_ID = 0x17ef  # Lenovo
PRODUCT_ID = 0x60b5 # X1 Tablet Thin Keyboard Gen3
#INTERFACE = 0 # keyboard
INTERFACE = 1  # keyboard Fn
#INTERFACE = 2 # mouse (touchpad / trackpoint)


x1tbl = {
    'FnLockOff':    bytes([0x09, 0x54, 0x01]),  # works as expected
    'FnLockOn':     bytes([0x09, 0x54, 0x02]),  # works as expected
    'FnSpeakerOff': bytes([0x09, 0x64, 0x01]),  # LED on
    'FnSpeakerOn':  bytes([0x09, 0x64, 0x02]),  # LED off
    'FnMicOff':     bytes([0x09, 0x74, 0x01]),  # LED on
    'FnMicOn':      bytes([0x09, 0x74, 0x02]),  # LED off
}


def main():
    if len(sys.argv) <= 1:
        print('syntax: ', sys.argv[0], ' '.join(x1tbl.keys()))
        sys.exit(1)
    args = sys.argv[1:]
    for x in args:
        if x not in x1tbl.keys():
            print(x, 'is not a know command')
            print('syntax: ', sys.argv[0], ' '.join(x1tbl.keys()))
            sys.exit(1)

    with usb1.USBContext() as context:
        handle = context.openByVendorIDAndProductID(
                VENDOR_ID,
                PRODUCT_ID,
                skip_on_error=True,
                )
        if handle is None:
            print("Device not present, or user is not allowed to access device.")
            return

        handle.setAutoDetachKernelDriver(True)
        with handle.claimInterface(INTERFACE):
            for arg in args:
                print(arg)
                data = x1tbl[arg]
                handle.controlWrite(0x21, 9, 0x0209, 1, data, timeout=800)


if __name__ == '__main__':
    main()

# vim: hlsearch
