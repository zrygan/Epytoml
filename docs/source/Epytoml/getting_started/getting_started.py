from Epytoml import EpyBake
from Epytoml import Notaker

H = Notaker.headerClass()

Notaker.ntkGen("Getting Started with Epytoml and Notaker")

Notaker.makeTitle(
    {1: ["John", "Doe"], 2: ["Jane", "Doe"]},
    {"month": "November", "day": "25", "year": "2021"},
)

H.h("Getting Started with Notaker")

Notaker.hh("Headers in Notaker")

Notaker.t("Quick fox jumps nightly above wizard.")
Notaker.tL("Public junk dwarves hug my quartz fox.")
Notaker.tL("----------")
Notaker.t("Pack my box with five dozen liquor jugs.")
Notaker.t("The quick brown fox jumps over the lazy dog.")

Notaker.ntkShut()

EpyBake.preBake("ntk")

EpyBake.ntkBake("sample_1")
