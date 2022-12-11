import logging
import re
import sys
from math import prod

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))


class Monkey:
    description_pattern = re.compile(
        r"Monkey \d:\n\s+Starting items: (?P<starting_items>[\d, ]+)\n"
        r"\s+Operation: new = old (?P<operator>[*+]) (?P<operand>\d+|old)\n"
        r"\s+Test: divisible by (?P<divisor>\d+)\n"
        r"\s+If true: throw to monkey (?P<true_monkey>\d+)\n"
        r"\s+If false: throw to monkey (?P<false_monkey>\d+)"
    )

    def __init__(
        self,
        description: str,
        monkeys: list["Monkey"],
        relief_factor: int = 3,
        worries_managed: bool = False,
    ):
        self.monkeys = monkeys
        self.relief_factor = relief_factor
        self.inspection_count = 0

        match_groups = Monkey.description_pattern.match(description).groupdict()

        self.items = [
            int(item) for item in match_groups.get("starting_items").split(", ")
        ]
        self.operator = match_groups.get("operator")
        self.operand = match_groups.get("operand")
        self.divisor = int(match_groups.get("divisor"))
        self.true_monkey = int(match_groups.get("true_monkey"))
        self.false_monkey = int(match_groups.get("false_monkey"))

        self._divisor_product = None
        self.worries_managed = worries_managed

    @property
    def divisor_product(self):
        if self._divisor_product is None:
            self._divisor_product = prod(monkey.divisor for monkey in self.monkeys)

        return self._divisor_product

    def inspect(self, item: int) -> int:
        self.inspection_count += 1

        logger.debug(f"\tMonkey inspects an item with a worry level of {item}.")

        if self.operand == "old":
            operand = item
            operand_text = "itself"
        else:
            operand = int(self.operand)
            operand_text = operand

        if self.operator == "*":
            result = item * operand
            operation_text = "multiplied"
        else:
            result = item + operand
            operation_text = "increased"

        logger.debug(
            f"\t\tWorry level is {operation_text} by {operand_text} to {result}."
        )

        return result

    def throw(self, item: int) -> None:
        divisible = item % self.divisor == 0

        logger.debug(
            f"\t\tCurrent worry level is {'' if divisible else 'not '}divisible by {self.divisor}."
        )

        next_monkey = self.true_monkey if divisible else self.false_monkey

        logger.debug(
            f"\t\tItem with worry level {item} is thrown to monkey {next_monkey}."
        )

        self.monkeys[next_monkey].catch(item)

    def catch(self, item: int):
        if self.worries_managed:
            # throwback to number theory
            item %= self.divisor_product

        self.items.append(item)

    def take_turn(self) -> None:
        while self.items:
            item = self.inspect(self.items.pop(0)) // self.relief_factor
            logger.debug(
                f"\t\tMonkey gets bored with item. Worry level is divided by {self.relief_factor} to {item}."
            )
            self.throw(item)


def monkey_business(monkeys: list[Monkey], round_count: int):
    for round_number in range(round_count):
        logger.info(f"Starting round {round_number + 1}")

        for i, monkey in enumerate(monkeys):
            logger.debug(f"Monkey {i}:")
            monkey.take_turn()

        logger.debug(
            f"\nAfter round {round_number + 1}, the monkeys are holding items with these worry levels:"
        )
        for i, monkey in enumerate(monkeys):
            logger.debug(f"Monkey {i}: {', '.join(str(item) for item in monkey.items)}")

    logger.debug("\n")

    inspection_counts = [monkey.inspection_count for monkey in monkeys]

    for i, inspection_count in enumerate(inspection_counts):
        logger.debug(f"Monkey {i} inspected items {inspection_count} times.")

    monkey_business = prod(sorted(inspection_counts, reverse=True)[:2])

    logger.info(f"Level of monkey business: {monkey_business}")


if __name__ == "__main__":
    with open("input.txt") as f:
        descriptions = f.read().split("\n\n")

    # Part 1
    logger.setLevel(logging.DEBUG)

    round_count = 20

    monkeys = list()
    monkeys += [Monkey(description, monkeys) for description in descriptions]

    monkey_business(monkeys, round_count)

    # Part 2
    logger.setLevel(logging.INFO)
    round_count = 10000

    monkeys = list()
    monkeys += [Monkey(description, monkeys, 1, True) for description in descriptions]

    monkey_business(monkeys, round_count)
