<!-- source: https://developers.google.com/tech-writing/error-messages/be-concise
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: be concise -->

- Home
- Technical Writing
- For Students
- Error Messages

# Be concise   Stay organized with collections   Save and categorize content based on your preferences.

[image: Spark icon]

- Prioritize conciseness in error messages by eliminating unnecessary text and focusing on the core issue.
- Use active voice instead of passive voice to make sentences shorter and clearer, as it improves readability.
- Be concise without sacrificing clarity; avoid making error messages so brief that they become ambiguous or cryptic.
- Error message example: "The SiteID
- The document refers to another unit with regards to tips for reducing sentence lengths.

Write concise error messages. Emphasize what's important. Cut unnecessary text. See the Short sentences unit of Tech Writing One for tips on reducing sentence length.

Not recommended

> Unable to establish connection to the SQL database.
> [Explanation of how to fix the issue.]

Recommended

> Can't connect to the SQL database.
> [Explanation of how to fix the issue.]

Not recommended

> The resource was not found and cannot be differentiated. What you selected doesn't exist in the cluster.
> [Explanation of how to find valid resources in the cluster.]

Recommended

> Resource <name> isn't in cluster <name>.
> [Explanation of how to find valid resources in the cluster.]

Converting from passive voice to active voice often makes sentences conciser and easier to understand:

Not recommended

> The Froobus operation is no longer supported by the Frambus app.

Recommended

> The Frambus app no longer supports the Froobus operation.

In your enthusiasm to be concise, don't remove so many words that the resulting error message becomes cryptic. For example, don't reduce the preceding error message down to the following:

Not recommended

> Unsupported.

### Multiple choice exercise

Reorder and shorten the following start of an error message. How many words can you remove?  The SiteID <SiteID> you have entered is invalid.

5
Yes. The error should read:
Invalid SiteID <SiteID>.
4
That's a concise error message, but you can shorten the error message even more.
3
You can remove more words.
None.
This message is not concise. You can definitely remove some words.
**Next unit:** Avoid double negatives

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["The core content focuses on writing effective error messages. Key actions include: shortening sentences, using active voice instead of passive voice, and cutting unnecessary text while still maintaining clarity. Examples demonstrate transforming verbose messages into concise ones, such as \"Can't connect to the SQL database\" instead of \"Unable to establish connection.\" Another example provides that \"Resource \u003cname\u003e isn't in cluster \u003cname\u003e\" is more concise than \"The resource was not found and cannot be differentiated.\" Finally an example shows that \"Invalid SiteID \u003cSiteID\u003e\" is better than \"The SiteID \u003cSiteID\u003e you have entered is invalid.\"\n"]]
