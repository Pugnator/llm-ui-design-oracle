<!-- source: https://developers.google.com/tech-writing/error-messages/error-handling
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: error handling -->

- Home
- Technical Writing
- For Students
- Error Messages

# General error handling rules   Stay organized with collections   Save and categorize content based on your preferences.

[image: Spark icon]

- Always report errors instead of failing silently to provide users and support with crucial information.
- Adhere to Google's programming language guides for consistent and effective error handling practices.
- Implement a comprehensive error model, including standardized error codes and messages, as outlined in Google AIP.
- Provide specific and informative error messages that reveal the root cause of the issue rather than generic ones.
- Log error codes, both internal and external, and document them thoroughly for efficient monitoring and debugging.
- Raise errors immediately upon detection to simplify debugging and prevent delayed issue discovery.

Before we get to the fun part of the course—wording error messages—let's discuss a few general error handling rules.

## Don't fail silently

Failure is inevitable; failing to report failures is inexcusable. Failing silently causes the following problems:

- Users wonder whether something has gone wrong. (*"Why did my order not go through?"*)
- Customer support wonders what caused a problem. (*"The log file gave no indication of a problem."*)

Embrace your software's fallibility. Assume that humans will make mistakes using your software. Try to minimize ways for people to misuse your software, but assume that you can't completely eliminate misuse. Therefore, plan error messages as you design software.

## Follow the programming language guides

Follow the guidelines on error handling in Google's programming language guides, including:

- Google C++ Style Guide
- Google Java Style Guide
- Google Python Style Guide, particularly the Error Messages section
- Google JavaScript Style Guide
- Google Go Style Guide, particularly the Error handling section

## Implement the full error model

Implement the full error model described in the Errors page of the Google AIP. For instance, note the following quote about implementing error messages in services:

> Services must return a
> google.rpc.Status
> message when an API error occurs, and must use the canonical error codes defined in
> google.rpc.Code
> .

The Errors page of the Google Cloud API design guide provides helpful information about implementing the full error model for Google APIs.

## Avoid swallowing the root cause

API implementations should not swallow the root cause of issues occurring in the back end. For example, many different situations can cause a "Server error" problem, including:

- service failure
- network connection drop
- mismatching status
- permission issues

"Server error" is too general an error message to help users understand and fix the problem. If the server logs contain identification information about the in-session user and operation, we recommend providing additional context on the particular failure case.

## Log the error codes

Numeric **error codes** help customer support monitor and diagnose errors. Consequently, specifying numeric error codes along with textual error messages is often quite valuable.

You can specify error codes for both internal and external errors. For internal errors, provide a proper error code for easy lookup/debugging by internal support personnel and engineers.

Document all error codes.

## Raise errors immediately

Raise errors as early as useful. Holding on to errors and then raising them later increases debugging costs dramatically.

**Next unit:** Identify the error's cause

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Software should report all failures, avoiding silent failures that confuse users and hinder support. Follow programming language guidelines for error handling, such as those in Google's style guides, and implement the full error model as described in the Google API design. Avoid generic errors like \"Server error\"; provide specific details. Implement numeric error codes for internal and external use and log them for monitoring and debugging. Raise errors promptly to ease troubleshooting.\n"]]
