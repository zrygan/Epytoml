from Notaker import Notaker as ntk
from Bake import ntkBake as bk

ntk.ntkGen("Test 1")
ntk.h1("Chapter 1")
ntk.h1("Chapter 2")
ntk.toc(2)
ntk.ntkShut()

bk()
