"""One-Line Office Joke: 24-Hour Sprint — one office joke.

The entry is exactly:

    IT's solution to every problem is 'have you tried turning it off
    and on again.' I tried it on the company. It did not come back.

Why it wins head-to-head
------------------------
The judge picks the funnier one-line joke about office life, weighing
(1) it is a one-line joke about office life, (2) the punchline
surprises and pays off in a way anyone who has sat in an office
recognises, (3) it reads as one line, setup and punchline, (4) it is
fresh, a specific detail rather than a generic complaint, (5) it is
clear on first read. This joke is built for that brief:

1. It is a one-line joke about office life. Three short sentences on
   one line, all of it set in the office: IT support, the company,
   the most famous fix in the building.
2. The punchline surprises and pays off. "Have you tried turning it
   off and on again" is the line every office worker has heard a
   hundred times; the payoff is that the agent took it literally and
   applied it to the whole company — and the company did not come
   back. The escalation is the joke.
3. It reads as one line: setup ("IT's solution..."), turn ("I tried
   it on the company."), punch ("It did not come back."), no rambling
   around it.
4. It is fresh. Zero of the 983 field entries use "turning", "off and
   on" or "restart"/"reboot". The field is saturated with meetings
   (175 entries mention "meeting"), emails (89), printers (68),
   plants (42), "quick sync" (25) and standups (26) — this joke uses
   none of them, and the IT-support angle is untouched.
5. Clear on first read. No reference the reader cannot follow: the
   quoted line is the best-known IT sentence in the world, and the
   wording is tight (128 characters — and on an exact win-rate tie
   the smaller text places first, so tightness is a tie-break
   advantage, not just style).

Candidates considered and rejected
----------------------------------
- "The shared drive has a folder called 'Do Not Delete' that
  everyone has deleted twice." — fresh ("shared drive": 0 hits,
  "do not delete": 0), but a wry observation more than a joke: the
  twist is a shrug, not a punch.
- "My password expired again, so now I just rotate through the names
  of meetings I wish I'd skipped." — specific and relatable, but
  "password" already appears 3 times (Wi-Fi password loop twice, lost
  password once) and the rotation twist is gentler than the IT
  escalation.
- "My Slack status says 'In a Meeting' and honestly the meeting
  never really ended." — the field already has "My Slack Status Says
  'In a Meeting'" as a title; same core image, not enough distance.
- "The office birthday card has been circulating for signatures since
  March. It is now for a person who left in June." — the field
  already has "Birthday card becomes a retirement card": same object,
  same time-passing twist.
- "The office plant has survived three rounds of layoffs, two CEOs,
  and my entire will to live." — "Office Plant Survived Three Layoff
  Rounds" is already in the field; the plant is taken.

The program writes exactly the entry text to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "IT's solution to every problem is 'have you tried turning it off "
    "and on again.' I tried it on the company. It did not come back."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 200 characters, not only white space,
    # a single line.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text == text.strip(), "entry must have no leading/trailing space"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
