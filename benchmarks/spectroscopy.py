from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import six  # noqa
import numpy as np
from skbeam.spectroscopy import align_and_scale


class TimeSuite:

    def setUp(self):
        E = np.linspace(0, 50, 1000)
        # this is not efficient for large lists, but quick and dirty
        e_list = []
        c_list = []
        for j in range(25, 35, 2):
            e_list.append(E)
            c_list.append(synthetic_data(E,
                                         j + j / 100,
                                         j / 10, 1000,
                                         2*np.pi * 6/50, 60))
        self.c_list = c_list
        self.e_list = e_list

    def time_align_and_scale(self):
        """Test skbeam.spectroscopy align_and_scale.

        This code and the code generated the synthetic data are borrowed
        from skbeam/tests/test_spectroscopy.py
        """
        e_cor_list, c_cor_list = align_and_scale(self.e_list, self.c_list)


def synthetic_data(E, E0, sigma, alpha, k, beta):
    """
    return synthetic data of the form
    d = alpha * e ** (-(E - e0)**2 / (2 * sigma ** 2) + beta * sin(k * E)
    Parameters
    ----------
    E : ndarray
        The energies to compute values at
    E0 : float
       Location of the peak
    sigma : float
       Width of the peak
    alpha : float
       Height of peak
    k : float
       Frequency of oscillations
    beta : float
       Magnitude of oscillations
    """
    return (alpha * np.exp(-(E - E0)**2 / (2 * sigma**2)) +
            beta * (1 + np.sin(k * E)))
