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

print("\nParte 3 - Item 4")

dss.text(f"compile [{dss_file}]")
dss.text(f"{my_loadshape}")
dss.text(f"batchedit load..* daily=my_loadshape")
dss.text("set mode=daily")

dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
dss.text("New Monitor.power element=Line.L115 terminal=1 mode=1 ppolar=NO")
dss.text("New Monitor.voltage element=Line.L115 terminal=1 mode=0")

dss.text("New EnergyMeter.meter_load_s48 element=Line.L47 terminal=1")
dss.text("New Monitor.power_load_s48 element=Load.s48 terminal=1 mode=1 ppolar=NO")
dss.text("New Monitor.voltage_load_s48 element=Load.s48 terminal=1 mode=0")

dss.text("solve")

dss.text("Plot monitor object=voltage_load_s48 channels=(1 3 5 ) bases=[2400 2400 2400]")
dss.text("Plot monitor object=voltage_load_s48 channels=(9 11 13 )")