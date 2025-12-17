# 💻 CHEM 284 - Algorithmic Scaling and Optimizations

## 🧪 Goal

The goal of this lab is to:

1. Familiarize yourself with **algorithms and ways to speed them up**.
2. Learn how to use **spatial decomposition to speed up calculations**. 
3. Practice using **cheminformatics code** and **visualize 3D structures**.
4. Profile the 2 versions of the code.

---
## 🗂️ Provided

- A `docker` file to set up the dev environment.
- Python script `main.py` to run the code.
- `data` folder contains all the structures.
- Jupyter notebook `visualize.ipynb` to create 3D visualizations for the complex and bins.
- A static HTML file with the receptor-ligand complex for you to view.

---
## 💻 Setup
```bash
./docker_build.sh # You may need to chmod +x
./docker_run.sh # You may need to chmod +x
```
To execute the code:
```
# From the main directory
python3 main.py
```

To run jupyter lab to run visualize.ipynb
```
# Make sure you are in the main directory
jupyter lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root
```

## ✅ Tasks
### Brute force with cut-off
Loop over all ligand atoms and then loop over all receptor atoms and add up their LJ potentials if they are within a cutoff distance of 5.0 Å. We use a cutoff here to make our results comparable with the binning approach, if we didn't do this, the total energies would be vastly different.

Euclidian distance calculation:

$$ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2} $$

However, you shouldn't need to write this out yourself because we are using numpy arrays so theres a built in function to do that for you!

### Binning with cut-off (spatial decomposition)
1) Divide the receptor up into bins of equal size and place receptor atoms inside of the bins. The easiest way to do this is by creating a hashmap where each key is the bin coordinate (x, y, z) and the value is a list of atom indices. You can use a `defaultdict(list)` for this. To create the key you can divide the atom coordinate by the bin_size.

```
# bin_size of 4.0 Å
[3.2, 7.5, 1.1] -> [0, 1, 0]
```

2) Once you have the bins, you will need a way to retrieve the neighbor bins for a ligand atom. You can create the key using the ligand atom coordinates and bin_size to determine what bin your ligand atom is in. Once you have that you will need to find all your neighbor bins in 3D space depending on the cutoff. For example, a bin_size of 1.0 Å and cutoff of 5.0 Å with have a bin_radius of 5. So our atom of interest in the most center bin and it will have 5 bins in each direction -x to x for all directions. This means there we will have to loop from -5 to 5 bins for each direction, x, y, z.

Hint: Think of a 3D [moore neighborhood](https://en.wikipedia.org/wiki/Moore_neighborhood) where the radius is determined by the bin_size and cutoff.

3) Once you have all the neighbor bins for a ligand atom, you can simply loop through all of their atoms indices to get each coordinate from receptor_coords and calculate the LJ potential!

My results show a ~ 9x speed up!
```
score_with_cutoff     energy= -2.125013  time=   0.15533s
scored_binned         energy= -2.125013  time=   0.01752s
```

### Extra time
1) You can view `visualize.ipynb` to see how the `receptor_ligand_complex.html` was generated and how the bins were visualized. There are many 3D mol visualizing tools available but this works in jupyter notebooks although it is limited in what it can show.

2) Think about how you could precompute the LJ potentials into a grid of points with LJ potentials? The idea would be that once your grid is created, you can associate a precomputed grid value for each ligand atom and just sum them up! 
    - How long do you think precomputing would take? 
    - How long do you think the actual calculation would take?
