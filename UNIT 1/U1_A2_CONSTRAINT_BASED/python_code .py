# ==========================================
# AI ASSESSMENT
# Q1: Backtracking Search
# Q2: BFS Robot Path Search
# Q3: Uniform Cost Search
# ==========================================

print("=" * 50)
print("QUESTION 1: BACKTRACKING SEARCH")
print("=" * 50)

doctors = ["D1", "D2", "D3"]
shifts = ["Morning", "Afternoon", "Night"]

def valid(assign):
    if "D1" in assign and assign["D1"] == "Night":
        return False

    if "D3" in assign and assign["D3"] == "Morning":
        return False

    if len(assign.values()) != len(set(assign.values())):
        return False

    if "D2" in assign and "D3" in assign:
        order = {"Morning": 1, "Afternoon": 2, "Night": 3}
        if order[assign["D2"]] >= order[assign["D3"]]:
            return False

    return True

def backtrack(assign, index):
    if index == len(doctors):
        return assign

    doctor = doctors[index]

    for shift in shifts:
        assign[doctor] = shift

        if valid(assign):
            result = backtrack(assign, index + 1)
            if result:
                return result

        del assign[doctor]

    return None

solution = backtrack({}, 0)

print("\nFinal Shift Assignment")
for doctor, shift in solution.items():
    print(doctor, "->", shift)


# ==========================================
print("\n" + "=" * 50)
print("QUESTION 2: BFS ROBOT PATH SEARCH")
print("=" * 50)

from collections import deque

grid = [
['S',0,0,'X',0],
[0,'X',0,'X',0],
[0,0,0,0,0],
['X','X',0,'X',0],
[0,0,0,0,'G']
]

start = (0,0)
goal = (4,4)

rows = len(grid)
cols = len(grid[0])

queue = deque([(start,[start])])
visited = {start}

moves = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    (x,y), path = queue.popleft()

    if (x,y) == goal:
        print("\nShortest Path:")
        print(path)
        print("Total Cost:", len(path)-1)
        break

    for dx,dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] != 'X' and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append(((nx,ny), path + [(nx,ny)]))


# ==========================================
print("\n" + "=" * 50)
print("QUESTION 3: UNIFORM COST SEARCH")
print("=" * 50)

import heapq

graph = {
    'S':[('A',1),('B',3)],
    'A':[('C',2)],
    'B':[('D',2)],
    'C':[('G',3)],
    'D':[('G',1)],
    'G':[]
}

priority_queue = [(0,'S',[])]
visited = set()

while priority_queue:

    cost,node,path = heapq.heappop(priority_queue)

    if node in visited:
        continue

    visited.add(node)
    path = path + [node]

    if node == 'G':
        print("\nOptimal Path:")
        print(" -> ".join(path))
        print("Minimum Cost:", cost)
        break

    for neighbour,weight in graph[node]:
        heapq.heappush(priority_queue,(cost+weight,neighbour,path))

print("\n========== PROGRAM COMPLETED ==========")
