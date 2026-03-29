import time

def show_solution(goal):

    if goal is None:
        print("No solution found.")
        return
    
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = current.parent

    path.reverse()

    num_disks = len(path[0].pegs)
    print(f"Solution found! ({len(path) - 1} moves for {num_disks} disks)\n")   
    print("=" * 40)

    for step, state in enumerate(path):
        peg_a = []
        peg_b = []
        peg_c = []

        for disk, peg in enumerate(state.pegs):
            disk_label = disk + 1
            if peg == 'A':
                peg_a.append(disk_label)
            elif peg == 'B':
                peg_b.append(disk_label)
            elif peg == 'C':
                peg_c.append(disk_label)

            if step == 0:
                print(f"Initial state:")

            else:
                mv = state.move
                disk_num = mv[0] + 1
                print(f"  Step {step}: Move disk {disk_num}  {mv[1]} -> {mv[2]}")

        print(f"    Peg A: {peg_a}")
        print(f"    Peg B: {peg_b}")
        print(f"    Peg C: {peg_c}")
        print("-" * 40)

        time.sleep(0.3)

    print(f"\nDone — total moves: {len(path) - 1}")        