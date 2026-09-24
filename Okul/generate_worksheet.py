# SAT Punctuation Masterclass & 30-Question Workbook Generator
# Data-driven version: edit QUESTIONS / RULES below, run to rebuild HTML.
# Aligned to College Board Digital SAT - Standard English Conventions.
import pathlib

QUESTIONS = [
 dict(n=1, level="EASY",
  passage="The James Webb Space Telescope collected data from distant planetary systems_______ it transmitted the high-resolution images back to researchers on Earth.",
  opts=["A) systems, it", "B) systems; it", "C) systems it", "D) systems, and, it"],
  ans="B", cat="Sentence Boundary",
  exp="Two independent clauses (ICs) with no conjunction. Semicolon is legal [IC; IC]. A is a comma splice, C is a run-on, D adds a stray second comma."),
 dict(n=2, level="EASY",
  passage="Before beginning the expedition into the deep Amazonian basin, the research team packed three indispensable items_______ solar-powered satellite phones, water purification tablets, and lightweight tents.",
  opts=["A) items:", "B) items;", "C) items,", "D) items—and"],
  ans="A", cat="Colon: List",
  exp="The text before the blank is a complete IC. A colon correctly introduces a list. Semicolon needs an IC after it (a list is not an IC). A comma cannot introduce a list here, and '—and' is unidiomatic."),
 dict(n=3, level="EASY",
  passage="During the archaeological excavation in Greece, the lead_______ field notebook was lost in a flash flood, forcing the team to reconstruct findings from secondary digital logs.",
  opts=["A) researchers", "B) researchers's", "C) researcher's", "D) researchers'"],
  ans="C", cat="Singular Possessive",
  exp="'The lead researcher' is singular, so singular possessive researcher's ('s). B is never valid, D is plural possessive (more than one researcher)."),
 dict(n=4, level="EASY",
  passage="Although the initial chemical reaction proceeded much slower than anticipated_______ the addition of a platinum catalyst rapidly accelerated the final compound synthesis.",
  opts=["A) anticipated,", "B) anticipated;", "C) anticipated", "D) anticipated:"],
  ans="A", cat="Dependent + Independent",
  exp="'Although...' is a dependent clause (DC). Pattern must be [DC, IC] — comma separates introductory DC from the main clause. Semicolon/colon cannot follow a DC."),
 dict(n=5, level="EASY",
  passage="The new urban renewal proposal promised to improve public transport infrastructure_______ it failed to address the pressing issue of affordable housing for lower-income residents.",
  opts=["A) infrastructure", "B) infrastructure,", "C) infrastructure; but", "D) infrastructure, but"],
  ans="D", cat="FANBOYS",
  exp="Two ICs joined by coordinating conjunction 'but' (FANBOYS) require comma before it: [IC, but IC]. B alone is a comma splice; semicolon + FANBOYS is never used on the SAT."),
 dict(n=6, level="EASY",
  passage="The arctic fox relies on_______ dense winter coat for survival, changing color from brown in summer to white in winter for seamless camouflage against snow.",
  opts=["A) it's", "B) its", "C) its'", "D) their"],
  ans="B", cat="Its vs. It's",
  exp="Possessive pronoun needed (the coat belongs to the fox): 'its'. 'It's' = 'it is'. 'Its'' does not exist. 'Their' is plural; the fox is singular."),
 dict(n=7, level="EASY",
  passage="The conference program featured speeches on climate adaptation, renewable energy grid integration_______ and biodiversity conservation strategies across agricultural land.",
  opts=["A) ,", "B) ;", "C) —", "D) NO PUNCTUATION"],
  ans="A", cat="Serial / Oxford Comma",
  exp="Standard list of three items: A, B, and C. SAT expects the Oxford comma before 'and'. Semicolon/dash are only for complex lists or breaks, not here."),
 dict(n=8, level="EASY",
  passage="Dr. Aris Thorne_______ a noted specialist in marine ecology, delivered the opening address at the international ocean conservation summit in Lisbon.",
  opts=["A) Thorne", "B) Thorne,", "C) Thorne;", "D) Thorne—"],
  ans="B", cat="Nonessential Opener",
  exp="The phrase closes with a comma before 'delivered', so it must open with a matching comma. Pair must match: comma–comma. Dash or semicolon would mismatch."),
 dict(n=9, level="EASY",
  passage="The architectural restoration team made an unexpected discovery behind the gallery wall_______ a fully preserved 16th-century fresco depicting a celestial map.",
  opts=["A) wall;", "B) wall, and", "C) wall—", "D) wall"],
  ans="C", cat="Single Dash = Colon",
  exp="IC followed by dramatic explanation. Single dash works like a colon. Semicolon fails because 'a fully preserved fresco' is a fragment, not an IC. B adds an illogical 'and'."),
 dict(n=10, level="EASY",
  passage="Solar panels have become significantly more efficient over the last decade_______ high installation costs continue to deter many low-income households from adopting the technology.",
  opts=["A) ; however,", "B) , however,", "C) ; however", "D) . However"],
  ans="A", cat="Conjunctive Adverb",
  exp="Joining two ICs with 'however' requires [IC; however, IC]. B is a comma splice. C misses the comma after 'however'. D misses the comma ('. However high...' is wrong)."),
 dict(n=11, level="MEDIUM",
  passage="In her analysis of 19th-century Gothic literature, scholar Maya Lin argues that one motif recurs throughout Mary Shelley's work_______ isolation in remote landscapes.",
  opts=["A) work:", "B) work;", "C) work,", "D) work"],
  ans="A", cat="Colon: Explanation",
  exp="IC before blank; 'isolation...' explains/amplifies it — colon is ideal. Semicolon fails (fragment after). Comma creates a splice/fragment problem. D creates a run-on of noun stuck to clause."),
 dict(n=12, level="MEDIUM",
  passage="The James Webb Space Telescope—a joint project involving NASA, the European Space Agency, and the Canadian Space Agency_______ has provided unprecedented imagery of deep space.",
  opts=["A) Agency,", "B) Agency—", "C) Agency;", "D) Agency"],
  ans="B", cat="Matching Dashes",
  exp="Parenthetical opens with em-dash, so it must close with em-dash. Mixing dash–comma or dash–semicolon is always wrong on the SAT."),
 dict(n=13, level="MEDIUM",
  passage="Renowned novelist_______ spent years studying historical archives in Mexico City before writing her award-winning book on early trade networks.",
  opts=["A) Isabel Allende,", "B) Isabel Allende—", "C) , Isabel Allende,", "D) Isabel Allende"],
  ans="D", cat="Essential Appositive",
  exp="Title + Name with no article ('Renowned novelist Isabel Allende') is essential — no commas. Adding one comma (A/B) strands the subject from its verb."),
 dict(n=14, level="MEDIUM",
  passage="After reviewing the laboratory_______ detailed reports on groundwater contamination, the regional agency ordered an immediate halt to industrial dumping.",
  opts=["A) technicians'", "B) technician's", "C) technicians", "D) technicians's"],
  ans="A", cat="Plural Possessive",
  exp="Reports belong to multiple technicians → plural possessive technicians' (s'). B is singular. C has no possession. D is never valid for regular plurals."),
 dict(n=15, level="MEDIUM",
  passage="Many migratory bird species rely on coastal wetlands for rest during seasonal travel_______ urban encroachment has destroyed over forty percent of these critical habitats.",
  opts=["A) travel,", "B) travel;", "C) travel", "D) travel, and,"],
  ans="B", cat="Comma Splice Avoidance",
  exp="Two ICs, no conjunction → semicolon. A is the classic comma-splice trap. C is a run-on. D is doubly punctuated and ungrammatical."),
 dict(n=16, level="MEDIUM",
  passage="The recent study revealed that students who participate in peer-led study groups tend to perform better on standardized exams_______ than students who study entirely in isolation.",
  opts=["A) ,", "B) ;", "C) NO PUNCTUATION", "D) —"],
  ans="C", cat="Unnecessary Punctuation",
  exp="Never separate 'exams' from its comparative 'than...' phrase. Any single mark breaks subject–comparison flow. This is the SAT 'DELETE' question type."),
 dict(n=17, level="MEDIUM",
  passage="The museum's new exhibit—which features artifacts from the Bronze Age_______ will remain open to the public until late December.",
  opts=["A) —", "B) ,", "C) ;", "D) NO PUNCTUATION"],
  ans="A", cat="Matching Dashes",
  exp="Nonessential clause opens with '—which', so it must close with '—'. Comma mismatches the opener; semicolon cannot close a dependent modifier."),
 dict(n=18, level="MEDIUM",
  passage="Linguists have long observed that languages evolve rapidly when geographically isolated cultures interact_______ new dialects frequently emerge within a few generations.",
  opts=["A) interact,", "B) interact", "C) interact and", "D) interact:"],
  ans="D", cat="Colon: Explanation",
  exp="First clause is a complete IC; second explains the result — colon fits [IC: IC-explanation]. A is a comma splice, B is a run-on, C joins two ICs with bare 'and' (needs ', and')."),
 dict(n=19, level="MEDIUM",
  passage="The hydrothermal vents along the ocean floor emit mineral-rich fluids_______ support unique ecosystems entirely independent of sunlight.",
  opts=["A) that,", "B) , which", "C) which,", "D) that;"],
  ans="B", cat="That vs. Which",
  exp="Non-restrictive 'which' clause needs a comma before 'which'. 'That' clauses are restrictive and never take a comma before 'that'. C misplaces the comma."),
 dict(n=20, level="MEDIUM",
  passage="Marine biologist Elena Gomez surveyed the coral reef off the coast of Belize_______ and recorded significant coral bleaching caused by rising water temperatures.",
  opts=["A) Belize,", "B) Belize;", "C) Belize", "D) Belize—"],
  ans="C", cat="Compound Predicate",
  exp="One subject (Gomez) + two verbs (surveyed... and recorded...) = compound predicate. Never put a comma/semicolon/dash between verb phrases sharing a subject."),
 dict(n=21, level="HARD",
  passage="The ancient clay tablets discovered by archaeologists in southern Iraq_______ contain detailed logs recording grain distribution among temple workers during the Sumerian period.",
  opts=["A) Iraq", "B) Iraq,", "C) Iraq;", "D) Iraq—"],
  ans="A", cat="Subject–Verb",
  exp="Long subject ('The ancient clay tablets... Iraq') + verb 'contain'. Never separate subject from verb with a single comma/dash/semicolon."),
 dict(n=22, level="HARD",
  passage="A prominent researcher at the Institute for Advanced Study_______ published a groundbreaking paper on quantum entanglement that challenged existing models.",
  opts=["A) Dr. Julian Vance,", "B) , Dr. Julian Vance,", "C) Dr. Julian Vance", "D) , Dr. Julian Vance"],
  ans="B", cat="Nonessential Name",
  exp="'A prominent researcher...' + name: the indefinite 'A' signals the name is extra info → needs commas both sides. A/C miss the opening comma; D misses the closing one."),
 dict(n=23, level="HARD",
  passage="Although many historians once attributed the decline of Mayan city-states solely to warfare, recent sediment samples taken from regional lakes—which show evidence of severe, multi-decade droughts_______ suggest that environmental disaster played a greater role.",
  opts=["A) droughts,", "B) droughts—", "C) droughts;", "D) droughts"],
  ans="B", cat="Nested Parenthetical",
  exp="Inner clause opens 'lakes—which...', so it must close with matching '—' before the main verb 'suggest'. Comma mismatches; semicolon cannot end a modifier."),
 dict(n=24, level="HARD",
  passage="The main obstacles facing commercial spaceflight companies are_______ high manufacturing costs, regulatory hurdles, and unpredictable atmospheric conditions during launch.",
  opts=["A) :", "B) ;", "C) —", "D) NO PUNCTUATION"],
  ans="D", cat="Colon Trap",
  exp="Never put colon/dash/semicolon directly after linking verb 'are' or a preposition. The list flows as the complement: 'are high costs...' with no mark."),
 dict(n=25, level="HARD",
  passage="The tardigrade, a microscopic organism capable of surviving extreme fluctuations, lowers_______ metabolic rate to near zero during periods of intense environmental stress.",
  opts=["A) its", "B) it's", "C) their", "D) its'"],
  ans="A", cat="Pronoun Agreement",
  exp="'The tardigrade' is singular → 'its'. 'Their' is plural. 'It's' = 'it is'. 'Its'' never exists."),
 dict(n=26, level="HARD",
  passage="_______ the committee members disagreed sharply on budget allocations for research software, they reached a consensus regarding hardware acquisitions for the lab.",
  opts=["A) However,", "B) Although", "C) Furthermore,", "D) Consequently,"],
  ans="B", cat="Subordinator vs. Adverb",
  exp="Only 'Although' creates a dependent clause [Although..., they...]. 'However/Furthermore/Consequently,' are conjunctive adverbs — starting with them plus a comma creates a comma splice."),
 dict(n=27, level="HARD",
  passage="Exhausted by months of deep-sea data collection_______ the marine biologists finally completed their comprehensive survey of cold-water coral reefs in the North Atlantic.",
  opts=["A) collection,", "B) collection;", "C) collection—", "D) collection"],
  ans="A", cat="Intro Modifier",
  exp="Introductory participial phrase ('Exhausted...') must be set off with a comma before the main clause subject. Semicolon needs an IC before it; a participial phrase is not an IC."),
 dict(n=28, level="HARD",
  passage="The team's research paper—published in the journal Science,_______ generated significant public interest in oceanic ecosystem restoration.",
  opts=["A) Science—", "B) Science,", "C) Science;", "D) Science"],
  ans="A", cat="Matching Dashes",
  exp="Nonessential opens with dash → must close with dash. The ',_______' after Science is the closing slot. Comma mismatches the opener."),
 dict(n=29, level="HARD",
  passage="The summit invited delegates from Tokyo, Japan_______ Paris, France_______ Nairobi, Kenya_______ and Bogotá, Colombia.",
  opts=["A) ; ; ;", "B) , , ,", "C) — — —", "D) : : :"],
  ans="A", cat="Supersemicolons",
  exp="Complex list where items already contain commas (City, Country) must use semicolons as super-separators to avoid confusion. Commas alone blur item boundaries."),
 dict(n=30, level="HARD",
  passage="In their study of ancient trade, archaeologists examined ceramic vessels found off Sicily_______ analysis of organic residue inside revealed traces of olive oil, wine, and resin from the 4th century BCE.",
  opts=["A) Sicily,", "B) Sicily", "C) Sicily, and,", "D) Sicily;"],
  ans="D", cat="Sentence Boundary",
  exp="Two ICs with no conjunction → semicolon. A is a comma splice, B is a run-on, C is doubly wrong (', and,' + splice)."),
]

