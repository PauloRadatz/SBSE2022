# -*- coding: utf-8 -*-
# @Time    : 7/8/2022 3:52 PM
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : Parte_03_Item_01.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import numpy as np


script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../../../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")
dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
dss.text("BusCoords BusCoords.dat")
dss.text("solve")

print("\nParte 3 - Item 7")

dss.text("ClearBusMarkers")
dss.text(f"set markcapacitor=yes")
dss.text(f"set markregulators=yes")
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")