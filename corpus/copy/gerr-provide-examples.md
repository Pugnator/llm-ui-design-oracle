<!-- source: https://developers.google.com/tech-writing/error-messages/provide-examples
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: provide examples -->

- Home
- Technical Writing
- For Students
- Error Messages

# Provide examples   Stay organized with collections   Save and categorize content based on your preferences.

[image: Spark icon]

- Error messages should be informative and include specific examples of correct input to guide users toward resolution.
- Instead of generic statements like "Invalid input", provide detailed explanations of the error, such as what is wrong and how to fix it.
- Error messages should be tailored to the user's context and knowledge, using familiar terms and examples.
- When illustrating correct input, ensure the examples are relevant to the error and provide sufficient context for understanding.

Supplement explanations with examples that illustrate how to correct the problem.

Not recommended

> Invalid email address.

Recommended

> The specified email address (robin) is missing an @ sign and a domain name. For example: robin@example.com.

Not recommended

> Invalid input.

Recommended

> Enter the pathname of a Windows executable file. An executable file ordinarily ends with the .exe suffix. For example: C:\Program Files\Custom Utilities\StringFinder.exe

Not recommended

> Do not declare types in the initialization list.

Recommended

> Do not declare types in the initialization list. Use calls instead, such as 'BankAccount(owner, IdNum, openDate)' rather than 'BankAccount(string owner, string IdNum, Date openDate)'

Not recommended

> Syntax error on token "||", "if" expected.

Recommended

> Syntax error in the "if" condition.
> The condition is missing an outer pair of parentheses. Add a pair of bounding opening and closing parentheses to the condition. For example:
> if (a > 10) || (b == 0) # Incorrect
> if ((a > 10) || (b == 0)) # Correct

### Multiple choice exercise

Which of the following error messages is best for an audience of people who drive cars?

The specified license plate (QB2 481) is invalid. Valid license plates start with three uppercase letters and end with three digits. For example: MBR 918 and NRS 727 are both valid license plates.
This error message provides two good examples of valid license plates.
The specified license plate (QB2 481) is invalid because license plates must start with three letters and end with three digits.
Although this error message surfaces the invalid input and provides an explanation of what went wrong, this error message lacks an example.
The specified license plate (QB2 481) is invalid. For example: MBR 918 and NRS 727 are both valid license plates.
The error message doesn't provide enough context to make the examples useful. The user might be asking, "Why are MBR 918 and NRS 727 valid but QB2 481 is invalid?"
**Next unit:** Be concise

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["The core content focuses on improving error messages by providing clear explanations and examples. Instead of vague messages like \"Invalid input,\" use specific details, e.g., \"The specified email address (robin) is missing an @ sign and a domain name; use robin@example.com.\" Correctly illustrate errors, such as showing the difference between `if (a \u003e 10) || (b == 0)` and `if ((a \u003e 10) || (b == 0))`. Provide examples of valid formats, like the correct license plate structures (e.g. MBR 918).\n"]]
