import numpy as np
import itertools
from concurrent.futures import ThreadPoolExecutor

def fit_squares(grid):
    rows, cols = grid.shape
    square_list = []
    for r in range(rows - 1):
        for c in range(cols - 1):
            if (
                grid[r, c] != 0
                and grid[r + 1, c] != 0
                and grid[r, c + 1] != 0
                and grid[r + 1, c + 1] != 0
            ):
                h = np.zeros(grid.shape)
                h[r, c] = 1
                h[r + 1, c] = 1
                h[r, c + 1] = 1
                h[r + 1, c + 1] = 1
                square_list.append(h)
    return square_list

def fit_vertical_bars(grid):
    rows, cols = grid.shape
    v_bar_list = []
    for r in range(rows - 2):
        for c in range(cols):
            if grid[r, c] != 0 and grid[r + 1, c] != 0 and grid[r + 2, c] != 0:
                h = np.zeros(grid.shape)
                h[r, c] = 1
                h[r + 1, c] = 1
                h[r + 2, c] = 1
                v_bar_list.append(h)
    return v_bar_list

def fit_horizontal_bars(grid):
    rows, cols = grid.shape
    h_bar_list = []
    for r in range(rows):
        for c in range(cols - 2):
            if grid[r, c] != 0 and grid[r, c + 1] != 0 and grid[r, c + 2] != 0:
                h = np.zeros(grid.shape)
                h[r, c] = 1
                h[r, c + 1] = 1
                h[r, c + 2] = 1
                h_bar_list.append(h)
    return h_bar_list

def check_combination(selector_de_peces, peces, shadow):
    suma_de_peces = np.sum(peces[np.array(selector_de_peces, dtype=bool)], axis=0)
    if np.array_equal(suma_de_peces, shadow):
        return selector_de_peces
    return None

def solve_tangram(shadow):
    sq = fit_squares(shadow)
    vb = fit_vertical_bars(shadow)
    hb = fit_horizontal_bars(shadow)
    block_list = sq + vb + hb

    peces = np.array(block_list)
    N = peces.shape[0]

    n_solutions = 0
    solutions = []

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(check_combination, selector_de_peces, peces, shadow)
            for selector_de_peces in itertools.product([0, 1], repeat=N)
        ]
        for future in futures:
            result = future.result()
            if result is not None:
                n_solutions += 1
                solutions.append(result)

    for i, solution in enumerate(solutions, 1):
        print(f"----- Solution {i} -----")
        print(f"Selector: {solution}")
        suma_de_peces = np.sum(peces[np.array(solution, dtype=bool)], axis=0)
        print(f"Solved grid:\n{suma_de_peces}")

    print(f"Total solutions: {n_solutions}")
    if not n_solutions:
        print("This grid has no possible solutions")

grid6x6 = np.array(
    [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]
)

print("GRID 1")
solve_tangram(grid6x6)
