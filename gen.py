#!/usr/bin/env python3

#
# This file is part of LitePCIe.
#
# Copyright (c) 2019-2020 Florent Kermarrec <florent@enjoy-digital.fr>
# Copyright (c) 2020 Antmicro <www.antmicro.com>
# SPDX-License-Identifier: BSD-2-Clause

"""
LitePCIE standalone core generator for proFPGA systems

LitePCIe aims to be directly used as a python package when the SoC is created using LiteX. However,
for some use cases it could be interesting to generate a standalone verilog file of the core:
- integration of the core in a SoC using a more traditional flow.
- need to version/package the core.
- avoid Migen/LiteX dependencies.
- etc...

The standalone core is generated from a YAML configuration file that allows the user to generate
easily a custom configuration of the core.
"""

import yaml
import argparse
import subprocess

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *

from litepcie.software import generate_litepcie_software_headers

from litepcie.gen import LitePCIeCore

from litex.build.generic_platform import *

def main():
    parser = argparse.ArgumentParser(description="LitePCIe standalone core generator for proFPGA systems")
    parser.add_argument("config", help="YAML config file")
    parser.add_argument("--doc",  action="store_true", help="Build documentation")
    args = parser.parse_args()
    core_config = yaml.load(open(args.config).read(), Loader=yaml.Loader)

    # Convert YAML elements to Python/LiteX --------------------------------------------------------
    for k, v in core_config.items():
        replaces = {"False": False, "True": True, "None": None}
        for r in replaces.keys():
            if v == r:
                core_config[k] = replaces[r]

    # Generate core --------------------------------------------------------------------------------
    if core_config["phy"] == "USP19PPCIEPHY":
        from litex.build.xilinx import XilinxPlatform
        from litex_on_profpga_systems.pcie.usppciephy import USP19PPCIEPHY
        platform = XilinxPlatform(core_config["phy_device"], io=[], toolchain="vivado")
        core_config["phy"]           = USP19PPCIEPHY
        core_config["qword_aligned"] = False
        core_config["endianness"]    = "little"
    else:
        raise ValueError("Unsupported PCIe PHY: {}".format(core_config["phy"]))
    soc      = LitePCIeCore(platform, core_config)
    builder  = Builder(soc, output_dir="build", compile_gateware=False)
    builder.build(build_name="litepcie_core", regular_comb=True)
    generate_litepcie_software_headers(soc, "./")

    if args.doc:
        soc.generate_documentation("litepcie_core")

if __name__ == "__main__":
    main()
