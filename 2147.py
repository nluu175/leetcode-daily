class Solution:
    """
    2147. Number of Ways to Divide a Long Corridor
    """

    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        count_S = corridor.count("S")

        # If total seats is not even or less than 2, impossible to divide
        if count_S % 2 != 0 or count_S < 2:
            return 0

        result = 1
        seat_count = 0
        plants_between_sections = 0

        for char in corridor:
            if char == "S":
                seat_count += 1

                # When we complete a section (2 seats), start counting plants
                if seat_count % 2 == 0 and seat_count < count_S:
                    plants_between_sections = 0
                # When we start a new section after counting plants
                elif seat_count % 2 == 1 and seat_count > 2:
                    # We have (plants_between_sections + 1) choices for divider placement
                    result = (result * (plants_between_sections + 1)) % MOD
            else:  # char == 'P'
                # Only count plants between sections (after completing a section)
                if seat_count % 2 == 0 and seat_count > 0 and seat_count < count_S:
                    plants_between_sections += 1

        return result


def main():
    corridor = "SSPPSPS"
    solution = Solution()
    result = solution.numberOfWays(corridor)

    print(result)


main()
