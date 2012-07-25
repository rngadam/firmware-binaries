firmware-binaries
=================

Firmware Binaries Images of Lophilo

To be put in BOOT (fat32) partition of the OS SDCard.

* boot.bin: bootloader, loaded by SAM9M10 MPU rom code at boot)
* grid.rbf: Lophilo GRID, the FPGA image into the Altera FPGA by the bootloader
* kernel.txt: versioning information
* nfsboot-debug.sh: example script to boot from NFS with debug kernel
* nfsboot.sh: example to boot from NFS with regular kernel
* nfsroot: pointer nfsroot to NFSROOT (example)
* vmlinux: uncompressed kernel
* vmlinux-debug: uncompressed debug kernel
* zImage: compressed kernel, loaded and started by bootloader
* zImage-debug: compressed debug kernel, loaded and started by bootloader
