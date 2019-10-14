from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        pass


class Revolution(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        f1 = FunctionGraph(lambda x: 1/x, x_min=0.1)
        f2 = FunctionGraph(lambda x: 1/x, x_max=-0.1, x_min=-10)
        func = VGroup(f1, f2)
        func2 = FunctionGraph(lambda x: 1/x, x_min=1)

        self.play(Write(func), Write(axes))
        self.wait()

        self.play(Transform(f1, func2), Uncreate(f2))
        self.wait()


class Horn(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=2*PI,
            checkerboard_colors=[]
        )
        surface.center()

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

    @staticmethod
    def func(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])
