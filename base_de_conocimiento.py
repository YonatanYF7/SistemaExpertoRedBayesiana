#base_de_conocimiento.py
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

def construir_red():
    red = BayesianNetwork([
        ('Lluvia', 'Atasco'),
        ('Accidente', 'Atasco'),
        ('Atasco', 'LlegaTarde'),
        ('Lluvia', 'UsaParaguas')
    ])
    
    cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.7], [0.3]])
    cpd_accidente = TabularCPD(variable='Accidente', variable_card=2, values=[[0.8], [0.2]])
    
    cpd_atasco = TabularCPD(variable='Atasco', variable_card=2,
                            values=[[0.9, 0.6, 0.7, 0.1],
                                    [0.1, 0.4, 0.3, 0.9]],
                            evidence=['Lluvia', 'Accidente'],
                            evidence_card=[2, 2])
    
    cpd_llegatarde = TabularCPD(variable='LlegaTarde', variable_card=2,
                                values=[[0.8, 0.3],
                                        [0.2, 0.7]],
                                evidence=['Atasco'],
                                evidence_card=[2])
    
    cpd_usaparaguas = TabularCPD(variable='UsaParaguas', variable_card=2,
                                 values=[[0.9, 0.2],
                                         [0.1, 0.8]],
                                 evidence=['Lluvia'],
                                 evidence_card=[2])
    
    red.add_cpds(cpd_lluvia, cpd_accidente, cpd_atasco, cpd_llegatarde, cpd_usaparaguas)
    
    assert red.check_model()
    
    return red
