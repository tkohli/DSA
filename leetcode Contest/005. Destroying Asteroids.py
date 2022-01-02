class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for ast in asteroids:
            if mass >= ast:
                mass += ast
            else:
                return False
        return True
