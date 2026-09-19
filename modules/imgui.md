# Domain module: imgui — binding the core to Dear ImGui

**Module ID:** `imgui`
**Requires:** UI Oracle core >= 4.0.0
**Status:** stable
**Opt in:** list `imgui` under `modules` in your project profile, and name
`Dear ImGui` (with branch and version) as the UI toolkit in the profile's
platform table. Doing so activates the applicability table below, which tells
a reviewer which core rules the toolkit cannot implement and how those are to
be reported.

Rule IDs in this module use the `UI-IMGUI-` prefix, reserved for it by the core
(`UI_ORACLE_CONTRACT.md`, namespace table).

---

## Why a module

The core was written for a Windows desktop application without naming a
toolkit, but several of its Tier 1 rules quote WinUI mechanisms: automation
roles, `TextScaleFactor`, `AutomationProperties.Name`, Segoe UI Variable's
axes. A project built on Dear ImGui cannot satisfy those as written — not
because it chose not to, but because the toolkit has no such mechanisms. Left
unstated, every ImGui project is silently non-conformant and every review
either invents a pass or fails the same rules forever.

This module does three things. It says, rule by rule, which core requirements
Dear ImGui can meet, which it meets in a different form, and which it cannot
meet at all. It restates the ones that change form in ImGui's own terms. And
it adds the rules that immediate-mode rendering makes necessary and that no
retained-mode source thought to write down — because in ImGui the UI exists
only while the code that draws it runs.

## The sources

Dear ImGui's own documentation, read in full and archived under
`corpus/imgui/` with URL, fetch date, licence (MIT) and library version in
each header. Version read: **1.93.0 WIP, master branch, 2026-09-19**.

| ID | File | What it contributes |
|---|---|---|
| `IMGUI-README` | `corpus/imgui/imgui-readme.md` | What the library is for and what it does not support |
| `IMGUI-FAQ` | `corpus/imgui/imgui-faq.md` | The ID stack, keyboard navigation, DPI, fonts, non-Latin text, multi-threading, input dispatch, skinning limits |
| `IMGUI-FONTS` | `corpus/imgui/imgui-fonts.md` | The embedded default font, loading scalable fonts, icon fonts, DPI, UTF-8, glyph coverage |
| `IMGUI-CPP` | `corpus/imgui/imgui-cpp-guide.md` | Mission statement; the controls guide (what every key does); the frame loop |
| `IMGUI-H` | `corpus/imgui/imgui-h.md` | The public header: every configuration flag with its default and comment, the style structure, popups, tooltips, shortcuts |
| `IMGUI-WIKI` | `corpus/imgui/imgui-wiki-*.md` | Getting Started (the game-loop assumption), Docking, Multi-Viewports |

**Authority.** Toolkit documentation is classed **Tier 1 (toolkit)**: it is
the authority on what the library does and on nothing else. Where a rule
below says what the toolkit *does*, the citation is to that documentation and
the confidence is HIGH. Where a rule says what a project *should therefore
do*, the design reasoning is the core's, and the rule cites the core rule it
serves.

What the toolkit says about itself, in its own words, because it frames every
rule here:

- *"designed to enable fast iterations and to empower programmers to create
  content creation tools and visualization / debug tools (as opposed to UI
  for the average end-user). It favors simplicity and productivity toward this
  goal and lacks certain features commonly found in more high-level libraries.
  Among other things, full internationalization (right-to-left text,
  bidirectional text, text shaping etc.) and accessibility features are not
  supported."* (`IMGUI-README`)
- *"Designed primarily for developers and content-creators, not the typical
  end-user!"* — with the stated weaknesses *"Doesn't look fancy by default"*
  and *"Limited layout features, intricate layouts are typically crafted in
  code."* (`IMGUI-CPP`, Mission statement)
- On skinning: *"Somewhat … as Dear ImGui is designed and optimized to create
  debug tools, the amount of skinning you can apply is limited."*
  (`IMGUI-FAQ`)
- On seriousness: *"built to be efficient and scalable toward the needs for
  AAA-quality applications running all day."* (`IMGUI-FAQ`)

The oracle takes no position on whether a product should be built on Dear
ImGui. It records that the toolkit's authors name three gaps — accessibility,
internationalisation and visual latitude — and the rules below are largely
about not pretending those gaps are closed.

---

## A. Applicability of the core

Read this table first in any review of an ImGui surface. A core rule not
listed applies unchanged.

