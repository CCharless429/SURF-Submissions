import numpy as np
import time
import matplotlib.pyplot as plt
import math

def complicated_function(num=int):
    #takes the digits of num and multiplies them together
    num_str = str(num)
    result = 1
    for c in num_str:
        result *= int(c)

    return result

def test_run (times=0):
    counter = 0
    duration_matrix = np.zeros((2, times))
    while counter < times:
        random_matrix = np.random.randint(0, 1000, (100, 100))
        #print(random_matrix)

        #naive loop
        result_matrix = np.zeros((100, 100))
        shape = np.shape(random_matrix)

        start = time.perf_counter()
        for i in range(shape[0]):
            for j in range(shape[1]):
                result_matrix[i, j] = complicated_function(random_matrix[i, j])
        end = time.perf_counter()
        duration_1 = end - start
        #print(counter)
        duration_matrix[0, counter] = duration_1
        #print(f"Naive Loop time: {duration} ns")

        # vectorize function
        start = time.perf_counter()
        result_matrix = np.zeros((100, 100))
        v_complicated_function = np.vectorize(complicated_function)
        result_matrix = v_complicated_function(random_matrix)
        end = time.perf_counter()
        duration_2 = end - start
        duration_matrix[1, counter] = duration_2
        #print(f"Vectorized Equation time: {duration} ns")
        counter += 1
    
    duration_matrix.round(4)

    def histogram_nloop ():
        naive_loop = duration_matrix[0, :]
        bin = np.arange(naive_loop.min(), naive_loop.max(), naive_loop.max() / 10.0)

        
        print("=== Naive Loop Stats ===")
        print(f"Mean: {math.trunc(np.mean(naive_loop) * 10000) / 10000} s")
        print(f"Median: {math.trunc(np.median(naive_loop) * 10000) / 10000} s")
        print(f"Standard Deviation: {math.trunc(np.std(naive_loop) * 10000) / 10000} s\n")

        # Uncomment two below to see graph
        #plt.hist(naive_loop, bin)
        #plt.show()

    def histogram_vectorize():
        vectorize = duration_matrix[1, :]

        bin = np.arange(vectorize.min(), vectorize.max(), vectorize.max() / 10.0)

        print("=== Vectorize Stats ===")
        print(f"Mean: {math.trunc(np.mean(vectorize) * 10000) / 10000} s")
        print(f"Median: {math.trunc(np.median(vectorize) * 10000) / 10000} s")
        print(f"Standard Deviation: {math.trunc(np.std(vectorize) * 10000) / 10000} s")

        # Uncomment two below to see graph
        #plt.hist(vectorize, bin)
        #plt.show()

    # Comment or uncomment next two lines to modify output
    histogram_nloop()
    histogram_vectorize()

test_run(1000)


