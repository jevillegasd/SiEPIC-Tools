import pya

# Netlist extraction will merge straight+bend sections into waveguide (1), 
# or extract each bend, straight section, etc. (0)
#WAVEGUIDE_extract_simple = 1
SIMPLIFY_NETLIST_EXTRACTION = True

#Create GUI's
from .core import WaveguideGUI, MonteCarloGUI, CalibreGUI, Net, Component
WG_GUI = WaveguideGUI()
MC_GUI = MonteCarloGUI()
DRC_GUI = CalibreGUI()

#Define global Net object that implements netlists and pin searching/connecting
NET = Net()

#Define global Component object
COMPONENT = Component()

#Define enumeration for pins
from .utils import enum
PIN_TYPES = enum('IO', 'OPTICAL', 'ELECTRICAL')

try:
  import numpy
except ImportError:
  MODULE_NUMPY = False
  
#ACTIONS = []



# Waveguide DevRec: space between the waveguide and the DevRec polygon
WG_DEVREC_SPACE = 1

# Path to Waveguide, path snapping to nearest pin. Search for pin with this distance:
PATH_SNAP_PIN_MAXDIST = 20

