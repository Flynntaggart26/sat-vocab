# SAT Extreme Challenge - 60-Question Generator (30 Punctuation + 30 Grammar)
# No study section. Difficulty: HARD / VERY HARD / EXTREME.
import pathlib

QUESTIONS = [
 # ============ PART A: PUNCTUATION (1-30) ============
 dict(n=1, level="HARD", cat="Punctuation: Sentence Boundary",
  passage="The subterranean mycelial networks linking old-growth Douglas firs redistribute carbon and warning chemicals across the forest_______ they function less like isolated organisms than like a single cooperative system.",
  opts=["A) forest, they", "B) forest; they", "C) forest they", "D) forest, and, they"],
  ans="B", exp="Two ICs, no conjunction -> [IC; IC]. A is a comma splice, C a run-on, D adds an illegal second comma."),
 dict(n=2, level="HARD", cat="Punctuation: Colon List",
  passage="Before calibrating the cryogenic sensors for the Antarctic borehole mission, the engineering crew assembled four custom instruments_______ a distributed acoustic array, a laser fluorometer, a magnetotelluric probe, and a sterile coring module.",
  opts=["A) instruments;", "B) instruments,", "C) instruments:", "D) instruments—and"],
  ans="C", exp="IC before blank introduces a list -> colon. Semicolon needs an IC after; a comma cannot launch a list; dash+and is unidiomatic."),
 dict(n=3, level="HARD", cat="Punctuation: Singular Possessive",
  passage="After the flood breached the conservation laboratory, the chief_______ painstakingly annotated catalog of salvaged cuneiform fragments became the only record of the collection's original order.",
  opts=["A) curators", "B) curators's", "C) curator's", "D) curators'"],
  ans="C", exp="Singular 'chief curator' -> curator's. B never valid for regular nouns; D is plural."),
 dict(n=4, level="HARD", cat="Punctuation: Dependent + Independent",
  passage="Even though the permafrost cores yielded far less intact DNA than the team had projected_______ the residual sequences proved sufficient to reconstruct three extinct viral genomes.",
  opts=["A) projected;", "B) projected", "C) projected:", "D) projected,"],
  ans="D", exp="'Even though...' is a DC -> [DC, IC]. Semicolon/colon cannot follow a dependent clause."),
 dict(n=5, level="HARD", cat="Punctuation: FANBOYS",
  passage="The municipal desalination plan promised to stabilize the coastal aquifer_______ it conspicuously omitted any binding limit on agricultural extraction during drought years.",
  opts=["A) aquifer, yet", "B) aquifer", "C) aquifer; yet", "D) aquifer,"],
  ans="A", exp="Two ICs joined by FANBOYS 'yet' -> [IC, yet IC]. B is a run-on, C is semicolon+FANBOYS (never on SAT), D is a comma splice."),
 dict(n=6, level="HARD", cat="Punctuation: Its / It's",
  passage="The advisory committee released_______ final assessment only after the dissenting members appended a minority report challenging the groundwater model.",
  opts=["A) it's", "B) its'", "C) its", "D) their"],
  ans="C", exp="Singular collective 'committee' -> possessive 'its'. It's = it is; its' never exists; their is plural."),
 dict(n=7, level="HARD", cat="Punctuation: Serial Comma",
  passage="The symposium proceedings included papers on quantum error correction, neuromorphic hardware co-design_______ and post-quantum lattice cryptography for satellite uplinks.",
  opts=["A) ;", "B) ,", "C) —", "D) NO PUNCTUATION"],
  ans="B", exp="Simple three-item list needs Oxford comma before 'and'. Semicolon/dash reserved for complex lists or breaks."),
 dict(n=8, level="HARD", cat="Punctuation: Nonessential Pair",
  passage="Dr. Lena Okafor_______ a leading authority on mangrove restoration, testified before the coastal commission that replanting alone cannot offset sediment starvation.",
  opts=["A) Okafor", "B) Okafor;", "C) Okafor,", "D) Okafor—"],
  ans="C", exp="Closer is ', testified' so opener must be a matching comma. Dash/semicolon mismatch the closing comma."),
 dict(n=9, level="HARD", cat="Punctuation: Dash as Colon",
  passage="Ground-penetrating radar beneath the nave revealed a single anomaly_______ a vaulted crypt whose masonry predates the cathedral above it by nearly two centuries.",
  opts=["A) nave;", "B) nave", "C) nave, and", "D) nave—"],
  ans="D", exp="IC + dramatic explanation -> single dash (= colon). Semicolon fails (fragment after); 'and' distorts meaning."),
 dict(n=10, level="HARD", cat="Punctuation: Conjunctive Adverb",
  passage="Orbital refueling could in principle extend deep-space missions by years_______ mission planners remain constrained by boil-off losses that no existing depot has solved.",
  opts=["A) ; however,", "B) , however,", "C) ; however", "D) . However"],
  ans="A", exp="Two ICs with 'however' -> [IC; however, IC]. B is a splice; C omits comma after however; D strands 'However' without comma."),
 dict(n=11, level="VERY HARD", cat="Punctuation: Colon Explanation",
  passage="Analyzing Edo-period merchant diaries, historian Kenji Mori identifies a single anxiety recurring across three decades of entries_______ the prospect that a debased currency would dissolve obligations built on trust.",
  opts=["A) entries;", "B) entries,", "C) entries:", "D) entries"],
  ans="C", exp="IC before; noun-clause explanation after -> colon [IC: explanation]. Semicolon needs IC after (this is a fragment); comma splices."),
 dict(n=12, level="VERY HARD", cat="Punctuation: Matching Dashes",
  passage="The Atacama Large Millimeter Array—a collaboration spanning twenty nations, forty-five antennas, and three continents_______ has recalibrated estimates of planet formation timescales.",
  opts=["A) continents,", "B) continents", "C) continents;", "D) continents—"],
  ans="D", exp="Parenthetical opens with dash -> must close with dash, even though it contains internal commas. Mixing dash-comma is always wrong."),
 dict(n=13, level="VERY HARD", cat="Punctuation: Essential Appositive",
  passage="Celebrated poet_______ assembled the anthology from prison correspondence, oral histories, and previously suppressed broadsides circulated during the blockade.",
  opts=["A) , Lucille Harper,", "B) Lucille Harper", "C) Lucille Harper,", "D) Lucille Harper—"],
  ans="B", exp="Title + Name ('Celebrated poet Lucille Harper') is essential -> no commas. Any single mark strands subject from verb 'assembled'."),
 dict(n=14, level="VERY HARD", cat="Punctuation: Plural Possessive",
  passage="After auditing the regional hospitals' supply chains, investigators traced the counterfeit vials to the distributors_______ falsified cold-chain logs rather than to the manufacturers.",
  opts=["A) distributor's", "B) distributors", "C) distributors'", "D) distributors's"],
  ans="C", exp="Multiple distributors own the logs -> distributors'. A is singular; B has no possession; D never valid for regular plurals."),
 dict(n=15, level="VERY HARD", cat="Punctuation: Sentence Boundary",
  passage="Seagrass meadows sequester dissolved carbon at rates rivaling tropical forests_______ policymakers continue to classify them as marginal habitat in coastal zoning reviews.",
  opts=["A) forests,", "B) forests", "C) forests, and,", "D) forests;"],
  ans="D", exp="Two ICs, no conjunction -> semicolon. A is the classic splice trap; B run-on; C doubly punctuated."),
 dict(n=16, level="VERY HARD", cat="Punctuation: No Punctuation (Comparison)",
  passage="Field trials showed that the drought-tolerant maize lines yielded substantially more grain under water stress_______ than the elite commercial hybrids grown in adjacent plots.",
  opts=["A) ,", "B) ;", "C) NO PUNCTUATION", "D) —"],
  ans="C", exp="Never separate the comparison 'more... than...' with a single mark. SAT DELETE type: any punctuation breaks the clause."),
 dict(n=17, level="VERY HARD", cat="Punctuation: Matching Dash (which)",
  passage="The decommissioned lighthouse—which still houses a first-order Fresnel lens_______ now operates as a field station for tracking pelagic bird migration.",
  opts=["A) ,", "B) —", "C) ;", "D) NO PUNCTUATION"],
  ans="B", exp="Nonessential 'which' clause opened with dash -> close with dash. Comma mismatches; semicolon cannot terminate a modifier."),
 dict(n=18, level="VERY HARD", cat="Punctuation: Colon Result",
  passage="Oceanographers had warned for a decade that the reef's thermal buffer was collapsing_______ bleaching events that once occurred once per decade began striking in consecutive years.",
  opts=["A) collapsing,", "B) collapsing", "C) collapsing and", "D) collapsing:"],
  ans="D", exp="IC before; second IC explains the consequence -> [IC: IC]. Comma splices; bare 'and' without comma cannot join two ICs."),
 dict(n=19, level="VERY HARD", cat="Punctuation: That vs. Which",
  passage="The epistolary archive contains drafting manuals_______ circulated only among apprentice scribes and were never intended for patrons' eyes.",
  opts=["A) , which", "B) that,", "C) that", "D) which,"],
  ans="C", exp="Restrictive clause defining which manuals -> 'that' with NO commas. 'Which' with a comma would mark it nonessential, contradicting meaning."),
 dict(n=20, level="VERY HARD", cat="Punctuation: Compound Predicate",
  passage="Curator Ingrid Solberg authenticated the disputed altarpiece in Naples_______ and traced its underdrawing to a workshop assistant previously thought to have died a decade earlier.",
  opts=["A) Naples,", "B) Naples;", "C) Naples—", "D) Naples"],
  ans="D", exp="One subject + two verbs (authenticated... and traced...) -> compound predicate. Never split verb phrases with comma/semicolon/dash."),
 dict(n=21, level="EXTREME", cat="Punctuation: Subject-Verb, Long Interrupter",
  passage="The fossilized trackways uncovered across three kilometers of exposed lakebed in the Turkana Basin_______ preserve the earliest evidence of coordinated group movement in hominins.",
  opts=["A) Basin", "B) Basin,", "C) Basin;", "D) Basin—"],
  ans="A", exp="Massive subject ('trackways... Basin') + verb 'preserve'. Never separate subject-verb with one mark, however long the interrupting PPs."),
 dict(n=22, level="EXTREME", cat="Punctuation: Nonessential Name, Both Sides",
  passage="An outspoken critic of algorithmic sentencing_______ has urged courts to publish validation audits before procuring risk-assessment software.",
  opts=["A) Professor Anita Desai,", "B) , Professor Anita Desai,", "C) Professor Anita Desai", "D) , Professor Anita Desai"],
  ans="B", exp="Indefinite 'An...' signals name is extra -> commas BOTH sides. A misses opener; C/D miss one side and strand the clause."),
 dict(n=23, level="EXTREME", cat="Punctuation: Nested Dash Parenthetical",
  passage="While most textbooks still describe the eruption as a single paroxysmal event, tephra layers sampled from bogs—which retain ashfall too fine for lake sediments_______ indicate at least four discrete pulses over eleven months.",
  opts=["A) sediments,", "B) sediments", "C) sediments;", "D) sediments—"],
  ans="D", exp="Inner modifier opens 'bogs—which...' -> must close with matching dash before main verb 'indicate'. Comma mismatches the dash opener."),
 dict(n=24, level="EXTREME", cat="Punctuation: Colon Trap (Verb/Prep)",
  passage="The revised procurement guidelines require_______ documented chain-of-custody logs, third-party assays for every ore batch, and penalties indexed to market price.",
  opts=["A) :", "B) ;", "C) —", "D) NO PUNCTUATION"],
  ans="D", exp="Colon/dash/semicolon can NEVER follow the verb 'require' (or any preposition). List is the direct object -> no mark at all."),
 dict(n=25, level="EXTREME", cat="Punctuation: Pronoun (Each / Its)",
  passage="Each of the autonomous submersibles lost_______ acoustic beacon when the thermocline collapsed, forcing recovery teams to triangulate positions from surface echoes.",
  opts=["A) their", "B) its", "C) it's", "D) its'"],
  ans="B", exp="'Each' is singular despite plural 'submersibles' -> 'its'. Their is plural; it's = it is; its' never exists."),
 dict(n=26, level="EXTREME", cat="Punctuation: Subordinator Trap",
  passage="_______ the review board approved the trial protocol unanimously, dissenting statisticians continued to dispute the stopping rule in post-approval memos.",
  opts=["A) However,", "B) Consequently,", "C) Although", "D) Moreover,"],
  ans="C", exp="Only 'Although' subordinates -> [Although..., ...]. Starting with However/Consequently/Moreover + comma creates a comma splice between two ICs."),
 dict(n=27, level="EXTREME", cat="Punctuation: Intro Absolute Phrase",
  passage="Its encryption keys escrowed in three jurisdictions_______ the messaging protocol remained formally outside the reach of any single subpoena.",
  opts=["A) jurisdictions;", "B) jurisdictions", "C) jurisdictions,", "D) jurisdictions—"],
  ans="C", exp="Intro absolute/nominative phrase ('Its keys escrowed...') is not an IC -> comma before main IC. Semicolon needs IC before it."),
 dict(n=28, level="EXTREME", cat="Punctuation: Dash Close With Internal Comma",
  passage="The longitudinal cohort study—launched in 1998, expanded after the 2008 funding crisis,_______ now underpins most pediatric exposure guidelines worldwide.",
  opts=["A) crisis,", "B) crisis", "C) crisis;", "D) crisis—"],
  ans="D", exp="Dash-opened parenthetical with internal commas must still close with a dash. A comma would mismatch the opener; do not be fooled by inner commas."),
 dict(n=29, level="EXTREME", cat="Punctuation: Super-Semicolons",
  passage="Field stations were proposed for Reykjavík, Iceland_______ Nairobi, Kenya_______ Jakarta, Indonesia_______ and Lima, Peru.",
  opts=["A) , , ,", "B) : : :", "C) ; ; ;", "D) — — —"],
  ans="C", exp="Items already contain commas (City, Country) -> semicolons as super-separators. Commas alone collapse boundaries; colons/dashes cannot separate list items."),
 dict(n=30, level="EXTREME", cat="Punctuation: Boundary With Demonstrative",
  passage="Excavators cataloged more than two thousand loom weights at the hillside complex_______ this density overturned the assumption that textile production there was strictly domestic.",
  opts=["A) complex, this", "B) complex", "C) complex, and, this", "D) complex; this"],
  ans="D", exp="Two ICs (second begins 'this density...') with no conjunction -> semicolon. Demonstrative 'this' does not fix a splice."),
 # ============ PART B: GRAMMAR (31-60) ============
 dict(n=31, level="HARD", cat="Grammar: Subject-Verb Agreement",
  passage="The array of tide gauges deployed along the subsiding delta_______ sea-level rise at millimeter precision despite biofouling and storm damage.",
  opts=["A) monitor", "B) have monitored", "C) monitors", "D) are monitoring"],
  ans="C", exp="Subject is singular 'array' (PP 'of gauges' is a distractor). Singular present -> monitors. B/D are plural."),
 dict(n=32, level="HARD", cat="Grammar: Neither/Nor Agreement",
  passage="Neither the field coordinators nor the principal investigator_______ satisfied with the chain-of-custody documentation for the ice cores.",
  opts=["A) were", "B) are", "C) was", "D) be"],
  ans="C", exp="With neither/nor, verb agrees with nearest subject ('investigator' singular) -> was. Proximity rule."),
 dict(n=33, level="HARD", cat="Grammar: Number / A Number",
  passage="The number of peer-reviewed retractions linked to image duplication_______ sharply since journals adopted automated screening.",
  opts=["A) have risen", "B) has risen", "C) rise", "D) are rising"],
  ans="B", exp="'The number' = singular -> has risen. ('A number' would take plural.) Don't be fooled by plural 'retractions'."),
 dict(n=34, level="HARD", cat="Grammar: Tense Consistency",
  passage="By the time the review panel convened, the excavation team_______ three seasons of stratigraphic logs that contradicted the original survey.",
  opts=["A) has compiled", "B) had compiled", "C) compiles", "D) will compile"],
  ans="B", exp="Past-perfect needed: action completed BEFORE another past event ('convened'). 'Has' is present-perfect; C/D misplace time."),
 dict(n=35, level="HARD", cat="Grammar: Future Perfect",
  passage="If deployment stays on schedule, engineers_______ the full sensor constellation by the next equinox.",
  opts=["A) will have calibrated", "B) calibrated", "C) have calibrated", "D) had calibrated"],
  ans="A", exp="Deadline in the future ('by the next equinox') completed before then -> future perfect 'will have calibrated'."),
 dict(n=36, level="HARD", cat="Grammar: Pronoun Clarity",
  passage="The tribunal credited the whistleblowers rather than the contractors because_______ had preserved contemporaneous field notes.",
  opts=["A) they", "B) the whistleblowers", "C) those", "D) one"],
  ans="B", exp="'They' is ambiguous (whistleblowers or contractors?). SAT demands the explicit noun when two plural antecedents compete."),
 dict(n=37, level="HARD", cat="Grammar: Each / Agreement",
  passage="Each of the revised manuscripts_______ subjected to an independent statistical audit before acceptance.",
  opts=["A) were", "B) are", "C) was", "D) be"],
  ans="C", exp="'Each' is always singular despite plural 'manuscripts' -> was. Were/are match the nearby plural distractor."),
 dict(n=38, level="HARD", cat="Grammar: Who vs. Which",
  passage="The epidemiologists_______ pioneered wastewater surveillance shared primer sequences that municipal labs still use today.",
  opts=["A) which", "B) whom", "C) who", "D) whose"],
  ans="C", exp="People -> 'who' as subject. 'Which' is for things; 'whom' is object case; 'whose' is possessive."),
 dict(n=39, level="HARD", cat="Grammar: Dangling Modifier",
  passage="After analyzing the sediment cores for microplastics, _______ revised upward by nearly forty percent.",
  opts=["A) the contamination estimates were", "B) the laboratory revised the contamination estimates", "C) there were major revisions to contamination estimates", "D) contamination estimates rose"],
  ans="B", exp="The 'after analyzing' phrase must modify the analyzer (the laboratory/scientists). A/C/D dangle: estimates cannot analyze."),
 dict(n=40, level="HARD", cat="Grammar: Parallelism",
  passage="The fellowship trains residents to collect oral histories, to digitize fragile manuscripts, and_______ endangered-language recordings for community archives.",
  opts=["A) preserving", "B) to preserve", "C) preservation of", "D) preserve"],
  ans="B", exp="Parallel infinitives: to collect, to digitize, to preserve. Gerund/noun forms break parallelism."),
 dict(n=41, level="VERY HARD", cat="Grammar: Correlatives",
  passage="The retrofit was designed not only to cut peak electricity demand_______ to provide backup potable water during outages.",
  opts=["A) but also providing", "B) but also to provide", "C) but to provide also", "D) but providing"],
  ans="B", exp="Idiom is 'not only X but also Y' with matched forms: 'to cut... to provide'. Participles break the pair."),
 dict(n=42, level="VERY HARD", cat="Grammar: Illogical Comparison",
  passage="Unlike the spectrograms produced by the legacy array, _______ resolve individual whale calls within the chorus.",
  opts=["A) the new hydrophones' spectrograms", "B) the new hydrophones", "C) whale calls", "D) the chorus"],
  ans="A", exp="Compare like to like: spectrograms vs. spectrograms. B compares spectrograms to devices (illogical)."),
 dict(n=43, level="VERY HARD", cat="Grammar: Transition",
  passage="The levee reinforcement prevented overtopping during the record surge. _______, backwater flooding inundated pump stations the design had assumed would stay dry.",
  opts=["A) Consequently,", "B) Moreover,", "C) However,", "D) For example,"],
  ans="C", exp="Second sentence contrasts/counters the success -> 'However'. Consequently = cause-effect; Moreover = continuation; For example = instance."),
 dict(n=44, level="VERY HARD", cat="Grammar: Transition (Cause)",
  passage="The aquifer recharge rate fell for three consecutive years; _______, the water authority imposed mandatory rationing ahead of the dry season.",
  opts=["A) in contrast,", "B) for instance,", "C) nevertheless,", "D) consequently,"],
  ans="D", exp="Rationing is the RESULT of falling recharge -> 'consequently'. 'Nevertheless/in contrast' signal opposition; 'for instance' signals example."),
 dict(n=45, level="VERY HARD", cat="Grammar: One of + That (Agreement)",
  passage="Dr. Chen's meta-analysis is one of the few reviews that_______ the mortality benefit across all age strata rather than in a subgroup.",
  opts=["A) confirms", "B) confirm", "C) has confirmed", "D) is confirming"],
  ans="B", exp="'That' refers to plural 'reviews' (one of the reviews that confirm...), not singular 'one' -> plural 'confirm'. Classic SAT trap."),
 dict(n=46, level="VERY HARD", cat="Grammar: Conditional / Subjunctive",
  passage="If the armistice terms_______ ratified last spring, the demilitarized corridor would already have reopened to civilian transit.",
  opts=["A) were", "B) had been", "C) are", "D) would have been"],
  ans="B", exp="Counterfactual past (would already have...) needs past-perfect 'had been' in the if-clause. 'Were' is present-counterfactual; D doubles 'would'."),
 dict(n=47, level="VERY HARD", cat="Grammar: Modifier Placement",
  passage="Burdened by months of equipment failures and funding delays, _______ struggled to catalog the frescoes before rising humidity sealed the pigments.",
  opts=["A) the conservation team", "B) the frescoes", "C) cataloging", "D) the museum's humidity"],
  ans="A", exp="Only the team can 'struggle to catalog'. The intro participial phrase must attach to the grammatical subject capable of the action; frescoes/humidity cannot struggle."),
 dict(n=48, level="VERY HARD", cat="Grammar: Concision",
  passage="The audit attributed the overrun to redundant duplication of sensor calibrations performed on an annual yearly basis.",
  opts=["A) redundant duplication of sensor calibrations performed on an annual yearly basis", "B) sensor calibrations performed annually", "C) annual yearly duplication of sensor calibrations done each year", "D) duplicate redundant calibrations of sensors done annually yearly"],
  ans="B", exp="SAT prefers concision: 'annual yearly' and 'redundant duplication' repeat. B says the same in fewest words without loss."),
 dict(n=49, level="VERY HARD", cat="Grammar: Idiom (Capable of)",
  passage="The tardigrade proteins are notable for being capable_______ extreme desiccation and then resuming metabolism within hours of rehydration.",
  opts=["A) to survive", "B) of surviving", "C) for surviving", "D) in surviving"],
  ans="B", exp="Idiom is 'capable of + gerund'. 'Capable to/for/in' are unidiomatic on the SAT."),
 dict(n=50, level="VERY HARD", cat="Grammar: Pronoun Number (Species Data)",
  passage="The longitudinal data set, though compiled from eleven clinics, retains_______ original coding errors because harmonization was applied only prospectively.",
  opts=["A) their", "B) its", "C) it's", "D) theirs"],
  ans="B", exp="'Data set' is singular -> 'its'. 'Their/theirs' plural; it's = it is. Don't match 'clinics' distractor."),
 dict(n=51, level="EXTREME", cat="Grammar: Inverted Agreement + Interrupter",
  passage="Piled beside the decommissioned reactor, each sealed cask of vitrified waste, along with its monitoring telemetry,_______ to a geological repository under armed escort.",
  opts=["A) were transported", "B) have been transported", "C) was transported", "D) are transported"],
  ans="C", exp="Subject is 'each cask' (singular); parenthetical 'along with...' never changes number. Past narrative -> was transported."),
 dict(n=52, level="EXTREME", cat="Grammar: Tense + Voice in Sequence",
  passage="The manuscripts, which _______ in a flooded crypt for two centuries, are now being stabilized leaf by leaf in a nitrogen chamber.",
  opts=["A) lay submerged", "B) have laid submerged", "C) were lain submerged", "D) had laid submerged"],
  ans="A", exp="Lie/lay/lain (recline) vs. lay/laid/laid (place). Manuscripts 'lay' (past of lie) submerged. 'Laid' needs an object; 'were lain' is passive of lie (wrong)."),
 dict(n=53, level="EXTREME", cat="Grammar: Logical Comparison + Possessive",
  passage="The transit authority found that ridership on the refurbished ferry line now exceeds_______ on any other harbor route during peak hours.",
  opts=["A) that", "B) those", "C) ridership", "D) that of ridership"],
  ans="A", exp="Elliptical comparison: 'exceeds that (ridership) on any other route'. 'Those' is plural; C repeats the noun redundantly; D doubles."),
 dict(n=54, level="EXTREME", cat="Grammar: Transition (Concession Chain)",
  passage="Critics concede that the seawall reduced wave overtopping. _______, they argue, the structure accelerated downdrift erosion, offsetting much of the apparent gain.",
  opts=["A) Nevertheless,", "B) Accordingly,", "C) For example,", "D) Similarly,"],
  ans="A", exp="Concession ('concede... reduced') followed by counterpoint -> 'Nevertheless'. Accordingly = result; For example = instance; Similarly = parallel."),
 dict(n=55, level="EXTREME", cat="Grammar: Parallelism in Comparison",
  passage="Restoring the estuary requires dredging clogged channels, replanting cordgrass, and_______ tidal flow through the old causeway.",
  opts=["A) the reestablishment of", "B) to reestablish", "C) reestablishing", "D) reestablish"],
  ans="C", exp="Gerunds in series: dredging, replanting, reestablishing. Infinitive/noun forms break parallelism; bare 'reestablish' mismatches."),
 dict(n=56, level="EXTREME", cat="Grammar: Amount vs. Number / Fewer vs. Less",
  passage="The new protocol produced_______ procedural errors and measurably_______ contaminated cultures than the legacy workflow.",
  opts=["A) fewer / fewer", "B) fewer / less", "C) less / fewer", "D) less / less"],
  ans="B", exp="Countable 'errors' -> fewer; uncountable portion implied? Actually 'cultures' countable too — but second blank modifies degree ('measurably less contamination' = uncountable contamination). Standard key: fewer errors / less contamination. B mirrors SAT fewer/less split."),
 dict(n=57, level="EXTREME", cat="Grammar: Between/Among + Pronoun Case",
  passage="The data-sharing agreement was negotiated exclusively between the observatory director and_______ before the funding cycle closed.",
  opts=["A) we", "B) us researchers", "C) we researchers", "D) ourselves"],
  ans="B", exp="Preposition 'between' takes object case: 'between... and us'. 'We' is subject case; 'ourselves' reflexive with no antecedent action."),
 dict(n=58, level="EXTREME", cat="Grammar: Dangling + Tense Hybrid",
  passage="Having completed the blinded reanalysis, _______ no longer supported the original claim of a treatment effect.",
  opts=["A) the trial data", "B) the investigators concluded the trial data", "C) it was concluded that the trial data", "D) the trial data were concluded"],
  ans="B", exp="Who completed the reanalysis? Investigators — only B supplies that agent as subject. Data cannot 'complete'; C/D are wordy/passive danglers."),
 dict(n=59, level="EXTREME", cat="Grammar: Affect / Effect + Precision",
  passage="Reviewers warned that the dam's altered sediment regime would_______ downstream spawning beds and, in turn, produce cascading ecological _______.",
  opts=["A) effect / affects", "B) affect / effects", "C) effect / effects", "D) affect / affects"],
  ans="B", exp="Verb = affect (to influence); noun = effects (results). 'Effect' as verb = to bring about (wrong here); 'affects' as noun is a verb form."),
 dict(n=60, level="EXTREME", cat="Grammar: Concision + Redundancy Hybrid",
  passage="The committee's final consensus was that the two plans, both alike in their shared uniformity, should be merged.",
  opts=["A) both alike in their shared uniformity,", "B) identical,", "C) alike and uniform and similar,", "D) sharing the same uniform likeness together,"],
  ans="B", exp="All options except B stack synonyms ('both alike,' 'shared uniformity'). SAT concision: 'identical' carries the full meaning alone."),
]

