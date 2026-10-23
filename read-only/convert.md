# How to convert existing reStructuredText documentation to MyST

To convert existing reST documents to MyST, you can use the rst2myst CLI script shipped by RST-to-MyST. The script supports converting the documents one by one, or scanning a series of directories to convert them in bulk.

After installing `rst-to-myst`, you can run the script as follows:

```
$ rst2myst convert docs/source/index.rst  # Converts index.rst to index.md
$ rst2myst convert docs/**/*.rst  # Convert every .rst file under the docs directory
```

This will create a .md MyST file for every .rst source file converted.

Source: https://docs.readthedocs.com/platform/stable/guides/migrate-rest-myst.html#how-to-convert-existing-restructuredtext-documentation-to-myst