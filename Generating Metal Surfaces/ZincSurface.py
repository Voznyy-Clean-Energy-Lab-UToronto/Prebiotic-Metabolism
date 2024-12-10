import numpy as np

def generate_hcp_xyz(a, c, nx, ny, nz):
    """Generates an .xyz file for an hcp lattice.

    Args:
        a: Lattice parameter a.
        c: Lattice parameter c.
        nx, ny, nz: Number of unit cells in x, y, z directions.
    """

    # Calculate lattice vectors
    a1 = np.array([a, 0, 0])
    a2 = np.array([a/2, a*np.sqrt(3)/2, 0])
    a3 = np.array([0, 0, c])

    # Generate atomic positions
    positions = []
    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                base_vector = ix*a1 + iy*a2 + iz*a3
                positions.append(base_vector)
                positions.append(base_vector + a3/2 + a1/3 + a2/3)

    # Write .xyz file
    with open('zinc_hcp_10x10x1.xyz', 'w') as f:
        f.write(f"{len(positions)}\n")
        f.write("Zinc hcp 10x10x1 unit cells\n")
        for pos in positions:
            f.write(f"Zn {pos[0]} {pos[1]} {pos[2]}\n")

# Example usage:
a = 2.6649  # Å
c = 4.9468  # Å
nx, ny, nz = 10, 10, 1
generate_hcp_xyz(a, c, nx, ny, nz)