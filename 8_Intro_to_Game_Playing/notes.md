# ***Introduction to Game Playing AI***

## ***Goal***
The goal of this lesson is to design an AI that is smarter than us in playing a real game

## ***Main Topics***
> The Notes below is taken during my readings from AIMA Book 3rd Edition
and [University of Washington AI CS573 Class Notes](https://courses.cs.washington.edu/courses/csep573/)

- [x] Adversarial Search
  - In Multi Agent environments, each agent needs to consider the actions of other agents and how they affect it own welfare. The unpredictability nature of these other agents can introduce contingencies into agent's problem-solving process.
  - Here we will talk more about competitive environments, in which the agents goals are in conflict, giving rise to [`Adversarial Search`](../Notes/UW_AI_CS573/lectures/05-games.pdf) problems

  ### Games as Adversarial Search
  - `States`:
    - Board Configurations
  - `Initial State`:
    - The board position and which player will move
  - `Successor Function`:
    - Returns a list of (move, state) pairs, each indicating a legal move and the resulting state
  - `Terminal Test`:
    - Determines when the game is over
  - `Utility Function`:
    - Gives a numerical value in terminal states (child nodes) (e.g., -1, 0, +1 for loss, tie, win)

    ```
      In a normal search problem, the optimal solution would be a sequence of actions leading to a goal
      state-a terminal state that is a win. In Adversarial Search, MIN has something to say about it. MAX
      therefore must find a contingent strategy, which specifies MAX's move in the initial state, then
      MAX's moves in the states resulting from every possible response by MIN, then MAX's moves in the
      states resulting from every possible response by MIN to those moves, and so on. This is exactly
      analogous to the AND-OR search algorithm with MAX Playing the role of OR and MIN equivalent to AND.
      Roughly speaking, an optimal strategy leads to outcomes at least as good as any other strategy when
      one is playing an infallible opponent.
    ```

- [x] Minimax Algorithm

  ### Mini-Max Terminology
  - `move` : a move by both players
  - `ply` : a half-move
  - `utility function` : The Function applied to leaf nodes
  - `backed-up value`
    - of a max-position: The value of it largest Successor
    - of a min-position: The value of it smallest successor
  - `Minimax procedure` : Search down several level; at the bottom level apply the utility function, back-up values all the way up to the root node, and that node selects the move

  ```
  Given a game tree, the optimal strategy can be determined from the minimax value
of each node, which we write as MINIMAX(n). The minimax value of a node is the utility
(for MAX) of being in the corresponding state, assuming that both players play optimally
from there to the end of the game. Obviously, the minimax value of a terminal state is just
its utility. Furthermore, given a choice, MAX prefers to move to a state of maximum value,
whereas MIN prefers a state of minimum value. For more Info (Check AIMA 3rd Edition Page 164)
  ```

  #### Minimax Strategy
  - Why do we take the min value every other level of the tree?
  - These nodes represent the opponent's choice of move
  - The computer assumes that the human will choose that move that is of least value to the computer

    For pseudo-code of Minimax Algorithm check Page 22 of [this](https://github.com/maheshbabugorantla/Udacity-AIND/blob/unstable/Notes/UW_AI_CS573/lectures/05-games.pdf) document


- [ ] Alpha-Beta Pruning
- [ ] Evaluation Functions
- [ ] Isolation Game Player
- [ ] Multi-Player, Probabilistic Games
