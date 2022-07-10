# -*- coding: utf-8 -*-
# @Time    : 7/8/2022 3:52 PM
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : Parte_03_Item_01.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib


script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../../../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

print("\nParte 3 - Item 5")

dss.text(f"compile [{dss_file}]")
dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
dss.text("Buscoords Buscoords.dat ")
dss.text("solve")

dss.regcontrols_first()
for _ in range(dss.regcontrols_count()):
    print(f"{dss.regcontrols_read_name()} with tap number = {dss.regcontrols_read_tap_number()}")
    dss.regcontrols_next()