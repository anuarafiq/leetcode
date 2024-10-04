class Solution(object):
    def spiralOrder(self, matrix):
        UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
        answer = []
        m, n = len(matrix), len(matrix[0])
        direction = RIGHT
        i, j = 0, 0

        r_wall = n
        l_wall = -1
        u_wall = 0
        d_wall = m

        while len(answer) != m * n:
            if direction == RIGHT:
                while j < r_wall:
                    answer.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                r_wall -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < d_wall:
                    answer.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                d_wall -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > l_wall:
                    answer.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                l_wall += 1
                direction = UP
            else:
                while i > u_wall:
                    answer.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                u_wall += 1
                direction = RIGHT
            
        return answer
