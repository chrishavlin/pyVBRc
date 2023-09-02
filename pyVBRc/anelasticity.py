import abc

import numpy as np


class DissipationMechanism(abc.ABC):
    @abc.abstractmethod
    def integrate(self):
        # each class must implement its own
        pass

    @abc.abstractmethod
    def evaulate(self):
        # evaluate for a single
        pass

    @abc.abstractmethod
    def get_func(self):
        # evaluate for a single
        pass


class AbsorptionPeak(DissipationMechanism):
    def __init__(
        self, strength, peak_period, peak_width, lower_limit=None, upper_limit=None
    ):
        self.strength = strength
        self.peak_period = peak_period
        self.peak_width = peak_width
        if lower_limit is None:
            lower_limit = 0.0
        self.lower_limit = lower_limit
        if upper_limit is None:
            upper_limit = np.inf
        self.upper_limit = upper_limit


class HighTemperatureBackground(DissipationMechanism):
    def __init__(self, strength, alpha, lower_limit, upper_limit):
        self.strength = strength
        self.alpha = alpha
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit


class ExtendedBurgers:
    def __init__(self):
        pass
