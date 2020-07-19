class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x = 0
        y = 0
        spiral = []
        if len(matrix) == 0:
            return []
        elif len(matrix) == 1:
            return matrix[0]
        top_limit = 0
        right_limit = len(matrix[0]) - 1
        bottom_limit = len(matrix) - 1
        left_limit = 0
        while len(spiral) < len(matrix) * len(matrix[0]):
            top_limit += 1
            while x < right_limit:
                spiral.append(matrix[y][x])
                x += 1
            if len(spiral) + 1 == len(matrix) * len(matrix[0]):
                if matrix[y][x] != spiral[len(spiral) - 1]:
                    spiral.append(matrix[y][x])
                    return spiral
            right_limit -= 1
            while y < bottom_limit:
                spiral.append(matrix[y][x])
                y += 1
            if len(spiral) + 1 == len(matrix) * len(matrix[0]):
                if matrix[y][x] != spiral[len(spiral) - 1]:
                    spiral.append(matrix[y][x])
                    return spiral
            bottom_limit -= 1
            while x > left_limit:
                spiral.append(matrix[y][x])
                x -= 1
            if len(spiral) + 1 == len(matrix) * len(matrix[0]):
                if matrix[y][x] != spiral[len(spiral) - 1]:
                    spiral.append(matrix[y][x])
                    return spiral
            left_limit += 1
            while y > top_limit:
                spiral.append(matrix[y][x])
                y -= 1
            if len(spiral) + 1 == len(matrix) * len(matrix[0]):
                if matrix[y][x] != spiral[len(spiral) - 1]:
                    spiral.append(matrix[y][x])
                    return spiral
        return spiral