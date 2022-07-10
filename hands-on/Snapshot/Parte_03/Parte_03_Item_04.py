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

print("\nParte 3 - Item 4")

dss.text(f"compile [{dss_file}]")
dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
dss.text("Buscoords Buscoords.dat ")
dss.text("solve")

dss.lines_write_name("L116")
dss.circuit_set_active_element("Line.L116")

print(f"a")
print(f"Bus1 = {dss.lines_read_bus1()}")
print(f"Bus2 = {dss.lines_read_bus2()}")
print(f"Bus1 and Bus2 = {dss.cktelement_read_bus_names()}")

print(f"b")
print(f"Linecode = {dss.lines_read_linecode()}")

print(f"c")
print(f"unit = {dss.lines_read_units()}")
print(f"Rmatrix = {dss.lines_read_rmatrix()} Ohm/km")
print(f"Xmatrix = {dss.lines_read_xmatrix()} Ohm/km")
print(f"Cmatrix = {dss.lines_read_cmatrix()} nF/km")

print(f"d")
v_mag_bus1 = np.array(dss.cktelement_voltages_mag_ang()[:6:2])
v_ang_bus1 = np.array(dss.cktelement_voltages_mag_ang()[1:6:2])
print(f"V_mag_bus1 = {v_mag_bus1} V")
print(f"V_ang_bus1 = {v_ang_bus1} deg")

v_mag_bus2 = np.array(dss.cktelement_voltages_mag_ang()[6:12:2])
v_ang_bus2 = np.array(dss.cktelement_voltages_mag_ang()[7:12:2])
print(f"V_mag_bus2 = {v_mag_bus2} V")
print(f"V_ang_bus2 = {v_ang_bus2} deg")

print(f"e")
i_mag_bus1 = np.array(dss.cktelement_currents_mag_ang()[:6:2])
i_ang_bus1 = np.array(dss.cktelement_currents_mag_ang()[1:6:2])
print(f"i_mag_bus1 = {i_mag_bus1} A")
print(f"i_ang_bus1 = {i_ang_bus1} deg")
i_mag_bus2 = np.array(dss.cktelement_currents_mag_ang()[6:12:2])
i_ang_bus2 = np.array(dss.cktelement_currents_mag_ang()[7:12:2])
print(f"i_mag_bus2 = {i_mag_bus2} A")
print(f"i_ang_bus2 = {i_ang_bus2} deg")