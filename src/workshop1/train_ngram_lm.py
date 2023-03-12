import click
import pickle
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE


@click.command()
@click.option("--train_file", type=click.Path(exists=True), required=True)
@click.option("--ngram", type=int, default=2, help="ngram size")
def main(train_file: str, ngram: int):
    sentences = open.read(train_file, "r").readlines()
    sentences = [sentence.split(" ") for sentence in sentences]
    train, vocab = padded_everygram_pipeline(2, sentences)
    lm = MLE(ngram)
    lm.fit(train, vocab)
    with open(f"lm_{ngram}_{train_file}.pkl", "wb") as f:
        pickle.dump(lm, f)


if __name__ == "__main__":
    main()
