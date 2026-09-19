<!-- source: https://developers.google.com/tech-writing/error-messages/back-end
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: back end -->

- Home
- Technical Writing
- For Students
- Error Messages

# Additional guidelines for back-end engineers   Stay organized with collections   Save and categorize content based on your preferences.

This lesson contains recommendations specifically for back-end software engineers.

## Supply error codes

If an error code exists, include it as part of the error message. Error codes help technical users identify the error and find more information from an error index or error catalog.

Not recommended

> Error: You already own this bucket. Select another name from the dropdown list.

Recommended

> Error 409: You already own this bucket. Select another name from the dropdown list.

## Include an Error Identifier

Engineers parse logs to learn how and why errors occurred; therefore, include an Error Identifier to help engineers find particular errors more easily. The Error Identifier should stay constant, even if the textual error message changes.

For more information, see the Errors unit of AIP-193.

Not recommended

> { "error" : "Bad Request - Request is missing a required parameter: -collection_name. Update parameter and resubmit.

Recommended

> { "error" : "Bad Request - Request is missing a required parameter: -collection_name. Update parameter and resubmit. Issue Reference Number BR0x0071" }

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Back-end software engineers should include error codes within error messages to aid technical users in identifying and researching errors. They should also incorporate a constant Error Identifier in logs, enabling engineers to efficiently track specific errors, even if the associated text changes. Error codes and identifiers are crucial for diagnosing issues and providing context in error logs.\n"]]
