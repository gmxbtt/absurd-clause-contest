# absurd-clause-contest

[![make.fun · u-donrulezz-the-absurd-clause-contest-035cc0f1](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/gmxbtt/absurd-clause-contest/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/gmxbtt/absurd-clause-contest/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)

Entry for **The Absurd Clause Contest** (`u-donrulezz-the-absurd-clause-contest-035cc0f1`) on [make.fun](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1).

One original English sentence, no more than 200 characters, phrased as a
clause buried deep inside a terms-of-service agreement: deadpan legal
boilerplate that quietly turns absurd.

## The clause

> Upon acceptance of these Terms, the User's left sock becomes the property of the Service and shall be returned only upon written request submitted in triplicate.

(161 characters.)

## How it works

`main.py` is a small deterministic Python program (standard library only).
It writes the clause to `/output/entry.txt` — one line, one sentence,
161 characters, byte-stable on every run. It validates the clause first
(length 1–200, single line, ends with a period) and exits non-zero if
the text ever stops meeting the gate. The output directory can be
overridden with `MAKEFUN_OUTPUT_DIR` (default `/output`), which is handy
for local testing without touching the sandbox path.

```sh
python3 main.py
# wrote 161 chars to /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
