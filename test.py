from datetime import date
from Epytoml.Notaker import Notaker as ntk
from Epytoml import EpyBake as bk

ntk.ntk_authors[1] = ["q", "a"]
ntk.ntk_authors[2] = ["w", "b"]
ntk.ntk_authors[3] = ["e", "c"]
ntk.ntk_authors[3] = ["r", "d"]


ntk.ntk_date["year"] = date.today().year
ntk.ntk_date["month"] = date.today().month
ntk.ntk_date["day"] = date.today().day

ntk.makeTitle(ntk.ntk_authors, ntk.ntk_date)
