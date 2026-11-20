# Stock Desk — daily book ingest runbook (Workflow A, 1–3 books a day)

Folder: the books folder on Cyrus's computer, reached with device_bash at
`"$HOME/mnt/stocks books "` (the name ends in a space; always quote it). Do all reading and
writing there with device_bash. Run every helper with `python3 -I` from that folder.

```
text/<Key>.md          converted books with [[Key p.N]] (PDF page) or [[Key loc.N]] (ebook segment) markers
text/catalog.json      converter stats per book
desk/playbook.md       THE RULES LEDGER (working copy — canonical during ingestion)
desk/library.md        the queue: Order, Day, Key, Words, Units, Last marker, Status, Date ingested, Rules added
desk/notes/<Key>.md    your running notes while reading a book (survive context compaction)
desk/runs/             one run report per book: <YYYY-MM-DD>-<Key>.md
desk/backups/          playbook/library copies taken before each write
tools/read_chunk.py    python3 -I tools/read_chunk.py <Key> <start_unit> 30000  → next chunk + "NEXT: n" or "END OF BOOK"
tools/check_playbook.py python3 -I tools/check_playbook.py --read <Key>=<last unit read> ...
```

## 0. Start
1. Today's date = the run date in America/Los_Angeles.
2. Read `desk/playbook.md` header, "Index by school", "Conflicts", "Principles" and "Ingest log" in full.
   The Rules section can be long: don't re-read all of it; grep it by keyword when merging (step 4).
3. Read `desk/library.md`. Pick today's books: the first row whose Status is `pending` or
   `partial (stopped …)`, then the next `pending` rows in Order while the day stays at ≤3 books and
   ≤120,000 words in total (a `partial` book counts only its unread words). Rows marked
   `blocked` or `deferred` are skipped. A single book over the budget is read up to the budget
   and marked partial; it is resumed first tomorrow.
4. If no row is pending or partial, the library is done: skip to FINISH and say so.

## Per book — A1 to A6. Finish one book completely (including its writes) before starting the next.

**A1 Read in order, never by search.** Start at unit 1 (or the unit after the `stopped` marker
for a partial book; its earlier notes are in `desk/notes/<Key>.md`). Loop:
`python3 -I tools/read_chunk.py <Key> <unit> 30000`, read the whole chunk, then APPEND to
`desk/notes/<Key>.md` (heredoc append, never rewrite) the candidate rules and principles from that
chunk with their unit numbers, the conditions attached to them, and any evidence the author gives
(sample, period, study, own trade, or nothing). Continue at `NEXT:` until `END OF BOOK`.
Validate: you reached `END OF BOOK`. If the day's word budget or your context forces a stop,
write `stopped <marker>` as the last line of the notes and mark the book partial.
Never fill a gap from memory or training knowledge of the book.

**A2 Rule or principle.** A RULE can be written IF <measurable condition> THEN <action> | EXIT
<condition> | INVALIDATED BY <condition>, and every input is observable — price, volume, a
financial-statement line, IV, a date — with a named data source (price history, 10-K/10-Q,
options chain, earnings calendar, 13F/Form 4…). Anything else ("cut losses short", "know what you
own") is a PRINCIPLE: one line in Principles with its cite. An input with no data source makes it
a principle.

**A3 Grade the book's support, not the idea.** A = the book reports a systematic test (defined
rules, sample size, period); B = cites outside studies or data, method not fully shown; C = the
author's own trades or case examples; D = assertion only. An author's win rate or return goes in
as "author claims X [BOOK Key p.N]", never as a probability. Support sitting on a
`[Numeric table omitted…]` page → add `check table p.N` and grade on the text you have.
Nothing is graded A or B without a cite to the page/loc that shows the sample, period or study.

**A4 Merge.** Before adding a rule, grep `desk/playbook.md` for its key terms and read the
candidate rule blocks. Same rule already there → add this book's cite to that rule's Sources
line (`agrees: [BOOK Key p.N]`); no duplicates. Contradiction (buy weakness vs buy strength;
hold through drawdowns vs fixed % stops) → keep both, add each to the other's Conflicts line,
add the pair to the Conflicts section, and name the condition that decides between them
(horizon, market regime, school). Never average two rules into one. Every rule gets exactly one
school: value | growth/momentum | swing-technical | day-trading | options-income |
options-directional | risk/sizing | process. Every new rule starts `Status: UNTESTED`.

