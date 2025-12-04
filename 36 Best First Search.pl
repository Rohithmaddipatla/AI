% ---------- Graph Edges ----------
edge(0, 1, 3).
edge(0, 2, 6).
edge(0, 3, 5).
edge(1, 4, 9).
edge(1, 5, 8).
edge(2, 6, 12).
edge(2, 7, 14).
edge(3, 8, 7).
edge(8, 9, 5).
edge(8, 10, 6).
edge(9, 11, 1).
edge(9, 12, 10).
edge(9, 13, 2).

% Undirected graph
connected(X, Y, C) :- edge(X, Y, C).
connected(X, Y, C) :- edge(Y, X, C).

% ---------- Best First Search ----------
best_first_search(Start, Goal) :-
    bestfs([0-Start], Goal, []).

% If the current node is Goal, print it
bestfs([_ - Goal | _], Goal, _) :-
    write(Goal), nl, !.

% Expand the next node
bestfs([_ - Node | Rest], Goal, Visited) :-
    write(Node), write(' '),

    findall(Cost - Child,
            (connected(Node, Child, Cost),
             \+ member(Child, Visited)),
            Children),

    keysort(Children, SortedChildren),

    append(SortedChildren, Rest, NewQueue),

    bestfs(NewQueue, Goal, [Node | Visited]).
