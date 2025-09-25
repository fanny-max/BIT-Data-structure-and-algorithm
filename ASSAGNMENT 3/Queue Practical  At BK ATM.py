from collections import deque

# 1. Initialize the queue with 8 clients
# The clients are labeled by their initial position in the queue
initial_clients = [f"Client {i}" for i in range(1, 9)]
bk_queue = deque(initial_clients)

print("Initial BK ATM Queue (Front to Back):", list(bk_queue))
print(f"Total clients: {len(bk_queue)}")

# 2. Simulate serving the first three clients
num_to_serve = 3
served_clients = []

print(f"\nOperation: Serving the first {num_to_serve} clients...")

# Loop 3 times to serve the first three clients
for i in range(num_to_serve):
    # popleft() removes the client from the front (left side) and returns them
    if bk_queue:
        served_client = bk_queue.popleft()
        served_clients.append(served_client)

# The third served client is the last one added to the served_clients list
if len(served_clients) >= 3:
    third_served = served_clients[2] # Index 2 is the third element
else:
    third_served = "Not enough clients were served to identify the third."

print(f"Clients served in order: {served_clients}")
print(f"Remaining Queue: {list(bk_queue)}")

# 3. Output the result
print("\nWho is third served? The client third served is:", third_served)