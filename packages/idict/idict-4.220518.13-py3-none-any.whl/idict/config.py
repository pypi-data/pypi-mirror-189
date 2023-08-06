#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the idict project.
#  Please respect the license - more about this in the section (*) below.
#
#  idict is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  idict is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with idict.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is illegal and unethical regarding the effort and
#  time spent here.
from pathlib import Path
from typing import TypeVar, Dict, Union

from idict.persistence.disk import Disk

VT = TypeVar("VT")

GLOBAL = {
    "cache": Disk(f"{Path.home()}/{'.idict/shelve.db'}"),
    "compression_cache": {},
    "compression_cachesize": 0,
    "compression_cachelimit": 1_000_000_000,
}


def setup(cache: Union[Disk, Dict[str, VT]] = None, compression_cachelimit_MB: float = None):
    """
    Global behavior of idict

    Parameters
    ----------
    cache
        Dict-like storage accessed through '^' operator.
    compression_cachelimit_MB
        Amount of MBs reserved for keeping compressed values in memory.
        Higher values accelerate persisting original values as compression is already done at hashing.
    """
    if cache is not None:
        GLOBAL["cache"] = cache
    if compression_cachelimit_MB is not None:
        GLOBAL["compression_cachelimit"] = int(compression_cachelimit_MB * 1_000_000)
