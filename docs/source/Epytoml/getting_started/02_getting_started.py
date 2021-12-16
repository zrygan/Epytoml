from Epytoml import EpyBake
from Epytoml import Notaker

Notaker.ntkGen("Using Other Notaker Functions")

Notaker.makeTitle({1: ["John", "Doe"]})

Notaker.h3("These two texts have 10 blank lines in between them")

Notaker.t("Woven silk pyjamas exchanged for blue quartz.")

Notaker.nl(10)

Notaker.t("My girl wove six dozen plaid jackets before she quit.")

Notaker.h3("Making texts glow")

Notaker.lightUp("Make this text glow")

Notaker.nl(3)

Notaker.lightUpBlock("The whole text box is highlighted!")

Notaker.lightUpBlockS()

Notaker.hh("This Header is highlighted")

Notaker.tL("Foo")
Notaker.tL("Bar")
Notaker.tL("Baz")
Notaker.tL("qux")
Notaker.tL("quux")
Notaker.tL("quuz")

Notaker.lightUpBlockE()

Notaker.hh("Adding Notes")

Notaker.t("Grumpy wizards make a toxic brew for the jovial queen.")

Notaker.note("This is a note sample")

Notaker.ntkShut()

EpyBake.preBake("ntk")
