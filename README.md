# Lenovo Thinkpad X1 Tablet Gen3 (20KJ)

Add support for Lenovo Thinkpad X1 Tablet Gen3 trackpoint and buttons


Build
=====

```
sudo apt-get install build-essential libelf-dev
cd linux-4.15
make

# next step will fail if you have secure boot enabled in BIOS as this module will not be signed
make insmod

# XXX: only do this if you can live without Secure Boot (...)
make install
```


Upstream
========
Patch was submitted to linux kernel on 9 feb 2019

https://www.spinics.net/lists/linux-input/msg60060.html
