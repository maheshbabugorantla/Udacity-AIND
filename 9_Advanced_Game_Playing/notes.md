# ***Advanced Game Playing***
> The Below notes is made through my reading from [this](https://www.cs.ubc.ca/~hutter/teaching/cpsc322/2-Search6-final.pdf)

## ***Iterating Deepening***

### Iterative Deepening DFS: Motivation

Want low space complexity but completeness and optimality

Key Idea: re-compute elements of the frontier rather than saving them

|      | Complete     | Optimal     | Time     | Space     |
| :------------- | :------------- | :------------- | :------------- | :------------- |
| ***DFS***       | N (Y if no cycles)       | N       | O(b<sup>m</sup>)       | O(mb)       |
| ***BFS***       | Y       | Y       | O(b<sup>m</sup>)       | O(b<sup>m</sup>)       |
| ***LCFS*** (when arc costs available)       | Y (Costs > 0)       | Y (Costs > 0)       | O(b<sup>m</sup>)       | O(b<sup>m</sup>)       |
| ***Best First*** (When h available)     | N       | N       | O(b<sup>m</sup>)       | O(b<sup>m</sup>)       |
| ***A<sup>*</sup>*** (when arc costs and 'h' available)       | Y (Costs > 0, h admissible)       | Y (Costs >= 0, h admissible)       | O(b<sup>m</sup>)       | O(b<sup>m</sup>)       |

### Iterative Deepening DFS (IDS) in a Nutshell
- Use DFS to look for solutions at depth 1, then 2, then 3, etc
  - For depth D, ignore any paths with longer length
  - Depth-bounded depth-first search


  ![Iterative Deepening Visualisation](./iterative_deepening.png)

#### (Time) Complexity of IDS
- That sounds wasteful!
- Let's analyze the time complexity
- For a solution at depth `m` with branching factor `b`

|  Depth    | Total # of paths at that level     | # times created by BFS (or DFS)    | # times created by IDS     | Total # paths for IDS     |
| :-------------  | :-------------  | :------------- | :------------- | :------------- |
| ***1***         | b       | 1       | m       | mb       |
| ***2***       | b<sup>2</sup>       | 1      | m-1       | (m-1)b<sup>2</sup>       |
| ***.***       | .       | .       | .       | .       |
| ***.***       | .       | .       | .       | .       |
| ***.***       | .       | .       | .       | .       |
| ***m - 1***   | b<sup>m-1</sup>   | 1       | 2       | 2b<sup>m-1</sup> |
| ***m*** | b<sup>m</sup> | 1       | 1       | b<sup>m</sup> |


|      | Complete     | Optimal     | Time     | Space     |
| :------------- | :------------- | :------------- | :------------- | :------------- |
| ***DFS***       | N (Y if no cycles)       | N       | O(b<sup>m</sup>)       | O(mb)       |
| ***BFS***       | Y       | Y       | O(b<sup>m</sup>)       | O(b<sup>m</sup>)       |
| ***IDS***       | Y       | Y       | O(b<sup>m</sup>)       | O(mb)       |
| ***LCFS*** (when arc costs available)       | Y (Costs > 0)       | Y (Costs > 0)       | O(b<sup>m</sup>)       | O(b<sup>m</sup>)       |
| ***Best First*** (When h available)       | N       | N       | O(b<sup>m</sup>)       | O(b<sup>m</sup>)       |
| ***A<sup>*</sup>*** (when arc costs and 'h' available)       | Y (Costs > 0, h admissible)       | Y (Costs >= 0, h admissible)       | O(b<sup>m</sup>)       | O(b<sup>m</sup>)       |
