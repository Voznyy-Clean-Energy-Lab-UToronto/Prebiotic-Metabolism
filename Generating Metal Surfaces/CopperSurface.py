import numpy as np

def generate_fcc_xyz(a, nx, ny, nz):
    """Generates an .xyz file for an fcc lattice.

    Args:
        a: Lattice parameter a.
        nx, ny, nz: Number of unit cells in x, y, z directions.
    """

    # Calculate lattice vectors
    a1 = np.array([a, 0, 0])
    a2 = np.array([0, a, 0])
    a3 = np.array([0, 0, a])

    # Generate atomic positions
    positions = []
    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                base_vector = ix*a1 + iy*a2 + iz*a3
                positions.append(base_vector)
                positions.append(base_vector + a1/2 + a2/2)
                positions.append(base_vector + a2/2 + a3/2)
                positions.append(base_vector + a1/2 + a3/2)

    # Write .xyz file
    with open('copper_fcc_10x10x1.xyz', 'w') as f:
        f.write(f"{len(positions)}\n")
        f.write("Copper fcc 10x10x10 unit cells\n")
        for pos in positions:
            f.write(f"Cu {pos[0]} {pos[1]} {pos[2]}\n")

# Example usage:
a = 3.6149  # Å
nx, ny, nz = 10, 10, 1
generate_fcc_xyz(a, nx, ny, nz)