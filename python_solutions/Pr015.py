from helper_functions import timer

@timer
def count_ways(grid_rows : int, grid_cols: int) -> int:
    """
    Compute available lattice paths in a grid.
    
    Notes
    -----
    More information about lattice paths can be found here
    <https://stemhash.com/counting-lattice-paths/>
    
    Parameters
    ----------
    grid_rows, grid_cols : `int`
		Grid size.
    
    Returns
    -------
    path_number : `int`
		Available lattice paths in corresponding grid.	
    """
    # Each cell represents the number of possible ways that
    # a grid edge can be accessed.
    rows = grid_rows + 1
    cols = grid_cols + 1
    grid = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Set grid border values equal to <1>.
    for i in range(rows):
        grid[i][0] = 1
    for j in range(cols):
        grid[0][j] = 1
    
    # With the use of Dynamic Programming, we compute each cell
    # available paths by adding the paths from previous 
    # (up and left) values.
    for i in range(1,rows):
        for j in range(1,cols):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
                    
    path_number = grid[grid_rows][grid_cols]
    return path_number
        
if (__name__ == "__main__"):
    N1,ANS1 = 2, 6
    N2,ANS2 = 20, 137846528820
    
    assert(count_ways(N1,N1) == ANS1)
    ans = count_ways(N2,N2)
    print(f"Problem 15 answer is {ans}")
    assert(ans == ANS2)
