from typing import overload
from c import float_p

class vec2:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None: ...
    def copy(self) -> vec2: ...
    def __add__(self, other: vec2) -> vec2: ...
    def __sub__(self, other: vec2) -> vec2: ...
    def __mul__(self, other: float) -> vec2: ...
    def __truediv__(self, other: float) -> vec2: ...
    def dot(self, other: vec2) -> float: ...
    def cross(self, other: vec2) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> vec2: ...
    def rotate(self, radians: float) -> vec2: ...
    def addr(self) -> float_p: ...

class vec3:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None: ...
    def copy(self) -> vec3: ...
    def __add__(self, other: vec3) -> vec3: ...
    def __sub__(self, other: vec3) -> vec3: ...
    def __mul__(self, other: float) -> vec3: ...
    def __truediv__(self, other: float) -> vec3: ...
    def dot(self, other: vec3) -> float: ...
    def cross(self, other: vec3) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> vec3: ...
    def addr(self) -> float_p: ...

class vec4:
    x: float
    y: float
    z: float
    w: float

    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    def copy(self) -> vec4: ...
    def __add__(self, other: vec4) -> vec4: ...
    def __sub__(self, other: vec4) -> vec4: ...
    def __mul__(self, other: float) -> vec4: ...
    def __truediv__(self, other: float) -> vec4: ...
    def dot(self, other: vec4) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> vec4: ...
    def addr(self) -> float_p: ...

class mat3x3:
    _11: float
    _12: float
    _13: float
    _21: float
    _22: float
    _23: float
    _31: float
    _32: float
    _33: float

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _11, _12, _13, _21, _22, _23, _31, _32, _33) -> None: ...
    @overload
    def __init__(self, a: list[list]): ...

    def set_zeros(self) -> None: ...
    def set_ones(self) -> None: ...
    def set_identity(self) -> None: ...

    def copy(self) -> mat3x3: ...
    def determinant(self) -> float: ...
    def transpose(self) -> mat3x3: ...

    def __getitem__(self, index: tuple[int, int]) -> float: ...
    def __setitem__(self, index: tuple[int, int], value: float) -> None: ...
    def __add__(self, other: mat3x3) -> mat3x3: ...
    def __sub__(self, other: mat3x3) -> mat3x3: ...
    def __mul__(self, other: float) -> mat3x3: ...
    def __truediv__(self, other: float) -> mat3x3: ...

    def __invert__(self) -> mat3x3: ...
    @overload
    def __matmul__(self, other: mat3x3) -> mat3x3: ...
    @overload
    def __matmul__(self, other: vec3) -> vec3: ...

    @staticmethod
    def zeros() -> mat3x3: ...
    @staticmethod
    def ones() -> mat3x3: ...
    @staticmethod
    def identity() -> mat3x3: ...

    # affine transformations
    @staticmethod
    def trs(t: vec2, r: float, s: vec2) -> mat3x3: ...

    def is_affine(self) -> bool: ...

    def _t(self) -> vec2: ...
    def _r(self) -> float: ...
    def _s(self) -> vec2: ...

    def transform_point(self, p: vec2) -> vec2: ...
    def transform_vector(self, v: vec2) -> vec2: ...
