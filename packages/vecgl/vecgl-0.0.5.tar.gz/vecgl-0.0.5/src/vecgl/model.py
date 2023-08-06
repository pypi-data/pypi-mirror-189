from typing import Iterable, List, Union

from vecgl.linalg import (Mat4, Vec3, Vec4, mul_mat4, mul_mat4_vec4, str_vec4,
                          vec3_to_homogenious_vec4)

kDefaultSurfaceColor = "lightgray"
kDefaultLineColor = "black"


class Point:

    def __init__(self, p: Vec4, color: str):
        self.p = p
        self.color = color

    def transform(self, U: Mat4) -> "Point":
        transformed_p = mul_mat4_vec4(U, self.p)
        return Point(transformed_p, self.color)

    def __str__(self) -> str:
        return str_vec4(self.p)


class Line:

    def __init__(self, p: Vec4, q: Vec4, color: str):
        self.p = p
        self.q = q
        self.color = color

    def transform(self, U: Mat4) -> "Line":
        transformed_p = mul_mat4_vec4(U, self.p)
        transformed_q = mul_mat4_vec4(U, self.q)
        return Line(transformed_p, transformed_q, self.color)

    def __str__(self) -> str:
        return f"{str_vec4(self.p)} to {str_vec4(self.q)}"

    def __eq__(self, other) -> bool:
        return isinstance(
            other, Line
        ) and self.p == other.p and self.q == other.q and self.color == other.color


class Triangle:

    def __init__(self, p: Vec4, q: Vec4, r: Vec4, color: str):
        self.p = p
        self.q = q
        self.r = r
        self.color = color

    def transform(self, U: Mat4) -> "Triangle":
        transformed_p = mul_mat4_vec4(U, self.p)
        transformed_q = mul_mat4_vec4(U, self.q)
        transformed_r = mul_mat4_vec4(U, self.r)
        return Triangle(transformed_p, transformed_q, transformed_r,
                        self.color)

    def __str__(self) -> str:
        return f"{str_vec4(self.p)}, {str_vec4(self.q)}, {str_vec4(self.r)}"


class Model:

    def __init__(self):
        self.points: List[Point] = []
        self.lines: List[Line] = []
        self.triangles: List[Triangle] = []

    def add_point(self, p: Union[Vec3, Vec4], color: str = kDefaultLineColor):
        p = vec3_to_homogenious_vec4(p)
        self.points.append(Point(p, color))

    def add_line(self,
                 p: Union[Vec3, Vec4],
                 q: Union[Vec3, Vec4],
                 color: str = kDefaultLineColor):
        p = vec3_to_homogenious_vec4(p)
        q = vec3_to_homogenious_vec4(q)
        self.lines.append(Line(p, q, color))

    def add_line_chain(self,
                       ps: Iterable[Union[Vec3, Vec4]],
                       color: str = kDefaultLineColor):
        p = None
        for q in ps:
            if p is not None:
                self.add_line(p, q, color)
            p = q

    def add_triangle(
        self,
        p: Union[Vec3, Vec4],
        q: Union[Vec3, Vec4],
        r: Union[Vec3, Vec4],
        color: str = kDefaultSurfaceColor,
    ):
        p = vec3_to_homogenious_vec4(p)
        q = vec3_to_homogenious_vec4(q)
        r = vec3_to_homogenious_vec4(r)
        self.triangles.append(Triangle(p, q, r, color))

    def add_triangle_strip(self,
                           ps: Iterable[Union[Vec3, Vec4]],
                           color: str = kDefaultSurfaceColor):
        p, q = None, None
        for r in ps:
            if p is not None and q is not None:
                self.add_triangle(p, q, r, color)
            p = q
            q = r

    def add_model(self, model: "Model"):
        self.points += model.points
        self.lines += model.lines
        self.triangles += model.triangles

    def _transform(self, U: Mat4):
        transformed = Model()
        transformed.points = [pt.transform(U) for pt in self.points]
        transformed.lines = [ln.transform(U) for ln in self.lines]
        transformed.triangles = [tr.transform(U) for tr in self.triangles]
        return transformed

    def transform(self, *Us: Mat4):
        return self._transform(mul_mat4(*Us))
