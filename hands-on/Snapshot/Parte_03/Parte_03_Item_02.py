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

print("\nParte 3 - Item 2")

dss.text(f"compile [{dss_file}]")
dss.text("solve")

print(f"a")
print(f"Plosses = {dss.circuit_losses()[0] / 10 ** 3} kW")

print(f"b")
print(f"Qlosses = {dss.circuit_losses()[1] / 10 ** 3} kvar")

print(f"c")
print(f"Plinelosses = {dss.circuit_line_losses()[0]} kW")
print(f"Qlinelosses = {dss.circuit_line_losses()[1]} kvar")

print(f"d")
print(f"Ptransformerlosses = {dss.circuit_losses()[0] / 10 ** 3 - dss.circuit_line_losses()[0]} kW")
print(f"Qtransformerlosses = {dss.circuit_losses()[1] / 10 ** 3 - dss.circuit_line_losses()[1]} kvar")
