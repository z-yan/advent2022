class Display:
    relevant_cycles = {i for i in range(20, 221, 40)}

    def __init__(self):
        self._clock = 0
        self.x = 1
        self.crt = [["."] * 40 for _ in range(6)]
        self.total_signal_strength = 0

    @property
    def clock(self):
        return self._clock

    @clock.setter
    def clock(self, clock):
        self._clock = clock

        # Part 1
        if self.clock in Display.relevant_cycles:
            signal_strength = self.clock * self.x
            self.total_signal_strength += signal_strength
            print(f"cycle no. {clock}, signal_strength {signal_strength}")

        # Part 2
        screen_row = (self.clock - 1) // 40
        screen_col = (self.clock - 1) % 40

        self.crt[screen_row][screen_col] = "#" if abs(self.x - screen_col) <= 1 else "."

    def render(self, instructions: list[list[str]]):
        for instruction in instructions:
            self.clock += 1

            if len(instruction) > 1:
                # addx instruction
                self.clock += 1
                self.x += int(instruction[1])

        # Part 1
        print(f"\nTotal signal strength: {self.total_signal_strength}\n")

        # Part 2
        for screen_row in self.crt:
            print("".join(screen_row))


if __name__ == "__main__":
    display = Display()
    instructions = [line.split() for line in open("input.txt").read().splitlines()]
    display.render(instructions)
