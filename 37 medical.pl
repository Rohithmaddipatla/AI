ask(Patient, Symptom, Reply) :-
    write('Does '), write(Patient), write(' have '),
    write(Symptom), write(' (y/n)? '),
    read(Reply).

diagnose :-
    write('Enter patient name: '),
    read(P),
    ask(P, fever, F),
    ask(P, cough, C),
    ask(P, runny_nose, RN),
    ask(P, rash, R),
    ask(P, headache, H),
    decide(P, F, C, RN, R, H).

decide(P, y, y, y, y, _) :-
    write(P), write(' probably has measles.'), nl.
decide(P, y, _, y, y, y) :-
    write(P), write(' probably has german_measles.'), nl.
decide(P, y, y, _, _, y) :-
    write(P), write(' probably has flu.'), nl.
decide(P, _, _, _, _, _) :-
    write(P), write(' probably has unknown.'), nl.
