import numpy as np
import time
from collections import defaultdict
from utils import load_data, print_score

TRUE_ENERGY = -2.125013


def lj_potential(r, eps=0.2, sigma=2.0):
    """Lennard-Jones-like potential."""
    sr6 = (sigma / r)**6
    sr12 = sr6 * sr6
    return 4 * eps * (sr12 - sr6)


# Stage 1: Brute force with cutoff
def score_with_cutoff(ligand_coords: np.array,
                      receptor_coords: np.array,
                      cutoff=5.0):
    energy = 0.0

    # YOUR CODE HERE

    return energy


# Stage 2: Spatial Binning
def make_bins(atoms: np.array, bin_size=1.0):
    bins = defaultdict(list)

    # YOUR CODE HERE

    return bins


def get_neighbor_bins(key: tuple[int], radius_bins=1):
    neighbors = []

    # YOUR CODE HERE

    return neighbors


def score_binned(ligand_coords: np.array, 
                 receptor_coords: np.array, 
                 bin_size=1.0, cutoff=5.0):
    receptor_bins = make_bins(receptor_coords, bin_size)
    energy = 0.0
    radius_bins = int(np.ceil(cutoff / bin_size))

    # YOUR CODE HERE

    return energy


def main():
    # Load data
    ligand_coords, receptor_coords = load_data()

    # Stage 1
    start = time.time()
    e = score_with_cutoff(ligand_coords, receptor_coords)
    print_score("score_with_cutoff", time.time()-start, e)
    assert abs(e - TRUE_ENERGY) < 1e-6

    # Stage 2
    start = time.time()
    e = score_binned(ligand_coords, receptor_coords)
    print_score("scored_binned", time.time()-start, e)
    assert abs(e - TRUE_ENERGY) < 1e-6


if __name__ == "__main__":
    main()
