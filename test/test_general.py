from main import s
import pytest
import zipfile
from os import remove


@pytest.mark.parametrize(
    "strk",
    [
        (
            """"Did you win your sword fight?"
    "Of course I won the fucking sword fight," Hiro says. "I'm the greatest sword fighter in the world."
    "And you wrote the software."
    "Yeah. That, too," Hiro says.",
    """,
            0.63,
        ),
        (
            "\ncouldn't leave so soon after her arrival, in all politeness to her \nhost. And it so happened that adjacent to a couch on which she ",
            0.82,
        ),
        ("aaaaaaaaaa", 0.2),
        ("abaaadfaa", 1.0),
    ],
)
def test_zip_output(strk):
    strk, comp_ratio = strk
    string_to_zip("sample.txt", strk)
    with open("sample.zip", "rb") as f:
        z = zipfile.ZipFile(f)
        assert z.namelist() == ["sample.txt"]
        assert z.read("sample.txt") == strk.encode("ascii")
        remove("sample.zip")
