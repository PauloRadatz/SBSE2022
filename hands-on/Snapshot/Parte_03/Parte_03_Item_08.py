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

print("\nParte 3 - Item 8")

nodes = dss.circuit_all_node_names()
voltages = dss.circuit_all_bus_vmag_pu()
min_voltage = min(voltages)
min_voltage_index = voltages.index(min_voltage)
bus_min_voltage = nodes[min_voltage_index].split(".")[0]

# dss.text("BusCoords BusCoords.dat")
dss.text("ClearBusMarkers")
dss.text(f"AddBusMarker Bus={bus_min_voltage} code=7 color=Red size=10")
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")