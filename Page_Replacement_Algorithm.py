import matplotlib.pyplot as plt

class PageReplacementSimulator:
    def __init__(self, reference_string, frame_size):
        self.reference_string = reference_string
        self.frame_size = frame_size
        self.page_faults = 0
        self.page_hits = 0
        self.page_frames = []

    def reset(self):
        self.page_faults = 0
        self.page_hits = 0
        self.page_frames = []

    def fifo(self):
        self.reset()
        page_sequence = []
        for page in self.reference_string:
            if page not in self.page_frames:
                self.page_faults += 1
                page_sequence.append(page)
                if len(self.page_frames) == self.frame_size:
                    self.page_frames.pop(0)
                self.page_frames.append(page)
            else:
                self.page_hits += 1
                page_sequence.append(None)
        return page_sequence

    def optimal(self):
        self.reset()
        page_sequence = []
        for i, page in enumerate(self.reference_string):
            if page not in self.page_frames:
                self.page_faults += 1
                page_sequence.append(page)
                if len(self.page_frames) == self.frame_size:
                    distances = {}
                    for f in self.page_frames:
                        try:
                            distances[f] = self.reference_string.index(f, i + 1)
                        except ValueError:
                            distances[f] = float('inf')
                    page_to_remove = max(distances, key=distances.get)
                    self.page_frames.remove(page_to_remove)
                self.page_frames.append(page)
            else:
                self.page_hits += 1
                page_sequence.append(None)
        return page_sequence

    def lru(self):
        self.reset()
        page_sequence = []
        for page in self.reference_string:
            if page not in self.page_frames:
                self.page_faults += 1
                page_sequence.append(page)
                if len(self.page_frames) == self.frame_size:
                    self.page_frames.pop(0)
                self.page_frames.append(page)
            else:
                self.page_hits += 1
                page_sequence.append(None)
                self.page_frames.remove(page)
                self.page_frames.append(page)
        return page_sequence

    def clock(self):
        self.reset()
        page_sequence = []
        clock_hand = 0
        clock_bits = [0] * self.frame_size

        for page in self.reference_string:
            if page not in self.page_frames:
                self.page_faults += 1
                page_sequence.append(page)
                while True:
                    if clock_bits[clock_hand] == 0:
                        if len(self.page_frames) == self.frame_size:
                            self.page_frames[clock_hand] = page
                        else:
                            self.page_frames.append(page)
                        clock_bits[clock_hand] = 1
                        break
                    else:
                        clock_bits[clock_hand] = 0
                        clock_hand = (clock_hand + 1) % self.frame_size
            else:
                self.page_hits += 1
                page_sequence.append(None)
        return page_sequence

    def get_hit_ratio(self):
        total_references = len(self.reference_string)
        return self.page_hits / total_references if total_references > 0 else 0

    def simulate_algorithm(self, algorithm):
        page_sequence = []
        if algorithm.lower() == 'fifo':
            page_sequence = self.fifo()
        elif algorithm.lower() == 'optimal':
            page_sequence = self.optimal()
        elif algorithm.lower() == 'lru':
            page_sequence = self.lru()
        elif algorithm.lower() == 'clock':
            page_sequence = self.clock()
        return page_sequence

    def plot_page_sequence(self, algorithm, page_sequence):
        plt.figure(figsize=(10, 6))
        plt.title(f"Page Sequence - {algorithm}")
        plt.xlabel("Reference String Index")
        plt.ylabel("Page Number")
        plt.plot(range(len(page_sequence)), page_sequence, marker='o', linestyle='None', color='blue')
        plt.xticks(range(len(self.reference_string)), range(len(self.reference_string)))
        plt.yticks(range(max(self.reference_string) + 1))
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7]
    frame_size = 3
    simulator = PageReplacementSimulator(reference_string, frame_size)
    algorithms = ['FIFO', 'Optimal', 'LRU', 'Clock']

    for algorithm in algorithms:
        page_sequence = simulator.simulate_algorithm(algorithm)
        print(f"Algorithm: {algorithm}")
        print(f"Page Faults: {simulator.page_faults}")
        print(f"Page Hits: {simulator.page_hits}")
        print(f"Hit Ratio: {simulator.get_hit_ratio()}")
        print("Page Sequence:", page_sequence)
        print()
        simulator.plot_page_sequence(algorithm, page_sequence)
