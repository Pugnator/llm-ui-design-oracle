<!-- source: https://design-system.service.gov.uk/components/details/
     fetched: 2026-09-19
     licence: Open Government Licence v3.0 (content); MIT (code) — https://design-system.service.gov.uk/
     title: Details – GOV.UK Design System
     ms.date:  -->

#  Details

Make a page easier to scan by letting users reveal more detailed information only if they need it.

Open this example in a new tab: details

- HTML

- Nunjucks

HTML

```
<details class="govuk-details">
<summary class="govuk-details__summary">
<span class="govuk-details__summary-text">
Help with nationality
</span>
</summary>
<div class="govuk-details__text">
We need to know your nationality so we can work out which elections you’re entitled to vote in.
If you cannot provide your nationality, you’ll have to send copies of identity documents through the post.
</div>
</details>
```

## When to use this component

Use the details component to make a page easier to scan when it contains information that only some users will need.

## When not to use this component

Do not use the details component to hide information that the majority of your users will need.

## Decide between using details, accordions and tabs

The Details component, Accordion component, and Tabs component all hide sections of content which a user can choose to reveal.

Use the details component instead of tabs or an accordion if you only have 1 section of content.

The details component is less visually prominent than tabs and accordions, so tends to work better for content which is not as important to users.

## How it works

The details component is a short link that shows more detailed help text when a user clicks on it.

There are 2 ways to use the details component. You can use HTML or, if you are using Nunjucks or the GOV.UK Prototype Kit, you can use the Nunjucks macro.

Open this example in a new tab: details second

- HTML

- Nunjucks

HTML

```
<details class="govuk-details">
<summary class="govuk-details__summary">
<span class="govuk-details__summary-text">
Help with nationality
</span>
</summary>
<div class="govuk-details__text">
We need to know your nationality so we can work out which elections you’re entitled to vote in.
If you cannot provide your nationality, you’ll have to send copies of identity documents through the post.
</div>
</details>
```

### Write clear link text

Make the link text short and descriptive so users can quickly work out if they need to click on it.

## Research on this component

There is evidence that some users avoid clicking the link to show more details, as they think it will take them away from the page.

There are concerns that some users of voice assist software will not be able to interact with the component. Some software might require the user to specifically refer to the link to show more details as a button in order to interact with it.
