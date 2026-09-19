<!-- source: https://developers.google.com/tech-writing/error-messages/show-fix
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: show fix -->

- Home
- Technical Writing
- For Students
- Error Messages

# Explain how to fix the problem   Stay organized with collections   Save and categorize content based on your preferences.

Create **actionable error messages**. That is, after explaining the cause of the problem, explain how to fix the problem.

Not recommended

> The client app on your device is no longer supported.

Recommended

> The client app on your device is no longer supported. To update the client app, click the
> Update app
> button.

Here's a second example:

Not recommended

> Could not fetch resource:
> - Quota 'CPUS' exceeded. Limit: 1.0 in region us-central-1.

Recommended

> You requested 2.0 CPUs, which exceeds your quota of 1.0 CPUs in the us-central-1 region. To fix the problem, take either of the following actions:
> - Increase your CPU quota in the us-central-1 region.
> - Make your request in a region where you have more CPU quota.
> See
> [URL of documentation]
> for details.

**Next unit:** Provide examples

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-31 UTC."],[],["Error messages should be actionable, explaining both the problem's cause and its solution. Instead of simply stating an issue, provide clear instructions on how to resolve it. For example, instead of stating \"The client app is unsupported,\" the message should read \"The client app is unsupported. To update, click the **Update app** button\", thus directing the user toward a fix.\n"]]