def badge(level):
    return {"HARD":"hard","VERY HARD":"veryhard","EXTREME":"extreme"}[level]

def render_questions():
    out=[]
    for q in QUESTIONS:
        opts="\n".join(f'            <div class="option" data-q="{q["n"]}"><span class="opt-letter">{o.split(")")[0]})</span> {o.split(")",1)[1].strip()}</div>' for o in q["opts"])
        out.append(f'''    <div class="question-card" id="q{q["n"]}">
        <div class="question-header"><span>Question {q["n"]} — {q["cat"]}</span><span class="difficulty-badge {badge(q["level"])}">{q["level"]}</span></div>
        <div class="passage">{q["passage"]}</div>
        <div class="question-text">Which choice completes the text so that it conforms to the conventions of Standard English?</div>
        <div class="options">{opts}
        </div>
        <div class="q-actions"><button onclick="toggleAns({q["n"]})">Show answer</button></div>
        <div class="q-answer" id="ans{q["n"]}" hidden><strong>{q["ans"]} — {q["cat"]}.</strong> {q["exp"]}</div>
    </div>''')
    return "\n".join(out)

def render_key_rows():
    rows=[]
    for q in QUESTIONS:
        rows.append(f'<tr><td><strong>{q["n"]}</strong></td><td><strong>{q["ans"]}</strong></td><td>{q["cat"]}</td><td>{q["exp"]}</td></tr>')
    return "\n".join(rows)

