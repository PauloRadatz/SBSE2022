# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../../../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

my_loadshape = "New Loadshape.my_loadshape " \
               "npts=24 " \
               "interval=1 " \
               "mult=(0.39, 0.29, 0.25, 0.23, 0.31, 0.49, 0.58, 0.46, 0.51, 0.52, 0.58, 0.59, 0.63, 0.56, 0.54, 0.54, 0.58, 0.72, 0.86, 0.91, 1, 0.74, 0.51)"

print("\nParte 3 - Item 1")

dss.text(f"compile [{dss_file}]")
dss.text(f"{my_loadshape}")
dss.text(f"batchedit load..* daily=my_loadshape")
dss.text("set mode=daily")

dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
dss.text("New Monitor.power element=Line.L115 terminal=1 mode=1 ppolar=NO")
dss.text("New Monitor.voltage element=Line.L115 terminal=1 mode=0")

dss.text("solve")

dss.meters_write_name("Feeder")
register_names = dss.meters_register_names()
register_values = dss.meters_register_values()

print(f"a")
print(f"Energy= {register_values[register_names.index('kWh')]} kWh")

print(f"b")
print(f"Max P = {register_values[register_names.index('Max kW')]} kW")

print(f"c")
print(f"Plosses = {register_values[register_names.index('Zone Losses kWh')]} kWh")