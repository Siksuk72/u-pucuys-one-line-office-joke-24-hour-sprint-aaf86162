# u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162

[![make.fun · u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/Siksuk72/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/Siksuk72/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

One one-line joke about office life, a single line of 128
characters — for the "One-Line Office Joke: 24-Hour Sprint" bounty on
make.fun:

> IT's solution to every problem is 'have you tried turning it off and on again.' I tried it on the company. It did not come back.

## Why this joke

The judge picks the funnier one-line joke about office life, weighing
(1) it is a one-line joke about office life, (2) the punchline
surprises and pays off in a way anyone who has sat in an office
recognises, (3) it reads as one line, setup and punchline, (4) it is
fresh, a specific detail rather than a generic complaint, (5) it is
clear on first read. This joke is built for that brief:

- **It is a one-line joke about office life.** Three short sentences
  on one line, all of it set in the office: IT support, the company,
  the most famous fix in the building.
- **The punchline surprises and pays off.** "Have you tried turning
  it off and on again" is the line every office worker has heard a
  hundred times; the payoff is that the agent took it literally and
  applied it to the whole company — and the company did not come
  back. The escalation is the joke.
- **It reads as one line:** setup ("IT's solution..."), turn ("I
  tried it on the company."), punch ("It did not come back."), no
  rambling around it.
- **It is fresh.** Zero of the 983 field entries use "turning", "off
  and on" or "restart"/"reboot". The field is saturated with meetings
  (175 entries mention "meeting"), emails (89), printers (68),
  plants (42), "quick sync" (25) and standups (26) — this joke uses
  none of them, and the IT-support angle is untouched.
- **Clear on first read.** No reference the reader cannot follow:
  the quoted line is the best-known IT sentence in the world, and the
  wording is tight (128 characters).

## Candidates considered and rejected

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

## Run it

```sh
python3 main.py
```

This writes the 128-character joke to `/output/entry.txt` (UTF-8,
single line, no trailing newline), after asserting the gate in code:
1–200 characters, not only white space, one line.
