class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up position and speed, then sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        prev_time = 0  # Time of the last fleet
        
        for pos, spd in cars:
            time = (target - pos) / spd  # Time to reach target
            if time > prev_time:
                # New fleet
                fleets += 1
                prev_time = time
            # else: merges into previous fleet
        
        return fleets
