"""Collection of functions for the manipulation of time series."""

import os.path as _os_path
import sys as _sys
import warnings as _warnings

import cltoolbox
from toolbox_utils import tsutils as _tsutils

__all__ = [
    "unstack",
    "accumulate",
    "add_trend",
    "aggregate",
    "calculate_fdc",
    "calculate_kde",
    "clip",
    "convert",
    "convert_index",
    "convert_index_to_julian",
    "converttz",
    "correlation",
    "createts",
    "date_offset",
    "date_slice",
    "describe",
    "dtw",
    "equation",
    "ewm_window",
    "expanding_window",
    "fill",
    "filter",
    "fit",
    "forecast",
    "gof",
    "lag",
    "normalization",
    "pca",
    "pct_change",
    "peak_detection",
    "pick",
    "plot",
    "rank",
    "read",
    "regression",
    "remove_trend",
    "replace",
    "rolling_window",
    "stack",
    "stdtozrxp",
    "tstopickle",
    "unstack",
]

from .functions.accumulate import accumulate
from .functions.add_trend import add_trend
from .functions.aggregate import aggregate
from .functions.calculate_fdc import calculate_fdc
from .functions.calculate_kde import calculate_kde
from .functions.clip import clip
from .functions.convert import convert
from .functions.convert_index import convert_index
from .functions.convert_index_to_julian import convert_index_to_julian
from .functions.converttz import converttz
from .functions.correlation import correlation
from .functions.createts import createts
from .functions.date_offset import date_offset
from .functions.date_slice import date_slice
from .functions.describe import describe
from .functions.dtw import dtw
from .functions.equation import equation
from .functions.ewm_window import ewm_window
from .functions.expanding_window import expanding_window
from .functions.fill import fill
from .functions.filter import filter
from .functions.fit import fit
from .functions.forecast import forecast
from .functions.gof import gof
from .functions.lag import lag
from .functions.normalization import normalization
from .functions.pca import pca
from .functions.pct_change import pct_change
from .functions.peak_detection import peak_detection
from .functions.pick import pick
from .functions.plot import plot
from .functions.rank import rank
from .functions.read import read
from .functions.regression import regression
from .functions.remove_trend import remove_trend
from .functions.replace import replace
from .functions.rolling_window import rolling_window
from .functions.stack import stack
from .functions.stdtozrxp import stdtozrxp
from .functions.tstopickle import tstopickle
from .functions.unstack import unstack

_warnings.filterwarnings("ignore")


@cltoolbox.command()
def about():
    """Display version number and system information."""
    _tsutils.about(__name__)


def main():
    """Set debug and run cltoolbox.main function."""
    if not _os_path.exists("debug_tstoolbox"):
        _sys.tracebacklimit = 0
    cltoolbox.main()


if __name__ == "__main__":
    main()
