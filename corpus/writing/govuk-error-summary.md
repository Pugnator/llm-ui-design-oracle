<!-- source: https://design-system.service.gov.uk/components/error-summary/
     fetched: 2026-09-19
     licence: Open Government Licence v3.0 (content); MIT (code) — https://design-system.service.gov.uk/
     title: Error summary – GOV.UK Design System
     ms.date:  -->

#  Error summary

Use this component at the top of a page to summarise any errors a user has made.

When a user makes an error, you must show both an error summary and an Error message component next to each answer that contains an error.

Open this example in a new tab: error summary

- HTML

- Nunjucks

HTML

```
<div class="govuk-error-summary" data-module="govuk-error-summary">
<div role="alert">
<h2 class="govuk-error-summary__title">
There is a problem
</h2>
<div class="govuk-error-summary__body">
<ul class="govuk-list govuk-error-summary__list">
<li>
<a href="#">Enter your full name</a>
</li>
<li>
<a href="#">The date your passport was issued must be in the past</a>
</li>
</ul>
</div>
</div>
</div>
```

## When to use this component

Always show an error summary when there is a validation error, even if there’s only one.

## How it works

You must:

- move keyboard focus to the error summary (the govuk-frontend javascript will do this for you)

- include the heading ‘There is a problem’

- link to each of the answers that have validation errors

- make sure the error messages in the error summary are worded the same as those which appear next to the inputs with errors

As well as showing an error summary, follow the Validation pattern - for example, by adding ‘Error: ’ to the beginning of the page <title> so screen readers read it out as soon as possible.

And make your error messages clear and concise.

There are 2 ways to use the error summary component. You can use HTML or, if you are using Nunjucks or the GOV.UK Prototype Kit, you can use the Nunjucks macro.

Open this example in a new tab: error summary second

- HTML

- Nunjucks

HTML

```
<div class="govuk-error-summary" data-module="govuk-error-summary">
<div role="alert">
<h2 class="govuk-error-summary__title">
There is a problem
</h2>
<div class="govuk-error-summary__body">
<ul class="govuk-list govuk-error-summary__list">
<li>
<a href="#">Enter your full name</a>
</li>
<li>
<a href="#">The date your passport was issued must be in the past</a>
</li>
</ul>
</div>
</div>
</div>
```

### Linking from the error summary to each answer

You must link the errors in the error summary to the answer they relate to.

For questions that require a user to answer using a single field, like a file upload, select, textarea, text input or character count, link to the field.

Open this example in a new tab: linking from the error summary to an answer that uses a single field – error summary

- HTML

- Nunjucks

HTML

```
<div class="govuk-error-summary" data-module="govuk-error-summary">
<div role="alert">
<h2 class="govuk-error-summary__title">
There is a problem
</h2>
<div class="govuk-error-summary__body">
<ul class="govuk-list govuk-error-summary__list">
<li>
<a href="#full-name-input">Enter your full name</a>
</li>
</ul>
</div>
</div>
</div>
<h1 class="govuk-heading-l">Your details</h1>
<div class="govuk-form-group govuk-form-group--error">
<label class="govuk-label" for="full-name-input">
Full name
</label>
<p id="full-name-input-error" class="govuk-error-message">
<span class="govuk-visually-hidden">Error:</span> Enter your full name
</p>
<input class="govuk-input govuk-input--error" id="full-name-input" name="name" type="text" aria-describedby="full-name-input-error" autocomplete="name">
</div>
```

When a user has to enter their answer into multiple fields, such as the day, month and year fields in the date input component, link to the first field that contains an error.

If you do not know which field contains an error, link to the first field.

Open this example in a new tab: linking from the error summary to an answer that uses multiple fields – error summary

- HTML

- Nunjucks

HTML

```
<div class="govuk-error-summary" data-module="govuk-error-summary">
<div role="alert">
<h2 class="govuk-error-summary__title">
There is a problem
</h2>
<div class="govuk-error-summary__body">
<ul class="govuk-list govuk-error-summary__list">
<li>
<a href="#passport-issued-year">Passport issue date must include a year</a>
</li>
</ul>
</div>
</div>
</div>
<div class="govuk-form-group govuk-form-group--error">
<fieldset class="govuk-fieldset" role="group" aria-describedby="passport-issued-error">
<legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
<h1 class="govuk-fieldset__heading">
When was your passport issued?
</h1>
</legend>
<p id="passport-issued-error" class="govuk-error-message">
<span class="govuk-visually-hidden">Error:</span> Passport issue date must include a year
</p>
<div class="govuk-date-input" id="passport-issued">
<div class="govuk-date-input__item">
<div class="govuk-form-group">
<label class="govuk-label govuk-date-input__label" for="passport-issued-day">
Day
</label>
<input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-day" name="passport-issued-day" type="text" value="5" inputmode="numeric">
</div>
</div>
<div class="govuk-date-input__item">
<div class="govuk-form-group">
<label class="govuk-label govuk-date-input__label" for="passport-issued-month">
Month
</label>
<input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-month" name="passport-issued-month" type="text" value="12" inputmode="numeric">
</div>
</div>
<div class="govuk-date-input__item">
<div class="govuk-form-group">
<label class="govuk-label govuk-date-input__label" for="passport-issued-year">
Year
</label>
<input class="govuk-input govuk-date-input__input govuk-input--error govuk-input--width-4" id="passport-issued-year" name="passport-issued-year" type="text" inputmode="numeric">
</div>
</div>
</div>
</fieldset>
</div>
```