| Core rule | In Dear ImGui | Report as |
|---|---|---|
| `UI-A11Y-001` keyboard operability | Achievable: keyboard navigation exists but is **off by default** | Applies; see `UI-IMGUI-002` |
| `UI-A11Y-002` Text and Edit roles | **Cannot be met.** No accessibility tree; the public header contains no accessibility API (verified by search of `imgui.h`, 1.93.0) | `N/A (TOOLKIT)` — never PASS |
| `UI-A11Y-003` survive text scale 2.25× | The Windows `TextScaleFactor` is not read; ImGui has its own global scale the application may expose | Applies in the form of `UI-IMGUI-011` |
| `UI-A11Y-004` equivalent for text in graphics | No consumer for an accessible name exists | `N/A (TOOLKIT)`; the copyability half survives as `UI-IMGUI-018` |
| `UI-ICON-002` accessible name + tooltip | Name half cannot be met; tooltip half can | Name: `N/A (TOOLKIT)`. Tooltip: `UI-IMGUI-012` makes it MUST |
| `UI-ICON-003` Segoe Fluent Icons | Achievable by merging the icon font (`IMGUI-FONTS`, Using Icon Fonts) | Applies; verify the font is present on every supported Windows version |
| `UI-TYPO-001` type ramp in epx | ImGui sizes are pixels: `GetFontSize() == FontSizeBase * (FontScaleMain * FontScaleDpi * …)` | Applies in the form of `UI-IMGUI-009`: the ramp as multiples of the base size |
| `UI-TYPO-002` legibility floor | Applies unchanged, at every scale | See `UI-IMGUI-010` |
| `UI-TYPO-003` Semibold, no italic | ImGui does not synthesise weights; each weight is a separate font input | Applies; a project that wants Semibold loads it |
| `UI-TYPO-007` one family, Segoe UI Variable | The font documentation read does not mention variable-font axes | Applies as "one family"; the variable axes are unverified in this toolkit |
| `UI-COLOR-001` 4.5:1 | Applies unchanged; the built-in styles are not measured palettes | See `UI-IMGUI-013` |
| `UI-COLOR-002` both themes | The toolkit does not read the OS theme | Applies; `UI-IMGUI-013` |
| `UI-COLOR-005` semantic roles | The style palette is a role palette with no error/warning/success roles | Applies; `UI-IMGUI-014` |
| `UI-KBD-002` tab order | Tab order is submission order | Applies; `UI-IMGUI-004` |
| `UI-KBD-004`, `UI-DLG-004` Escape and Enter | Non-modal popups close on Escape; **modals do not** | Applies; `UI-IMGUI-006` |
| `UI-SEL-001` focus visible | The navigation cursor hides itself when the mouse is used | Applies; `UI-IMGUI-003` |
| `UI-FB-005` background work does not freeze | In immediate mode a blocked frame freezes *everything* | Applies with more force; `UI-IMGUI-007` |
| `UI-ARCH-002` persist workspace state | Built in (`imgui.ini`), but relative to the working directory by default | Applies; `UI-IMGUI-015` |
| `UI-NAV-002` spatial stability | Windows move when dragged by their body, by default | Applies; `UI-IMGUI-016` |
| `UI-KBD-005` shortcuts shown in place | Menu items display a shortcut string that is **not processed** | Applies; `UI-IMGUI-017` |

`N/A (TOOLKIT)` is a reporting class the contract defines (§5): the rule is
neither passed nor derogated; it is recorded in the profile under *Known
non-conformance* with this module as the reason. The contract's bar on
derogating accessibility MUSTs is not relaxed: an ImGui project is
non-conformant on `UI-A11Y-002` and says so.

---

## B. Input

### UI-IMGUI-001 — Declare the toolkit and what it cannot do
**Level:** MUST **Authority:** Tier 1 (toolkit) **Confidence:** HIGH
**Provenance:** SOURCE RULE

A profile that enables this module MUST name the Dear ImGui branch and version
in use, and MUST list `UI-A11Y-002` and the name half of `UI-A11Y-004` and
`UI-ICON-002` under *Known non-conformance*, citing this module.

**Rationale.** The toolkit states that *"accessibility features are not
supported"* (`IMGUI-README`). A review cannot pass a rule the toolkit cannot
implement, and a profile that omits the fact invites a reviewer to invent a
pass. The contract requires non-conformance to be visible, not silent.

**Sources.** `IMGUI-README` (The Pitch); `UI_ORACLE_CONTRACT.md` §5, §6.

**Review test.** Open the profile. Is the version stated? Are the three
toolkit-limited rules listed as known non-conformance?

---

### UI-IMGUI-002 — Keyboard navigation is enabled
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE

An ImGui product MUST set `ImGuiConfigFlags_NavEnableKeyboard`, and MUST NOT
set `ImGuiWindowFlags_NoNavInputs` or `ImGuiItemFlags_NoNav` on a working
surface or an item the user must reach.

**Rationale.** The flag is described as the *"Master keyboard navigation
enable flag. Enable full Tabbing + directional arrows + Space/Enter to
activate"*, with the header noting that basic tabbing and Ctrl+Tab work even without it
(`IMGUI-H`, `ImGuiConfigFlags_`). Without it the
controls guide's keyboard section — arrows to move through items, Enter and
Space to activate, Escape to leave, Menu or Shift+F10 for the context menu,
Ctrl+Tab then Ctrl+Arrows to move a window — does not exist (`IMGUI-CPP`,
Controls guide). The Getting Started examples set it in every backend
combination. `UI-KBD-001` and `UI-A11Y-001` require it; the toolkit leaves it
off.

