<!-- source: https://developers.google.com/tech-writing/error-messages/identify-the-cause
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: identify the cause -->

- Home
- Technical Writing
- For Students
- Error Messages

# Identify the error's cause   Stay organized with collections   Save and categorize content based on your preferences.

Tell users exactly what went wrong. Be specific—vague error messages frustrate users.

Not recommended

> Bad directory.

Recommended

> The
> [Name of directory]
> directory exists but is not writable. To add files to this directory, the directory must be writable.
> [Explanation of how to make this directory writable.]

Not recommended

> Invalid field 'picture'.

Recommended

> The 'picture' field can only appear once on the command line; this command line contains the 'picture' field
> <N>
> times.
> Note: Prior to version 2.1, you could specify the 'picture' field more than once, but more recent versions no longer support this.

**Next unit:** Identify the user's invalid inputs

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Error messages should be specific, not vague. Instead of \"Bad directory,\" indicate the directory name and the specific issue, like lack of write permissions, providing instructions on resolution. For invalid fields, specify the field and the problem, for example, the 'picture' field appearing multiple times when only one instance is allowed. Explain changes in versions if applicable. The goal is to clearly inform the user about the error and how to fix it.\n"]]
