"""
Useful basic routines for managing Fresnel reflection

Todo:
    * improve documentation of each routine

Scott Prahl
Apr 2018
"""

import numpy as np

__all__ = ['r_par',
           'r_per',
           't_par',
           't_per',
           'R_par',
           'R_per',
           'T_par',
           'T_per',
           'R_unpolarized']


def r_par(m, theta):
    """
    Calculates the reflected amplitude for parallel polarized light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        reflected field amplitude             [-]
    """
    c = m * m * np.cos(theta)
    s = np.sin(theta)
    d = np.sqrt(m * m - s * s)
    rp = (c - d) / (c + d)
    return np.real_if_close(rp)


def r_per(m, theta):
    """
    Calculates the reflected amplitude for perpendicular polarized light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        reflected field amplitude             [-]
    """
    c = np.cos(theta)
    s = np.sin(theta)
    d = np.sqrt(m * m - s * s)
    rs = (c - d) / (c + d)
    return np.real_if_close(rs)


def t_par(m, theta):
    """
    Calculates the transmitted amplitude for parallel polarized light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        transmitted field amplitude           [-]
    """
    c = np.cos(theta)
    s = np.sin(theta)
    d = np.sqrt(1 - (s/m) ** 2)
    tp = 2 * c / (m * c + d)
    return np.real_if_close(tp)


def t_per(m, theta):
    """
    Calculates the transmitted amplitude for perpendicular polarized light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        transmitted field amplitude           [-]
    """
    c = np.cos(theta)
    s = np.sin(theta)
    d = np.sqrt(m * m - s * s)
    ts = 2 * c / (c + d)
    return np.real_if_close(ts)


def R_par(m, theta):
    """
    Calculates the reflected irradiance for parallel polarized light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        reflected power                       [-]
    """
    return abs(r_par(m, theta))**2


def R_per(m, theta):
    """
    Calculates the reflected irradiance for perpendicular polarized light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        reflected irradiance                  [-]
    """
    return abs(r_per(m, theta))**2


def T_par(m, theta):
    """
    Calculates the transmitted irradiance for parallel polarized light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        transmitted irradiance                [-]
    """
    return abs(t_par(m, theta))**2


def T_per(m, theta):
    """
    Calculates the transmitted irradiance for perpendicular polarized light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        transmitted irradiance                [-]
    """
    return abs(t_per(m, theta))**2


def R_unpolarized(m, theta):
    """
    Calculates the reflected irradiance for unpolarized incident light

    Args:
        m :     complex index of refraction   [-]
        theta : angle from normal to surface  [radians]
    Returns:
        reflected irradiance                  [-]
    """
    return (R_par(m, theta) + R_per(m, theta)) / 2
