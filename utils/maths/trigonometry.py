import numpy as np

TWO_PI = np.pi * 2

def period(interval=TWO_PI):
    def fn(frequency=1):
        return interval / frequency
    return fn


def wave_at(fnc):
    def fn(amplitude=1, frequency=1, h_shift=0, v_shift=0):
        def gn(x):
            return (amplitude * fnc(frequency * (x - h_shift))) + v_shift
        return gn
    return fn


def wave(fnc):
    def fn(amplitude=1, frequency=1, h_shift=0, v_shift=0):
        def gn(t):
            return (amplitude * fnc(frequency * (t - h_shift))) + v_shift
        return gn
    return fn
