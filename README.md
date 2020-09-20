# Lenovo Thinkpad X1 Tablet Gen3 (20KJ)

Add support for Lenovo Thinkpad X1 Tablet Gen3 trackpoint and buttons


Build
=====

```
sudo apt-get install build-essential libelf-dev linux-headers-`uname -r`
cd linux-5.4.66
make

# next step will fail if you have secure boot enabled in BIOS as this module will not be signed
make insmod

# XXX: only do this if you can live without Secure Boot (...) or learn how to sign kernel modules
make install
```


Upstream
========

Patch was submitted to linux kernel on 9 feb 2019.

https://www.spinics.net/lists/linux-input/msg60060.html

Was included in 5.1

Upstream
========

After hid refactoring in early 5.x, this patch stoped to work.

New patch was submitted to on 19 sep 2020.

It will hopefully be included in 5.10
