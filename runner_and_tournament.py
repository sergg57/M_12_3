class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        if self.full_distance <= (2*min(self.participants, key=lambda runner: runner.speed).speed):
            result = sorted(self.participants, key=lambda runner: runner.speed, reverse=True)
            for i in range(0,len(result)):
                finishers[i+1] = result[i]
            return finishers
        else:
            while self.participants:
                for participant in self.participants:
                    participant.run()

                    if participant.distance >= self.full_distance:
                        finishers[place] = participant
                        place += 1
                        self.participants.remove(participant)
            return finishers


if __name__ == '__main__':
    runner1 = Runner('Useyn', 10)
    runner2 = Runner('Andrey', 9)
    runner3 = Runner('Nick', 3)
    tournament = Tournament(6, runner1, runner2, runner3)
    all_results = tournament.start()

    result = {}

    print({key: value.name for key, value in all_results.items()})