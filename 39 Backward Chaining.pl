% ---------- FACTS ----------
has_wings.
cannot_fly.

% ---------- RULES ----------
can_fly :- has_wings.

bird(eagle) :- can_fly.
bird(penguin) :- cannot_fly.

% ---------- BACKWARD CHAINING RULES ----------
infer(X) :- bird(X).                     % If X is a bird
infer(X) :- can_fly, X = eagle.          % If it can fly → eagle
infer(X) :- cannot_fly, X = penguin.     % If it cannot fly → penguin
