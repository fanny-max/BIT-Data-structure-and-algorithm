# Initialize the stack (list) with the topics
ur_stack = ["TopicA", "TopicB", "TopicC"]

print("Original Stack (LIFO):", ur_stack)

# 1. Pop the top element
# The pop() method removes and returns the last element (the 'top' of the stack)
popped_topic = ur_stack.pop()

print(f"\nOperation: Pop 1 element (The element '{popped_topic}' was removed).")

# 2. Check the new top element
# The new top element is simply the last element remaining in the list
if ur_stack:
    # Use index -1 to access the last element without removing it
    new_top = ur_stack[-1]
else:
    new_top = "The stack is empty."

print("\nRemaining Stack:", ur_stack)
print("Which is top? The new top element is:", new_top)