stag(_).
malattie([raffreddore,febbre,malditesta,polmonite,bronchite]).
raffreddore:-tosse, starnuti, congestioneNasale.
febbre:- sudorazione, brividi, doloriMuscolari, stanchezza.
malditesta:- nausea, vomito, fotofobia.
polmonite:- respirazioneAffanosa, tosseSecca,tosseGrassa.
bronchite:- respirazioneAffanosa, tosse, fiatoCorto, respiroSibilante, tossePersistente.


tosse:- evidence(stag(ST), true), (ST=estate, tosse(0.3);
                                   ST=autunno,tosse(0.7); 
                                   ST=inverno, tosse(0.9); 
                                   ST=primavera, tosse(0.6)
                                  ).
starnuti:- evidence(stag(ST), true), (ST=estate, starnuti(0.1);
                                      ST=autunno, starnuti(0.5);
                                      ST=inverno, starnuti(0.6);
                                      ST=primavera, starnuti(0.5)
                                     ).
congestioneNasale:- evidence(stag(ST), true), (ST = inverno, congestioneNasale(0.3);
                                               ST=autunno, congestioneNasale(0.6);
                                               ST=inverno, congestioneNasale(0.7);
                                               ST=primavera, congestioneNasale(0.7)
                                              ).

sudorazione:- evidence(stag(ST), true), (ST = inverno, sudorazione(0.5);
                                   ST=autunno, sudorazione(0.5); 
                                   ST=inverno, sudorazione(0.5); 
                                   ST=primavera, sudorazione(0.5)
                                  ).
brividi:- evidence(stag(ST), true), (ST = inverno, brividi(0.5);
                                   ST=autunno, brividi(0.5); 
                                   ST=inverno, brividi(0.5); 
                                   ST=primavera, brividi(0.5)
                                  ).
doloriMuscolari:- evidence(stag(ST), true), (ST = inverno, doloriMuscolari(0.5);
                                   ST=autunno, doloriMuscolari(0.5); 
                                   ST=inverno, doloriMuscolari(0.5); 
                                   ST=primavera, doloriMuscolari(0.5)
                                  ). 
stanchezza:- evidence(stag(ST), true), (ST = inverno, stanchezza(0.5);
                                   ST=autunno, stanchezza(0.5); 
                                   ST=inverno, stanchezza(0.5); 
                                   ST=primavera, stanchezza(0.5)
                                  ).
nausea:- evidence(stag(ST), true), (ST = inverno, nausea(0.5);
                                   ST=autunno, nausea(0.5); 
                                   ST=inverno, nausea(0.5); 
                                   ST=primavera, nausea(0.5)
                                  ).
vomito:- evidence(stag(ST), true), (ST = inverno, vomito(0.5);
                                   ST=autunno, vomito(0.5); 
                                   ST=inverno, vomito(0.5); 
                                   ST=primavera, vomito(0.5)
                                  ).
fotofobia:- evidence(stag(ST), true), (ST = inverno, fotofobia(0.5);
                                   ST=autunno, fotofobia(0.5); 
                                   ST=inverno, fotofobia(0.5); 
                                   ST=primavera, fotofobia(0.5)
                                  ).
respirazioneAffanosa:- evidence(stag(ST), true), (ST = inverno, respirazioneAffanosa(0.3);
                                   ST=autunno, respirazioneAffanosa(0.6); 
                                   ST=inverno, respirazioneAffanosa(0.7); 
                                   ST=primavera, respirazioneAffanosa(0.8)
                                  ).
tosseSecca:- evidence(stag(ST), true), (ST = inverno, tosseSecca(0.3);
                                   ST=autunno, tosseSecca(0.8); 
                                   ST=inverno, tosseSecca(0.5); 
                                   ST=primavera, tosseSecca(0.5)
                                  ).
tosseGrassa:- evidence(stag(ST), true), (ST = inverno, tosseGrassa(0.2);
                                   ST=autunno, tosseGrassa(0.7); 
                                   ST=inverno, tosseGrassa(0.8); 
                                   ST=primavera, tosseGrassa(0.4)
                                  ).
fiatoCorto:- evidence(stag(ST), true), (ST = inverno, fiatoCorto(0.5);
                                   ST=autunno, fiatoCorto(0.5); 
                                   ST=inverno, fiatoCorto(0.5); 
                                   ST=primavera, fiatoCorto(0.5)
                                  ).
respiroSibilante:- evidence(stag(ST), true), (ST = inverno, respiroSibilante(0.4);
                                   ST=autunno, respiroSibilante(0.7); 
                                   ST=inverno, respiroSibilante(0.6); 
                                   ST=primavera, respiroSibilante(0.5)
                                  ).
tossePersistente:- evidence(stag(ST), true), (ST = inverno, tossePersistente(0.3);
                                   ST=autunno, tossePersistente(0.7); 
                                   ST=inverno, tossePersistente(0.8); 
                                   ST=primavera, tossePersistente(0.4)
                                  ).
P::tossePersistente(P).
P::respiroSibilante(P).
P::fiatoCorto(P).
P::tosseGrassa(P).
P::tosseSecca(P).
P::fotofobia(P).
P::vomito(P).
P::nausea(P).
P::stanchezza(P).
P::doloriMuscolari(P).
P::brividi(P).
P::sudorazione(P).
P::congestioneNasale(P).
P::starnuti(P).
P::tosse(P).
P::respirazioneAffanosa(P).