from collections import deque
import heapq

# ----------------------------
# 1. Water Jug Problem
# ----------------------------
def water_jug():
    print("\n--- Water Jug Problem ---")
    steps = [
        "Fill 3-gallon jug",
        "Pour into 4-gallon jug",
        "Fill 3-gallon jug again",
        "Pour into 4-gallon jug until full",
        "Empty 4-gallon jug",
        "Pour remaining 2 gallons into 4-gallon jug"
    ]

    states = [
        (0,3),
        (3,0),
        (3,3),
        (4,2),
        (0,2),
        (2,0)
    ]

    for i in range(len(steps)):
        print(f"Step {i+1}: {steps[i]} -> State {states[i]}")

    print("\nGoal Achieved: 2 gallons in 4-gallon jug")


# ----------------------------
# 2. Mars Rover
# ----------------------------
def mars_rover():
    print("\n--- Mars Rover Intelligent Agent ---")

    print("\nPercepts:")
    print("- Camera Images")
    print("- Rock Samples")
    print("- Temperature")
    print("- Obstacles")
    print("- Battery Level")

    print("\nActions:")
    print("- Move")
    print("- Collect Samples")
    print("- Capture Images")
    print("- Send Data")
    print("- Avoid Obstacles")

    print("\nEnvironment:")
    print("- Partially Observable")
    print("- Dynamic")
    print("- Sequential")

    print("\nAgent Type: Utility-Based Agent")


# ----------------------------
# 3. 8 Queens
# ----------------------------
N = 8

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve(board, col + 1):
                return True

            board[i][col] = 0

    return False


def queens():
    print("\n--- 8 Queens Problem ---")

    board = [[0] * N for _ in range(N)]

    if solve(board, 0):
        for row in board:
            print(row)
    else:
        print("No Solution")


# ----------------------------
# 4. OLA Cab Booking
# ----------------------------
def ola():
    print("\n--- OLA Cab Booking ---")

    pickup = input("Enter Pickup Location: ")
    destination = input("Enter Destination: ")

    print("\nAvailable Cabs")
    print("1. Mini")
    print("2. Micro")
    print("3. Sedan")
    print("4. Shared")
    print("5. Prime")

    choice = int(input("Choose Cab: "))

    cab = {
        1: "Mini",
        2: "Micro",
        3: "Sedan",
        4: "Shared",
        5: "Prime"
    }

    print("\nBooking Confirmed")
    print("Pickup:", pickup)
    print("Destination:", destination)
    print("Cab:", cab.get(choice, "Mini"))


# ----------------------------
# 5. Uniform Cost Search
# ----------------------------
graph = {
    'S': [('A',1),('G',12)],
    'A': [('B',3),('C',1)],
    'B': [('D',3)],
    'C': [('D',1),('G',2)],
    'D': [('G',3)],
    'G': []
}


def ucs(start, goal):
    queue = [(0,start,[start])]
    visited = set()

    while queue:
        cost,node,path = heapq.heappop(queue)

        if node == goal:
            return cost,path

        if node not in visited:
            visited.add(node)

            for neighbour,weight in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(queue,(cost+weight,neighbour,path+[neighbour]))

    return None


def uniform_cost():
    print("\n--- Uniform Cost Search ---")

    cost,path = ucs('S','G')

    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)


# ----------------------------
# Main Menu
# ----------------------------
while True:

    print("\n========== AI PROGRAM ==========")
    print("1. Water Jug Problem")
    print("2. Mars Rover")
    print("3. 8 Queens Problem")
    print("4. OLA Cab Booking")
    print("5. Uniform Cost Search")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        water_jug()

    elif choice == '2':
        mars_rover()

    elif choice == '3':
        queens()

    elif choice == '4':
        ola()

    elif choice == '5':
        uniform_cost()

    elif choice == '6':
        print("Thank You")
        break

    else:
        print("Invalid Choice")
