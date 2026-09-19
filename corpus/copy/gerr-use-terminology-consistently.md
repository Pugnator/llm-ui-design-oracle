<!-- source: https://developers.google.com/tech-writing/error-messages/use-terminology-consistently
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: use terminology consistently -->

- Home
- Technical Writing
- For Students
- Error Messages

# Use terminology consistently   Stay organized with collections   Save and categorize content based on your preferences.

Use terminology consistently for all error messages within a single product area. If you call something a "datastore" in one error message, then call the same thing a "datastore" in all the other error messages.

Not recommended

> Can't connect to cluster at 127.0.0.1:56. Check whether minikube is running.

Recommended

> Can't connect to minikube at 127.0.0.1:56. Check whether minikube is running.

Note:
Some authoring systems automatically recommend synonyms to ensure that you don't keep repeating the same word. Yes, variety spices up paragraphs. However, variety in error messages can confuse users.
Error messages must appear consistently with similar formats and non-contradictory content; that is, the same problem must generate the same error message. For example, if different parts of an app each detect problems with internet connection, both parts should emit the same error message.

**Next unit:** Format error messages to enhance readability

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Error messages should maintain consistent terminology within a product area; for instance, a \"datastore\" should always be referred to as such. Identical problems should trigger the same error message across an application. Avoid using synonyms for the same element in messages, as this can confuse users. Consistency in error message content and format is crucial for clear user understanding.\n"]]
