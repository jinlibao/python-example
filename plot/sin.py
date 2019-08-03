#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sin.py - 2019-08-02 20:21
#
# Copyright © 2019 Libao Jin <jinlibao@outlook.com>
# Distributed under terms of the MIT license.
#
'''
Sin
'''

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


class Sin(object):

    def __init__(self):
        plt.style.use('ggplot')
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')

    def plot(self, x, y, filename):
        with PdfPages(filename) as pdf:
            fig = plt.figure()
            plt.plot(x, y)
            plt.show(block=False)
            pdf.savefig(fig)

    def test(self):
        x = np.linspace(-6, 6, 200)
        y = np.sin(x)
        self.plot(x, y, 'sin.pdf')


if __name__ == '__main__':
    c = Sin()
    c.test()
'''
End of file
'''
