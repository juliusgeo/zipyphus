# ZIP files from scratch, the hard way, in Python

This project contains a very lean implementation of the ZIP specification--without the use of existing ZIP file compressors. `zlib` is not used,
and `zipfile` library is only used to check that the resulting ZIP file can be correctly decompressed. It implements
LZ77 compression, transforms it into a DEFLATE bitstream and then wraps it in the correct ZIP file headers.

# How?

The ZIP file format is relatively complex, but I made a few decisions that simplified this implementation:

- Only DEFLATE compression is supported
- The DEFLATE compression uses fixed Huffman coding to encode the tokens
- The ZIP files created only have a singular file and no directory structure
- Only supports strings, not binary data

# Why?

Because I can. 
ZIP files are ubiquitous, but all of the existing tools for creating them are simply too easy,
efficient, and well-documented. I knew that there had to be a worse solution out there, so I made one.


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





