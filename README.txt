To use this library add the following to your KiCAD Path: 

KICAD_USER_LIBRARY : <path to this directory>
KICAD_USER_3DMOD : <path to this directory>/user-3dmodels/


========== Schematic Symbol Import ==========

Once added to the Path open the KiCAD Library Editor, navigate to:
    Preferences -> Component Libraries
    
In the "Component library files" section click Add and navigate to the 
UserSymbols.lib file in the user-symbols directory

Once complete you should be able to use this new library in the KiCAD 
Schematic Editor


============= PCB Layout Import =============

Open Pcbnew in KiCAD
Under Preferences -> Footprint Libraries Manager scroll to the bottom of 
"Global libraries" and click "Append Library"

In the new empty row put in a nickname for the new library (UserFootprints) and
the absolute path to the user-footprints/UserFootprints.pretty/ directory from 
this repository