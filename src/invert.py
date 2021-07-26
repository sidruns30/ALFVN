"""
ALFVN: Adaptive Lightweight Finite Volume Numerics
*****************invert.py********************
Get primitives from conservatives and vice-versa
Prim to cons:
    rho_c = rho_p
    p1 = rho_p * v1
    ...
    E = rho_p / 2 * |v|**2 + P / (gamma - 1)

Cons to prim:
    rho_p = rho_c
    v1 = p1 / rho_c
    ...
    P = (gamma - 1) * (E - |p|**2 / 2 * rho_c)
"""

# Input takes in either a cell_centered or a face_centered array object
def prim_to_cons(cell_array_obj):

    # Density
    cell_array_obj.cons_rho = cell_array_obj.prim_rho

    # Momentum
    cell_array_obj.cons_momx = cell_array_obj.prim_rho * cell_array_obj.prim_velx
    cell_array_obj.cons_momy = cell_array_obj.prim_rho * cell_array_obj.prim_vely
    cell_array_obj.cons_momz = cell_array_obj.prim_rho * cell_array_obj.prim_velz

    # Energy
    cell_array_obj.cons_en = 0.5 * cell_array_obj.prim_rho * (cell_array_obj.prim_velx**2 + 
                             cell_array_obj.prim_vely**2 + cell_array_obj.prim_velz**2) +
                             cell_array_obj.prim_press / (cell_array_obj.gas_gamma - 1)

def cons_to_prim(cell_array_obj):
    
    # Density
    cell_array_obj.prim_rho = cell_array_obj.cons_rho

    # Momentum
    cell_array_obj.prim_velx = cell_array_obj.cons_momx / cell_array_obj.cons_rho
    cell_array_obj.prim_vely = cell_array_obj.cons_momy / cell_array_obj.cons_rho
    cell_array_obj.prim_velz = cell_array_obj.cons_momz / cell_array_obj.cons_rho

    # Energy
    cell_array_obj.prim_press = (cell_array_obj.cons_en - (0.5 * (cell_array_obj.cons_momx**2
                                + cell_array_obj.cons_momy**2 + cell_array_obj.cons_momz**2)
                                ) / cons_array_obj.cons_rho ) * (cons_array_obj.gas_gamma - 1)
