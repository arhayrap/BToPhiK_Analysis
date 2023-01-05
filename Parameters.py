import warnings
import awkward as ak
import numpy as np
import pandas as pd
import pickle
import array
import copy
import ROOT as rt
import root_numpy as rtnp
import hist as hs
from hist.intervals import ratio_uncertainty
from coffea import processor
from coffea.nanoevents.methods import vector, candidate
from numba import jit
from coffea.nanoevents import BaseSchema
import mplhep as hep
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import date
import matplotlib.pyplot as plt
import matplotlib
import gc
import os

today = date.today()
plt.style.use(hep.style.CMS)
# base = "/uscms/home/ahayrape/nobackup/BToPhiK_py/"