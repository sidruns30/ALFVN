"""
ALFVN: Adaptive Lightweight Finite Volume Numerics
*****************plm.py********************
Get the primitives at the cell faces from the cell
centers

Note that we not changing the edge cells in the FC array
"""

from src.baige import cell_centered as CC, face_centered as FC

def plm(CC, FC):

    # Taking the average at the cell centers from the cell edges
    
    # Set rho face
    FC.prim_rho[1:-1,1:-1,1:-1] = (CC.prim_rho[1:,1:,1:] + CC.prim_rho[:-1,:-1,:-1])/2

    # Set vel face
    FC.prim_velx[1:-1,1:-1,1:-1] = (CC.prim_velx[1:,1:,1:] + CC.prim_velx[:-1,:-1,:-1])/2
    FC.prim_vely[1:-1,1:-1,1:-1] = (CC.prim_vely[1:,1:,1:] + CC.prim_vely[:-1,:-1,:-1])/2
    FC.prim_velz[1:-1,1:-1,1:-1] = (CC.prim_velz[1:,1:,1:] + CC.prim_velz[:-1,:-1,:-1])/2

    # Set press face
    FC.prim_rho[1:-1,1:-1,1:-1] = (CC.prim_press[1:,1:,1:] + CC.prim_press[:-1,:-1,:-1])/2
