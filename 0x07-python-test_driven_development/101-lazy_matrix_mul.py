#!/usr/bin/python3
"""
     Module for lazy matrix multplication


"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Lazy matrix """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    return np.dot(m_a, m_b)
