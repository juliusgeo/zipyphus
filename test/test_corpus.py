import pytest

from main import string_to_zip
import zipfile
import os

CORPUS_DIR = "corpus/brown_corpus"


@pytest.mark.parametrize("file", os.listdir(CORPUS_DIR)[:])
def test_brown_corpus(file):
    filepath = os.path.join(CORPUS_DIR, file)
    strk = open(filepath, "r").read()
    string_to_zip("sample.txt", strk)
    print(strk.encode("ascii"))
    with open("sample.zip", "rb") as f:
        z = zipfile.ZipFile(f)
        assert z.namelist() == ["sample.txt"]
        assert z.read("sample.txt") == strk.encode("ascii")
        os.remove("sample.zip")
