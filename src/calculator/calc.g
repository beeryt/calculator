start: expression;

expression: add;

// Math expression syntax (PEMDAS)
?add: (add add_symbol)? mul;
?mul: (mul mul_symbol)? exp;
?exp: (exp exp_symbol)? term;
@term: negate | number | '\(' expression '\)';
negate: '-' term;

number: '[\d.]+';
exp_symbol: '\^';
mul_symbol: '\*' | '/' | '%';
add_symbol: '\+' | '-';
WHITESPACE: '[ \t]+' (%ignore);
