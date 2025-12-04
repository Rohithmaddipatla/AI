% ---------- FACTS ----------
has_wings.
cannot_fly.

% ---------- RULES ----------
can_fly :- has_wings.

bird(eagle) :- can_fly.
bird(penguin) :- cannot_fly.

% ---------- FORWARD CHAINING RULE ----------
infer(X) :- bird(X).
