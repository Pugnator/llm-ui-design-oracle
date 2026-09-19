<!-- source: https://www.gnu.org/prep/standards/html_node/Non_002dGNU-Standards.html
     fetched: 2026-09-19
     licence: GNU Free Documentation License 1.3 or later, no Invariant Sections, no Front-Cover or Back-Cover Texts — https://www.gnu.org/prep/standards/standards.html (GNU Coding Standards, last updated as shown on the page)
     title: GNU Coding Standards — Non-GNU Standards -->


Next: Writing Robust Programs, Up: Program Behavior for All Programs [Contents][Index]

### 4.1 Non-GNU Standards ¶

The GNU Project regards standards published by other organizations as suggestions, not orders. We consider those standards, but we do not “obey” them. In developing a GNU program, you should implement an outside standard’s specifications when that makes the GNU system better overall in an objective sense. When it doesn’t, you shouldn’t.

In most cases, following published standards is convenient for users—it means that their programs or scripts will work more portably. For instance, GCC implements nearly all the features of Standard C as specified by that standard. C program developers would be unhappy if it did not. And GNU utilities mostly follow specifications of POSIX; shell script writers and users would be unhappy if our programs were incompatible.

But we do not follow either of these specifications rigidly, and there are specific points on which we decided not to follow them, so as to make the GNU system better for users.

For instance, Standard C says that nearly all extensions to C are prohibited. How silly! GCC implements many extensions, some of which were later adopted as part of the standard. If you want these constructs to give an error message as “required” by the standard, you must specify ‘--pedantic’, which was implemented only so that we can say “GCC is a 100% implementation of the standard”, not because there is any reason to actually use it.

POSIX specifies that ‘df’ and ‘du’ must output sizes by default in units of 512 bytes. What users want is units of 1k, so that is what we do by default. If you want the ridiculous behavior “required” by POSIX, you must set the environment variable ‘POSIXLY_CORRECT’ (which was originally going to be named ‘POSIX_ME_HARDER’).

GNU utilities also depart from the letter of the POSIX specification when they support long-named command-line options, and intermixing of options with ordinary arguments. This minor incompatibility with POSIX is never a problem in practice, and it is very useful.

In particular, don’t reject a new feature, or remove an old one, merely because a standard says it is “forbidden” or “deprecated”.

Next: Writing Robust Programs, Up: Program Behavior for All Programs [Contents][Index]
