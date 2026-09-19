<!-- source: https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography
     fetched: 2026-09-19
     licence: CC BY 4.0 — https://github.com/MicrosoftDocs/windows-dev-docs/blob/docs/LICENSE
     title: Typography in Windows - Windows apps
     ms.date: 2021-06-24 -->

# Typography in Windows

[image: Several words rendered in Segoe UI Variable]

As the visual representation of language, typography's main task is to communicate information. The Windows type system helps you create structure and hierarchy in your content in order to maximize legibility and readability in your UI.

Segoe UI Variable is the new system font for Windows. It is a refreshed take on the classic Segoe and uses variable font technology to dynamically provide great legibility at very small sizes, and improved outlines at display sizes.

Tip

This article describes how the Fluent Design language is applied to Windows apps. For more information, see **Fluent Design - Typography**.

## Using Segoe Fluent Variable

Segoe UI Variable supports two axes for finer control of text: **weight** and **optical size**.

- The weight axis (`wght`) is incremental with weights from Thin (100) to Bold (700).
- The optical size axis (`opsz`) is automatic and on by default. It controls the shape and size of the counters in the font, to prioritize legibility at the small sizes and personality at the large sizes (for optical scaling from 8pt to 36pt).

When using XAML common controls, the Segoe UI Variable font will be selected by default for supported languages. When this font or another variable font with an optical axis is used, the optical size will automatically match the requested font-size. When using HTML, optical scaling is also automatic, but you will need to specify the Segoe UI Variable font in CSS.

[image: The word 'Segoe' rendered in Segoe UI Variable with several aspects of the typeface highlighted]

### Weights

| Weight name | Weight axis value | Visual |
|---|---|---|
| **Light** | 300 | [image: The word 'Segoe' rendered in Segoe UI Variable light] |
| **Semilight** | 350 | [image: The word 'Segoe' rendered in Segoe UI Variable semilight] |
| **Regular** | 400 | [image: The word 'Segoe' rendered in Segoe UI Variable regular] |
| **Semibold** | 600 | [image: The word 'Segoe' rendered in Segoe UI Variable semibold] |
| **Bold** | 700 | [image: The word 'Segoe' rendered in Segoe UI Variable bold] |

### Optical axis

[image: A lower case letter a rendered in Segoe UI Variable with outlines of the different shapes it can have based on the context in which it is being rendered]

## Typography best practices in Windows 11

Windows 11 uses Segoe UI Variable with the following attributes based on the context in which the text is being displayed.

| Attribute | Value | Notes |
|---|---|---|
| **Weight** | Regular, Semibold | Use regular weight for most text, use Semibold for titles |
| **Alignment** | Left, Center | Align left by default, Align center only in rare cases such as text below icons |
| **Minimum values** | 14px Semibold, 12px Regular | Text smaller than these sizes and weights are illegible in some languages |
| **Casing** | Sentence case | Use sentence casing for all UI text, including titles |
| **Truncation** | Ellipses and clipping | Use ellipses in most cases; clipping is only used in rare cases |

## Examples

Open the WinUI 3 Gallery app and see Typography principles in action

> The **WinUI 3 Gallery** app includes interactive examples of most WinUI controls, features, and functionality. Get the app from the Microsoft Store or get the source code on GitHub

## Typography in Windows Apps

[image: hero image]

As the visual representation of language, typography's main task is to communicate information. Its style should never get in the way of that goal. In this article, we'll discuss how to style typography in your Windows app to help users understand content easily and efficiently.

### Font

You should use one font throughout your app's UI, and we recommend sticking with the default font for Windows apps, **Segoe UI Variable**. It's designed to maintain optimal legibility across sizes and pixel densities and offers a clean, light, and open aesthetic that complements the content of the system.

[image: Sample text of Segoe UI Variable font.]

To display non-English languages or to select a different font for your app, please see Languages and Fonts for our recommended fonts for Windows apps.

### Size and scaling

