<!-- source: https://www.gnu.org/prep/standards/html_node/File-Usage.html
     fetched: 2026-09-19
     licence: GNU Free Documentation License 1.3 or later, no Invariant Sections, no Front-Cover or Back-Cover Texts — https://www.gnu.org/prep/standards/standards.html (GNU Coding Standards, last updated as shown on the page)
     title: GNU Coding Standards — File Usage -->


Previous: Memory Usage, Up: Program Behavior for All Programs [Contents][Index]

### 4.13 File Usage ¶

Programs should be prepared to operate when /usr and /etc are read-only file systems. Thus, if the program manages log files, lock files, backup files, score files, or any other files which are modified for internal purposes, these files should not be stored in /usr or /etc.

There are two exceptions. /etc is used to store system configuration information; it is reasonable for a program to modify files in /etc when its job is to update the system configuration. Also, if the user explicitly asks to modify one file in a directory, it is reasonable for the program to store other files in the same directory.
