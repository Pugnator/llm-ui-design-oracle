<!-- source: https://developers.google.com/tech-writing/error-messages/set-tone
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://developers.google.com/site-policies
     title: Google — Writing Helpful Error Messages: set tone -->

- Home
- Technical Writing
- For Students
- Error Messages

# Set the right tone   Stay organized with collections   Save and categorize content based on your preferences.

[image: Spark icon]

- Use a positive, instructive tone in error messages, guiding users on how to rectify the issue rather than simply stating the problem.
- Avoid unnecessary apologies or humor, as these can be misinterpreted or detract from the message's clarity.
- Maintain a neutral and objective tone, focusing on the issue itself rather than blaming the user.
- Ensure error messages are clear, concise, and easily understood by providing specific details and potential solutions.
- Consider cultural nuances and user expectations when crafting error messages for a global audience.

The tone of your error messages can have a significant effect on how your users interpret them.

### Be positive

Instead of telling the user what they did wrong, tell the user how to get it right.

Not recommended

> You didn't enter a name.

Recommended

> Enter a name.

Not recommended

> You entered an invalid postal code.

Recommended

> Enter a valid postal code.
> [Explanation of valid postal code.]

Not recommended

> ANSI C++ forbids declaration 'ostream' with no type 'ostream'.

Recommended

> ANSI C++ requires a type for declaration 'ostream' with type 'ostream'.

### Don't be overly apologetic

While maintaining positivity, avoid the words "sorry" or "please." Focus instead on clearly describing the problem and solution.

Note:
Different cultures interpret apologies differently. Some cultures expect apologies in certain situations; other cultures find apologies from software corporations somewhat insincere. Although this lesson suggests avoiding apologies, be aware of your target audience's expectations.
Not recommended

> We're sorry, a server error occurred and we're temporarily unable to load your spreadsheet. We apologize for the inconvenience. Please wait a while and try again.

Recommended

> Google Docs is temporarily unable to open your spreadsheet. In the meantime, try right-clicking the spreadsheet in the doc list to download it.

### Avoid humor

Don't attempt to make error messages humorous. Humor in error messages can fail for the following reasons:

- Errors frustrate users. Angry users are generally not receptive to humor.
- Users can misinterpret humor. (Jokes don't always cross borders well.)
- Humor can detract from the goal of the error message.

Not recommended

> Is the server running? Better go catch it :D.

Recommended

> The server is temporarily unavailable. Try again in a few minutes.

### Don't blame the user

If possible, focus the error message on what went wrong rather than assigning blame.

Not recommended

> You specified a printer that's offline.

Recommended

> The specified printer is offline.

### Multiple choice exercise

Which of the following error messages do not use the appropriate tone?

1. Sorry, you are not allowed to leave feedback.
2. You entered an invalid title for your item.
3. 404 Error. Oops, that is embarrassing.

1, 2, and 3.

All of these errors are inappropriate.

1

1 is inappropriate, but that's not all.

2

2 is inappropriate, but that's not all.

3

3 is inappropriate, but that's not all.

**Next unit:** Want to play a game?

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-31 UTC."],[],["Error messages should focus on positive solutions rather than user mistakes. Instead of pointing out errors, direct users on how to correct them. Avoid apologies and humor, as these can be misinterpreted or detract from the message's purpose. Frame the issue objectively, without blaming the user. Messages should be clear and helpful, offering solutions or alternative actions, like providing clear instructions. The exercise highlights that apologetic or humorous tones are inappropriate for error messages.\n"]]
