from Epytoml import Notaker as ntk
from Epytoml import ShortcutMiner as mine
from Epytoml import EpyBake as bk
from Epytoml import Meaningless as mn

head = ntk.headerClass()
short = ntk.shortcutsClass()
auto = ntk.automationClass()

articleShortcuts = {
    1: ["`!1", "Python"],
    2: ["`!2", "to"],
    3: ["`!3", "the"],
    4: ["`!4", "a"],
    5: ["`!5", "is"],
    6: ["`!6", "and"],
    7: ["`!7", "of"],
    8: ["`!8", "language"],
    9: ["`!9", "in"],
    10: ["`!10", "C"],
    11: ["`!11", "it"],
    12: ["`!12", "an"],
    13: ["`!13", "programming"],
    14: ["`!14", "programmer"],
}

short.mergeShortcut(articleShortcuts)

sampleFileName = "Sample Epytoml"

ntk.ntkGen(sampleFileName)

chapter1 = "Introduction to Epytoml"

head.h(chapter1)
auto.autoLink(chapter1)

ntk.tL(
    "Epytomil (The Epitome of Python to Markup Language), is a python package that converts plain text into a specified markup language using python.",
    "b",
)

ntk.note(
    "Please note that this project is usable and stable, however most functions and modules are underdevelopment."
)

chapter2 = "Getting Started"

head.h(chapter2)
auto.autoLink(chapter2)

ntk.hh("Randomly Generated Text Using Meaningless")

text1 = mn.deadText(250, 7, 1)

ntk.t(text1)

line = mn.horiLine(240)

ntk.h3("Wikipedia article on the Python programming language!")

ntk.tL(
    """`!1 `!5 `!12 open source `!13 `!8
that was made `!2 be easy-`!2-read `!6 powerful. A Dutch `!14
named Guido van Rossum made `!1 `!9 1991. He named `!11 after `!3
television show Monty `!1's Flying Circus. Many `!1 examples
`!6 tutorials include jokes from `!3 show. `!1 `!5 `!12 interpreted
`!8. Interpreted languages do not need `!2 be compiled `!2 run.
A program called `!12 interpreter runs `!1 code on almost any kind
`!7 computer. This means that `!4 `!14 can change `!3 code `!6
quickly see `!3 results. This also means `!1 `!5 slower than `!4
compiled `!8 like `!10, because `!11 `!5 not running machine code
directly. `!1 `!5 `!4 good `!13 `!8 for beginners.
It `!5 `!4 high-level `!8, which means `!4 `!14 can focus
on what `!2 do instead `!7 how `!2 do `!11. Writing programs `!9 `!1
takes less time than `!9 some other languages.`!1 drew inspiration
from other `!13 languages like `!10, `!10++, Java, Perl, `!6 Lisp.
`!1's developers try `!2 avoid changing `!3 `!8 `!2 make `!11
better until they have `!4 lot `!7 things `!2 change. Also, they try not
`!2 make small repairs, called patches, `!2 unimportant parts `!7 `!3
CPython reference implementation that would make `!11 faster. When speed
`!5 important, `!4 `!1 `!14 can move some `!7 `!3 work `!7 `!3
program `!2 other parts written `!9 `!13 languages like `!10 or
PyPy, `!4 just-`!9-time compiler. It translates `!4 `!1 script into
`!10 `!6 makes direct `!10-level API calls into `!3 `!1 interpreter.
Keeping `!1 fun `!2 use `!5 `!12 important goal `!7 `!1 ’s developers.
It reflects `!9 `!3 `!8's name, `!4 tribute `!2 `!3 British comedy group
Monty `!1. On occasions, they are playful approaches `!2 tutorials `!6
reference materials, such as referring `!2 spam `!6 eggs instead `!7 `!3
standard foo `!6 bar."""
)

ntk.lightUp(line, "black", "red")

head.toc(3)

short.readMain()

ntk.ntkShut()

bk.ntkBake(ntk.ntk_ContWhole, "example")
