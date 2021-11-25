from datetime import date
from Epytoml.Notaker import Notaker as ntk
from Epytoml import EpyBake as bk

ntk.ntk_authors[1] = ["q", "a"]
ntk.ntk_authors[2] = ["w", "b"]
ntk.ntk_authors[3] = ["e", "c"]
ntk.ntk_authors[4] = ["r", "d"]

ntk.makeTitle(ntk.ntk_authors)

print(ntk.ntk_ContMakeTitle)
