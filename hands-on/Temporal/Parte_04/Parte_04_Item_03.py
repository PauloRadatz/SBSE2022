import py_dss_interface
import os
import pathlib
import pandas as pd

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../../../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

my_loadshape = "New Loadshape.my_loadshape " \
               "npts=24 " \
               "interval=1 " \
               "mult=(0.39, 0.29, 0.25, 0.23, 0.31, 0.49, 0.58, 0.46, 0.51, 0.52, 0.58, 0.59, 0.63, 0.56, 0.54, 0.54, " \
               "0.58, 0.72, 0.86, 0.91, 1, 0.74, 0.51) "

print("\nParte 5 - Item 3")
di_voltexceptions_1_file = pathlib.Path(script_path).joinpath("../../../feeders", "123Bus", "ieee123", "DI_yr_0", "DI_VoltExceptions_1.csv")

dss.text(f"compile [{dss_file}]")
dss.text(f"{my_loadshape}")
dss.text(f"batchedit load..* daily=my_loadshape")
dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")

dss.text("BusCoords BusCoords.dat")
dss.text("new loadshape.gen npts=24 interval=1 mult=[0 0 0 0 0 0 .1 .2 .3  .5  .8  .9  1.0  1.0  .99  .9  .7  .4  .1 "
         "0  0  0  0  0]")
dss.text("new generator.gen bus1=108 kv=4.160 kw=6000 pf=1 daily=gen")


dss.text("set demandinterval=True")
dss.text("set voltexceptionreport=True")

dss.text("set mode=daily")
dss.text("set maxiterations=20")


dss.text("solve")
dss.text("closeDI")

voltage_results_df = pd.read_csv(di_voltexceptions_1_file, index_col=0)
num_ov = sum(voltage_results_df[' "Overvoltage"'])
print(f"Actual Number of nodes with Overvoltage = {num_ov} \n")

for pf in [1, -.99, -.98, -.97, -.96, -.95]:
    dss.text(f"compile [{dss_file}]")
    dss.text(f"{my_loadshape}")
    dss.text(f"batchedit load..* daily=my_loadshape")

    dss.text("BusCoords BusCoords.dat")
    dss.text("new loadshape.gen npts=24 interval=1 mult=[0 0 0 0 0 0 .1 .2 .3  .5  .8  .9  1.0  1.0  .99  .9  .7  .4  "
             ".1 0  0  0  0  0]")
    dss.text("new generator.gen bus1=108 kv=4.160 kw=6000 pf=1 daily=gen")

    dss.text("set demandinterval=True")
    dss.text("set voltexceptionreport=True")

    dss.text("set mode=daily")
    dss.text("set maxiterations=20")

    dss.text(f"edit generator.gen pf={pf}")

    dss.text("solve")
    dss.text("closeDI")

    voltage_results_df = pd.read_csv(di_voltexceptions_1_file, index_col=0)

    num_ov = sum(voltage_results_df[' "Overvoltage"'])

    print(f"pf={pf:<5} : Number of nodes with Overvoltage = {num_ov}")

    if not (voltage_results_df[' "Overvoltage"'] > 0).any() or \
            (voltage_results_df[' "Undervoltages"'] > 0).any() or \
            (voltage_results_df[' "LV Overvoltage"'] > 0).any() or \
            (voltage_results_df[' "LV Undervoltages"']).any():
        break

print(f"\nResult: pf={pf}")
