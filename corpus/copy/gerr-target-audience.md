<!-- source: https://developers.google.com/tech-writing/error-messages/target-audience
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: target audience -->

- Home
- Technical Writing
- For Students
- Error Messages

# Write for the target audience   Stay organized with collections   Save and categorize content based on your preferences.

[image: Spark icon]

- Error messages should use language and terminology tailored to the specific target audience, avoiding jargon or technical terms they may not understand.
- Consider the audience's knowledge base when crafting error messages, opting for clear and concise explanations instead of technical details that might be confusing.
- Provide helpful and reassuring information in error messages, guiding users towards solutions instead of simply stating the problem.
- Error messages for broad audiences should avoid technical terms like "server" or "CPU," focusing on user-friendly language and explanations.
- When dealing with technical concepts like file formats, error messages should either target technical audiences or provide additional context and support for non-technical users.

Tailor the error message to the target audience. That is:

- Use appropriate terminology for that target audience.
- Be mindful of what the target audience knows and doesn't know.

Beware of the  curse of knowledge when writing error messages. A term familiar to you might not be familiar to your target audience. For example, the following error message contains terminology appropriate for a target audience of ML experts. If the target audience includes a significant number of people who aren't ML experts, then the error message is mystifying:

Recommended for ML experts only

> Exploding gradient problem. To fix this problem, consider gradient clipping.

Now compare the following two error messages. The first error message contains technical truth, but terms like *server*, *client*, *farm*, and *CPU* are not going to help most consumers:

Inappropriate for shoppers

> A server dropped your client's request because the server farm is running at 92% CPU capacity. Retry in five minutes.

The second error message is more suitable (and comforting) for a non-technical audience:

Appropriate for shoppers

> So many people are shopping right now that our system can't complete your purchase. Don't worry--we won't lose your shopping cart. Please retry your purchase in five minutes.

### Multiple choice exercise

Which audience(s) is the following error message appropriate for?

- This app does not support JPG files. You may only upload SVG or PNG files.

Software Engineers, System Administrators, and technical end-users
All three of those audiences understand different file formats.
People using an app to upload receipts.
This error message will frustrate users unfamiliar with file formats (which is a lot of people). To become more useful, this error message would require additional information explaining how end-users can determine file format. Furthermore, some end users don't know what
upload
means.
Inappropriate for any audience.
Most technical people are familiar with different file formats, so this is a good, concise error message for certain people.
**Next unit:** Use terminology consistently

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Error messages should be tailored to the target audience's knowledge level. Use appropriate terminology and avoid technical jargon unfamiliar to them. For example, messages suitable for ML experts or software engineers may confuse non-technical users. A good error message considers what the audience knows and doesn't know, explaining complex concepts if necessary. Avoid the curse of knowledge and ensure that the message is clear to the intended audience, like when specifying accepted file types.\n"]]
