# Zipyphus: ZIP compressor for the damned

Traditional ZIP file compressors are too easy to use, and rob the user of the vital character-building experience that comes with
using poorly made software. For the more Sisyphean users looking for an uphill battle, this project is for you.

This project is a ZIP file compressor that is difficult to use, limited in scope, but easy to understand (only ~300 LOC!).
`zlib` is not used, and the `zipfile` library is only used to check that the resulting ZIP file can be correctly decompressed. It implements
LZ77 compression, transforms it into a DEFLATE bitstream and then wraps it in the correct ZIP file headers.

# How?

The ZIP file format is relatively complex, but I made a few executive decisions to make my life easier:

- Only DEFLATE compression is supported (I don't like the acronyms of the other compression methods. Sorry.)
- The DEFLATE compression uses fixed Huffman coding to encode the tokens (dynamic Huffman trees are too much work)
- The ZIP files created only have a singular file and no directory structure (multiple files == "bloat")


# Why?

Because I can.

# Usage

Not recommended. However, if you insist:

```python
strk = """
"Did you win your sword fight?"
"Of course I won the fucking sword fight," Hiro says. "I'm the greatest sword fighter in the world."
"And you wrote the software."
"Yeah. That, too," Hiro says."
"""
string_to_zip("sample.txt", strk)
```



