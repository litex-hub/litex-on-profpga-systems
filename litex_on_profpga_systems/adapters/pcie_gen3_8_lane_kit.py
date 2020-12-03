#
# This file is part of LiteX-on-proFPGA-Systems.
#
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *

# PCIe gen3 8-lane Kit -----------------------------------------------------------------------------

def pcie_gen3_8_lane_adapter(site, lanes=8):
    assert lanes in [4, 8]
    if lanes == 4:
        return [
            # FIXME: use real connector name, fake ones used since no access to documentation.
            ("pcie_x4", 0,
                Subsignal("rst_n", Pins(f"{site}:io0"), IOStandard("LVCMOS12")),
                Subsignal("clk_n", Pins(f"{site}:io1")),
                Subsignal("clk_p", Pins(f"{site}:io2")),
                Subsignal("rx_n",  Pins(f"{site}:io3  {site}:io4  {site}:io5 {site}:io6 ")),
                Subsignal("rx_p",  Pins(f"{site}:io11 {site}:io12 {site}:io3 {site}:io14")),
                Subsignal("tx_n",  Pins(f"{site}:io19 {site}:io20 {site}:io1 {site}:io22")),
                Subsignal("tx_p",  Pins(f"{site}:io27 {site}:io28 {site}:io9 {site}:io30")),
            ),
        ]
    if lanes == 8:
        return [
            # FIXME: use real connector name, fake ones used since no access to documentation.
            ("pcie_x8", 0,
                Subsignal("rst_n", Pins(f"{site}:io0"), IOStandard("LVCMOS12")),
                Subsignal("clk_n", Pins(f"{site}:io1")),
                Subsignal("clk_p", Pins(f"{site}:io2")),
                Subsignal("rx_n",  Pins(f"{site}:io3  {site}:io4  {site}:io5  {site}:io6  {site}:io7  {site}:io8  {site}:io9  {site}:io10")),
                Subsignal("rx_p",  Pins(f"{site}:io11 {site}:io12 {site}:io13 {site}:io14 {site}:io15 {site}:io16 {site}:io17 {site}:io18")),
                Subsignal("tx_n",  Pins(f"{site}:io19 {site}:io20 {site}:io21 {site}:io22 {site}:io23 {site}:io24 {site}:io25 {site}:io26")),
                Subsignal("tx_p",  Pins(f"{site}:io27 {site}:io28 {site}:io29 {site}:io30 {site}:io31 {site}:io32 {site}:io33 {site}:io34")),
            ),
        ]
