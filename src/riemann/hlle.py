"""
ALFVN: Adaptive Lightweight Finite Volume Numerics
*****************hlle.py********************
Solve the Riemann problem using the HLLE solver
Takes the primitives at the face centers and solves
for conservatives
"""

from src.baige import face_centered as FC
import numpy as np

def hlle(FC):
    
    # Setting a fake velocity for now to compute fluxes
    vel = np.ones(3)

    # Set rho flux
    FC.flux_rho[:,:,:,0] = FC.prim_rho * vel[0]
    FC.flux_rho[:,:,:,1] = FC.prim_rho * vel[1]
    FC.flux_rho[:,:,:,2] = FC.prim_rho * vel[2]
    
    # Set mom x flux
    FC.flux_momx[:,:,:,0] = FC.prim_rho * FC.prim_velx * vel[0]
    FC.flux_momx[:,:,:,1] = FC.prim_rho * FC.prim_velx * vel[1]
    FC.flux_momx[:,:,:,2] = FC.prim_rho * FC.prim_velx * vel[2]
    
    # Set mom y flux
    FC.flux_momy[:,:,:,0] = FC.prim_rho * FC.prim_vely * vel[0]
    FC.flux_momy[:,:,:,1] = FC.prim_rho * FC.prim_vely * vel[1]
    FC.flux_momy[:,:,:,2] = FC.prim_rho * FC.prim_vely * vel[2]
    
    # Set mom z flux
    FC.flux_momz[:,:,:,0] = FC.prim_rho * FC.prim_velz * vel[0]
    FC.flux_momz[:,:,:,1] = FC.prim_rho * FC.prim_velz * vel[1]
    FC.flux_momz[:,:,:,2] = FC.prim_rho * FC.prim_velz * vel[2]

    # Set energy flux
    FC.flux_en[:,:,:,0] = (FC.press / (FC.gas_gamma - 1) + (np.square(FC.prim_velx)
                            + np.square(FC.prim_vely) + np.square(FC.prim_velz)) *
                            FC.rho / 2) * vel[0]
    FC.flux_en[:,:,:,1] = (FC.press / (FC.gas_gamma - 1) + (np.square(FC.prim_velx)
                            + np.square(FC.prim_vely) + np.square(FC.prim_velz)) *
                            FC.rho / 2) * vel[1]
    FC.flux_en[:,:,:,2] = (FC.press / (FC.gas_gamma - 1) + (np.square(FC.prim_velx)
                            + np.square(FC.prim_vely) + np.square(FC.prim_velz)) *
                            FC.rho / 2) * vel[2]
