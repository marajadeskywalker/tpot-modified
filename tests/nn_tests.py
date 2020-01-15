# -*- coding: utf-8 -*-

"""This file is part of the TPOT library.

TPOT was primarily developed at the University of Pennsylvania by:
    - Randal S. Olson (rso@randalolson.com)
    - Weixuan Fu (weixuanf@upenn.edu)
    - Daniel Angell (dpa34@drexel.edu)
    - and many more generous open source contributors

TPOT is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

TPOT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with TPOT. If not, see <http://www.gnu.org/licenses/>.

"""

from tpot import TPOTClassifier, TPOTRegressor
from tpot.config.classifier_nn import classifier_config_nn
import tpot.nn

import numpy as np
import scipy as sp
import nose
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.utils.estimator_checks import check_estimator
from nose.tools import nottest

train_test_split = nottest(train_test_split)

# For testing, we just use sklearn's small - but widely used - breast cancer
# dataset
cancer_data = load_breast_cancer()

def test_pytorch_lr_is_valid_estimator():
    """Ensure that PytorchLRClassifier passes scikit-learn's estimator validity
    checks."""
    check_estimator(tpot.nn.PytorchLRClassifier)