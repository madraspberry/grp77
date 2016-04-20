import input_gen as ig
import kex_p as kex
import random

def main():
    num_iterations = 100
    max_corpus_size = 50
    test_cases = [
        [2, 3],
        [4, 5]

    ]

    with open("statistics.csv", "w") as f:
        for t in test_cases:
            f.write("{},{},{},{}\n".format("corpus size", "avg % correct", "min operations", "max operations"))
            corpus_size = 5
            while corpus_size <= max_corpus_size:
                print("Corpus size: {}, min: {}, max: {}, iterations: {}".format(corpus_size, t[0], t[1], num_iterations))
                (min, max, avg) = run_case(corpus_size, t[0], t[1], num_iterations)
                print("... testcase done! min: {}, max: {}, avg: {}\n".format(min, max, avg))
                f.write("{},{},{},{}\n".format(corpus_size, avg, t[0], t[1]))
                corpus_size += 5
        f.close()

def run_case(corpus_size, operations_min, operations_max, num_iterations):
    min = 100
    max = 0
    all = []
    while num_iterations > 0:
        corpus = ig.gen_corpus(num_results=corpus_size, min_operations=operations_min, max_operations=operations_max)
        percentage = kex.kex(corpus)
        all.append(percentage)

        if percentage > max:
            max = percentage
        if percentage < min:
            min = percentage

        num_iterations -= 1

    avg = sum(all) / len(all)

    return (min, max, avg)

def stub_kex():
    return random.randint(0,100)

if __name__ == "__main__":
    main()
