from collections import deque

def sensor_buffer_simulation(max_size, new_samples):
    """
    Simulates a fixed-size FIFO buffer for an edge device using a deque.
    
    Args:
        max_size (int): The maximum number of elements the buffer can hold.
        new_samples (list): A list of new data points (e.g., sensor readings) 
                            to add to the buffer.
                            
    Returns:
        deque: The final state of the buffer.
    """
    # Initialize the buffer with a maximum size
    sensor_buffer = deque(maxlen=max_size)
    print(f"--- Initializing Buffer (Max Size: {max_size}) ---")
    print(f"Current Buffer: {list(sensor_buffer)}")
    
    for sample in new_samples:
        print(f"\nIncoming Sample: {sample}")
        
        # When maxlen is set, appending automatically pushes the oldest item off 
        # the opposite end (FIFO behavior).
        sensor_buffer.append(sample)
        
        # This check is just for demonstration purposes, to show when an item is dropped.
        if len(sensor_buffer) == max_size:
             # Since it's FIFO (First-In, First-Out), the first item added 
             # (the oldest) is the first one dropped when the size limit is hit.
             print("Buffer is full. The oldest item was automatically dropped.")
             
        print(f"Updated Buffer: {list(sensor_buffer)}")
        
    return sensor_buffer

# --- Simulation Parameters ---

BUFFER_MAX_SIZE = 5
INCOMING_DATA = [101, 102, 103, 104, 105, 106, 107] # 7 total samples

# Run the simulation
final_buffer = sensor_buffer_simulation(BUFFER_MAX_SIZE, INCOMING_DATA)

print("\n----------------------------------------------------")
print(f"**Final Buffer Contents (The latest {BUFFER_MAX_SIZE} samples):**")
print(list(final_buffer))