# -*- coding: utf-8 -*-
"""Generate the oracle's figures as SVG, locally, with no external assets.

The oracle has to be usable by someone who has none of the source books, so
anything it relies on a diagram to say has to ship with it. SVG because it is
text: diffable, reviewable, and it scales with the reader's zoom.

Both figures use currentColor for ink so they stay legible in light and dark
themes, which is UI-COLOR-002 applied to the oracle's own artwork.
"""
import io
import os

# Standalone repo layout: figures sit beside the documents that use them.
# Run from the repository root.
OUT = 'img'
os.makedirs(OUT, exist_ok=True)

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
        'width="%d" height="%d" font-family="Segoe UI Variable, Segoe UI, sans-serif" '
        'fill="currentColor" role="img" aria-label="%s">\n'
        '<style>svg{color:#1a1a1a}'
        '@media (prefers-color-scheme:dark){svg{color:#e8e8e8}}'
        'text{font-size:13px}.h{font-size:15px;font-weight:600}'
        '.s{font-size:11px;opacity:.75}.box{fill:none;stroke:currentColor;'
        'stroke-width:1.25;opacity:.55}.ax{stroke:currentColor;stroke-width:1.25;'
        'opacity:.55}.tick{stroke:currentColor;stroke-width:1.25;opacity:.55}</style>\n')

# ── Figure 1: posture ────────────────────────────────────────────────────
w, h = 860, 330
f1 = [HEAD % (w, h, w, h, 'Sovereign and transient posture compared')]
f1.append('<text class="h" x="16" y="26">Posture decides density, labelling and control size</text>')
f1.append('<text class="s" x="16" y="46">UI-GLOBAL-001. Classify the surface before designing it.</text>')

cols = [
    (16, 'SOVEREIGN', 'Inhabited for hours. The user becomes expert.', [
        'Full screen, persistent, multi-pane',
        'Dense layout is legitimate',
        'Auxiliary controls may be small and close',
        'Colour in small accents, not large splashes',
        'Icon-only controls acceptable — seen daily',
        'Optimise for the intermediate, not first run',
    ]),
    (440, 'TRANSIENT', 'Invoked, used, dismissed. Never becomes familiar.', [
        'Appears on demand, leaves quickly',
        'Generous spacing is legitimate',
        'Controls large and clearly separated',
        'Labels in words, not ambiguous glyphs',
        'Every action spelled out',
        'Optimise for someone who has forgotten it',
    ]),
]
for x, title, sub, items in cols:
    f1.append('<rect class="box" x="%d" y="62" width="404" height="246" rx="6"/>' % x)
    f1.append('<text class="h" x="%d" y="88">%s</text>' % (x + 18, title))
    f1.append('<text class="s" x="%d" y="107">%s</text>' % (x + 18, sub))
    for i, it in enumerate(items):
        y = 134 + i * 27
        f1.append('<circle cx="%d" cy="%d" r="2.5" opacity=".55"/>' % (x + 22, y - 4))
        f1.append('<text x="%d" y="%d">%s</text>' % (x + 34, y, it))
f1.append('<text class="s" x="16" y="324">Applying either column to the other posture is the most '
          'common structural error this oracle catches.</text>')
f1.append('</svg>\n')
io.open(os.path.join(OUT, 'posture.svg'), 'w', encoding='utf-8').write('\n'.join(f1))

# ── Figure 2: response-time deadlines ────────────────────────────────────
w, h = 860, 300
f2 = [HEAD % (w, h, w, h, 'Human response-time deadlines on a logarithmic scale')]
f2.append('<text class="h" x="16" y="26">What the system owes the user, by elapsed time</text>')
f2.append('<text class="s" x="16" y="46">§14. Orders of magnitude, not precise thresholds.</text>')

y0 = 96
f2.append('<line class="ax" x1="60" y1="%d" x2="810" y2="%d"/>' % (y0, y0))
marks = [
    (60,  '0.1 s',  'Acknowledge', 'Anything slower breaks the sense that the click caused the result.'),
    (250, '~1 s',   'Stay conversational', 'A gap longer than a turn in conversation. Show the busy state.'),
    (440, '10 s',   'Attention leaves', 'Past the limit of held attention. Progress and an estimate, or the user must rebuild context.'),
    (700, '> 10 s', 'Give the work back', 'Determinate progress, a time estimate, a cancel, and an interactive UI meanwhile.'),
]
for x, label, head, note in marks:
    f2.append('<line class="tick" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x, y0 - 8, x, y0 + 8))
    f2.append('<text class="h" x="%d" y="%d">%s</text>' % (x, y0 - 18, label))
    f2.append('<text x="%d" y="%d">%s</text>' % (x, y0 + 32, head))
    # wrap the note by hand at ~46 chars
    words, line, lines = note.split(), '', []
    for wd in words:
        if len(line) + len(wd) + 1 > 46:
            lines.append(line); line = wd
        else:
            line = (line + ' ' + wd).strip()
    lines.append(line)
    for j, ln in enumerate(lines[:4]):
        f2.append('<text class="s" x="%d" y="%d">%s</text>' % (x, y0 + 52 + j * 16, ln))

f2.append('<text class="s" x="16" y="286">Derived from published durations of perceptual and cognitive '
          'processes; see Appendix A. Each deadline is roughly ten times the one before it.</text>')
f2.append('</svg>\n')
io.open(os.path.join(OUT, 'response-time.svg'), 'w', encoding='utf-8').write('\n'.join(f2))

for n in ('posture.svg', 'response-time.svg'):
    print('%-20s %6d bytes' % (n, os.path.getsize(os.path.join(OUT, n))))
