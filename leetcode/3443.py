class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # (x, y) represents the current position, starting at (0,0)
        x, y = 0, 0  
        
        # Stores the maximum distance from the origin
        maxi = 0  
        
        # Keeps track of the number of moves made
        move_count = 1  
        
        # Loop through each character in the input string
        for direction in s:
            # Move in the respective direction
            if direction == 'N':  # Move up
                y += 1
            elif direction == 'W':  # Move left
                x -= 1
            elif direction == 'S':  # Move down
                y -= 1
            else:  # Move right ('E')
                x += 1
            
            # Calculate the current Manhattan distance from the origin
            curr_distance = abs(x) + abs(y)
            
            # Update the maximum distance considering:
            # - The current distance
            # - The potential extra distance that can be covered using 'k' extra moves
            maxi = max(maxi, curr_distance, min(move_count, curr_distance + (k * 2)))
            
            # Increment the move counter
            move_count += 1  

        # Return the maximum distance reached
        return maxis