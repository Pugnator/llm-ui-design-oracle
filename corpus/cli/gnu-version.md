<!-- source: https://www.gnu.org/prep/standards/html_node/_002d_002dversion.html
     fetched: 2026-09-19
     licence: GNU Free Documentation License 1.3 or later, no Invariant Sections, no Front-Cover or Back-Cover Texts — https://www.gnu.org/prep/standards/standards.html (GNU Coding Standards, last updated as shown on the page)
     title: GNU Coding Standards — --version -->


Next: --help, Up: Standards for Command Line Interfaces [Contents][Index]

#### 4.8.1 --version ¶

The standard `--version` option should direct the program to print information about its name, version, origin and legal status, all on standard output, and then exit successfully. Other options and arguments should be ignored once this is seen, and the program should not perform its normal function.

The first line is meant to be easy for a program to parse; the version number proper starts after the last space. In addition, it contains the canonical name for this program, in this format:

```
GNU Emacs 19.30
```

The program’s name should be a constant string; *don’t* compute it from `argv[0]`. The idea is to state the standard or canonical name for the program, not its file name. There are other ways to find out the precise file name where a command is found in `PATH`.

If the program is a subsidiary part of a larger package, mention the package name in parentheses, like this:

```
emacsserver (GNU Emacs) 19.30
```

If the package has a version number which is different from this program’s version number, you can mention the package version number just before the close-parenthesis.

If you *need* to mention the version numbers of libraries which are distributed separately from the package which contains this program, you can do so by printing an additional line of version info for each library you want to mention. Use the same format for these lines as for the first line.

Please do not mention all of the libraries that the program uses “just for completeness”—that would produce a lot of unhelpful clutter. Please mention library version numbers only if you find in practice that they are very important to you in debugging.

The following line, after the version number line or lines, should be a copyright notice. If more than one copyright notice is called for, put each on a separate line.

Next should follow a line stating the license, preferably using one of the abbreviations below, and a brief statement that the program is free software, and that users are free to copy and change it. Also mention that there is no warranty, to the extent permitted by law. See recommended wording below.

It is ok to finish the output with a list of the major authors of the program, as a way of giving credit.

Here’s an example of output that follows these rules:

```
GNU hello 2.3
Copyright (C) 2007 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

You should adapt this to your program, of course, filling in the proper year, copyright holder, name of program, and the references to distribution terms, and changing the rest of the wording as necessary.

This copyright notice only needs to mention the most recent year in which changes were made—there’s no need to list the years for previous versions’ changes. You don’t have to mention the name of the program in these notices, if that is inconvenient, since it appeared in the first line. (The rules are different for copyright notices in source files; see Copyright Notices in Information for GNU Maintainers.)

Translations of the above lines must preserve the validity of the copyright notices (see Internationalization). If the translation’s character set supports it, the ‘(C)’ should be replaced with the copyright symbol, as follows:

©

Write the word “Copyright” exactly like that, in English. Do not translate it into another language. International treaties recognize the English word “Copyright”; translations into other languages do not have legal significance.

Finally, here is the table of our suggested license abbreviations. Any abbreviation can be followed by ‘vversion[+]’, meaning that particular version, or later versions with the ‘+’, as shown above. In the case of a GNU license, *always* indicate the permitted versions in this way.

In the case of exceptions for extra permissions with the GPL, we use ‘/’ for a separator; the version number can follow the license abbreviation as usual, as in the examples below.

GPL
GNU General Public License, https://www.gnu.org/licenses/gpl.html.

LGPL
GNU Lesser General Public License, https://www.gnu.org/licenses/lgpl.html.

GPL/Ada
GNU GPL with the exception for Ada.

Apache
The Apache Software Foundation license, https://directory.fsf.org/wiki/License:Apache2.0.

Artistic
The Artistic license used for Perl, https://directory.fsf.org/wiki/License:ArtisticLicense2.0.

Expat
The Expat license, https://directory.fsf.org/wiki/License:Expat.

MPL
The Mozilla Public License, https://directory.fsf.org/wiki/License:MPLv2.0.

OBSD
The original (4-clause) BSD license, incompatible with the GNU GPL,
 https://directory.fsf.org/wiki/License:BSD_4Clause.

PHP
The license used for PHP, https://directory.fsf.org/wiki/License:PHPv3.01.

public domain
The non-license that is being in the public domain,
 https://www.gnu.org/licenses/license-list.html#PublicDomain.

Python
The license for Python, https://directory.fsf.org/wiki/License:Python2.0.1.

RBSD
The revised (3-clause) BSD, compatible with the GNU GPL,
 https://directory.fsf.org/wiki/License:BSD_3Clause.

X11
The simple non-copyleft license used for most versions of the X Window System, https://directory.fsf.org/wiki/License:X11.

Zlib
The license for Zlib, https://directory.fsf.org/wiki/License:Zlib.

More information about these licenses and many more are on the GNU licensing web pages, https://www.gnu.org/licenses/license-list.html.

Next: --help, Up: Standards for Command Line Interfaces [Contents][Index]
