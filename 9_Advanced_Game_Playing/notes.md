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

### Understanding Exponential Time

![Understanding the Exponential Timing for a tree with branching factor of 2](./understanding_exponential_timing.png)
*Exponential Timing for a tree with a branching factor of 2*

![Understanding the Exponential Timing for a tree with branching factor of 3](./exponential_timing_bf_3.png)
*Exponential Timing for a tree with a branching factor of 3*

Table for how the above values for the tree with branching factor 3 are obtained

  | Tree Nodes | Iterative Deepening Nodes     |
  | :------------- | :------------- |
  | 1       | 1 + 0 = 1             |
  | 4 (1 + 3)       | 4 + 1 = 5     |
  | 13 (1 + 3 + 9)  | 13 + 5 = 18   |
  | 40 (1 + 3 + 9 + 27)  | 40 + 18 = 58 |
  | 121 (1 + 3 + 9 + 27 + 81)  | 121 + 58 = 179 |

Let us try to extend the same to the trees that have a branching factor of `k` and a depth level of `n`.

Lets us to generalize first the case for a tree with a branching factor of 3
<center>
a<sub>0</sub> = 1
<br>
a<sub>1</sub> = 3a<sub>0</sub> + 1
<br>
a<sub>2</sub> = 3a<sub>1</sub> + 1
<br>
Therefore, a<sub>n</sub> = 3a<sub>n-1</sub> + 1
<br>
a<sub>n</sub> = 3a<sub>n-1</sub> + 1
<br>
a<sub>n</sub> = 3(3a<sub>n-2</sub> + 1) + 1
a<sub>n</sub> = 3(3(3a<sub>n-3</sub> + 1) + 1) + 1
<br>
.
<br>
.
<br>
.
<br>
.
<br>
<br>
a<sub>n</sub> = 3<sup>n-1</sup> + 3<sup>n-2</sup> + 3<sup>n-3</sup> + ..... + 9 + 3  + 1 + 1
<br>
<br>
The above summation series is a geometric series with `a` = 3 and `r` = 3
<br>
<br>
a<sub>n</sub> = 3<sup>n-1</sup> + 3<sup>n-2</sup> + 3<sup>n-3</sup> + ..... + 9 + 3  + 1 + 1
<br>
a<sub>n</sub> = 3(3<sup>n</sup> - 1)/2 + 1
<br>
a<sub>n</sub> = (3<sup>n+1</sup> - 1)/2

<br>
Similarly, we can extend the same derivation to determine the exponential timing for a tree with a branching factor of `k` and a depth-level of `n` as a<sub>n</sub> = (k<sup>n+1</sup> - 1)/(k - 1)
<br>
</center>

## Varying Branching Factor
