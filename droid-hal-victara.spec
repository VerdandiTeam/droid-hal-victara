# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device victara
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto X 2014

%define installable_zip 1

%define enable_kernel_update 1

%define straggler_files \
/init.mmi.boot.sh\
/init.mmi.radio.sh\
/init.mmi.touch.sh\
/init.mmi.usb.sh\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

