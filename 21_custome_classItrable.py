class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start  # initialize current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
    
Countdown = Countdown(5)
for number in Countdown:
    print(number)