**Sources.** `IMGUI-H` (`ImGuiConfigFlags_NavEnableKeyboard`,
`ImGuiWindowFlags_NoNavInputs`, `ImGuiItemFlags_NoNav`); `IMGUI-CPP`
(Controls guide, Keyboard controls); `IMGUI-WIKI` Getting Started
(initialisation in every example); `IMGUI-FAQ` (How can I enable keyboard or
gamepad controls?). Core `UI-KBD-001`, `UI-A11Y-001`.

**Review test.** Search the initialisation for the flag. Then unplug the
mouse and complete the primary loop.

---

### UI-IMGUI-003 — The navigation cursor stays visible and distinct
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

`io.ConfigNavCursorVisibleAuto` MUST remain enabled (its default) or
`io.ConfigNavCursorVisibleAlways` be set; `ImGuiCol_NavCursor` MUST meet the
contrast floor against every background it is drawn over, and MUST be
distinguishable from the hovered, active and selected treatments
(`ImGuiCol_FrameBgHovered`, `ImGuiCol_FrameBgActive`, `ImGuiCol_Header`).

**Rationale.** By default *"Using directional navigation key makes the cursor
visible. Mouse click hides the cursor"* (`IMGUI-H`, `ConfigNavCursorVisibleAuto`),
so keyboard focus is shown exactly when the keyboard is the active input —
which satisfies `UI-SEL-001` only if the cursor colour is legible and unlike
the other states. `ImGuiCol_NavCursor` is *"Color of keyboard/gamepad
navigation cursor/rectangle, when visible"*; the style enumerates the hover,
active and header colours separately, which is what makes distinctness
achievable and therefore required. Pressing Escape may clear the focused item
(`ConfigNavEscapeClearFocusItem`, default true), which is the core's Escape
semantics.

**Sources.** `IMGUI-H` (`ConfigNavCursorVisibleAuto`,
`ConfigNavCursorVisibleAlways`, `ConfigNavEscapeClearFocusItem`,
`ImGuiCol_NavCursor`, `ImGuiCol_FrameBgHovered`, `ImGuiCol_FrameBgActive`,
`ImGuiCol_Header`). Core `UI-SEL-001`, `UI-COLOR-001`, `UI-COLOR-003`.

**Review test.** Tab through both themes. Is the cursor visible on every item,
and can you tell it from a hovered item and from a selected one? Grey the
screenshot: still?

---

### UI-IMGUI-004 — Submission order is tab order, so submit in reading order
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 1 **Confidence:** HIGH
**Provenance:** DERIVED RULE

Items MUST be submitted in the order the eye reads them. Where layout
primitives (`SameLine`, columns, tables) put an item somewhere other than
where the code order suggests, the code order MUST be arranged so that Tab
still follows the visible order.

**Rationale.** The toolkit keeps no widget tree: *"UI library stores minimal
amounts of data. At one point in time, it typically doesn't know or remember
which other widgets are displayed and which widgets are coming next"*
(`IMGUI-FAQ`, difference from traditional toolkits). Tab therefore visits
items in the order the frame submitted them; there is no tab-index to correct
it afterwards. `UI-KBD-002` requires tab order to follow visual order, so the
only lever is submission order.