Font sizes in XAML apps automatically scale on all devices. The scaling algorithm ensures that a 24 px font on a large screen 10 feet away is just as legible as a 24 px font on a small screen that's a few inches away.

[image: viewing distances for different devices.]

Because of how the scaling system works, you're designing in effective pixels, not actual physical pixels, and you shouldn't have to alter font sizes for different screens sizes or resolutions.

### Hierarchy

Users rely on visual hierarchy when scanning a page: headers summarize content, and body text provides more detail. To create a clear visual hierarchy in your app, follow the Windows type ramp.

[image: Screenshot of three lines of text where the font size gets smaller from one line to the next.]

### Type ramp

The Windows type ramp establishes crucial relationships between the type styles on a page, helping users read content easily. All sizes are in effective pixels and are optimized for Windows apps running on all screen sizes.

Windows 11 uses the following values for various types of text in the UI.

| Example | Weight | Size/line height |
|---|---|---|
| [image: Example of caption text] | Small | 12/16 epx |
| [image: Example of body text] | Text | 14/20 epx |
| [image: Example of body strong text] | Text semibold | 14/20 epx |
| [image: Example of body large text] | Text | 18/24 epx |
| [image: Example of body large strong text] | Text semibold | 18/24 epx |
| [image: Example of subtitle text] | Display semibold | 20/28 epx |
| [image: Example of title text] | Display semibold | 28/36 epx |
| [image: Example of title large text] | Display semibold | 40/52 epx |
| [image: Example of display text] | Display semibold | 68/92 epx |

These type styles are available as XAML static resources that follow the XAML type ramp conventions, so you can use them directly in your app.

Note

Bold and Italic styles are not part of the Windows type ramp. Use Semibold instead of Bold for emphasis. Italic is excluded because it can reduce readability and legibility, particularly for people with dyslexia.

### Alignment

The default TextAlignment is Left, and in most instances, flush-left and ragged right provides consistent anchoring of the content and a uniform layout. For RTL languages, see Adjusting layout and fonts to support globalization.

[image: Shows flush-left text.]

```
<TextBlock TextAlignment="Left">
```

### Character count

[image: Fourth screenshot of a green bar that has a green check mark and the word Do in it.] Keep to 50–60 letters per line for ease of reading.

