#
# This file is part of LiteX-on-proFPGA-Systems.
#
# Copyright (c) 2020 Antmicro <www.antmicro.com>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk
    ("clk300", 0,
        Subsignal("n", Pins("CA40"), IOStandard("LVDS")),
        Subsignal("p", Pins("CA39"), IOStandard("LVDS")),
    ),
]

# Connectors ---------------------------------------------------------------------------------------

_connectors = [
    ("TA1", { # FIXME: use real connector name, fake ones used since no access to documentation.
        "io0"  : "E40",
        "io1"  : "AU10",
        "io2"  : "AU11",
        "io3"  : "AJ1",
        "io4"  : "AK3",
        "io5"  : "AL1",
        "io6"  : "AM3",
        "io7"  : "AN1",
        "io8"  : "AP3",
        "io9"  : "AR1",
        "io10" : "AT3",
        "io11" : "AJ2",
        "io12" : "AK4",
        "io13" : "AL2",
        "io14" : "AM4",
        "io15" : "AN2",
        "io16" : "AP4",
        "io17" : "AR2",
        "io18" : "AT4",
        "io19" : "AL6",
        "io20" : "AM8",
        "io21" : "AN6",
        "io22" : "AP8",
        "io23" : "AR6",
        "io24" : "AT8",
        "io25" : "AU6",
        "io26" : "AV8",
        "io27" : "AL7",
        "io28" : "AM9",
        "io29" : "AN7",
        "io30" : "AP9",
        "io31" : "AR7",
        "io32" : "AT9",
        "io33" : "AU7",
        "io34" : "AV9",
    }),
    ("TA2", {}), # FIXME: TBD
    ("TA3", {}), # FIXME: TBD
    ("TA4", {}), # FIXME: TBD
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name   = "clk300"
    default_clk_period = 1e9/300e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xcvu19p-fsva3824-2-e", _io, _connectors, toolchain="vivado")

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        # For passively cooled boards, overheating is a significant risk if airflow isn't sufficient
        self.add_platform_command("set_property BITSTREAM.CONFIG.OVERTEMPSHUTDOWN ENABLE [current_design]")
        # Reduce programming time
        self.add_platform_command("set_property BITSTREAM.GENERAL.COMPRESS TRUE [current_design]")

        # TA1 pins Internal Vref
        self.add_platform_command("set_property INTERNAL_VREF 0.90 [get_iobanks 69]")
        self.add_platform_command("set_property INTERNAL_VREF 0.90 [get_iobanks 70]")
        self.add_platform_command("set_property INTERNAL_VREF 0.90 [get_iobanks 71]")

        self.add_period_constraint(self.lookup_request("clk300", 0, loose=True), 1e9/300e6)