def badge(level):
    return {"EASY":"easy","MEDIUM":"medium","HARD":"hard"}[level]

def render_questions():
    out=[]
    for q in QUESTIONS:
        opts="\n".join(f'            <div class="option" data-q="{q["n"]}"><span class="opt-letter">{o.split(")")[0]})</span> {o.split(")",1)[1].strip()}</div>' for o in q["opts"])
        out.append(f'''    <div class="question-card" id="q{q["n"]}">
        <div class="question-header"><span>Question {q["n"]}</span><span class="difficulty-badge {badge(q["level"])}">{q["level"]}</span></div>
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

CSS = """:root{--navy:#1a365d;--blue:#2b6cb0;--light:#f8fafc;--border:#e2e8f0;--red:#e53e3e;--green:#38a169;--orange:#dd6b20}
*{box-sizing:border-box}body{font-family:'Segoe UI',-apple-system,Roboto,Arial,sans-serif;color:#1a202c;line-height:1.55;background:#fff;margin:0;padding:0 20px 60px}
.topbar{position:sticky;top:0;background:var(--navy);color:#fff;padding:10px 16px;display:flex;gap:12px;align-items:center;z-index:10;margin:0 -20px}
.topbar a{color:#bee3f8;text-decoration:none;font-size:9pt;font-weight:600}.topbar .spacer{flex:1}.topbar button{background:#fff;color:var(--navy);border:0;border-radius:6px;padding:6px 12px;font-weight:700;cursor:pointer}
.header{text-align:center;border-bottom:3px double var(--navy);padding:18px 0 14px}.header h1{margin:0;font-size:24pt;color:var(--navy);text-transform:uppercase;letter-spacing:1px}.header p{color:#4a5568;font-weight:600}
.student-info{display:flex;gap:12px;flex-wrap:wrap;justify-content:space-between;font-size:10pt;border:1px solid #cbd5e0;padding:10px 15px;border-radius:8px;background:var(--light);margin-top:14px}
.section-title{background:var(--navy);color:#fff;padding:9px 12px;font-size:12pt;font-weight:800;text-transform:uppercase;border-radius:6px;margin:30px 0 14px;letter-spacing:.5px}
.subsection-title{font-size:11pt;font-weight:800;color:var(--blue);border-bottom:2px solid #ebf8ff;padding-bottom:4px;margin:18px 0 10px}
.rule-card{border:1px solid var(--border);border-left:5px solid #3182ce;background:var(--light);padding:12px 16px;margin-bottom:14px;border-radius:0 8px 8px 0;font-size:9.5pt}
.rule-card strong{color:#2c5282}.formula{font-family:Consolas,'Courier New',monospace;background:#edf2f7;padding:2px 6px;border-radius:4px;font-weight:700}
.trap-box{border:1px solid #feb2b2;border-left:5px solid var(--red);background:#fff5f5;padding:10px 14px;margin-bottom:14px;border-radius:0 8px 8px 0;font-size:9.5pt}.trap-box strong{color:#9b2c2c}
table.ref{width:100%;border-collapse:collapse;font-size:9pt;margin:10px 0}table.ref th,table.ref td{border:1px solid #cbd5e0;padding:7px 9px;text-align:left;vertical-align:top}table.ref th{background:var(--blue);color:#fff;font-size:8pt;text-transform:uppercase}
.question-card{border:1px solid var(--border);border-radius:8px;padding:14px 16px;margin-bottom:14px;page-break-inside:avoid;background:#fff}
.question-header{font-weight:800;font-size:10pt;display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.difficulty-badge{padding:3px 8px;font-size:7.5pt;font-weight:800;border-radius:4px;color:#fff}.easy{background:var(--green)}.medium{background:var(--orange)}.hard{background:var(--red)}
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
<title>Digital SAT Punctuation Masterclass & 30-Question Practice Guide</title>
<style>{CSS}</style>
</head>
<body>
<nav class="topbar"><strong>SAT Punctuation</strong><a href="#rules">Rules</a><a href="#practice">Practice 30</a><a href="#key">Answer Key</a><span class="spacer"></span><button onclick="toggleAll(true)">Show all answers</button><button onclick="toggleAll(false)">Hide</button><button onclick="doPrint()">Print / PDF</button></nav>
<div class="header"><h1>SAT Punctuation Masterclass</h1><p>College Board-Aligned Rules & 30-Question Progressive Practice — Digital SAT Reading & Writing</p></div>
<div class="student-info"><span><strong>Name:</strong> _______________________</span><span><strong>Date:</strong> ______________</span><span><strong>Target:</strong> R&W 700+</span><span><strong>Time:</strong> 32 min</span></div>

<div class="section-title" id="rules">Module 1: SAT Punctuation Rules (What the Test Actually Tests)</div>
<div class="subsection-title">How to attack any punctuation question — 3-step method</div>
<div class="rule-card"><strong>1. Find the clause types.</strong> Is the text before the blank an Independent Clause (IC = full sentence) or Dependent/Fragment? Is the text after an IC, list, or modifier?<br><strong>2. Apply the allowed patterns only.</strong> SAT has a closed set — if it is not on the list, it is wrong.<br><strong>3. Check matching & traps.</strong> Pairs must match (comma–comma, dash–dash); never separate subject–verb or verb–object; colon never follows a verb/preposition.</div>

<div class="subsection-title">1. Sentence boundaries — the #1 SAT skill</div>
<div class="rule-card">Two ICs can be joined in <strong>only 4 ways</strong>:<br>• <span class="formula">IC . IC</span> period<br>• <span class="formula">IC ; IC</span> semicolon<br>• <span class="formula">IC , FANBOYS IC</span> — comma + For / And / Nor / But / Or / Yet / So<br>• <span class="formula">IC : IC</span> colon, only when clause 2 explains/amplifies clause 1<br><br>Conjunctive adverbs (however, therefore, moreover, consequently, furthermore) are <strong>not</strong> FANBOYS: use <span class="formula">IC ; however, IC</span>.</div>
<div class="trap-box"><strong>Comma splice = always wrong:</strong> <span class="formula">IC , IC</span> ✗. Run-on <span class="formula">IC IC</span> ✗. Semicolon + FANBOYS (<span class="formula">IC ; but IC</span>) ✗. Comma + conjunctive adverb (<span class="formula">IC , however IC</span>) ✗.</div>

<div class="subsection-title">2. Colons — strict entry condition</div>
<div class="rule-card"><strong>Before a colon must be a complete IC.</strong> After can be a list, single noun, phrase, or explaining IC: <span class="formula">IC : list / detail / explanation</span>.<br>Single dash <span class="formula">—</span> introducing an explanation works identically: <span class="formula">IC — explanation</span>.</div>
<div class="trap-box"><strong>Colon trap:</strong> never after a verb or preposition. ✗ <em>The obstacles are: cost, rules...</em> ✓ <em>The obstacles are cost, rules...</em> ✓ <em>Three obstacles remain: cost, rules...</em></div>

<div class="subsection-title">3. Semicolons — only 2 jobs</div>
<div class="rule-card">1) <span class="formula">IC ; IC</span> (no conjunction). 2) Super-separator in complex lists: <span class="formula">Tokyo, Japan ; Paris, France ; Nairobi, Kenya</span>. Nothing else. A semicolon can never join IC + fragment, DC + IC, or close a modifier.</div>

<div class="subsection-title">4. Commas — 5 legal uses, 5 bans</div>
<div class="rule-card"><strong>Use comma for:</strong> 1) <span class="formula">IC , FANBOYS IC</span> 2) <span class="formula">DC , IC</span> (Although..., ...) 3) Intro phrase <span class="formula">Phrase , IC</span> 4) Nonessential pair <span class="formula">, phrase ,</span> 5) Simple list <span class="formula">A , B , and C</span> (Oxford comma expected).</div>
<div class="trap-box"><strong>Never use a single comma to:</strong> 1) separate subject–verb 2) separate verb–object 3) surround <em>that</em> (restrictive) 4) join two verbs of one subject (<em>surveyed... and recorded...</em>) 5) separate comparison (<em>better... than...</em>).</div>

<div class="subsection-title">5. Dashes & nonessential elements — matching rule</div>
<div class="rule-card">Removable info must be wrapped in <strong>matching</strong> marks: <span class="formula">, X ,</span> or <span class="formula">— X —</span> or <span class="formula">( X )</span>. Open dash → close dash. Open comma → close comma. Mixing (— X ,) is always wrong.</div>

<div class="subsection-title">6. That / Which / Who (+ essential vs. nonessential names)</div>
<div class="rule-card">• <strong>that</strong> = restrictive, essential, <strong>no commas</strong>: <em>fluids that support...</em><br>• <strong>which / who</strong> non-restrictive = extra info, <strong>comma before</strong>: <em>fluids, which support...</em><br>• Title + Name without article = essential, no commas: <em>novelist Isabel Allende spent...</em><br>• General noun + <em>, Name ,</em> = nonessential: <em>A researcher, Dr. Vance, published...</em> / <em>The astronomer, Carl Sagan, studied...</em></div>

<div class="subsection-title">7. Apostrophes & possessive pronouns (high-yield table)</div>
<table class="ref"><tr><th>Situation</th><th>Form</th><th>Example</th></tr>
<tr><td>Singular noun</td><td><span class="formula">'s</span></td><td>researcher's notebook</td></tr>
<tr><td>Plural ending in s</td><td><span class="formula">s'</span></td><td>technicians' reports</td></tr>
<tr><td>Irregular plural</td><td><span class="formula">'s</span></td><td>children's room</td></tr>
<tr><td>Possessive pronoun (no apostrophe ever)</td><td>its / their / whose / your</td><td>its fur (≠ it's = it is)</td></tr>
<tr><td>Contraction</td><td>it's / they're / who's / you're</td><td>it's = it is; they're = they are</td></tr></table>
<div class="trap-box"><strong>its' never exists. researchers's never exists for regular plurals.</strong> Check singular vs. plural from context ('the lead researcher' → singular).</div>

<div class="section-title" id="practice">Module 2: 30 SAT-Style Practice Questions</div>
<div class="subsection-title">Level 1: Foundation (1–10) · Level 2: Standard (11–20) · Level 3: Traps (21–30) — click an option, then Show answer</div>
RENDER_Q
<div class="page-break"></div>
<div class="section-title" id="key">Module 3: Answer Key & Explanations</div>
<table class="answer-key-table"><thead><tr><th style="width:5%">#</th><th style="width:8%">Ans</th><th style="width:14%">Category</th><th>Why</th></tr></thead><tbody>
RENDER_KEY
</tbody></table>
<script>{JS}</script>
</body></html>"""

HTML = HTML.replace("RENDER_Q", render_questions()).replace("RENDER_KEY", render_key_rows())
out = pathlib.Path(__file__).with_name("SAT_Punctuation_Masterclass.html")
out.write_text(HTML, encoding="utf-8")
print(f"Generated {out} with {len(QUESTIONS)} questions.")
