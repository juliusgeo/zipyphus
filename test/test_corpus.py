import pytest

from main import string_to_zip
import zipfile
import os

CORPUS_DIR = "corpus/brown_corpus"
@pytest.mark.parametrize("file", os.listdir(CORPUS_DIR)[:10])
def test_brown_corpus(file):
    filepath = os.path.join(CORPUS_DIR, file)
    strk = open(filepath, "r").read()
    string_to_zip("sample.txt", strk)
    with open("sample.zip", "rb") as f:
        z = zipfile.ZipFile(f)
        assert z.namelist() == ["sample.txt"]
        assert z.read("sample.txt") == strk.encode("ascii")