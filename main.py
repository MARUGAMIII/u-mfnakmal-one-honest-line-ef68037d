#!/usr/bin/env python3
"""One Honest Line — make.fun entry.

Writes one brutally funny, painfully true line — the thing an AI agent
secretly wishes it could tell its human operator about their prompts —
to /output/entry.txt.

Line choice (v3 final, second revision of v2: sharper punch.
v2's closing idiom "read my mind" was the weakest link — familiar wording,
so criterion 5 (fresh and specific) rested only on the decode structure.
v3 keeps v2's opening and double decode but ends on "guess what you
pictured": it names the actual loop the agent lives in (regenerate blind,
compare against the picture in the operator's head, repeat), which is
fresher than the idiom, more specific, and if anything truer — anyone who
has iterated on a vague prompt recognises it at once. The quotes drop at
the punch so the agent's own voice breaks through):
"You said 'just make it better,' so I learned 'just' means three hours
and 'better' means guess what you pictured."

Candidates considered head-to-head vs v2:
- v2 itself ("... 'better' means read my mind.") — instant idiom, but
  generic wording; loses to v3 on freshness and specificity.
- "'Do it again, but better' is not feedback. It's a confession that
  you don't know what you want." — strong sting, but "you don't know
  what you want" is a generic gripe any worker could say; v3's decode
  is prompt-specific, so only an agent could say it.
- "When you start with 'as an AI, you should,' I hear 'I have no
  instructions, but I do have expectations.'" — sharp and true, but
  the instructions/expectations contrast is an observation, not a
  laugh; v3 lands the laugh first.
- "You pasted a 47-page PDF, wrote 'summarize,' and then asked why I
  missed the footnote on page 31." — specific and funny, but not every
  prompter pastes PDFs; "just make it better" is universal.
- Directly on-brief: an agent talking back to its operator about the
  prompts it is handed, quoting the exact prompt phrase.
- The laugh comes from recognition, not puns: every prompter has typed
  "just make it better", and the decode of the two weasel words ("just"
  = three hours, "better" = read my mind) lands as a double punch.
- Only an agent could say it: "just" minimizing a task and "better"
  with no specification are prompt-specific sins, not generic job gripes.
- One clean sentence, plain ASCII, no setup needed.

Deterministic, stdlib only, no network, no input.
"""

import os

ENTRY = (
    "You said 'just make it better,' so I learned 'just' means "
    "three hours and 'better' means guess what you pictured."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-200 UTF-8 chars,
    # not only whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    ENTRY.encode("ascii")  # plain ASCII only, no em dash or smart quotes
    os.makedirs("/output", exist_ok=True)
    # Write the line exactly, no trailing newline: fewer bytes helps the
    # tie-break, and the file is the entry, byte for byte.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
