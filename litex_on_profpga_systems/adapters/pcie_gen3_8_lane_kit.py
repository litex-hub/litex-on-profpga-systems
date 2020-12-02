#
# This file is part of LiteX-on-proFPGA-Systems.
#
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *

# PCIe gen3 8-lane Kit (downgraded to 4-lanes) -----------------------------------------------------

def pcie_gen3_x4_adapter(site):
    return [
        ("pcie_x4", 0,
            Subsignal("rst_n", Pins(f"{site}:0"), IOStandard("LVCMOS12")),
            Subsignal("clk_n", Pins(f"{site}:1")),
            Subsignal("clk_p", Pins(f"{site}:2")),
            Subsignal("rx_n",  Pins(f"{site}:3  {site}:4  {site}:5  {site}:6 ")),
            Subsignal("rx_p",  Pins(f"{site}:11 {site}:12 {site}:13 {site}:14")),
            Subsignal("tx_n",  Pins(f"{site}:19 {site}:20 {site}:21 {site}:22")),
            Subsignal("tx_p",  Pins(f"{site}:27 {site}:28 {site}:29 {site}:30")),
        ),
    ]

# PCIe gen3 8-lane Kit -----------------------------------------------------------------------------

def pcie_gen3_x8_adapter(site):
    return [
        ("pcie_x8", 0,
            Subsignal("rst_n", Pins(f"{site}:0"), IOStandard("LVCMOS12")),
            Subsignal("clk_n", Pins(f"{site}:1")),
            Subsignal("clk_p", Pins(f"{site}:2")),
            Subsignal("rx_n",  Pins(f"{site}:3  {site}:4  {site}:5  {site}:6  {site}:7  {site}:8  {site}:9  {site}:10")),
            Subsignal("rx_p",  Pins(f"{site}:11 {site}:12 {site}:13 {site}:14 {site}:15 {site}:16 {site}:17 {site}:18")),
            Subsignal("tx_n",  Pins(f"{site}:19 {site}:20 {site}:21 {site}:22 {site}:23 {site}:24 {site}:25 {site}:26")),
            Subsignal("tx_p",  Pins(f"{site}:27 {site}:28 {site}:29 {site}:30 {site}:31 {site}:32 {site}:33 {site}:34")),
        ),
    ]
