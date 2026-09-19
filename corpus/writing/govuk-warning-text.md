<!-- source: https://design-system.service.gov.uk/components/warning-text/
     fetched: 2026-09-19
     licence: Open Government Licence v3.0 (content); MIT (code) — https://design-system.service.gov.uk/
     title: Warning text – GOV.UK Design System
     ms.date:  -->

#  Warning text

Open this example in a new tab: warning text

- HTML

- Nunjucks

HTML

```
<div class="govuk-warning-text">
<span class="govuk-warning-text__icon" aria-hidden="true">!</span>
<strong class="govuk-warning-text__text">
<span class="govuk-visually-hidden">Warning</span>
You can be fined up to £5,000 if you do not register.
</strong>
</div>
```

## When to use this component

Use the warning text component when you need to warn users about something important, such as legal consequences of an action, or lack of action, that they might take.

## How it works

There are 2 ways to use the warning text component. You can use HTML or, if you are using Nunjucks or the GOV.UK Prototype Kit, you can use the Nunjucks macro.

Open this example in a new tab: warning text second

- HTML

- Nunjucks

HTML

```
<div class="govuk-warning-text">
<span class="govuk-warning-text__icon" aria-hidden="true">!</span>
<strong class="govuk-warning-text__text">
<span class="govuk-visually-hidden">Warning</span>
You can be fined up to £5,000 if you do not register.
</strong>
</div>
```

You might need to rewrite the hidden text (‘Warning’ in the example) to make it appropriate for your context.
