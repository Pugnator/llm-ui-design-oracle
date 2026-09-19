<!-- source: https://www.gnu.org/prep/standards/html_node/User-Interfaces.html
     fetched: 2026-09-19
     licence: GNU Free Documentation License 1.3 or later, no Invariant Sections, no Front-Cover or Back-Cover Texts — https://www.gnu.org/prep/standards/standards.html (GNU Coding Standards, last updated as shown on the page)
     title: GNU Coding Standards — Standards for Interfaces Generally -->


Next: Finding the Program’s Executable and Associated Files, Previous: Formatting Error Messages, Up: Program Behavior for All Programs [Contents][Index]

### 4.5 Standards for Interfaces Generally ¶

Please don’t make the behavior of a utility depend on the name used to invoke it. It is useful sometimes to make a link to a utility with a different name, and that should not change what it does. Thus, if you make foo a link to ls, the program should behave the same regardless of which of those names is used to invoke it.

Instead, use a run time option or a compilation switch or both to select among the alternate behaviors. You can also build two versions of the program, with different default behaviors, and install them under two different names.

Likewise, please don’t make the behavior of a command-line program depend on the type of output device it gets as standard output or standard input. Device independence is an important principle of the system’s design; do not compromise it merely to save someone from typing an option now and then. (Variation in error message syntax when using a terminal is ok, because that is a side issue that people do not depend on.)

If you think one behavior is most useful when the output is to a terminal, and another is most useful when the output is a file or a pipe, then it is usually best to make the default behavior the one that is useful with output to a terminal, and have an option for the other behavior. You can also build two different versions of the program with different names.

There is an exception for programs whose output in certain cases is binary data. Sending such output to a terminal is useless and can cause trouble. If such a program normally sends its output to stdout, it should detect, in these cases, when the output is a terminal and give an error message instead. The `-f` option should override this exception, thus permitting the output to go to the terminal.

Compatibility requires certain programs to depend on the type of output device. It would be disastrous if `ls` or `sh` did not do so in the way all users expect. In some of these cases, we supplement the program with a preferred alternate version that does not depend on the output device type. For example, we provide a `dir` program much like `ls` except that its default output format is always multi-column format.

Next: Finding the Program’s Executable and Associated Files, Previous: Formatting Error Messages, Up: Program Behavior for All Programs [Contents][Index]