**A5 Cut.** At most 20 new rules per book: keep the 20 with the best grade and clearest inputs;
list the rest by title in the run report. Paraphrase everything. At most one quote per rule,
≤25 words, only when the exact wording matters; never transcribe passages, tables or lists.

**A6 Write — edit in place, never retype the file.**
1. Back up: `cp desk/playbook.md desk/backups/playbook-<date>-<Key>.md` (same for library.md).
2. Preferred: put the book's new rules, merges, principles, conflicts and Ingest-log row in a batch
   JSON (desk/runs/batch-<date>-<Key>.json) and run `python3 -I tools/add_to_playbook.py <batch>`;
   it backs up the playbook, assigns IDs at write time and updates the index (format in the
   script's header). Otherwise: write the new rule blocks (schema in the playbook header, IDs from
   "Next rule ID" upward) to a temp file with a heredoc, then insert them with a short python
   read-modify-write: new blocks
   go at the end of the Rules section (replace `_(none yet)_` the first time); bump
   "Next rule ID"; add IDs under "Index by school" (`- <school>: R-001 short name, …`); add merged
   cites to existing Sources lines; add Conflicts pairs; add Principles lines; append one
   Ingest log row: `| <date> | <Key> | <units read>/<total> | <n new> | <n merged> | <n principles> | <flags> |`.
3. Update the book's row in `desk/library.md` with python: Status `done` or
   `partial (stopped <marker>)`, Date ingested, Rules added (`<new> new, <merged> merged`).
4. Validate: `python3 -I tools/check_playbook.py --read <Key>=<last unit read>`. It must print
   `"ok": true`. If not, fix the playbook (or restore the backup and redo the insert) until it
   does. Never leave a failing playbook.
5. Write the run report to `desk/runs/<date>-<Key>.md` (≤200 words): book; units read of total;
   rules added / merged / conflicted by school and grade; principles added; partial and table
   flags; the one rule from this book most worth testing first, and why.

## Mirror to the project (after all of today's books)
If the Projects tool is available in this session: stage `desk/playbook.md` and `desk/library.md`
(device_stage_files on `/Users/EXP/Desktop/stocks books /desk/...`), copy them into your working
directory, and `project_write` them to `claude/playbook.md` and `claude/library.md` with
`local_path`. If the tool is missing or a write fails, say "project copy not updated — the copy
in the books folder is current" in the report. Never claim a save that didn't succeed.

## Refresh the dashboard (after all of today's books)
Dashboard: https://claude.ai/artifact/Ri161Q5n4fg1zJsQ8e38vM (datasets `rules`, `principles`,
`library`, each an attached JSON file). Run `python3 -I tools/export_dashboard.py`, stage
`desk/dashboard/rules.json`, `principles.json` and `library.json`, copy them into your working
directory, and for each one: ArtifactData `get` collection "datasets", doc_id <name> (note its
`version` and `source.url`); Artifact publish with that url, `asset: true`, `file_path` = the file
(each JSON in its own call); ArtifactData `update` that dataset with
`{source: {kind: "file", url: <new /_blob url>, name: "<name>.json", format: "json"},
updated: {at: <UTC now>, by: "Claude (daily book ingest)"}, edit: {via: "claude", at: <UTC now>}}`
and `if_version`. Never delete the old file: Cyrus approves cleanups himself. List each superseded
file in the report (which dataset it fed, its upload time and size) so he can decide.
Never edit the dashboard's page (files/index.html). If the tools are missing, say "dashboard not
refreshed" in the report.

## Never
- Build, merge or grade a rule from memory, training knowledge or a page you didn't read today.
- Pull market data, name tickers, or make calls: this run builds the playbook only.
- Delete files (the folder doesn't allow it) or rewrite a file from tool output.
- Change an existing rule's Status (only Workflow D or a real test does that).

## FINISH
SendUserMessage (≤250 words): each book's title, units read of total, rules added/merged/
conflicted by school and grade, principles, flags, the rule most worth testing first; the
playbook's total rule count; tomorrow's book(s); whether the project copy was updated. If the
library is finished: say so, give the totals by school and grade, suggest pausing this
scheduled task, and say the next step is setting up the daily watchlist scan (Workflow B/C).
Then a one-line PushNotification (book + rule most worth testing). Your final reply repeats the message.
