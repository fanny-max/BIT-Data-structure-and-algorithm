import array
# integer
temperatures = [4, 2, 5, 3, 6, 1, 5, 2]
total_temp = sum(temperatures)
avg_temp = total_temp / len(temperatures)
min_temp = min(temperatures)
max_temp = max(temperatures)
print(f"Temperatures: {temperatures}")
print(f"Total: {total_temp}")
print(f"Average: {avg_temp:.2f}")
print(f"Minimum: {min_temp}")
print(f"Maximum: {max_temp}\n")
# Strings
report_title = "Cold Chain Temperature Log Report"
report = f"""
{report_title}
Summary:
The total sum of all temperature readings is {total_temp} degrees.
The average temperature recorded is {avg_temp:.2f} degrees.
"""
print(report)
# Booleans
threshold = 3.5
is_valid_chain = (avg_temp <= threshold) and (max_temp <= 5)
if is_valid_chain:
    print("Below Standard: The cold chain is operating within the required temperature range.")
else:
    print("Above Standard: The cold chain has exceeded the standard temperature threshold.")
# Lists: Manipulate a list of temperature readings
temp_readings = [4.1, 2.5, 5.0, 3.2]
print(f"Original List: {temp_readings}")
# Add a new element
temp_readings.append(3.8)
# Remove an element
for temp in temp_readings:
    if temp > 4.5:
        temp_readings.remove(temp)
        break
# Sort and display
temp_readings.sort()
print(f"Modified and Sorted List: {temp_readings}\n")
# Arrays: Use Python's 'array' module for a fixed-size numeric subset
# Using 'f' for float data type
temp_array = array.array('f', [4.1, 2.5, 5.0, 3.2])
sum_array = sum(temp_array)
sum_list = sum([4.1, 2.5, 5.0, 3.2])
print(f"Array: {temp_array}")
print(f"Sum of Array: {sum_array:.2f}")
print(f"Sum of List: {sum_list:.2f}")
print(f"Are the sums equal? {sum_array == sum_list}\n")
# Dictionaries
log_records = [
    {'id': 101, 'name': 'Sensor A', 'value': 2.5},
    {'id': 102, 'name': 'Sensor B', 'value': 4.1},
    {'id': 103, 'name': 'Sensor C', 'value': 3.7}
]
print(f"Original Records: {log_records}")
# Update one record
for record in log_records:
    if record['id'] == 102:
        record['value'] = 3.9
        break
# Delete another record
log_records = [record for record in log_records if record['id'] != 101]
# Compute the total
total_value = sum(record['value'] for record in log_records)
print(f"Modified Records: {log_records}")
print(f"Total value of 'value' field: {total_value:.2f}")