For questions that require a user to select one or more options from a list using radios or checkboxes, link to the first radio or checkbox.

Open this example in a new tab: linking from the error summary to checkboxes – error summary

- HTML

- Nunjucks

HTML

```
<div class="govuk-error-summary" data-module="govuk-error-summary">
<div role="alert">
<h2 class="govuk-error-summary__title">
There is a problem
</h2>
<div class="govuk-error-summary__body">
<ul class="govuk-list govuk-error-summary__list">
<li>
<a href="#nationality">Select if you are British, Irish or a citizen of a different country</a>
</li>
</ul>
</div>
</div>
</div>
<div class="govuk-form-group govuk-form-group--error">
<fieldset class="govuk-fieldset" aria-describedby="nationality-hint nationality-error">
<legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
<h1 class="govuk-fieldset__heading">
What is your nationality?
</h1>
</legend>
<div id="nationality-hint" class="govuk-hint">
If you have dual nationality, select all options that are relevant to you
</div>
<p id="nationality-error" class="govuk-error-message">
<span class="govuk-visually-hidden">Error:</span> Select if you are British, Irish or a citizen of a different country
</p>
<div class="govuk-checkboxes" data-module="govuk-checkboxes">
<div class="govuk-checkboxes__item">
<input class="govuk-checkboxes__input" id="nationality" name="nationality" type="checkbox" value="british" aria-describedby="nationality-item-hint">
<label class="govuk-label govuk-checkboxes__label" for="nationality">
British
</label>
<div id="nationality-item-hint" class="govuk-hint govuk-checkboxes__hint">
including English, Scottish, Welsh and Northern Irish
</div>
</div>
<div class="govuk-checkboxes__item">
<input class="govuk-checkboxes__input" id="nationality-2" name="nationality" type="checkbox" value="irish">
<label class="govuk-label govuk-checkboxes__label" for="nationality-2">
Irish
</label>
</div>
<div class="govuk-checkboxes__item">
<input class="govuk-checkboxes__input" id="nationality-3" name="nationality" type="checkbox" value="other">
<label class="govuk-label govuk-checkboxes__label" for="nationality-3">
Citizen of another country
</label>
</div>
</div>
</fieldset>
</div>
```

### Where to put the error summary

Put the error summary at the top of the main container. If your page includes breadcrumbs or a back link, place it below these, but above the <h1>.

Open this example in a new tab: full page example – error summary

- HTML

- Nunjucks

HTML

```
<div class="govuk-width-container">
<a href="#" class="govuk-back-link">Back</a>
<main class="govuk-main-wrapper " id="main-content" role="main">
<div class="govuk-grid-row">
<div class="govuk-grid-column-two-thirds">
<form action="/form-handler" method="post" novalidate>
<div class="govuk-error-summary" data-module="govuk-error-summary">
<div role="alert">
<h2 class="govuk-error-summary__title">
There is a problem
</h2>
<div class="govuk-error-summary__body">
<ul class="govuk-list govuk-error-summary__list">
<li>
<a href="#passport-issued-year">Passport issue date must include a year</a>
</li>
</ul>
</div>
</div>
</div>
<div class="govuk-form-group govuk-form-group--error">
<fieldset class="govuk-fieldset" role="group" aria-describedby="passport-issued-error">
<legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
<h1 class="govuk-fieldset__heading">
When was your passport issued?
</h1>
</legend>
<p id="passport-issued-error" class="govuk-error-message">
<span class="govuk-visually-hidden">Error:</span> Passport issue date must include a year
</p>
<div class="govuk-date-input" id="passport-issued">
<div class="govuk-date-input__item">
<div class="govuk-form-group">
<label class="govuk-label govuk-date-input__label" for="passport-issued-day">
Day
</label>
<input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-day" name="passport-issued-day" type="text" value="5" inputmode="numeric">
</div>
</div>
<div class="govuk-date-input__item">
<div class="govuk-form-group">
<label class="govuk-label govuk-date-input__label" for="passport-issued-month">
Month
</label>
<input class="govuk-input govuk-date-input__input govuk-input--width-2" id="passport-issued-month" name="passport-issued-month" type="text" value="12" inputmode="numeric">
</div>
</div>
<div class="govuk-date-input__item">
<div class="govuk-form-group">
<label class="govuk-label govuk-date-input__label" for="passport-issued-year">
Year
</label>
<input class="govuk-input govuk-date-input__input govuk-input--error govuk-input--width-4" id="passport-issued-year" name="passport-issued-year" type="text" inputmode="numeric">
</div>
</div>
</div>
</fieldset>
</div>
<button type="submit" class="govuk-button" data-module="govuk-button">
Continue
</button>
</form>
</div>
</div>
</main>
</div>
```
