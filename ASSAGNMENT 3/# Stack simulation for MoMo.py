# The list of steps in the MoMo process, for demonstration
momo_steps = ['PIN', 'Amount', 'Confirm']

print("Original Steps:", momo_steps)

# We will "undo" (remove) two steps: 'Amount' and 'Confirm'
steps_to_undo = ['Amount', 'Confirm']

print(f"\nSteps to Undo (Remove): {steps_to_undo}")

# Iterate and remove the two specified steps
for step in steps_to_undo:
    try:
        momo_steps.remove(step)
    except ValueError:
        print(f"Warning: Step '{step}' not found.")

# The remaining step
remaining_steps = momo_steps

print("Remaining Steps:", remaining_steps)

# You can check the number remaining
print(f"\nNumber of remaining steps: {len(remaining_steps)}")