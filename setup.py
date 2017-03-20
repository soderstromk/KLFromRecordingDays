import cx_Freeze
import sys
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\soderstromk\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tcl8.6" #C:\Users\soderstromk\AppData\Local\Programs\Python\Python35\tcl\tcl8.6
os.environ['TK_LIBRARY'] = "C:\\Users\\soderstromk\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("KLFromRecordingDays.py", base=base)]

cx_Freeze.setup(
	name = "KLFromRecordingDays",
	options = {"build_exe": {"packages":["tkinter","numpy"], "include_files": 'C:\\Windows\\System32\\userenv.dll'}},
    version = "1.1",
    description = "Calculates KL distances by day from multiday SAP2011 MySQL tables",
    executables = executables
    )