**Sources.** `IMGUI-FAQ` (What is the difference between Dear ImGui and
traditional UI toolkits?); `IMGUI-CPP` (Read first: "Your code creates the UI
every frame"). Core `UI-KBD-002`.

**Review test.** Tab across a row built with `SameLine` and down a table. Does
focus move the way the layout reads?

---

### UI-IMGUI-005 — Every interactive item has a unique, stable ID
**Level:** MUST **Authority:** Tier 1 (toolkit) **Confidence:** HIGH
**Provenance:** SOURCE RULE

No two interactive items in the same scope MAY share an ID. Items generated in
loops MUST be wrapped in `PushID`/`PopID`; same-label items MUST carry a
`##suffix`; an item whose visible label changes while it should keep its
state MUST use `###id`. `io.ConfigDebugHighlightIdConflicts` MUST stay enabled
in development builds.

**Rationale.** In the toolkit's own capitals: *"USING THE SAME LABEL+ID IS THE
MOST COMMON USER MISTAKE! USING AN EMPTY LABEL IS THE SAME AS USING THE SAME
LABEL AS YOUR PARENT WIDGET!"* The consequence is a UI defect the operator
sees: *"Interacting with either button will trigger the first one"*
(`IMGUI-FAQ`, About the ID Stack system). The header's remedy list is the
rule's text: *"Code should use PushID()/PopID() in loops, or append "##xx" to
same-label identifiers … Empty label e.g. Button("") == same ID as parent
widget/node."* (`IMGUI-H`, `ConfigDebugHighlightIdConflicts`.) The `###` form matters for `UI-NAV-002`: the FAQ states that using the same
ID keeps associated state, such as whether the widget is focused, when the
label changes — a button that toggles between *Enable* and *Disable* otherwise
drops keyboard focus every time it is pressed.

**Sources.** `IMGUI-FAQ` (About the ID Stack system; How can I make a label
dynamic?); `IMGUI-H` (`ConfigDebugHighlightIdConflicts`,
`ImGuiItemFlags_AllowDuplicateId`). Core `UI-GLOBAL-005`, `UI-NAV-002`.

**Review test.** Run a development build through every screen with the
conflict highlighter on. Any popup is a FAIL. Then press a button whose label
changes: does focus stay on it?

---

### UI-IMGUI-006 — A modal defines Enter and Escape itself
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 3 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Every `BeginPopupModal` MUST handle Escape as cancel and Enter as its default
action, and MUST give its default item focus on appearance
(`SetItemDefaultFocus`). A modal whose default action is destructive MUST NOT
bind it to Enter (`UI-DLG-005`).

**Rationale.** The toolkit closes only non-modal popups on Escape: *"If not
modal: they can be closed by clicking anywhere outside them, or by pressing
Escape"*, whereas `BeginPopupModal` will *"block every interaction behind the
window, cannot be closed by user"* (`IMGUI-H`, Popups, Modals). Nothing
defines Enter. Core `UI-DLG-004` requires both to be defined and Escape never
to commit; in ImGui that is code the project writes, or it is absent.
`SetItemDefaultFocus` exists to *"make last item the default focused item of a
newly appearing window"*.

**Sources.** `IMGUI-H` (Popups, Modals; `BeginPopupModal`;
`SetItemDefaultFocus`; `Shortcut`). Core `UI-DLG-004`, `UI-DLG-005`,
`UI-KBD-004`, `UI-EDIT-003`.

**Review test.** Open every modal. Press Escape: does it close without
applying? Press Enter: does the stated default run, and is it non-destructive?

---

### UI-IMGUI-007 — Nothing slower than a frame runs in the frame
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 2 **Confidence:** HIGH
**Provenance:** DERIVED RULE

Work that can take longer than one frame — I/O, network, recognition, search,
compilation — MUST run off the UI thread and be polled by the frame. Worker
threads MUST NOT call into the ImGui context. Results MUST be handed back as
data the next frame reads.

**Rationale.** *"Your code creates the UI every frame of your application
loop, if your code doesn't run the UI is gone!"* (`IMGUI-CPP`, Read first).
There is no separate message pump to keep the window painting: a blocking call
inside the frame freezes every window, every animation and every cancel
button at once, which fails `UI-FB-005` totally rather than partially and
makes `UI-FB-004`'s cancel unreachable. On threads: *"A same Dear ImGui
context may be not used from multiple threads in parallel"* (`IMGUI-FAQ`,
About Multi-Threading). The toolkit's own performance goal — *"A typical idle
frame should never call malloc/free"* — sets the scale of what a frame is for.

**Sources.** `IMGUI-CPP` (Read first; How a simple application may look
like); `IMGUI-FAQ` (About Multi-Threading). Core `UI-FB-001`, `UI-FB-004`,
`UI-FB-005`.

**Review test.** Start the slowest operation. Does the busy indicator animate
and does the cancel button respond while it runs? Grep worker code for
`ImGui::`.

---

### UI-IMGUI-008 — An idle tool does not redraw continuously
**Level:** SHOULD **Authority:** Tier 1 (toolkit) + Tier 2 **Confidence:** MEDIUM
**Provenance:** DERIVED RULE

A sovereign ImGui tool SHOULD wait for input or a timer when nothing is
changing, rather than rendering at display rate while idle.

**Rationale.** The toolkit assumes a game loop: applications *"are expected to
update continuously at interactive framerates (e.g. 60 FPS)"*, and *"going
idle, using variable frame rates … are technically possible but currently not
well supported by default"* (`IMGUI-WIKI`, Getting Started). A desktop tool
inhabited all day (`UI-ARCH-001`) that spins at full rate while the operator
reads is doing work with no user-visible effect. No source in the corpus
quantifies the cost, which is why this is SHOULD and MEDIUM; the rule rests on
the toolkit's own statement that continuous update is a default, not a
requirement.

**Exceptions.** Surfaces that are genuinely animating (a live plot, a
playing preview), and hosts whose own rendering already runs continuously.

**Sources.** `IMGUI-WIKI` Getting Started (What is a Game Loop?). Core
`UI-ARCH-001`.

**Review test.** Leave the tool idle with a process monitor open. Is it
consuming as if it were busy?

---

## C. Text, scale and colour

### UI-IMGUI-009 — DPI is declared, and sizes are multiples of the font size
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE

