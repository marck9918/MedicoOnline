from problog.program import PrologFile, ProbLogObject
from problog.logic import Var,Term
from problog.engine import DefaultEngine
from problog.engine import ClauseDBEngine
from problog import get_evaluatable
from problog.program import PrologFile
from problog.formula import LogicFormula
from problog.core import ProbLogObject
from datetime import datetime
import ast

malattie_kb={}
model =PrologFile('kb.pl')

def datacorrente():
    return datetime.fromtimestamp(datetime.timestamp(datetime.now())).strftime("%d %m %Y")

def stagioneCorrente():
    data = datacorrente()
    giorno = int(data[0:2])
    mese = int(data[3:5])
    if((mese == 12 and giorno>=23) or (mese<3) or (mese == 3 and giorno<=20)):
        stag="inverno"
    if((mese == 3 and giorno>=21) or (3<mese<6) or (mese == 6 and giorno<=21)):
        stag="primavera"
    if((mese == 6 and giorno>=22) or (6<mese<9) or (mese == 9 and giorno<=22)):
        stag="estate"
    if((mese == 9 and giorno>=23) or (9<mese<12) or (mese == 12 and giorno<=22)):
        stag="autunno"
    return stag


def presenzaChiave(key, diz):
    if key in diz:
        return True
    else:
        return False
    
def presenzaValore(val, diz):
    for i in range(0,len(diz)):
        t=diz[i].split(", ")
        if val in t:
            return True

    return False

def listaMalattie():
    return list(malattie_kb.keys())

def estrapolaMalattie():
    
    s = query(Term('query',Term('malattie',Var('A'))))
    start=s.find("[",0,len(s))+1
    end=s.find("]",0,len(s))
    s=s[start:end]
    for x in s.split(", "):
        malattie_kb[x]=""

def estrapolaSintomi():
    for key in malattie_kb:
        malattie_kb[key]=sintomi(key)

def probMalattia(listaSintomi):
    db = DefaultEngine(label_all=True).prepare(model)
    db.add_fact(Term("evidence",Term("stag",Term(stagioneCorrente())),Term("true")))
    
    listaSintomi = listaSintomi.split(",")
    
    for k in listaSintomi:        
        if not presenzaValore(k,list(malattie_kb.values())):
            raise ValueError(k + " non è un sintomo presente nella kb.")
    for k in listaSintomi:
        db.add_fact(Term("evidence",Term(k),Term("true")))
    for key in malattie_kb:
         db.add_fact(Term("query",Term(key)))

 
    prob = str(get_evaluatable().create_from(db).evaluate()).replace("{","").replace("}","").split(", ")
    m=0
    for i in range(0, len(prob)):
        l=prob[i].split(": ")
        n = float(l[1])
        if (n > m):
            m = n
            probMax = l
        
    return probMax

def sintomi(nomeMalattia):
    if not presenzaChiave(nomeMalattia,malattie_kb):
         raise ValueError(nomeMalattia + " non è presente nella lista delle malattie.")
    s = query(Term('query',Term('clause',Term(nomeMalattia),Var('B'))))
    start=s.find(nomeMalattia,0,len(s))+len(nomeMalattia)+2
    s=s[start:len(s)-8]
    malattie_kb[nomeMalattia]=s
    return malattie_kb[nomeMalattia]

def query(term):
    db = DefaultEngine(label_all=True).prepare(model)
    db.add_fact(Term("evidence",Term("stag",Term(stagioneCorrente())),Term("true")))
    db.add_fact(term)
    return str(get_evaluatable().create_from(db).evaluate())

estrapolaMalattie()
estrapolaSintomi()



