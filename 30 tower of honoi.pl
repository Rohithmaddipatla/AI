% Towers of Hanoi
% hanoi(N, Source, Auxiliary, Destination)

hanoi(0, _, _, _) :- 
    !.   % No moves needed for 0 disks

hanoi(N, Source, Aux, Dest) :-
    N > 0,
    M is N - 1,
    hanoi(M, Source, Dest, Aux),
    move(Source, Dest),
    hanoi(M, Aux, Source, Dest).

move(X, Y) :-
    write('Move disk from '), write(X),
    write(' to '), write(Y), nl.
