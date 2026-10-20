# Static-Site

A from-scratch Markdown-to-HTML static site generator in Python.

Built for Boot.dev's
[Build a Static Site Generator in Python](https://www.boot.dev/courses/build-static-site-generator-python)
course.

## What was provided vs. what I wrote

| | |
|---|---|
| Provided by Boot.dev | The course lessons and spec, test expectations, and the Tolkien-themed demo content/assets under `content/` and `static/`. There was no generator implementation. |
| Written by me | The `src/` node model, inline Markdown parser, block parser, HTML renderer, recursive asset copying, page generation, dev server integration, and the test suite; 22 commits. |
| Not provided | No static-site generator code. |

## Run

```bash
./main.sh
python3 server.py --dir public
```

Then open `http://localhost:8888`.

## Test

```bash
./test.sh
```

The four test modules cover HTML nodes, text nodes, inline parsing, and block parsing.

## Limitations

- Supports a deliberately small Markdown subset (headings, paragraphs, lists, blockquotes, fenced code, inline code, bold/italic, links, and images).
- The course demo site is small; the generator is not intended to replace Hugo or Jekyll.
