import math
import multiprocessing as mp

def f(x):
    return math.cos(x) + math.log((x + 1) ** 2)

def compute_range(x_values):
    return [f(x) for x in x_values]


if __name__ == "__main__":
    start = 1.0
    end = 1e6
    step = 0.01

    # przygotowanie danych
    x_values = []
    x = start
    while x <= end:
        x_values.append(x)
        x += step

    cpu_count = mp.cpu_count()
    chunk_size = len(x_values) // cpu_count

    chunks = [
        x_values[i:i + chunk_size]
        for i in range(0, len(x_values), chunk_size)
    ]

    with mp.Pool(cpu_count) as pool:
        results = pool.map(compute_range, chunks)

    values = [v for chunk in results for v in chunk]

    print(f"Computed {len(values)} values")