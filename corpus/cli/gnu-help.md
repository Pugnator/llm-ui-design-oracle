<!-- source: https://www.gnu.org/prep/standards/html_node/_002d_002dhelp.html
     fetched: 2026-09-19
     licence: GNU Free Documentation License 1.3 or later, no Invariant Sections, no Front-Cover or Back-Cover Texts — https://www.gnu.org/prep/standards/standards.html (GNU Coding Standards, last updated as shown on the page)
     title: GNU Coding Standards — --help -->


Previous: --version, Up: Standards for Command Line Interfaces [Contents][Index]

#### 4.8.2 --help ¶

The standard `--help` option should output brief documentation for how to invoke the program, on standard output, then exit successfully. Other options and arguments should be ignored once this is seen, and the program should not perform its normal function.

Near the end of the ‘--help’ option’s output, please place lines giving the email address for bug reports, the package’s home page (normally ‘`https://www.gnu.org/software/pkg`’), and the general page for help using GNU programs. The format should be like this:

```
Report bugs to: mailing-address
pkg home page: <https://www.gnu.org/software/pkg/>
General help using GNU software: <https://www.gnu.org/gethelp/>
```

It is ok to mention other appropriate mailing lists and web pages.