The process MUST declare DPI awareness to Windows. Fonts MUST be scaled through
`style.FontScaleDpi` and style metrics through `style.ScaleAllSizes`. Sizes
and positions in UI code MUST NOT be hard-coded pixel constants; they are
expressed as multiples of `GetFontSize()` or `GetFrameHeight()`. The type ramp
(`UI-TYPO-001`) is therefore declared as multiples of `style.FontSizeBase`
and applied with `PushFont(nullptr, size)`.

**Rationale.** *"On Windows, you need to inform Windows that your application
is DPI aware! If this is not done, Windows will scale the application window
and the UI text will be blurry"* — via the Win32 backend's
`ImGui_ImplWin32_EnableDpiAwareness()` or an application manifest
(`IMGUI-FAQ`, How should I handle DPI?). The scaling model is stated in the
header: *"ImGui::GetFontSize() == FontSizeBase * (FontScaleMain * FontScaleDpi
* other_scaling_factors)"* (`IMGUI-H`, `ImGuiStyle`). And the FAQ's
instruction is the rule's last clause: *"Your UI code should avoid using
hardcoded constants for size and positioning. Prefer to express values as
multiple of reference values such as ImGui::GetFontSize() or
ImGui::GetFrameHeight()."* The FAQ also warns that style scaling *"is still
massively work in progress"* and that `ScaleAllSizes` should be called once;
a project that changes scale at runtime resets the style first.

**Sources.** `IMGUI-FAQ` (How should I handle DPI in my application?);
`IMGUI-FONTS` (same heading; Dynamic Fonts system in 1.92); `IMGUI-H`
(`ImGuiStyle` font scaling; `ScaleAllSizes`). Core `UI-TYPO-001`,
`UI-A11Y-003`.

**Review test.** Run at 100% and 200% display scale on Windows. Is text sharp
and is every padding scaled? Grep UI code for numeric literals passed as
sizes.

---

### UI-IMGUI-010 — Ship a scalable font that clears the floor at every scale
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A product MUST load a scalable TTF/OTF font and MUST NOT ship the embedded
bitmap default. The smallest size the ramp produces, after `FontScaleMain`
and `FontScaleDpi`, MUST satisfy `UI-TYPO-002`.

**Rationale.** The embedded default is *"ProggyClean.ttf … a 13 pixels high,
pixel-perfect font used by default. ProggyClean does not scale very nicely"*
(`IMGUI-FONTS`). The toolkit's own examples *"are unable to load a custom
font from the file-system, so they look ugly"* (`IMGUI-FAQ`, DPI). Since 1.92
*"fonts may be dynamically used at any size"*; nothing prevents a project
from meeting the platform floor, so the floor applies. Small sizes rasterised
with stb_truetype *"may appear a little blurry or hard to read"*; the fonts
document offers `imgui_freetype` with auto-hinting, which *"makes a big
difference especially at smaller resolutions"*.

**Sources.** `IMGUI-FONTS` (Dear ImGui: Using Fonts; Using FreeType
Rasterizer); `IMGUI-FAQ` (How can I load a different font than the default?).
Core `UI-TYPO-002`.

**Review test.** Which font file does the build load? What is the smallest
rendered size at the lowest supported scale? Is it at or above 12 px Regular
or 14 px Semibold?

---

### UI-IMGUI-011 — The operator can scale text, and the layout survives 2.25×
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE (ImGui form of `UI-A11Y-003`)

A product MUST expose a text-scale setting to the operator (through
`style.FontScaleMain`), persist it, and remain usable — nothing clipped,
every command reachable — with the scale at 2.25.

**Rationale.** Windows' own text-scale setting is not read by the toolkit, so
the platform's range cannot arrive by itself; but the mechanism exists:
`FontScaleMain` is the *"Main global scale factor. May be set by application
once, or exposed to end-user"* (`IMGUI-H`, `ImGuiStyle`). The number is the
platform's — `TextScaleFactor` is *"a double in the range [1,2.25]"*
(`corpus/platform/ms-accessible-text-requirements.md`) — and the oracle keeps
it rather than inventing another. `io.FontAllowUserScaling` (Ctrl+Wheel per
window) is a convenience, not a substitute for a persisted setting.

**Sources.** `IMGUI-H` (`ImGuiStyle::FontScaleMain`, `FontAllowUserScaling`);
`MS-A11Y-TEXT` (text scale range). Core `UI-A11Y-003`, `UI-LAY-004`.

**Review test.** Set the scale to 2.25 at the minimum window size. Is every
command still reachable? Restart: is the scale remembered?

---

### UI-IMGUI-012 — An icon-only control has a tooltip, and it works from the keyboard
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE (tightens `UI-ICON-002`)

Every icon-only control MUST have a text tooltip set with `SetItemTooltip`
(or the `IsItemHovered(ImGuiHoveredFlags_ForTooltip)` idiom), so that it
appears both for a stationary pointer and for keyboard navigation.