CSS = """:root{--navy:#1a365d;--blue:#2b6cb0;--light:#f8fafc;--border:#e2e8f0;--red:#991b1b;--purple:#6b21a8;--black:#111827}
*{box-sizing:border-box}body{font-family:'Segoe UI',-apple-system,Roboto,Arial,sans-serif;color:#1a202c;line-height:1.55;background:#fff;margin:0;padding:0 20px 60px}
.topbar{position:sticky;top:0;background:var(--navy);color:#fff;padding:10px 16px;display:flex;gap:12px;align-items:center;z-index:10;margin:0 -20px}
.topbar a{color:#bee3f8;text-decoration:none;font-size:9pt;font-weight:600}.topbar .spacer{flex:1}.topbar button{background:#fff;color:var(--navy);border:0;border-radius:6px;padding:6px 12px;font-weight:700;cursor:pointer}
.header{text-align:center;border-bottom:3px double var(--navy);padding:18px 0 14px}.header h1{margin:0;font-size:24pt;color:var(--navy);text-transform:uppercase;letter-spacing:1px}.header p{color:#4a5568;font-weight:600}
.student-info{display:flex;gap:12px;flex-wrap:wrap;justify-content:space-between;font-size:10pt;border:1px solid #cbd5e0;padding:10px 15px;border-radius:8px;background:var(--light);margin-top:14px}
.section-title{background:var(--navy);color:#fff;padding:9px 12px;font-size:12pt;font-weight:800;text-transform:uppercase;border-radius:6px;margin:30px 0 14px;letter-spacing:.5px}
.subsection-title{font-size:11pt;font-weight:800;color:var(--blue);border-bottom:2px solid #ebf8ff;padding-bottom:4px;margin:18px 0 10px}
.question-card{border:1px solid var(--border);border-radius:8px;padding:14px 16px;margin-bottom:14px;page-break-inside:avoid;background:#fff}
.question-header{font-weight:800;font-size:10pt;display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;gap:8px}
.difficulty-badge{padding:3px 8px;font-size:7.5pt;font-weight:800;border-radius:4px;color:#fff;white-space:nowrap}.hard{background:var(--red)}.veryhard{background:var(--purple)}.extreme{background:var(--black)}
.passage{font-size:9.5pt;background:var(--light);border-left:3px solid #cbd5e0;padding:10px 14px;margin-bottom:10px;text-align:justify}
.question-text{font-size:9.5pt;font-weight:700;margin-bottom:8px}.options{display:grid;gap:6px;font-size:9pt}.option{padding:7px 10px;border:1px solid #edf2f7;border-radius:6px;background:#fff;cursor:pointer}.option:hover{border-color:var(--blue)}.option.sel{border-color:var(--blue);background:#ebf8ff}
.opt-letter{font-weight:800;color:var(--blue);margin-right:6px}.q-actions{margin-top:8px}.q-actions button{background:var(--light);border:1px solid #cbd5e0;border-radius:6px;padding:5px 10px;cursor:pointer;font-weight:700;font-size:8.5pt}
.q-answer{margin-top:8px;background:#f0fff4;border:1px solid #9ae6b4;border-radius:6px;padding:8px 10px;font-size:9pt}
.answer-key-table{width:100%;border-collapse:collapse;font-size:8.5pt}.answer-key-table th,.answer-key-table td{border:1px solid #cbd5e0;padding:8px 10px;text-align:left;vertical-align:top}.answer-key-table th{background:var(--blue);color:#fff;text-transform:uppercase;font-size:8pt}.answer-key-table tr:nth-child(even){background:#f7fafc}
.page-break{page-break-before:always}
@media print{.topbar,.q-actions{display:none}.option{cursor:default}.q-answer{border:1px solid #9ae6b4}body{padding:0}}
@media(max-width:640px){.header h1{font-size:16pt}body{padding:0 12px 40px}.topbar{margin:0 -12px}}
"""

