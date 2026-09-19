<!-- source: https://developers.google.com/tech-writing/error-messages/invalid-inputs
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: invalid inputs -->

- Home
- Technical Writing
- For Students
- Error Messages

# Identify the user's invalid inputs   Stay organized with collections   Save and categorize content based on your preferences.

[image: Spark icon]

- Error messages should clearly identify the specific user input causing the error, going beyond generic statements.
- When invalid input is lengthy, consider progressive disclosure or truncation to manage information overload.
- Ideal error messages present the incorrect value alongside the expected format or constraint for immediate user understanding and correction.
- Highlighting both the incorrect input and the required criteria empowers users to effectively resolve the issue.

If the error involves values that the user can enter or modify (for example, text, settings, command-line parameters), then the error message should identify the offending value(s).

Not recommended

> Funds can only be transferred to an account in the same country.

Recommended

> You can only transfer funds to an account within the same country. Sender account's country (UK) does not match the recipient account's country (Canada).

Not recommended

> Invalid postal code.

Recommended

> The postal code for the US must consist of either five or nine digits. The specified postal code (4872953) contained seven digits.

If the invalid input is a very long value that spans many lines, consider doing one of the following:

- Disclose the bad input progressively; that is, provide one or more clickable ellipses to enable users to control how much additional error information they want to see.
- Truncate the bad input, keeping only its essential parts.

### Multiple choice exercise

Which of the following error messages is best?
The specified bid ($5) is below the minimum bid ($8).
This answer surfaces the invalid input and provides enough information for the bidder to compare their bid with the minimum bid.
The specified bid is too low.
This error message doesn't surface the invalid input.
The specified bid ($5) is too low.
Although this error message does surface the invalid input, the error message doesn't provide enough information for the user to fix the problem.
The specified bid is below the minimum bid ($8).
This answer doesn't surface the invalid input.
**Next unit:** Specify requirements and constraints

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Error messages should identify invalid user-entered values, such as text, settings, or parameters. For example, messages should state the specific mismatch between sender and recipient countries or the incorrect number of digits in a postal code. For long inputs, use progressive disclosure or truncation. The best error messages include the specific invalid input and provide enough information, such as the minimum requirement, for the user to fix the error, like a bid being below the minimum.\n"]]
