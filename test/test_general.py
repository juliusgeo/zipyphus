from main import length_code, distance_code, string_to_zip
import pytest
import zipfile


length_test_cases = [
    ((3, 3), 257, 0),
    ((4, 4), 258, 0),
    ((5, 5), 259, 0),
    ((6, 6), 260, 0),
    ((7, 7), 261, 0),
    ((8, 8), 262, 0),
    ((9, 9), 263, 0),
    ((10, 10), 264, 0),
    ((11, 12), 265, 1),
    ((13, 14), 266, 1),
    ((15, 16), 267, 1),
    ((17, 18), 268, 1),
    ((19, 22), 269, 2),
    ((23, 26), 270, 2),
    ((27, 30), 271, 2),
    ((31, 34), 272, 2),
    ((35, 42), 273, 3),
    ((43, 50), 274, 3),
    ((51, 58), 275, 3),
    ((59, 66), 276, 3),
    ((67, 82), 277, 4),
    ((83, 98), 278, 4),
    ((99, 114), 279, 4),
    ((115, 130), 280, 4),
    ((131, 162), 281, 5),
    ((163, 194), 282, 5),
    ((195, 226), 283, 5),
    ((227, 257), 284, 5),
    ((258, 258), 285, 0),
]

def test_length_code():
    for val in sorted(length_test_cases):
        for i in range(val[0][0], val[0][1] + 1):
            a, _, b = length_code(i)
            _, c, d = val
            assert (a, b) == (c, d)

test_dist = {
    (
        (1, 1),
        0,
        0,
    ),
    (
        (2, 2),
        1,
        0,
    ),
    (
        (3, 3),
        2,
        0,
    ),
    (
        (4, 4),
        3,
        0,
    ),
    (
        (5, 6),
        4,
        1,
    ),
    (
        (7, 8),
        5,
        1,
    ),
    (
        (9, 12),
        6,
        2,
    ),
    (
        (13, 16),
        7,
        2,
    ),
    (
        (17, 24),
        8,
        3,
    ),
    (
        (25, 32),
        9,
        3,
    ),
    (
        (33, 48),
        10,
        4,
    ),
    (
        (49, 64),
        11,
        4,
    ),
    (
        (65, 96),
        12,
        5,
    ),
    (
        (97, 128),
        13,
        5,
    ),
    (
        (129, 192),
        14,
        6,
    ),
    (
        (193, 256),
        15,
        6,
    ),
    (
        (257, 384),
        16,
        7,
    ),
    (
        (385, 512),
        17,
        7,
    ),
    (
        (513, 768),
        18,
        8,
    ),
    (
        (769, 1024),
        19,
        8,
    ),
    (
        (1025, 1536),
        20,
        9,
    ),
    (
        (1537, 2048),
        21,
        9,
    ),
    (
        (2049, 3072),
        22,
        10,
    ),
    (
        (3073, 4096),
        23,
        10,
    ),
    (
        (4097, 6144),
        24,
        11,
    ),
    (
        (6145, 8192),
        25,
        11,
    ),
    (
        (8193, 12288),
        26,
        12,
    ),
    (
        (12289, 16384),
        27,
        12,
    ),
}
def test_dist_code():
    for val in sorted(test_dist):
        for i in range(val[0][0], val[0][1] + 1):
            a, extra, b = distance_code(i)
            _, c, d = val
            assert (a, b) == (c, d)

@pytest.mark.parametrize("strk", [""""Did you win your sword fight?"
    "Of course I won the fucking sword fight," Hiro says. "I'm the greatest sword fighter in the world."
    "And you wrote the software."
    "Yeah. That, too," Hiro says."
    """, "aaaaaaaaaa", "abaaadfaa"])
def test_zip_output(strk):
    string_to_zip("sample.txt", strk)
    with open("sample.zip", "rb") as f:
        z = zipfile.ZipFile(f)
        assert z.namelist() == ["sample.txt"]
        assert z.read("sample.txt") == strk.encode("ascii")

