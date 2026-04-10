# Tower of Hanoi using AI Search Algorithms

This project implements multiple Artificial Intelligence search algorithms to solve the Tower of Hanoi problem. The aim is to compare uninformed and informed search strategies on different problem sizes and evaluate their performance.

The implementation supports running individual algorithms as well as comparing all algorithms on predefined test cases.

---

## Problem Description

The Tower of Hanoi consists of three pegs and a number of disks of different sizes. Initially, all disks are stacked on one peg in decreasing order. The goal is to move all disks to another peg while following these rules:

* Only one disk can be moved at a time
* A larger disk cannot be placed on a smaller disk
* Only the top disk from a peg can be moved

This problem is commonly used to study search algorithms and heuristic efficiency.

---

## Implemented Algorithms

The project includes the following algorithms:

* BFS (Breadth First Search)
* IDDFS (Iterative Deepening DFS)
* Greedy Best First Search
* A* Search
* IDA* Search

---

## Heuristics

Two heuristics are provided:

* h1 — simple misplaced disk heuristic
* h2 — improved disk position heuristic

Heuristics are used by Greedy, A*, and IDA*.

---

## Command Format

All algorithms can be executed using:

python main.py <algorithm> <heuristic> <difficulty>

### Arguments

**algorithm**
Search algorithm to run:

bfs
iddfs
greedy
astar
idastar

**heuristic**
Heuristic function (used only for informed search):

h1
h2

For BFS and IDDFS, heuristic value is ignored but still passed for consistency.

---

## Example Runs

Run BFS on easy case:

python main.py bfs h1 3

Run Greedy search:

python main.py greedy h1 3

Run A* on medium case:

python main.py astar h2 4

Run IDDFS:

python main.py iddfs h1 4

Run IDA* on hard case:

python main.py idastar h2 5

---

## Compare All Algorithms

To compare all algorithms:

python compare_algorithms.py

This will display:

* solution depth
* nodes explored
* execution time
* performance comparison

---

## Project Structure

.
├── main.py
├── compare_algorithms.py
├── cases.py
│
├── algorithms/
│   ├── bfs.py
│   ├── iddfs.py
│   ├── greedy.py
│   ├── astar.py
│   └── idastar.py
│
├── heuristics/
│   ├── h1.py
│   └── h2.py
│
├── core/
│   ├── state.py
│   └── moves.py
│
└── visualization/
    └── visualizer.py

---

## Output

Each run prints:

* algorithm used
* number of moves
* nodes expanded
* execution time
* solution path

---

## Complexity Overview

| Algorithm | Time   | Space  |
| --------- | ------ | ------ |
| BFS       | O(b^d) | O(b^d) |
| IDDFS     | O(b^d) | O(bd)  |
| Greedy    | O(b^m) | O(b^m) |
| A*        | O(b^d) | O(b^d) |
| IDA*      | O(b^d) | O(bd)  |

Where
b = branching factor
d = solution depth
m = maximum depth

---

## Suggested Demo Order

For demonstration:

1. python main.py bfs h1 3
2. python main.py greedy h1 3
3. python main.py astar h2 4
4. python main.py iddfs h1 4
5. python main.py idastar h2 5
6. python compare_algorithms.py

