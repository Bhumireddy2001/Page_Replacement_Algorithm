Page Replacement Algorithm Simulator with User-Friendly Interface

    •	This Python script simulates different page replacement algorithms: FIFO, Optimal, LRU, and Clock. It takes a reference string and a frame size as input and outputs page faults, page hits, hit ratio, and visualizes the page sequence for each algorithm.

Prerequisites
    •	Python 3.x installed on your system.
    •	Matplotlib library for plotting.

Installation
    1.	Clone the repository:
        https://github.com/Bhumireddy2001/Page_Replacement_Algorithm.git

    2.	Navigate to the project directory:
        cd desktop
        cd Page_Replacement_Algorithm

    3.	Install Dependencies
        Pip install matplotlib

Usage
    1.	Run the script:
        python Page_Replacement_Algorithm

    2.	View the output:
        •	The script will prompt you with the results for each algortithm.
        •	It will also display a plot showing the page sequence for each algorithm.

    3.	Modify input parameters
        •	You can modify the ‘reference_string’ and ‘frame_size’ variables in the ‘__main__’ block of the script to test different scenarios.

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
