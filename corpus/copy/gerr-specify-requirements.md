<!-- source: https://developers.google.com/tech-writing/error-messages/specify-requirements
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: specify requirements -->

- Home
- Technical Writing
- For Students
- Error Messages

# Specify requirements and constraints   Stay organized with collections   Save and categorize content based on your preferences.

Help users understand requirements and constraints. Be specific. Don't assume that users know the limitations of your system.

Not recommended

> The combined size of the attachments is too big.

Recommended

> The combined size of the attachments (14MB) exceeds the allowed limit (10MB).
> [Details about possible solution.]

Not recommended

> Permission denied.

Recommended

> Permission denied. Only users in <group name> have access.
> [Details about adding users to the group.]

Not recommended

> Time-out period exceeded.

Recommended

> Time-out period (30s) exceeded.
> [Details about possible solution.]

**Next unit:** Explain how to fix the problem

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Users need clear, specific details about system limitations. Instead of vague messages, provide concrete information, like the exact size of attachments exceeding the limit (e.g., \"14MB exceeds 10MB\") or the precise timeout period (e.g., \"30s\"). When indicating permissions issues, specify the group with access (e.g., \"\u003cgroup name\u003e\"). Provide context on what is exceeding the limitations, and then provide a way to solve the issues.\n"]]
