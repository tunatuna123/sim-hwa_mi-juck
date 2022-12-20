from manim import *
import numpy as np
from scipy.misc import derivative
from math import exp

def f(x):
    return exp(1)**x

def draw_taylor(n,x):
    taylor = 0

    # Iterate over the terms of the Taylor series
    for i in range(n+1):
        # Compute the i-th derivative of f at x0
        deriv = derivative(f, n=i, x0=0, order=33)
        # Add the i-th term of the Taylor series to the approximation
        taylor += deriv * (x)**i / np.math.factorial(i)

    return taylor

class taylor(Scene):

    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )

        cos_x = axes.plot(
            lambda x: exp(x), 
            x_range=[-10,5], 
            color=RED
        )

        for i in range(1,21):
            globals()['taylor_graph_{}'.format(i)] = axes.plot(
                lambda x: draw_taylor(i,x),
                x_range=[-10,5],
                color=BLUE
            )
            globals()['text_{}'.format(i)] = Text(
                'n = {}'.format(i),
                font_size=35
            ).move_to([-3,3,0])

        self.play(Create(axes))
        self.play(Create(cos_x))
        self.wait()
        self.play(Create(taylor_graph_1), Create(text_1))

        for i in range(1,20):
            self.play(
                ReplacementTransform(globals()['taylor_graph_{}'.format(i)],globals()['taylor_graph_{}'.format(i+1)]),
                ReplacementTransform(globals()['text_{}'.format(i)],globals()['text_{}'.format(i+1)])
            )
        self.wait()
