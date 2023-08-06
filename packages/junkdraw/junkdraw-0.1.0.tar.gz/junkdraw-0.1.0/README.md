# Junkdraw

Easily create large numbers of arbitrary-sized random files.

Usage:

```shell
junkdraw <options>
```

options:

- `--path`: Path to save the generated files (default: `./junkdrawer/<desc>`)
- `--size`: Size of the generated file in bytes (default: 0)
- `--min-size`: Minimum size of the generated file in bytes
- `--max-size`: Maximum size of the generated file in bytes
- `--count`: Number of files to generate (default: 1)
- `--total-size`: Cumulative size of all files generated in bytes
- `--max-children`: Create no more than this many files or directories in any one directory (default: no limit)
- `--random`: Fill files with random data (default: leave empty)