[image: don't] Don't use fewer than 20 characters or more than 60 characters per line as this is difficult to read.

### Clipping and ellipses

When the amount of text extends beyond the space available, we recommend clipping the text and inserting ellipses [...], which is the default behavior of most WinUI text controls.

[image: Shows a device frame with some text clipping.]

```
<TextBlock TextWrapping="WrapWholeWords" TextTrimming="Clip"/>
```

[image: Fifth screenshot of a green bar that has a green check mark and the word Do in it.] Clip text, and wrap if multiple lines are enabled.

[image: don't] Don't use ellipses to avoid visual clutter.

Note

If containers are not well-defined (for example, no differentiating background color), or when there is a link to see more text, then use ellipses.

## Languages

Segoe UI Variable is our font for English, European languages, Greek, and Russian. For other languages, see the following recommendations.

### Globalizing/localizing fonts

Use the LanguageFont font-mapping APIs for programmatic access to the recommended font family, size, weight, and style for a particular language. The LanguageFont object provides access to the correct font info for various categories of content including UI headers, notifications, body text, and user-editable document body fonts. For more info, see Adjusting layout and fonts to support globalization.

### Fonts for non-Latin languages

| Font-family | Styles | Notes |
|---|---|---|
| Ebrima | Regular, Bold | User-interface font for African scripts (ADLaM, Ethiopic, N'Ko, Osmanya, Tifinagh, Vai). |
| Gadugi | Regular, Bold | User-interface font for North American scripts (Canadian Syllabics, Cherokee, Osage). |
| Leelawadee UI | Regular, Semilight, Bold | User-interface font for Southeast Asian scripts (Buginese, Khmer, Lao, Thai). |
| Malgun Gothic | Regular | User-interface font for Korean. |
| Microsoft JhengHei UI | Regular, Bold, Light | User-interface font for Traditional Chinese. |
| Microsoft YaHei UI | Regular, Bold, Light | User-interface font for Simplified Chinese. |
| Myanmar Text | Regular | Fallback font for Myanmar script. |
| Nirmala UI | Regular, Semilight, Bold | User-interface font for South Asian scripts (Bangla, Chakma, Devanagari, Gujarati, Gurmukhi, Kannada, Malayalam, Meetei Mayek, Odia, Ol Chiki, Sinhala, Sora Sompeng, Tamil, Telugu). |
| Segoe UI | Regular, Italic, Light Italic, Black Italic, Bold, Bold Italic, Light, Semilight, Semibold, Black | User-interface font for Arabic, Armenian, Georgian, and Hebrew. |
| SimSun | Regular | A legacy Chinese UI font. |
| Yu Gothic UI | Light, Semilight, Regular, Semibold, Bold | User-interface font for Japanese. |

## Fonts

### Sans-serif fonts

Sans-serif fonts are a great choice for headings and UI elements.

| Font-family | Styles | Notes |
|---|---|---|
| Arial | Regular, Italic, Bold, Bold Italic, Black | Supports European and Middle Eastern scripts (Latin, Greek, Cyrillic, Arabic, Armenian, and Hebrew). Black weight supports European scripts only. |
| Calibri | Regular, Italic, Bold, Bold Italic, Light, Light Italic | Supports European and Middle Eastern scripts (Latin, Greek, Cyrillic, Arabic and Hebrew). Arabic available in the uprights only. |
| Consolas | Regular, Italic, Bold, Bold Italic | Fixed width font that supports European scripts (Latin, Greek and Cyrillic). |
| Segoe UI | Regular, Italic, Light Italic, Black Italic, Bold, Bold Italic, Light, Semilight, Semibold, Black | User-interface font for European and Middle East scripts (Arabic, Armenian, Cyrillic, Georgian, Greek, Hebrew, Latin), and also Lisu script. |
| Selawik | Regular, Semilight, Light, Bold, Semibold | An open-source font that's metrically compatible with Segoe UI, intended for apps on other platforms that don't want to bundle Segoe UI. Get Selawik on GitHub. |

### Serif fonts

Serif fonts are good for presenting large amounts of text.

| Font-family | Styles | Notes |
|---|---|---|
| Cambria | Regular | Serif font that supports European scripts (Latin, Greek, Cyrillic). |
| Courier New | Regular, Italic, Bold, Bold Italic | Serif fixed width font that supports European and Middle Eastern scripts (Latin, Greek, Cyrillic, Arabic, Armenian, and Hebrew). |
| Georgia | Regular, Italic, Bold, Bold Italic | Supports European scripts (Latin, Greek and Cyrillic). |
| Times New Roman | Regular, Italic, Bold, Bold Italic | Legacy font that supports European scripts (Latin, Greek, Cyrillic, Arabic, Armenian, Hebrew). |

### Variable fonts

Variable fonts are good for precisely controlling the appearance of text.

| Font-family | Axes | Notes |
|---|---|---|
| Bahnschrift | Weight, Width | Variable font that supports Latin, Greek, and Cyrillic. |
| Segoe UI Variable | Weight, Optical Size | Variable font that supports Latin, Greek, and Cyrillic. |

### Symbols and icons

| Font-family | Styles | Notes |
|---|---|---|
| Segoe Fluent Icons | Regular | User-interface font for app icons. For more info, see the Segoe Fluent Icons font article. |
| Segoe UI Emoji | Regular | User-interface font for Emoji. |
| Segoe UI Symbol | Regular | Fallback font for symbols. |

## Related articles

- Text controls
- XAML theme resources
- XAML styles
- Microsoft Typography
- Variable Fonts

feedback section
end feedback section
feedback section

## Feedback

Was this page helpful?

No
Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

end feedback section

## Additional resources
