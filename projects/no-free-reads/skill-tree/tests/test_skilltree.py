import copy,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import skilltree_cli as st
class SkillTreeTests(unittest.TestCase):
    def setUp(self): self.t=st.read("skills.json");self.a=st.read("track-development-matrix.json");self.l=st.read("learning-ledger.json")
    def test_valid(self): self.assertEqual([],st.validate(self.t,self.a,self.l))
    def test_cycle_rejected(self):
        t=copy.deepcopy(self.t);t["nodes"][0]["requires"]=[t["nodes"][-1]["id"]]
        self.assertTrue(any("cycle" in x for x in st.validate(t,self.a,self.l)))
    def test_provenance_rejected(self):
        l=copy.deepcopy(self.l);next(x for x in l if x["record_id"]=="HEARD-001")["verbatim"]="overwritten"
        self.assertTrue(any("listener quote" in x for x in st.validate(self.t,self.a,l)))
    def test_all_still_unapproved(self):
        self.assertTrue(all(x["status"]=="SEED" for x in self.t["nodes"]))
        self.assertTrue(all(x["canon_status"]=="UNAPPROVED" for x in self.a))
if __name__=="__main__": unittest.main()
