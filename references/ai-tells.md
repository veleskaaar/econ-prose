# AI tells, filtered for the economics register

Merged from blader/humanizer (Wikipedia's "Signs of AI writing"), hardikpandya/stop-slop,
AIScientists-Dev/academic-humanizer, and Nanako0129/sepia's style and professional passes, keeping
only what applies to a formal economics paper and adding the register's own tells. One hit is not a
verdict. Count hits per paragraph; a cluster of three or more justifies a rewrite of that paragraph.
Patterns marked *weak alone* need company. Check `preserve.md` before flagging anything.

## A. Staging (sentences that signal instead of say)

**A1. Not X but Y.** "not X but Y", "not just/only/merely X, but Y", "it's not X, it's Y", "X rather
than Y" used as inflation, the split form "This does not mean X. It means Y." The negative half names
something no one claimed. State Y. Keep the frame only when X is a belief the reader holds and the
paper is correcting it (CD15: "this does not imply that decision makers are irrational").

**A2. One-line closers and dramatic fragments.** A one-sentence paragraph that restates the one
before; "That distinction matters."; "This is the key insight."; a sentence after an example that
names what it showed ("This shows the importance of..."). Cut the closer unless it adds a fact or a
consequence. A one-sentence paragraph that states a result is not this tell.

**A3. Sayings that sound deep.** "the real question is", "at its core", "fundamentally", "the heart
of the matter", "X is the currency of Y", "X becomes a trap". Replace with the specific claim.

**A4. Staged run-up.** "Let's dive in", "here's what you need to know", "it is worth pausing to
note", "Honestly,", "Look,". Delete the run-up. (The corpus's "Notice that" and "It is important to
notice at this point that" are not this tell when the sentence after them carries a fact.)

**A5. Arguing with no one.** "This is not to say", "To be clear", "One might be tempted to", "A
tempting approach would be", "Some might argue ... but". Remove the defense unless the objection is
one a referee would raise and the paper answers it in full; then attribute it ("A natural objection
is that ...; Section 5 shows that it does not apply because ...").

## B. Rhythm by rule

**B1. Forced triads.** Three parallel items where the meaning has two or four; three adjectives;
three short facts followed by a lesson. Keep three real things (three sources of uncertainty, three
assumptions). Flag only when the third pads.

**B2. Repeated sentence openings.** Three sentences in a row starting with the same subject ("The
agent ... The agent ... The agent ..."). Merge or vary. A deliberate anaphora ("First, ... Second,
... Third, ...") is not this tell.

**B3. Dashes everywhere.** Em dashes as the universal connector. Follow the document's policy; the
thesis uses none. Replace with a comma, colon, parentheses, or a period. Leave hyphens in compound
modifiers and in code, paths, labels.

**B4. Stacked qualifiers.** "could potentially", "might arguably", "it is also possible that", "in
some cases it may". Keep one calibrated hedge per uncertain claim. *Weak alone.*

**B5. Runs of same-length sentences.** Three or more adjacent sentences of about the same length.
Break the run by moving words, not adding them: split one long sentence, merge two short ones, or
cut a clause. Do not shorten everything.

**B6. Uniform paragraphs.** Every paragraph the same length and shape; every paragraph ending on a
punchy line. Vary by content, not by rule.

## C. Inflation and borrowed authority

**C1. Overused AI words.** delve, underscore (verb), highlight (verb, as a rider), tapestry,
landscape (abstract), realm, journey, testament, pivotal, crucial (filler), key (adjective, filler),
intricate/intricacies, meticulous, robust (figurative), seamless, vibrant, showcase, foster, harness,
navigate (figurative), leverage (verb, filler), interplay, enduring, garner, bolster, valuable,
enhance, additionally, notably, importantly (as a sentence adverb on every paragraph), quietly.
Technical uses stay (robust comparative statics; key lemma; leverage ratio).

**C2. Inflated significance.** "stands as a testament", "a pivotal moment", "plays a key role",
"marking a shift", "underscores its importance", "reflects a broader", "setting the stage for",
"paves the way for", "sheds light on", "of paramount importance", "bridges the gap", "opens new
avenues", "has the potential to revolutionize". Keep the fact, drop the significance.

**C3. Shallow -ing riders.** ", highlighting ...", ", underscoring ...", ", emphasizing ...",
", ensuring ...", ", reflecting ...", ", contributing to ...", ", showcasing ...". Delete the rider
or make it a sentence with a claim the paper supports.

**C4. Vague connection.** "associated with", "linked to", "tied to", "in connection with" when the
paper knows the relationship. Name it ("raises", "is necessary for", "is a special case of").

**C5. Copula avoidance.** "serves as", "stands as", "functions as", "represents" (for "is"),
"boasts", "features", "offers". Use "is", "are", "has".

**C6. Borrowed authority.** "experts argue", "it is widely accepted", "the literature suggests" with
no citation, "several studies" with no names. Cite the one or two papers that matter and say what
they found; otherwise cut.

**C7. Vague declaratives.** "The implications are significant." "The reasons are structural."
"This has important consequences." Name the implication, reason, or consequence.

## D. Formatting by rule

**D1. Bold as decoration.** Bold on every defined term after the first use; bold labels on every
list item. In LaTeX: `\emph{}` on first use of a defined term only; `\textbf{}` almost never in
prose.

**D2. Decorative headings.** Title Case in a document that uses sentence case; a heading written for
effect ("The decision, on one screen") instead of what the section holds. Section titles are edited
only when the user asks.

**D3. Heading repeated in the first sentence.** "## The agent's problem. We now study the agent's
problem." Cut the repeat.

**D4. Writing about the document instead of its subject.** "This section is organized as follows"
inside every subsection; "the table below compares" when the reader can see it. One roadmap at the
end of the introduction is convention; a roadmap in every section is this tell.

## E. Leftovers

**E1. Chatbot residue.** "Certainly", "I hope this helps", "Let me know", "Great question", "Here
is", "In this response". Delete outright.

**E2. Knowledge-limit disclaimers and guesses.** "as of my last update", "while specific details are
limited", "it is believed that" with no source, "likely" filling a gap in the record. State what the
paper does not show, or cut.

**E3. Drafting notes.** "[TODO]", "[citation needed]", "as discussed above" when nothing was
discussed, "see below" with nothing below. Resolve or flag to the author.

## F. Academic inflation (academic-humanizer, Layer 2, adapted)

**F1. Over-claiming verbs.** Theory *shows*, *characterizes*, *establishes*; experiments *find*,
*document*, *provide evidence*. Watch: prove (outside a proof), demonstrate (for empirical claims),
confirm, guarantee, "significantly" with no test. Match the verb to the evidence.

**F2. Significance hype.** See C2. Also "a first step toward", "an important step", "a crucial
ingredient", "fundamental" as filler.

**F3. Empty intensifiers.** "extensive", "comprehensive", "thorough", "a wide range of", "numerous",
"various", "rich". Replace with the count or the list.

**F4. Novelty padding.** "novel" more than once per section; "to the best of our knowledge"; "for
the first time"; "we are the first to". State what the paper does that the cited work does not.

**F5. Formulaic openers.** "In recent years, X has attracted increasing attention"; "With the rapid
development of"; "Despite recent advances"; "It is well known that" with no citation. Open with a
flat declarative (style-corpus §1.1).

**F6. Connective stacking.** Moreover / Furthermore / Additionally / In particular / Importantly /
Notably on consecutive sentences or paragraph openers. Let the logic carry; keep one connective
where the relation is not obvious.

**F7. Contribution-list cliches.** "(1) a novel model; (2) extensive analysis; (3) strong results".
Each item names a specific result with its condition ("for every uniformly posterior-separable
cost", "when the moral cost is strictly convex").

**F8. Citation dumping.** "[3, 7, 9, 12]" or a parenthetical list of eight papers after a general
claim. Cite the one or two that matter and say what they did (style-corpus §3.9).

**F9. Hedging by vagueness.** "somewhat", "relatively", "fairly", "to some extent", "quite",
"rather" with no comparison. Quantify, name the comparison, or cut.

**F10. Boilerplate emphasis.** "It is worth noting that", "It should be emphasized that", "It is
important to stress that", "Notably,", "Importantly," at the head of a sentence that would stand
without it. If it matters, the sentence shows it.

**F11. Overlong clause-stacked sentences.** Past about 35 words, or three or more subordinate
clauses chained with "which", "that", "while", "with". Split: one idea per sentence. Keep a long
sentence when its structure carries the logic (a condition and its consequence, a parallel list).

**F12. Nominalization.** "the determination of the threshold by the agent" for "the agent determines
the threshold"; "realization", "implementation", "utilization" as subjects. Turn back into verbs.
Standard nouns of the field stay (realization of a state; implementation in mechanism design).

**F13. Abstract-noun wrappers.** "a sense of", "the notion of" (when the notion is then defined,
fine; as filler, cut), "the presence of", "the fact that" (often deletable), "in terms of".

**F14. Elegant variation.** Cycling synonyms for one object (the agent / the employee / the worker /
the decision maker) within a section. One name per object, as the author's notation policy says.

## G. Quick scan order

1. E (leftovers): delete.
2. C1 and F5 (words and openers): replace.
3. A1, A2, C3, C5 (staging, riders, copula avoidance): rewrite the sentence.
4. F1 to F4, F6 to F10 (academic inflation): match verb to evidence, cut padding.
5. F11 to F14 (clause stacks, nominalizations, wrappers, variation): surgery.
6. B5 and B6 (rhythm): move words.
7. Then the voice pass from `style-corpus.md`, sparingly.
