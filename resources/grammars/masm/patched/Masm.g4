/**
 * Derived from the upstream MASM grammar in antlr/grammars-v4:
 * https://github.com/antlr/grammars-v4/tree/master/asm/masm
 *
 * The upstream grammar is educational and intentionally narrow. This patched
 * variant broadens support for modern MASM source layout used by Masma:
 * `.code/.data/.data?/.const`, `include/includelib`, `PROC/ENDP`,
 * `STRUCT/ENDS`, `UNION/ENDS`, `MACRO/ENDM`, `TYPEDEF`, labels,
 * data declarations, structured directives, conditional-assembly directives,
 * macro-loop directives (FOR/IRP/REPT/WHILE), and free-form instruction lines.
 */
grammar Masm;

compilationUnit
    : (line | EOL)* EOF
    ;

line
    : statement? EOL+
    ;

statement
    : includeStmt
    | equStmt
    | typedefStmt
    | namedSegmentStmt
    | simpleSegmentStmt
    | structStartStmt
    | unionStartStmt
    | structEndStmt
    | macroStartStmt
    | endmStmt
    | condAssembleStmt
    | condAssembleElse
    | condAssembleEndif
    | macroLoopStmt
    | procStartStmt
    | procEndStmt
    | labelStmt
    | dataDeclStmt
    | structuredDirectiveStmt
    | endStmt
    | instructionStmt
    ;

includeStmt
    : (INCLUDE | INCLUDELIB) lineItems?
    ;

equStmt
    : identifier EQU lineItems?
    ;

typedefStmt
    : identifier TYPEDEF lineItems?
    ;

namedSegmentStmt
    : identifier SEGMENT lineItems?
    ;

simpleSegmentStmt
    : DATA_SEG
    | DATAQ_SEG
    | CONST_SEG
    | CODE_SEG
    ;

structStartStmt
    : identifier STRUCT lineItems?
    ;

unionStartStmt
    : identifier UNION lineItems?
    ;

structEndStmt
    : identifier ENDS
    | ENDS
    ;

macroStartStmt
    : identifier MACRO lineItems?
    ;

endmStmt
    : ENDM
    ;

condAssembleStmt
    : (IFDEF | IFNDEF | IF1 | IF2 | IF_BARE | ELSEIF_BARE) lineItems?
    ;

condAssembleElse
    : ELSE_BARE
    ;

condAssembleEndif
    : ENDIF_BARE
    ;

macroLoopStmt
    : (FOR | FORC | IRP | IRPC | REPT | WHILE_BARE) lineItems?
    ;

procStartStmt
    : identifier PROC lineItems?
    ;

procEndStmt
    : identifier ENDP
    ;

labelStmt
    : identifier COLON
    ;

dataDeclStmt
    : identifier dataType lineItems?
    ;

structuredDirectiveStmt
    : structuredDirective lineItems?
    ;

endStmt
    : END lineItems?
    ;

instructionStmt
    : lineItems
    ;

lineItems
    : lineAtom+
    ;

lineAtom
    : WORD
    | STRING
    | COLON
    | dataType
    | structuredDirective
    ;

identifier
    : WORD
    ;

INCLUDE         : I N C L U D E ;
INCLUDELIB      : I N C L U D E L I B ;
EQU             : E Q U ;
TYPEDEF         : T Y P E D E F ;
PROC            : P R O C ;
ENDP            : E N D P ;
STRUCT          : S T R U C T ;
UNION           : U N I O N ;
ENDS            : E N D S ;
MACRO           : M A C R O ;
ENDM            : E N D M ;
END             : E N D ;
SEGMENT         : S E G M E N T ;

// Conditional assembly directives (bare, no dot)
IFDEF           : I F D E F ;
IFNDEF          : I F N D E F ;
IF1             : I F '1' ;
IF2             : I F '2' ;
IF_BARE         : I F ;
ELSEIF_BARE     : E L S E I F ;
ELSE_BARE       : E L S E ;
ENDIF_BARE      : E N D I F ;

// Macro-loop directives (bare, end with ENDM)
FOR             : F O R ;
FORC            : F O R C ;
IRP             : I R P ;
IRPC            : I R P C ;
REPT            : R E P T ;
WHILE_BARE      : W H I L E ;

DATA_SEG        : '.' D A T A ;
DATAQ_SEG       : '.' D A T A '?' ;
CONST_SEG       : '.' C O N S T ;
CODE_SEG        : '.' C O D E ;
IF_DIR          : '.' I F ;
ELSEIF_DIR      : '.' E L S E I F ;
ELSE_DIR        : '.' E L S E ;
ENDIF_DIR       : '.' E N D I F ;
WHILE_DIR       : '.' W H I L E ;
ENDW_DIR        : '.' E N D W ;
REPEAT_DIR      : '.' R E P E A T ;
UNTIL_DIR       : '.' U N T I L ;
UNTILCXZ_DIR    : '.' U N T I L C X Z ;
DB              : D B ;
DW              : D W ;
DD              : D D ;
DQ              : D Q ;
DT              : D T ;
BYTE            : B Y T E ;
WORD_TYPE       : W O R D ;
DWORD           : D W O R D ;
QWORD           : Q W O R D ;
TBYTE           : T B Y T E ;
REAL4           : R E A L '4' ;
REAL8           : R E A L '8' ;
REAL10          : R E A L '1' '0' ;

structuredDirective
    : IF_DIR
    | ELSEIF_DIR
    | ELSE_DIR
    | ENDIF_DIR
    | WHILE_DIR
    | ENDW_DIR
    | REPEAT_DIR
    | UNTIL_DIR
    | UNTILCXZ_DIR
    ;

dataType
    : DB
    | DW
    | DD
    | DQ
    | DT
    | BYTE
    | WORD_TYPE
    | DWORD
    | QWORD
    | TBYTE
    | REAL4
    | REAL8
    | REAL10
    ;

COLON           : ':' ;
STRING
    : '"' ( '\\' . | ~["\\\r\n] )* '"'
    | '\'' ( '\\' . | ~['\\\r\n] )* '\''
    ;
WORD            : ~[ \t\r\n:]+ ;
WS              : [ \t]+ -> skip ;
EOL             : '\r'? '\n' ;

fragment A : [aA] ;
fragment B : [bB] ;
fragment C : [cC] ;
fragment D : [dD] ;
fragment E : [eE] ;
fragment F : [fF] ;
fragment G : [gG] ;
fragment H : [hH] ;
fragment I : [iI] ;
fragment J : [jJ] ;
fragment K : [kK] ;
fragment L : [lL] ;
fragment M : [mM] ;
fragment N : [nN] ;
fragment O : [oO] ;
fragment P : [pP] ;
fragment Q : [qQ] ;
fragment R : [rR] ;
fragment S : [sS] ;
fragment T : [tT] ;
fragment U : [uU] ;
fragment V : [vV] ;
fragment W : [wW] ;
fragment X : [xX] ;
fragment Y : [yY] ;
fragment Z : [zZ] ;
