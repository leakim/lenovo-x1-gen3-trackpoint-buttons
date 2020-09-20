obj-m := hid-multitouch.o
KDIR := /lib/modules/$(shell uname -r)/build 
PWD := $(shell pwd) 
all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules 
clean: 
	$(MAKE) -C $(KDIR) M=$(PWD) clean
insmod:
	rmmod hid-multitouch || true
	insmod ./hid-multitouch.ko
install:
	install -m 644 -o root -g root  ./hid-multitouch.ko /lib/modules/$(shell uname -r)/kernel/drivers/hid/
