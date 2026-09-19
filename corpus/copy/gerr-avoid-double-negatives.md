<!-- source: https://developers.google.com/tech-writing/error-messages/avoid-double-negatives
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: avoid double negatives -->

- Home
- Technical Writing
- For Students
- Error Messages

# Avoid double negatives   Stay organized with collections   Save and categorize content based on your preferences.

[image: Spark icon]

- Double negatives in error messages confuse readers by using two negative words, making the message difficult to understand.
- Avoid using words like "not", "no", "prevents", and "forbidding" together in the same sentence as they create a double negative.
- Exceptions to exceptions should also be avoided as they introduce complexity and hinder comprehension.
- Instead of double negatives, use clear and affirmative language to express the intended message directly.
- By eliminating double negatives and exceptions to exceptions, error messages become easier to understand and act upon.

A **double negative** is a sentence or phrase that contains two negative words, such as:

- *not*, including contractions like *can't*, *won't*
- *no*

Readers find double negatives hard to parse. ("Wait, do two negatives make a positive or is the author of the error message using two negatives to emphasize something I shouldn't do?")

Some double negatives in error messages are blatant:

Not recommended

> You cannot not invoke this flag.

Recommended

> You must invoke this flag.

Other double negatives are more subtle. For example, the words *prevents* and *forbidding* in the following error message are both negatives, leading to a confusing message:

Not recommended

> The universal read permission on
> pathname
> prevents the operating system from forbidding access.

Recommended

> The universal read permission on
> pathname
> enables anyone to read this file. Giving access to everyone is a security flaw. See
> hyperlink
> for details on how to restrict readers.

Similarly, avoid exceptions to exceptions.

Not recommended

> The App Engine service account must have permissions on the image, except the Storage Object Viewer role, unless the Storage Object Admin role is available.

Recommended

> The App Engine service account must have one of the following roles:
> - Storage Object Admin
> - Storage Object Creator

**Next unit:** Write for the target audience

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Double negatives in writing, particularly in error messages, should be avoided due to their confusing nature. Examples include using \"not\" and \"no,\" or more subtle negatives like \"prevents\" and \"forbidding.\" Instead of \"You cannot not invoke this flag,\" use \"You must invoke this flag.\" Similarly, avoid exceptions to exceptions, and opt for clear, direct statements listing allowed conditions or actions, such as roles and permissions.\n"]]
