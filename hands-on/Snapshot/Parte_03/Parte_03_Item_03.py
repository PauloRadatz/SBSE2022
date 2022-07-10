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

print("\nParte 3 - Item 3")

dss.text(f"compile [{dss_file}]")
dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
dss.text("Buscoords Buscoords.dat ")
dss.text("solve")

dss.circuit_set_active_bus("152")

print(f"a")
v_mag = np.array(dss.bus_vmag_angle()[:6:2])
v_ang = np.array(dss.bus_vmag_angle()[1:6:2])

print(f"V_mag = {v_mag} V")
print(f"V_ang = {v_ang} deg")
print(f"b")

v_base = dss.bus_kv_base() * 1000.0
print(f"V_mag_pu = {v_mag / v_base} pu")
print(f"V_ang = {v_ang} deg")
print(f"Voltage base = {v_base} V")

print(f"f")
print(f"X = {dss.bus_read_x()}")
print(f"Y = {dss.bus_read_y()}")