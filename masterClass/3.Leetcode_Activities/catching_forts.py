# Function to calculate the maximum number of forts that can be captured
def captureForts(forts):
    # Initialize the maximum number of forts that can be captured to 0
    max_capture = 0
    # Variable to store the index of the last seen fort
    i = 0

    # Iterate through all elements in the 'forts' list
    for j in range(len(forts)):
        # Check if the current position has a fort (non-zero value)
        if forts[j]:
            # If the current fort is the opposite type of the previous fort
            if forts[j] == -forts[i]:
                # Calculate the number of capturable forts between and update max_capture
                max_capture = max(max_capture, j - i - 1)
            # Update the last seen fort index to the current index
            i = j
        else:
            # Continue to the next iteration if the current position is empty (zero)
            continue

    # Return the maximum number of forts that can be captured
    return max_capture

# Define the list of forts (1 for one type, -1 for the opposite type, 0 for empty space)
forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]
# Print the result of the function with the given list of forts
print(captureForts(forts))
