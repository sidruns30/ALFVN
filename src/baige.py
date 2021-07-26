"""
ALFVN: Adaptive Lightweight Finite Volume Numerics
Siddhant Solanki
****************baige.py**********************
Contains classes for cell centered and face centered arrays
The constructor
"""

import numpy as np

class cell_centered():
    # class constructor: initialize the prim and cons variables
    def __init__(self, nx, ny, nz, ngh, xi, xf, yi, yf, zi, zf, **kwargs):
        
        # Coordinates (do not contain ghost zones)
        self.x = np.linspace(xi, xf, nx)
        self.y = np.linspace(yi, yf, ny)
        self.z = np.linspace(zi, zf, nz)
        
        # Primitives
        self.prim_rho = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        self.prim_velx = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        self.prim_vely = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        self.prim_velz = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        self.prim_press = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        
        # Conservatives
        self.cons_rho = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        self.cons_momx = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        self.cons_momy = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        self.cons_momz = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
        self.cons_en = np.zeros((nx + 2*ngh, ny + 2*ngh, nz + 2*ngh))
       
        # Gas variable(s)
        if 'gas_gamma' not in kwargs: self.gas_gamma = 5/3
        else: self.gas_gamma = kwargs['gas_gamma']

class face_centered():
    # class constructor: initialize prim and flux variables
    def __init__(self, nx, ny, nz, ngh, xi, xf, yi, yf, zi, zf, **kwargs):
        
        # Coordinates (do not contain ghost zones)
        self.x = np.linspace(xi + (xf - xi)/nx, xf - (xf - xi)/nx, nx - 1)
        self.y = np.linspace(yi + (yf - yi)/ny, yf - (yf - yi)/ny, ny - 1)
        self.z = np.linspace(zi + (zf - zi)/nz, zf - (zf - zi)/nz, nz - 1)
        
        # Primitives
        self.prim_rho = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1))
        self.prim_velx = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1))
        self.prim_vely = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1))
        self.prim_velz = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1))
        self.prim_press = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1))
        
        # Fluxes for conservatives
        self.flux_rho = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1, 3))
        self.flux_momx = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1, 3))
        self.flux_momy = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1, 3))
        self.flux_momz = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1, 3))
        self.flux_en = np.zeros((nx + 2*ngh - 1, ny + 2*ngh - 1, nz + 2*ngh - 1, 3))

        # Gas variable(s)
        if 'gas_gamma' not in kwargs: self.gas_gamma = 5/3
        else: self.gas_gamma = kwargs['gas_gamma']