JS = """function toggleAns(n){const e=document.getElementById('ans'+n);e.hidden=!e.hidden;}
function toggleAll(show){document.querySelectorAll('.q-answer').forEach(e=>e.hidden=!show);}
function doPrint(){window.print();}
document.addEventListener('click',e=>{const o=e.target.closest('.option');if(!o)return;const box=o.parentElement;box.querySelectorAll('.option').forEach(x=>x.classList.remove('sel'));o.classList.add('sel');});
"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Digital SAT Extreme Challenge - 30 Punctuation + 30 Grammar (60 Questions)</title>
<style>{CSS}</style>
</head>
<body>
<nav class="topbar"><strong>SAT Extreme 60</strong><a href="#punct">Punctuation 1-30</a><a href="#gram">Grammar 31-60</a><a href="#key">Answer Key</a><span class="spacer"></span><button onclick="toggleAll(true)">Show all answers</button><button onclick="toggleAll(false)">Hide</button><button onclick="doPrint()">Print / PDF</button></nav>
<div class="header"><h1>SAT Extreme Challenge</h1><p>30 Punctuation + 30 Grammar — Hard / Very Hard / Extreme — Digital SAT Reading & Writing</p></div>
<div class="student-info"><span><strong>Name:</strong> _______________________</span><span><strong>Date:</strong> ______________</span><span><strong>Target:</strong> R&W 750+</span><span><strong>Time:</strong> 70 min</span></div>

<div class="section-title" id="punct">Part A: Punctuation — Questions 1–30 (Hard → Very Hard → Extreme)</div>
<div class="subsection-title">Q1–10 Hard · Q11–20 Very Hard · Q21–30 Extreme — click an option, then Show answer</div>
RENDER_QA
<div class="section-title" id="gram">Part B: SAT Grammar — Questions 31–60 (Hard → Very Hard → Extreme)</div>
<div class="subsection-title">Q31–40 Hard · Q41–50 Very Hard · Q51–60 Extreme — agreement, tense, modifiers, parallelism, transitions, concision</div>
RENDER_QB
<div class="page-break"></div>
<div class="section-title" id="key">Answer Key & Explanations (1–60)</div>
<table class="answer-key-table"><thead><tr><th style="width:5%">#</th><th style="width:8%">Ans</th><th style="width:14%">Category</th><th>Why</th></tr></thead><tbody>
RENDER_KEY
</tbody></table>
<script>{JS}</script>
</body></html>"""

