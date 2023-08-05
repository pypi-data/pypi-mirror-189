from ..cs import ColorSpace as ColorSpace
from numpy.typing import ArrayLike as ArrayLike

def create_cs_class_instance(cs_class: type[ColorSpace], whitepoint: ArrayLike, c: float, Y_b: float, L_A: float): ...
def stress_absolute(target: ArrayLike, actual: ArrayLike, weights: Union[float, ArrayLike] = ...) -> float: ...
def stress_relative(target: ArrayLike, actual: ArrayLike, weights: Union[float, ArrayLike] = ...) -> float: ...
