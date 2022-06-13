class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Find all external corners, we filter them using XOR 
        then total area of rectangle should be equal to area of rectangle with external corners
        """
        area = 0
        coordinates = set()  # only have even number of elements

        for x, y, X, Y in rectangles:
            area += ((Y-y) * (X-x))
            coordinates ^= {(x, y), (x, Y), (X, y), (X, Y)}

        if len(coordinates) != 4:
            return False
        x, y = min(coordinates, key=lambda x: x[0]+x[1])
        X, Y = max(coordinates, key=lambda x: x[0]+x[1])

        return ((Y-y) * (X-x)) == area
