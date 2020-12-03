#!/usr/bin/env python3

#
# This file is part of LiteX-on-proFPGA-Systems.
#
# Copyright (c) 2020 Florent Kermarrec <florent@enjoy-digital.fr>
# Copyright (c) 2020 Antmicro <www.antmicro.com>
# SPDX-License-Identifier: BSD-2-Clause

import os
import argparse

from migen import *

from litex_on_profpga_systems.platforms import profpga_vu19p
from litex_on_profpga_systems.adapters.pcie_gen3_8_lane_kit import *

from litex.soc.cores.clock import *
from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *

from litex_on_profpga_systems.pcie.usppciephy import USP19PPCIEPHY
from litepcie.core import LitePCIeEndpoint, LitePCIeMSI
from litepcie.frontend.dma import LitePCIeDMA
from litepcie.frontend.wishbone import LitePCIeWishboneBridge
from litepcie.software import generate_litepcie_software

# CRG ----------------------------------------------------------------------------------------------

class _CRG(Module):
    def __init__(self, platform, sys_clk_freq):
        self.clock_domains.cd_sys    = ClockDomain()

        # # #

        self.submodules.pll = pll = USPPLL(speedgrade=-2)
        pll.register_clkin(platform.request("clk300"), 300e6)
        pll.create_clkout(self.cd_sys, sys_clk_freq)

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
    def __init__(self, sys_clk_freq=int(200e6),
        with_pcie=False, pcie_site="TA1", pcie_speed="gen3", pcie_lanes=4, pcie_dmas=1,
        **kwargs):
        platform = profpga_vu19p.Platform()

        # SoCCore ----------------------------------------------------------------------------------
        kwargs["uart_name"] = "crossover" # Enforce Crossover UART.
        SoCCore.__init__(self, platform, sys_clk_freq,
            ident          = "LiteX SoC on proFPGA VU19P",
            ident_version  = True,
            **kwargs)

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = _CRG(platform, sys_clk_freq)

        # PCIe -------------------------------------------------------------------------------------
        if with_pcie:
            platform.add_extension(pcie_gen3_8_lane_adapter(site=pcie_site, lanes=pcie_lanes))
            pcie_data_width = {
               # Gen3
               "gen3:x4" : 128,
               "gen3:x8" : 256,
               # Gen4
               "gen4:x4" : 256,
               "gen4:x8" : 512,
            }[pcie_speed + f":x{pcie_lanes}"]
            self.submodules.pcie_phy = USP19PPCIEPHY(platform, platform.request(f"pcie_x{pcie_lanes}"),
                speed      = pcie_speed,
                data_width = pcie_data_width,
                bar0_size  = 0x20000)
            platform.add_false_path_constraints(self.crg.cd_sys.clk, self.pcie_phy.cd_pcie.clk)
            self.add_csr("pcie_phy")
            self.add_pcie(phy=self.pcie_phy, ndmas=pcie_dmas)

# Build --------------------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LiteX SoC on proFPGA VU19P")
    parser.add_argument("--build",         action="store_true", help="Build bitstream")
    parser.add_argument("--with-pcie",     action="store_true", help="Enable PCIe support")
    parser.add_argument("--pcie-site",     default="TA1",       help="PCIe site: TA1 (default)")
    parser.add_argument("--pcie-speed",    default="gen3",      help="PCIe speed: gen3 (default) or gen4")
    parser.add_argument("--pcie-lanes",    default="4",         help="PCIe lanes: 4 (default) or 8")
    parser.add_argument("--pcie-dmas",     default="1",         help="PCIe DMAs: 1 (default) up to 8")
    parser.add_argument("--driver",        action="store_true", help="Generate PCIe driver")
    parser.add_argument("--load",          action="store_true", help="Load bitstream")
    builder_args(parser)
    soc_core_args(parser)
    args = parser.parse_args()

    soc =  BaseSoC(
        with_pcie  = args.with_pcie,
        pcie_site  = args.pcie_site,
        pcie_speed = args.pcie_speed,
        pcie_lanes = int(args.pcie_lanes, 0),
        pcie_dmas  = int(args.pcie_dmas,  0),
        **soc_core_argdict(args))
    builder = Builder(soc, **builder_argdict(args))
    builder.build(run=args.build)

    if args.driver:
        generate_litepcie_software(soc, os.path.join(builder.output_dir, "driver"))

    if args.load:
        prog = soc.platform.create_programmer()
        prog.load_bitstream(os.path.join(builder.gateware_dir, soc.build_name + ".bit"))

if __name__ == "__main__":
    main()
