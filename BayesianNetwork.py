from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete.CPD import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.inference import ApproxInference
from pgmpy.sampling import BayesianModelSampling

medico_model = BayesianNetwork(
    [
        ("Stagione", "Vomito"),
        ("Stagione", "Fotofobia"),
        ("Stagione", "Nausea"),
        ("Stagione", "Tosse"),
        ("Stagione", "Starnuti"),
        ("Stagione", "CongestioneNasale"),
        ("Stagione", "Stanchezza"),
        ("Stagione", "Sudorazione"),
        ("Stagione", "DoloriMuscolari"),
        ("Stagione", "Brividi"),
        ("Stagione", "RespirazioneAffannosa"),
        ("Stagione", "TosseGrassa"),
        ("Stagione", "TosseSecca"),
        ("Stagione", "TossePersistente"),
        ("Stagione", "FiatoCorto"),
        ("Stagione", "RespiroSibilante"),

        ("Vomito", "Malditesta"),
        ("Fotofobia", "Malditesta"),
        ("Nausea", "Malditesta"),
        
        ("Tosse", "Raffreddore"),
        ("Starnuti", "Raffreddore"),
        ("CongestioneNasale", "Raffreddore"),
        
        ("Stanchezza", "Febbre"),
        ("Sudorazione", "Febbre"),
        ("DoloriMuscolari", "Febbre"),
        ("Brividi", "Febbre"),
        
        ("RespirazioneAffannosa", "Polmonite"),
        ("TosseSecca", "Polmonite"),
        ("TosseGrassa", "Polmonite"),
        
        ("FiatoCorto", "Bronchite"),
        ("RespiroSibilante", "Bronchite"),
        ("TossePersistente", "Bronchite"),
        ("RespirazioneAffannosa", "Bronchite"),

    ]
)