**Rationale.** With no accessible name possible, the tooltip is the only name
the control has; the core's SHOULD becomes MUST. The toolkit provides the
right idiom: `ImGuiHoveredFlags_ForTooltip` selects
`style.HoverFlagsForTooltipMouse` or `style.HoverFlagsForTooltipNav`
*"depending on active input type"*, and the mouse default is *"Stationary |
DelayShort"* — so the tooltip appears when the pointer rests, not on every
pass, and appears for the navigation cursor too (`IMGUI-H`, Tooltips). The
same flags default to `AllowWhenDisabled`, which is what lets a disabled
command explain itself (`UI-CMD-006`).

**Sources.** `IMGUI-H` (Tooltips; `ImGuiHoveredFlags_ForTooltip`;
`HoverFlagsForTooltipMouse`, `HoverFlagsForTooltipNav`;
`ImGuiHoveredFlags_AllowWhenDisabled`). Core `UI-ICON-002`, `UI-MOUSE-003`,
`UI-CMD-006`.

**Review test.** Navigate to each icon button with the keyboard. Does its
tooltip appear? Hover a disabled one: does it say why?

---

### UI-IMGUI-013 — Both themes are designed palettes, and the OS theme is followed
**Level:** MUST (designed) / SHOULD (followed) **Authority:** Tier 1 + Tier 1 (toolkit) **Confidence:** HIGH / MEDIUM
**Provenance:** SOURCE RULE + DERIVED RULE

A product MUST ship a light and a dark palette that each pass `UI-COLOR-001`,
and MUST NOT treat `StyleColorsDark`/`StyleColorsLight` as those palettes
without measuring them. It SHOULD select the palette from the Windows app
theme at start and when the setting changes.

**Rationale.** The built-in styles are starting points, described in the
header as *"new, recommended style (default)"* and, for light, *"best used
with borders and a custom, thicker font"* — a hint that legibility was not
guaranteed as shipped (`IMGUI-H`, Styles). Nothing in the documentation read
reads the operating-system theme, so following it is the project's code; the
core requires both themes to exist and be checked (`UI-COLOR-002`), and the
platform source says Windows defaults to the user's preference. Following
the OS is SHOULD and MEDIUM because no toolkit source describes a mechanism.

**Sources.** `IMGUI-H` (`StyleColorsDark`, `StyleColorsLight`, `ImGuiCol_`);
`corpus/platform/ms-color.md`. Core `UI-COLOR-001`, `UI-COLOR-002`.

**Review test.** Measure the lowest-contrast text in each palette. Switch the
Windows theme while the tool runs: does it follow, or is there at least a
setting?

---

### UI-IMGUI-014 — Semantic colours are roles, not literals
**Level:** SHOULD **Authority:** Tier 2 + Tier 1 (toolkit) **Confidence:** HIGH
**Provenance:** SOURCE RULE (ImGui form of `UI-COLOR-005`)

Error, warning, success, selection-in-content and confidence colours SHOULD be
defined once per palette beside the `ImGuiCol_` roles, and call sites SHOULD
NOT pass `IM_COL32(...)` or `ImVec4` literals for them.

**Rationale.** The style is already a role palette — `ImGuiCol_Text`,
`ImGuiCol_TextDisabled`, `ImGuiCol_FrameBg`, `ImGuiCol_NavCursor` and so on
(`IMGUI-H`, `ImGuiCol_`) — but it has no role for a semantic state, so
projects reach for literals, and a literal cannot switch with the theme or be
audited for contrast. `UI-COLOR-005` requires the roles to exist; this says
where they live in ImGui. `UI-COLOR-003` still applies: no state is colour
alone.

**Sources.** `IMGUI-H` (`ImGuiCol_` enumeration; `PushStyleColor`). Core
`UI-COLOR-003`, `UI-COLOR-005`.

**Review test.** Grep for `IM_COL32` and `ImVec4(` in UI code. Each hit: is
it a role, or a literal?

---

## D. Windows, layout and persistence

### UI-IMGUI-015 — Settings live in a per-user path, and the workspace has a default layout
**Level:** MUST (path) / SHOULD (layout) **Authority:** Tier 1 (toolkit) + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE + DERIVED RULE

`io.IniFilename` MUST point at a per-user, per-application path — never the
default relative name. A docked workspace SHOULD ship a default layout so the
first launch is the designed arrangement, not an empty dockspace and floating
windows.

**Rationale.** The header warns: *"default "imgui.ini" is relative to current
working dir!"* (`IMGUI-H`, `IniFilename`), and the fonts document records how
often the working directory is not what a developer assumed. A settings file
that lands wherever the shell happened to be is a workspace that forgets
itself, which is what `UI-ARCH-002` exists to prevent. On layout: docking
persists in the settings file, and for a programmatic default the wiki says
*"there is no great API for this yet"* and offers two routes — the
`DockBuilder` API in `imgui_internal.h` or *"manually create desired
settings, save them using SaveIniSettingsXXX() … and call
LoadIniSettingsXXX()"* (`IMGUI-WIKI`, Docking). Either satisfies the rule;
neither happens by itself.

