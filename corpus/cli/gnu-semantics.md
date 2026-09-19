<!-- source: https://www.gnu.org/prep/standards/html_node/Semantics.html
     fetched: 2026-09-19
     licence: GNU Free Documentation License 1.3 or later, no Invariant Sections, no Front-Cover or Back-Cover Texts — https://www.gnu.org/prep/standards/standards.html (GNU Coding Standards, last updated as shown on the page)
     title: GNU Coding Standards — Writing Robust Programs -->


Next: Library Behavior, Previous: Non-GNU Standards, Up: Program Behavior for All Programs [Contents][Index]

### 4.2 Writing Robust Programs ¶

Avoid arbitrary limits on the length or number of *any* data structure, including file names, lines, files, and symbols, by allocating all data structures dynamically. In most Unix utilities, “long lines are silently truncated”. This is not acceptable in a GNU utility.

Utilities reading files should not drop NUL characters, or any other nonprinting characters. Programs should work properly with multibyte character encodings, such as UTF-8. You can use libiconv to deal with a range of encodings.

Check every system call for an error return, unless you know you wish to ignore errors. Include the system error text (from `strerror`, or equivalent) in *every* error message resulting from a failing system call, as well as the name of the file if any and the name of the utility. Just “cannot open foo.c” or “stat failed” is not sufficient.

Check every call to `malloc` or `realloc` to see if it returned `NULL`. Check `realloc` even if you are making the block smaller; in a system that rounds block sizes to a power of 2, `realloc` may get a different block if you ask for less space.

You must expect `free` to alter the contents of the block that was freed. Anything you want to fetch from the block, you must fetch before calling `free`.

If `malloc` fails in a noninteractive program, make that a fatal error. In an interactive program (one that reads commands from the user), it is better to abort the command and return to the command reader loop. This allows the user to kill other processes to free up virtual memory, and then try the command again.

Use `getopt_long` to decode arguments, unless the argument syntax makes this unreasonable.

When static storage is to be written in during program execution, use explicit C code to initialize it. This way, restarting the program (without reloading it), or part of it, will reinitialize those variables. Reserve C initialized declarations for data that will not be changed.

Try to avoid low-level interfaces to obscure Unix data structures (such as file directories, utmp, or the layout of kernel memory), since these are less likely to work compatibly. If you need to find all the files in a directory, use `readdir` or some other high-level interface. These are supported compatibly by GNU.

The preferred signal handling facilities are the BSD variant of `signal`, and the POSIX `sigaction` function; the alternative USG `signal` interface is an inferior design.

Nowadays, using the POSIX signal functions may be the easiest way to make a program portable. If you use `signal`, then on GNU/Linux systems running GNU libc version 1, you should include bsd/signal.h instead of signal.h, so as to get BSD behavior. It is up to you whether to support systems where `signal` has only the USG behavior, or give up on them.

In error checks that detect “impossible” conditions, just abort. There is usually no point in printing any message. These checks indicate the existence of bugs. Whoever wants to fix the bugs will have to read the source code and run a debugger. So explain the problem with comments in the source. The relevant data will be in variables, which are easy to examine with the debugger, so there is no point moving them elsewhere.

Do not use a count of errors as the exit status for a program. *That does not work*, because exit status values are limited to 8 bits (0 through 255). A single run of the program might have 256 errors; if you try to return 256 as the exit status, the parent process will see 0 as the status, and it will appear that the program succeeded.

If you make temporary files, check the `TMPDIR` environment variable; if that variable is defined, use the specified directory instead of /tmp.

In addition, be aware that there is a possible security problem when creating temporary files in world-writable directories. In C, you can avoid this problem by creating temporary files in this manner:

```
fd = open (filename, O_WRONLY | O_CREAT | O_EXCL, 0600);
```

or by using the `mkstemps` function from Gnulib (see mkstemps in Gnulib).

In bash, use `set -C` (long name `noclobber`) to avoid this problem. In addition, the `mktemp` utility is a more general solution for creating temporary files from shell scripts (see mktemp invocation in GNU Coreutils).

Next: Library Behavior, Previous: Non-GNU Standards, Up: Program Behavior for All Programs [Contents][Index]
