#!./these_env/bin/python
import click
import glob
import os
import shutil

TASK_SEPARATOR ="\t"
SUBTASK_SEPARATOR = "\t\t"

CORPUS_PATH = "data/curated/corpus/generic/**/*.txt"


@click.group()
def cli():
    pass


@cli.group("corpus")
def corpus_group():
    """ Group of function to deal with corpora """

@corpus_group.command("lemmatize", help="Lemmatize texts")
@click.argument('lemmatizers', type=click.Choice(['collatinus', 'pie']), nargs=-1)
@click.option("--debug", is_flag=True)
def lemmatize(lemmatizers=[], debug=False):
    """ Lemmatize using LEMMATIZERS"""
    import helpers.lemmatizers
    text_files = glob.glob(CORPUS_PATH) + glob.glob(CORPUS_PATH.replace("*.", "."))
    if debug:
        text_files = text_files[-10:]
    if "pie" in lemmatizers:
        helpers.lemmatizers.run_pie_web(text_files=text_files, target_path="data/curated/corpus/generic/", threads=1)


if __name__ == "__main__":
    cli()