**Sources.** `IMGUI-H` (`IniFilename`, `WantSaveIniSettings`,
`LoadIniSettingsFromDisk`); `IMGUI-WIKI` Docking (Programmatically setting up
docking layout); `IMGUI-FONTS` (About Filenames). Core `UI-ARCH-002`,
`UI-LAY-004`, `UI-ARCH-001`.

**Review test.** Where is the settings file written? Launch from a different
directory: same layout? Delete it and launch: is the result the designed
workspace?

---

### UI-IMGUI-016 — Windows do not move when the operator drags their contents
**Level:** SHOULD **Authority:** Tier 1 (toolkit) + Tier 2 **Confidence:** MEDIUM
**Provenance:** DERIVED RULE

In a product, `io.ConfigWindowsMoveFromTitleBarOnly` SHOULD be set, or every
working window SHOULD be docked so that it cannot be dragged away by a slip.

**Rationale.** By default *"Drag on any empty space: Move window (unless
io.ConfigWindowsMoveFromTitleBarOnly = true)"* (`IMGUI-CPP`, Controls guide).
In a debug overlay that is convenient; in a sovereign workspace where the
operator drags to select, scrub or pan, a drag that starts a pixel off the
target relocates the pane — a capture slip (Johnson Ch. 15) that also breaks
`UI-NAV-002`. MEDIUM because the toolkit documents the option without
recommending either setting; the design reasoning is the core's.

**Sources.** `IMGUI-CPP` (Controls guide, Mouse controls); `IMGUI-H`
(`ConfigWindowsMoveFromTitleBarOnly`); `IMGUI-WIKI` Docking. Core
`UI-NAV-002`, `UI-ERR-002`.

**Review test.** Drag from an empty spot inside a pane. Did the pane move?

---

### UI-IMGUI-017 — A displayed shortcut is a bound shortcut
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Every shortcut string shown beside a `MenuItem` MUST correspond to a key chord
the application actually handles, and every handled chord that has a menu
item MUST be shown there.

**Rationale.** The header is explicit: *"MenuItem() keyboard shortcuts are
displayed as a convenience but _not processed_ by Dear ImGui at the moment"*
(`IMGUI-H`, Widgets: Menus). The toolkit offers `Shortcut()` and
`SetNextItemShortcut()` with routing flags for the binding itself. A label
that promises Ctrl+S and does nothing violates `UI-GLOBAL-005` — the state
of the system is misreported — and `UI-KBD-005`, whose whole value is that
the annotation teaches a working path.

**Sources.** `IMGUI-H` (Widgets: Menus; Inputs Utilities: Shortcut Testing &
Routing; `Shortcut`, `SetNextItemShortcut`). Core `UI-KBD-005`,
`UI-GLOBAL-005`, `UI-GLOBAL-003`.

**Review test.** For each menu item with a shortcut label, press it with the
menu closed. Does it run?

---

### UI-IMGUI-018 — Text the operator may need to take away is copyable
**Level:** SHOULD **Authority:** Tier 1 (toolkit) + Tier 3 **Confidence:** HIGH
**Provenance:** DERIVED RULE

Values the operator may need to paste elsewhere — an error's folded detail,
an identifier, a path, a log line, a measured number — SHOULD be presented in
a selectable control (an `InputText` with `ImGuiInputTextFlags_ReadOnly`) or
carry a copy command. Plain `Text()` SHOULD NOT be the only form of such
values.

**Rationale.** `Text()` output cannot be selected; the toolkit's whole-window
copy is marked experimental, with *"text output is in submission order rather
than spatial order"* (`IMGUI-H`, `ConfigWindowsCopyContentsWithCtrlC`). The
read-only input flag exists for exactly this. The writing module keeps the
transport's own words behind a disclosure so they can reach a bug report
(`UI-TEXT-008`, `UI-TEXT-011`); words that cannot be copied do not reach it.
This is also what remains of `UI-A11Y-004` in a toolkit without an
accessibility tree: the information is at least not trapped in pixels.

**Sources.** `IMGUI-H` (`ImGuiInputTextFlags_ReadOnly`,
`ConfigWindowsCopyContentsWithCtrlC`). Core `UI-A11Y-004`; module `writing`
`UI-TEXT-008`, `UI-TEXT-011`.

**Review test.** Trigger an error with a detail section. Can you get the
detail onto the clipboard without retyping it?

---

## E. Hosting and input dispatch

### UI-IMGUI-019 — Input goes to ImGui or to the host, decided by the capture flags
**Level:** MUST **Authority:** Tier 1 (toolkit) + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

An application that has its own input handling beside ImGui MUST forward
every input event to ImGui and MUST consult `io.WantCaptureMouse`,
`io.WantCaptureKeyboard` and `io.WantTextInput` before acting on the event
itself. Application hotkeys MUST NOT fire while a text field has focus.

