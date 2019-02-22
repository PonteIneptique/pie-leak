from .pie_impl import PieLemmatizer
import os
import shutil
from multiprocessing.pool import ThreadPool
from helpers.printing import TASK_SEPARATOR, SUBTASK_SEPARATOR


def run_pie_web(text_files, target_path="data/curated/corpus/generic/", verbose=True, threads=1):
    if verbose:
        print(TASK_SEPARATOR+"Lemmatizing {} texts with Pie".format(len(text_files)))

    files = 0
    lemmatizer = PieLemmatizer()

    if os.path.isdir(lemmatizer.path(target_path)):
        if verbose:
            print(SUBTASK_SEPARATOR+"Cleaning up old text")
        shutil.rmtree(lemmatizer.path(target_path))

    for filepath in text_files:
        lemmatizer.output(filepath)
        files += 1
        if verbose:
            print(
                SUBTASK_SEPARATOR +
                "{filename} done ({texts_done}/{total_texts}) ".format(
                    filename=filepath,
                    texts_done=files,
                    total_texts=len(text_files)
                )
            )