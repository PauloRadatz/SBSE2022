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

dss.text(f"compile [{dss_file}]")
dss.text("solve")

print("\nParte 3 - Item 1")

print(f"Converged: {dss.solution_read_converged()}")
print(f"P = {-1 * dss.circuit_total_power()[0]} kW")
print(f"Q = {-1 * dss.circuit_total_power()[1]} kvar")