**Rationale.** The FAQ's instruction and its reason: *"you should always pass
your mouse/keyboard inputs to Dear ImGui, regardless of the value
io.WantCaptureMouse/io.WantCaptureKeyboard"*, and *"When io.WantCaptureKeyboard
is set, you need to discard/hide the keyboard inputs from your underlying
application"* (`IMGUI-FAQ`, How can I tell whether to dispatch…). It adds that
the flag *"is more correct that any manual attempt to "check if the mouse is
hovering a window" (don't do that!)"* because it handles drags and modal
blocking. The failure this prevents is a mode slip (`UI-MODE-001`): typing
into a field and having the letters execute commands.

**Sources.** `IMGUI-FAQ` (How can I tell whether to dispatch mouse/keyboard to
Dear ImGui or my application?); `IMGUI-WIKI` Getting Started (step 9);
`IMGUI-H` (`ConfigNavCaptureKeyboard`). Core `UI-MODE-001`, `UI-ERR-002`.

**Review test.** Focus a text field and type the letters of every application
hotkey. Did anything but text happen?

---

### UI-IMGUI-020 — Non-Latin scripts are loaded, encoded and composed correctly
**Level:** MUST (when the profile lists such a script) **Authority:** Tier 1 (toolkit) **Confidence:** HIGH
**Provenance:** SOURCE RULE

Where the profile's platform table lists a script beyond basic Latin, the
loaded fonts MUST cover it (a merged font input where one file does not),
every string MUST reach the toolkit as UTF-8, and on Windows the IME position
MUST be provided by writing the window handle to
`GetMainViewport()->PlatformHandleRaw`.

**Rationale.** *"All your strings need to use UTF-8 encoding … Specifying
literal in your source code using a local code page … will NOT work!"*; and
for composition: *"if your language is relying on an Input Method Editor
(IME), you can write your HWND to ImGui::GetMainViewport()->PlatformHandleRaw
… to set your Microsoft IME position correctly"* (`IMGUI-FAQ`, non-Latin
characters). Font merging is the documented way to add coverage
(`IMGUI-FONTS`, Fonts Loading Instructions); since 1.92 glyph ranges need not
be pre-declared, but a font that lacks the glyph still lacks it. The toolkit
states it does not do *"right-to-left text, bidirectional text, text
shaping"* (`IMGUI-README`); a profile listing such a script records that as
toolkit-limited under `UI-IMGUI-001`.

**Sources.** `IMGUI-FAQ` (How can I display and input non-Latin characters?);
`IMGUI-FONTS` (Fonts Loading Instructions; About UTF-8 Encoding; Debug
Tools); `IMGUI-README`. Core `UI-TYPO-002`, `UI-TYPO-007`.

**Review test.** Type in the script with the IME. Does the candidate window
sit at the caret? Run `DebugTextEncoding` on a sample literal.

---

### UI-IMGUI-021 — The toolkit's own diagnostics do not reach the operator
**Level:** SHOULD **Authority:** Tier 1 (toolkit) + Tier 3 **Confidence:** HIGH
**Provenance:** SOURCE RULE

In a build shipped to operators, recoverable-error tooltips and asserts from
the toolkit SHOULD be routed to the log rather than shown, while remaining on
for developer builds.

**Rationale.** The header distinguishes the seats: *"Programmer seats: keep
asserts (default), or disable asserts and keep error tooltips … Non-programmer
seats: maybe disable asserts, but make sure errors are resurfaced (tooltips,
visible log entries, use callback etc.)"*, and insists that recovery is never
silent (`IMGUI-H`, Error handling options). A tooltip about a missing `End()`
is the transport speaking (`AP-26`); the operator's message is written by the
project (`UI-TEXT-001`), and the toolkit's text goes where the writing module
puts transport text (`UI-TEXT-011`).

**Sources.** `IMGUI-H` (`ConfigErrorRecovery*`, Debug options). Module
`writing` `UI-TEXT-001`, `UI-TEXT-011`; core `UI-ERR-001`.

**Review test.** In the release configuration, force a recoverable error. What
does the operator see, and what does the log record?

---

## What this module deliberately does not say

- **Whether Dear ImGui is a fit for the product.** The toolkit's authors say
  who it is for; the oracle records that and applies the core anyway.
- **A control-metric scale.** Padding, rounding and spacing remain project
  values in the profile, expressed as multiples of the font size
  (`UI-IMGUI-009`); no source supplies numbers and the core's silence stands.
- **Touch.** `style.TouchPadding` exists and the FAQ recommends *"a mouse or
  gamepad to allow optimizing for screen real-estate and precision"*; the
  core's touch-secondary position is unchanged.
- **Multi-viewports.** The wiki documents the feature and its Linux/Wayland
  limits; the core's `UI-ARCH-004` governs when to use extra windows and this
  module adds nothing.
- **Variable-font axes, right-to-left and shaped scripts.** Not covered by the
  documentation read; a project that needs them records a gap, not a pass.

## Anti-patterns this module adds

See `UI_ANTIPATTERNS.md` AP-27 (the blocking frame) and AP-28 (the colliding
ID).
