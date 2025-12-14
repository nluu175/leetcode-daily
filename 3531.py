class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # boundaries_of_x has min y and max y of that column
        boundaries_of_x = dict()
        boundaries_of_y = dict()
        count = 0

        for building in buildings:
            x, y = building[0], building[1]

            if x not in boundaries_of_x:
                boundaries_of_x[x] = [y, y]
            else:
                if (y < boundaries_of_x[x][0]):
                    boundaries_of_x[x][0] = y
                elif (y > boundaries_of_x[x][1]):
                    boundaries_of_x[x][1] = y

            if y not in boundaries_of_y:
                boundaries_of_y[y] = [x, x]
            else:
                if (x < boundaries_of_y[y][0]):
                    boundaries_of_y[y][0] = x
                elif (x > boundaries_of_y[y][1]):
                    boundaries_of_y[y][1] = x

        print("coors_x:", boundaries_of_x)
        print("coors_y:", boundaries_of_y)

        for building in buildings:
            x, y = building[0], building[1]

            # edge cases - building lies right next to the x-axis/y-axis
            if (x == n or y == 1):
                continue

            is_between_horizontal = (x > boundaries_of_y[y][0] and x < boundaries_of_y[y][1])
            if (not is_between_horizontal):
                continue

            is_between_vertical = (y > boundaries_of_x[x][0] and y < boundaries_of_x[x][1])
            if (not is_between_vertical):
                continue

            # if has_left and has_right and has_above and has_below:
            if is_between_horizontal and is_between_vertical:
                count += 1

        return count


def main():
    # n = 5
    # buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

    n = 3
    buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

    solution = Solution().countCoveredBuildings(n, buildings)

    print(solution)

main()
