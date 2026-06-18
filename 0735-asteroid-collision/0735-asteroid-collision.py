class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            survived =True
            while stack and stack[-1] > 0 and asteroid < 0: 
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    survived=False
                    break
                
                else:
                    survived =False
                    break
            if survived:
                stack.append(asteroid)
        return stack



            


