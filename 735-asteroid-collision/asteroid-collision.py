class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # Process collisions
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:   # top asteroid is smaller → it explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a:  # both same size → both explode
                    stack.pop()
                break
            else:
                # No collision → push asteroid
                stack.append(a)
        
        return stack
