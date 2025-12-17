from rdkit import Chem
import numpy as np


def print_score(name, time, energy=None):
    if energy is not None:
        print(f"{name:20s}  energy={energy:10.6f}  time={time:10.5f}s")
    else:
        print(f"{name:20s}                     time={time:10.5f}s")


def get_coords(mol):
    conf = mol.GetConformer()
    return np.array([list(conf.GetAtomPosition(i)) for i in range(mol.GetNumAtoms())])


def load_data(ligand_fname="data/estradiol.pdb",
              receptor_fname="data/1a52_cleaned.pdb"):
    ligand = Chem.MolFromPDBFile(ligand_fname, removeHs=False)
    receptor = Chem.MolFromPDBFile(receptor_fname, removeHs=False)

    ligand_coords = get_coords(ligand)
    receptor_coords = get_coords(receptor)

    return ligand_coords, receptor_coords
