import pickle
import click


@click.command()
@click.option("--lm_pickle", type=click.Path(exists=True), required=True)
def main(lm_pickle: str):
    with open(lm_pickle, "rb") as f:
        lm = pickle.load(f)
    lengths = [1, 2, 5, 10, 15, 20, 50]
    seeds = range(5)
    generations = []
    for length in lengths:
        for seed in seeds:
            generations.append(" ".join(lm.generate(length, random_seed=seed)))
    with open(f"generations_{lm_pickle}.txt", "w") as f:
        f.write("\n".join(generations))


if __name__ == "__main__":
    main()
