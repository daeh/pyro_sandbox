%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

import torch
torch.set_default_dtype(torch.float64)  # double precision for numerical stability

import collections
import argparse
import matplotlib.pyplot as plt

import pyro
import pyro.distributions as dist
import pyro.poutine as poutine
from pyro.optim import Adam
from pyro.infer import SVI, Trace_ELBO
from torch.distributions import constraints
import torch.nn.functional as F
from torch.autograd import Variable

# search_inference.py
# from search_inference import factor, HashingMarginal, memoize, Search

pyro.enable_validation(True)

# defining sigmoid, logistic functions that work on torch tensors
def sigmoid(x):
    return logistic(x, maxVal=1.0, steepness=1.0, midpoint=0.0)

def logistic(x, maxVal=1.0, steepness=1.0, midpoint=0.0):
    # https://en.wikipedia.org/wiki/Logistic_function
    return torch.tensor(maxVal)/(torch.tensor(1.)+torch.exp(-steepness*(x-midpoint)))

myPlotColors = ["olive", "green", "gold", "darkgrey", "red", "maroon", "darkorchid", "midnightblue"]


# %%

loc = 0
scale = 1
normal = dist.Normal(loc, scale)


#gittest