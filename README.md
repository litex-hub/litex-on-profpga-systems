```
                                 __   _ __      _  __
                                / /  (_) /____ | |/_/
                               / /__/ / __/ -_)>  <
                              /____/_/\__/\__/_/|_|
                                   / _ \/ _ \
                        _______  __\___/_//_/ ____         __
         ___  _______  / __/ _ \/ ___/ _ |   / __/_ _____ / /____ __ _  ___
        / _ \/ __/ _ \/ _// ___/ (_ / __ |  _\ \/ // (_-</ __/ -_)  ' \(_-<
       / .__/_/  \___/_/ /_/   \___/_/ |_| /___/\_, /___/\__/\__/_/_/_/___/
      /_/                                      /___/
                   Copyright (c) 2020, LiteX on proFPGA Systems Developers
```
[![](https://github.com/litex-hub/litex-on-profpga-systems/workflows/ci/badge.svg)](https://github.com/litex-hub/litex-on-profpga-systems/actions) ![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)

[> Intro
--------
In this repository, we experiment creating systems on proFPGA processing systems with LiteX.
proFPGA systems are generic FPGA processing systems exposing the FPGA's IOs on sereval sites
allowing the system to be customized with specific adapters boards.

The initial aim of this project is to demonstrate some LiteX based configurations on proFPGA hardware
and provide an infrastructure to easily modify/extend them using LiteX's flexibility.

<p align="center"><img width="800" src="https://github.com/litex-hub/litex-on-profpga-systems/raw/master/doc/intro.png"></p>

[> Features
-----------
**TODO**

[> Prerequisites
----------------
- Python3, Vivado.
- A proFPGA VU19P Board.
- A proFPGA PCIe Gen3 X8 Adapter Kit.

[> Installing LiteX
-------------------
```sh
$ wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py
$ chmod +x litex_setup.py
$ sudo ./litex_setup.py init install
$ python3 setup.py develop
```

[> Build and Load the bitstream
--------------------------------
```sh
$ ./profpga_vu19.py --with-pcie --pcie-speed=gen3 --pcie-lanes=4 --pcie-dmas=8 --build --load
```

[> Build LitePCIe standalone core for the ProFPGA VU19 and PCIe Gen3 X8 Adapter Kit
-----------------------------------------------------------------------------------
```sh
$ ./litepcie_gen litepcie_profpga_vu19p.yml
```

[> Tests
--------
**TODO**

[> License
----------
This project is released under the very permissive two-clause BSD license. Under
the terms of this license, you are authorized to use this project for closed-source
proprietary designs.
Even though we do not require you to do so, those things are awesome, so please
do them if possible:
 - tell us that you are using this project
 - cite this project in publications related to research it has helped
 - send us feedback and suggestions for improvements
 - send us bug reports when something goes wrong
 - send us the modifications and improvements you have done to this project.