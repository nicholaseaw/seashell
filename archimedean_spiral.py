"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "nicholas.eaw"
__version__ = "2020.07.09"

import rhinoscriptsyntax as rs
import math

def f(t):
    return t * math.sin(t)

def g(t):
    return t* math.cos(t)
    
def evaluate(t):
    point = (f(t), g(t), 0)
    rs.AddPoint(point)

def graph(t0, t1, dt):
    points = []
    curve = []
    
    t = t0
    
    while t <= t1:
        points.append((f(t), g(t), 0))
        evaluate(t)
        t = t + dt
    points.append((f(t1),g(t1),0))
    pl = rs.AddPolyline(points)
    curve.append(pl)
    
    return curve

a = graph(0,y,0.01)
        
    