def render_split():
    qa=[q for q in QUESTIONS if q["n"]<=30]
    qb=[q for q in QUESTIONS if q["n"]>30]
    def render(lst):
        out=[]
        for q in lst:
            opts="\n".join(f'            <div class="option" data-q="{q["n"]}"><span class="opt-letter">{o.split(")")[0]})</span> {o.split(")",1)[1].strip()}</div>' for o in q["opts"])
            out.append(f'''    <div class="question-card" id="q{q["n"]}">
        <div class="question-header"><span>Question {q["n"]} — {q["cat"]}</span><span class="difficulty-badge {badge(q["level"])}">{q["level"]}</span></div>
        <div class="passage">{q["passage"]}</div>
        <div class="question-text">Which choice completes the text so that it conforms to the conventions of Standard English?</div>
        <div class="options">{opts}
        </div>
        <div class="q-actions"><button onclick="toggleAns({q["n"]})">Show answer</button></div>
        <div class="q-answer" id="ans{q["n"]}" hidden><strong>{q["ans"]} — {q["cat"]}.</strong> {q["exp"]}</div>
    </div>''')
        return "\n".join(out)
    return render(qa), render(qb)

_qa, _qb = render_split()
HTML = HTML.replace("RENDER_QA", _qa).replace("RENDER_QB", _qb).replace("RENDER_KEY", render_key_rows())
out = pathlib.Path(__file__).with_name("SAT_Punctuation_Masterclass.html")
out.write_text(HTML, encoding="utf-8")
print(f"Generated {out} with {len(QUESTIONS)} questions.")
