# Efficient encoding

The [Bitmap file format](https://en.wikipedia.org/wiki/BMP_file_format) is usually a non-compressed format and thus
inefficient by default. In the previous examples though, the storage was particularly inefficient as it was using
text representation for ``True`` and ``False`` values, corresponding to the black/white color of each pixel.

For example, the 8x8 smiley from [step0501](../step0501) can be represented in a file as follows:

```text
8
8
False, False, False, False, False, False, False, False,
False, True, True, False, False, True, True, False,
False, True, True, False, False, True, True, False,
False, False, False, False, False, False, False, False,
False, False, False, False, False, False, False, False,
False, True, False, False, False, False, True, False,
False, False, True, True, True, True, False, False,
False, False, False, False, False, False, False, False,
```

When stored in a file, ``smiley.txt`` takes 448 bytes. Can we do better?

A first improvement is to forego the ``False`` and ``True`` values in text, and represent them in a more efficient
manner, e.g. using single-character values ``F`` and ``T``. We can also skip the commas, as we know that each value
is exactly one character.

```text
8
8
FFFFFFFF
FTTFFTTF
FTTFFTTF
FFFFFFFF
FFFFFFFF
FTFFFFTF
FFTTTTFF
FFFFFFFF
```

The resulting file, ``smiley-compact.txt`` takes only 86 bytes. This is ~19% of the initial ``smiley.txt`` file.
Can we do even better?

We could use Hexadecimal digits to represent 4 bits at once: 0 for ``0000``, 1 for ``0001``, ... and F for ``1111``.
This means that the string ``FTFFFFTF`` can be represented by the Hex values for ``1011`` and ``1101``, i.e., ``B`` and
``D``.

```text
8
8
00
66
66
00
00
BD
3C
00
```

The resulting file ``smiley-hex.txt`` takes only 38 bytes, a further improvement, as it is ~8.5% of the original
``smiley.txt``, or ~44% of the refined ``smiley-compact.txt``.

Can we improve this any further?

So far we have been working with text files. The nice thing with text files is that they are human-readable. You can
open them with a standard notes app and look at their contents. This is possible because text files use only text
characters, e.g. the standard alphabet with small ``a-z`` and capital ``A-Z`` letters, arithmetic digits ``0-9``, and
punctuation like commas ``,``, semicolons ``;``, etc. However, this means that values with no visual representation
are not used, i.e., the values 0-32 in the [ASCII table](https://www.rapidtables.com/code/text/ascii-table.html).

When there is a need for space efficiency, rather than human readability, as it is often the case with images, videos,
etc., then a full binary format is preferred. In this case the encoding could be improved even further by utilizing
just one byte for each 8 pixels (rather than two bytes, as is the case with using the Hex encoding).

Many of the popular formats in use today are binary. For instance formats used for image representation such as
[PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) and [GIF](https://en.wikipedia.org/wiki/GIF), for audio
such as [MP3](https://en.wikipedia.org/wiki/MP3) and for video such as
[AVI](https://en.wikipedia.org/wiki/Audio_Video_Interleave). 