#Nodo genitore rete
cpd_Stagione = TabularCPD(
   variable="Stagione", variable_card=4, values = [[0.25],[0.25],[0.25],[0.25]]
)
#-------------Nodi padri: Mal di testa-------------
cpd_fotofobia = TabularCPD(
   variable="Fotofobia",
   variable_card=2,
   values = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_vomito = TabularCPD(
   variable="Vomito",
   variable_card=2,
   values = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_nausea = TabularCPD(
   variable="Nausea",
   variable_card=2,
   values = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)

#-------------Nodi padri:_Raffreddore-------------
cpd_tosse = TabularCPD(
   variable="Tosse",
   variable_card=2,
   values = [[0.3, 0.7, 0.9, 0.6], [0.7, 0.3, 0.1, 0.4]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_starnuti = TabularCPD(
   variable="Starnuti",
   variable_card=2,
   values = [[0.1, 0.5, 0.6, 0.5], [0.9, 0.5, 0.4, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_congestioneNasale = TabularCPD(
   variable="CongestioneNasale",
   variable_card=2,
   values = [[0.3, 0.6, 0.7, 0.7], [0.7, 0.4, 0.3, 0.3]],
   evidence = ["Stagione"],
   evidence_card = [4],
)


#-------------Nodi padri:_Febbre-------------
cpd_stanchezza = TabularCPD(
   variable="Stanchezza",
   variable_card=2,
   values = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_brividi = TabularCPD(
   variable="Brividi",
   variable_card=2,
   values = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_sudorazione = TabularCPD(
   variable="Sudorazione",
   variable_card=2,
   values = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_doloriMuscolari = TabularCPD(
   variable="DoloriMuscolari",
   variable_card=2,
   values = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)

#-------------Nodi padri:_Polmonite-------------
cpd_tosseGrassa = TabularCPD(
   variable="TosseGrassa",
   variable_card=2,
   values = [[0.2, 0.7, 0.8, 0.4], [0.8, 0.3, 0.2, 0.6]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_tosseSecca = TabularCPD(
   variable="TosseSecca",
   variable_card=2,
   values = [[0.3, 0.8, 0.5, 0.5], [0.7, 0.2, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_respirazioneAffannosa = TabularCPD(
   variable="RespirazioneAffannosa",
   variable_card=2,
   values = [[0.3, 0.6, 0.7, 0.8], [0.7, 0.4, 0.3, 0.2]],
   evidence = ["Stagione"],
   evidence_card = [4],
)

#-------------Nodi padri:_Bronchite-------------
cpd_fiatoCorto = TabularCPD(
   variable="FiatoCorto",
   variable_card=2,
   values = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_respiroSibilante = TabularCPD(
   variable="RespiroSibilante",
   variable_card=2,
   values = [[0.4, 0.7, 0.6, 0.5], [0.6, 0.3, 0.4, 0.5]],
   evidence = ["Stagione"],
   evidence_card = [4],
)
cpd_tossePersistente = TabularCPD(
   variable="TossePersistente",
   variable_card=2,
   values = [[0.3, 0.7, 0.8, 0.4], [0.7, 0.3, 0.2, 0.6]],
   evidence = ["Stagione"],
   evidence_card = [4],
)


#---------

cpd_malditesta = TabularCPD(
   variable="Malditesta",
   variable_card=2,
   values = [[0.9, 0.45, 0.57, 0.24, 0.6, 0.3, 0.3, 0.2],
             [0.1, 0.55, 0.43, 0.76, 0.4, 0.7, 0.7, 0.8]],
   evidence=["Fotofobia","Nausea","Vomito" ],
   evidence_card = [2, 2, 2],
)
cpd_raffreddore = TabularCPD(
   variable="Raffreddore",
   variable_card=2,
   values = [[0.89, 0.44, 0.65, 0.2, 0.67, 0.36, 0.24, 0.1],
             [0.11, 0.56, 0.35, 0.8, 0.33, 0.64, 0.76, 0.9]],
   evidence=["Tosse","Starnuti","CongestioneNasale" ],
   evidence_card = [2, 2, 2],
)
cpd_polmonite = TabularCPD(
   variable="Polmonite",
   variable_card=2,
   values = [[0.99, 0.4, 0.6, 0.24, 0.34, 0.2, 0.18, 0.1],
             [0.01, 0.6, 0.4, 0.76, 0.66, 0.8, 0.82, 0.9]],
   evidence=["TosseGrassa","TosseSecca","RespirazioneAffannosa" ],
   evidence_card = [2, 2, 2],
)
cpd_bronchite = TabularCPD(
   variable="Bronchite",
   variable_card=2,
   values = [[0.98, 0.47, 0.49, 0.26, 0.25, 0.19, 0.24, 0.15,0.64, 0.24, 0.18, 0.17, 0.24, 0.2, 0.14, 0.09],
             [0.02, 0.53, 0.51, 0.74, 0.75, 0.81, 0.76, 0.85,0.36, 0.76, 0.82, 0.83, 0.76, 0.8, 0.86, 0.91]],
   evidence=["FiatoCorto","RespiroSibilante","TossePersistente","RespirazioneAffannosa"],
   evidence_card = [2, 2, 2, 2],
)

cpd_febbre = TabularCPD(
   variable="Febbre",
   variable_card=2,
   values = [[0.89, 0.48, 0.45, 0.25, 0.4, 0.34, 0.16, 0.12,0.4, 0.3, 0.24, 0.2, 0.25, 0.18, 0.15, 0.1],
             [0.11, 0.52, 0.55, 0.75, 0.6, 0.66, 0.84, 0.88,0.6, 0.7, 0.76, 0.8, 0.75, 0.82, 0.85, 0.9]],
   evidence=["Stanchezza","Brividi","Sudorazione","DoloriMuscolari"],
   evidence_card = [2, 2, 2, 2],
)

medico_model.add_cpds(
    cpd_Stagione, 
    cpd_fotofobia, 
    cpd_vomito, 
    cpd_nausea, 
    cpd_tosse, 
    cpd_starnuti, 
    cpd_congestioneNasale, 
    cpd_stanchezza, 
    cpd_brividi, 
    cpd_sudorazione, 
    cpd_doloriMuscolari, 
    cpd_tosseGrassa, 
    cpd_tosseSecca, 
    cpd_respirazioneAffannosa, 
    cpd_fiatoCorto, 
    cpd_respiroSibilante, 
    cpd_tossePersistente,
    cpd_febbre,
    cpd_bronchite,
    cpd_polmonite,
    cpd_malditesta,
    cpd_raffreddore
)

if __name__ == '__main__':
    
    print("Inferenza esatta con osservazioni")
    model_infer = VariableElimination(medico_model)
    q = model_infer.query(['Raffreddore'], evidence={'Tosse':1,'CongestioneNasale':1})
    print("Raffreddore sapendo di avere la tosse e la congestioneNasale\n",q)
    q = model_infer.map_query(['Raffreddore'], evidence={'Tosse':1,'CongestioneNasale':1})
    print("Classe maggioritaria: ",q)
    print("Inferenza approssimata con osservazioni")
    model_infer = ApproxInference(medico_model)
    q = model_infer.query(['Raffreddore'], evidence={'Tosse':1,'Starnuti':1,'CongestioneNasale':1})
    print("Raffreddore sapendo di avere tutti i sintomi\n",q)
