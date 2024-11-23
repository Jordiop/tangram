// Tangram adaptation of the Python program made for iedib

package main

import (
	"fmt"
)

var grid [][]int = [][]int{
	{1, 1, 1, 1, 1, 1},
	{1, 1, 1, 1, 1, 1},
	{1, 1, 1, 1, 1, 1},
	{1, 1, 1, 1, 1, 1},
	{1, 1, 1, 1, 1, 1},
	{1, 1, 1, 1, 1, 1},
}

func fitSquares(grid [][]int) [][][]int {
	rows := len(grid)
	cols := len(grid[0])
	squareList := [][][]int{}
	for r := 0; r < rows-1; r++ {
		for c := 0; c < cols-1; c++ {
			if grid[r][c] != 0 && grid[r+1][c] != 0 && grid[r][c+1] != 0 && grid[r+1][c+1] != 0 {
				h := make([][]int, rows)
				for i := range h {
					h[i] = make([]int, cols)
				}
				h[r][c] = 1
				h[r+1][c] = 1
				h[r][c+1] = 1
				h[r+1][c+1] = 1
				squareList = append(squareList, h)
			}
		}
	}
	return squareList
}

func main() {
	fmt.Println("Hello, World!")
	squares := fitSquares(grid)
	fmt.Println(squares)
}

// The Python code is the original code that needs to be adapted to GO.
// The code is a function that receives a grid and returns a list of squares that fit in the grid.
// The grid is a 2D array of integers, and the squares are 2x2 squares that are made of 1s.
// The function iterates over the grid and checks if the 2x2 square can be made with the 1s in the grid.
// If it can, it creates a new 2D array with the square and appends it to the list of squares.
