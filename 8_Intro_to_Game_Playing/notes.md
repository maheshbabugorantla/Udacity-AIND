# ***Introduction to Game Playing AI***

## ***Goal***
The goal of this lesson is to design an AI that is smarter than us in playing a real game

## ***Main Topics***
> The Notes below is taken during my readings from AIMA Book 3rd Edition

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

- [x] Minimax Algorithm

  ### Mini-Max Terminology
  

- [ ] Alpha-Beta Pruning
- [ ] Evaluation Functions
- [ ] Isolation Game Player
- [ ] Multi-Player, Probabilistic Games
