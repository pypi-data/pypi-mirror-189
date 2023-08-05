import numpy as np
from .._exceptions import ColorioError as ColorioError
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class JzAzBz(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    b: float
    g: float
    c1: Incomplete
    c2: Incomplete
    c3: Incomplete
    n: Incomplete
    p: Incomplete
    d: Incomplete
    d0: float
    M1: Incomplete
    M2: Incomplete
    def __init__(self) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, jzazbz: ArrayLike) -> np.ndarray: ...
