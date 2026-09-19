<!-- source: https://www.gnu.org/prep/standards/html_node/Memory-Usage.html
     fetched: 2026-09-19
     licence: GNU Free Documentation License 1.3 or later, no Invariant Sections, no Front-Cover or Back-Cover Texts — https://www.gnu.org/prep/standards/standards.html (GNU Coding Standards, last updated as shown on the page)
     title: GNU Coding Standards — Memory Usage -->


Next: File Usage, Previous: OID Allocations, Up: Program Behavior for All Programs [Contents][Index]

### 4.12 Memory Usage ¶

If a program typically uses just a few meg of memory, don’t bother making any effort to reduce memory usage. For example, if it is impractical for other reasons to operate on files more than a few meg long, it is reasonable to read entire input files into memory to operate on them.

However, for programs such as `cat` or `tail`, that can usefully operate on very large files, it is important to avoid using a technique that would artificially limit the size of files it can handle. If a program works by lines and could be applied to arbitrary user-supplied input files, it should keep only a line in memory, because this is not very hard and users will want to be able to operate on input files that are bigger than will fit in memory all at once.

If your program creates complicated data structures, just make them in memory and give a fatal error if `malloc` returns `NULL`.

Memory analysis tools such as `valgrind` can be useful, but don’t complicate a program merely to avoid their false alarms. For example, if memory is used until just before a process exits, don’t free it simply to silence such a tool.
