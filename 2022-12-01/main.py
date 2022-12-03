if __name__ == "__main__":
    calorie_sums = list()

    with open("input.txt") as f:
        curr_sum = 0

        for next_line in f:
            if next_line == "\n":
                calorie_sums.append(curr_sum)
                curr_sum = 0
            else:
                next_value = int(next_line)
                curr_sum += next_value

        if curr_sum > 0:
            calorie_sums.append(curr_sum)

    max_calories = max(calorie_sums)
    print(f"max value: {max_calories}")

    calories_sorted = sorted(calorie_sums, reverse=True)
    top_three = calories_sorted[:3]
    sum_top_three = sum(top_three)
    print(f"sum of top three: {sum_top_three}")
