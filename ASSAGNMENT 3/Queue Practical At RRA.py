from collections import deque

# 1. Initialize the queue with 9 citizens
# Using a deque for efficient front-of-line removal
initial_citizens = [f"Citizen{i}" for i in range(1, 10)]
rra_queue = deque(initial_citizens)

print("Initial RRA Queue (Front to Back):", list(rra_queue))
print(f"Total citizens: {len(rra_queue)}")

# 2. Serve 4 citizens
num_served = 4
served_citizens = []

print(f"\nOperation: Serving {num_served} citizens (Pop from the left/front)...")

for _ in range(num_served):
    # popleft() removes the citizen from the front (left side)
    if rra_queue:
        served_citizens.append(rra_queue.popleft())

print(f"Citizens Served: {served_citizens}")

# 3. Determine who is at the front
if rra_queue:
    # The new front is the first element remaining (index 0)
    front_citizen = rra_queue[0]
else:
    front_citizen = "The queue is empty."

print("\nRemaining Queue (Front to Back):", list(rra_queue))
print("Who is front? The citizen at the front is:", front_citizen)