# Generated from /Volumes/External/Code/Masma/resources/grammars/masm/patched/Masm.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,83,228,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,5,0,69,8,0,10,0,12,0,72,9,0,1,0,3,0,75,8,0,1,0,1,0,1,1,3,1,80,
        8,1,1,1,4,1,83,8,1,11,1,12,1,84,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,111,8,2,1,3,1,3,3,3,115,8,3,1,4,1,4,3,4,119,8,4,1,5,1,5,3,5,
        123,8,5,1,6,1,6,3,6,127,8,6,1,7,1,7,1,7,3,7,132,8,7,1,8,1,8,1,8,
        3,8,137,8,8,1,9,1,9,1,9,3,9,142,8,9,1,10,1,10,1,11,1,11,1,11,3,11,
        149,8,11,1,12,1,12,1,12,3,12,154,8,12,1,13,1,13,1,13,1,13,3,13,160,
        8,13,1,14,1,14,1,14,3,14,165,8,14,1,15,1,15,1,16,1,16,3,16,171,8,
        16,1,17,1,17,1,18,1,18,1,19,1,19,3,19,179,8,19,1,20,1,20,1,20,3,
        20,184,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,3,23,195,
        8,23,1,24,1,24,3,24,199,8,24,1,25,1,25,3,25,203,8,25,1,26,1,26,1,
        27,4,27,208,8,27,11,27,12,27,209,1,28,1,28,1,28,1,28,1,28,1,28,3,
        28,218,8,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,0,0,33,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,0,9,1,0,1,2,1,0,3,4,1,0,6,10,1,0,52,
        55,1,0,22,43,1,0,46,51,1,0,1,51,1,0,56,64,1,0,65,77,245,0,70,1,0,
        0,0,2,79,1,0,0,0,4,110,1,0,0,0,6,112,1,0,0,0,8,116,1,0,0,0,10,120,
        1,0,0,0,12,124,1,0,0,0,14,128,1,0,0,0,16,133,1,0,0,0,18,138,1,0,
        0,0,20,143,1,0,0,0,22,145,1,0,0,0,24,150,1,0,0,0,26,159,1,0,0,0,
        28,161,1,0,0,0,30,166,1,0,0,0,32,168,1,0,0,0,34,172,1,0,0,0,36,174,
        1,0,0,0,38,176,1,0,0,0,40,180,1,0,0,0,42,185,1,0,0,0,44,188,1,0,
        0,0,46,191,1,0,0,0,48,196,1,0,0,0,50,200,1,0,0,0,52,204,1,0,0,0,
        54,207,1,0,0,0,56,217,1,0,0,0,58,219,1,0,0,0,60,221,1,0,0,0,62,223,
        1,0,0,0,64,225,1,0,0,0,66,69,3,2,1,0,67,69,5,83,0,0,68,66,1,0,0,
        0,68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,74,
        1,0,0,0,72,70,1,0,0,0,73,75,3,4,2,0,74,73,1,0,0,0,74,75,1,0,0,0,
        75,76,1,0,0,0,76,77,5,0,0,1,77,1,1,0,0,0,78,80,3,4,2,0,79,78,1,0,
        0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,83,5,83,0,0,82,81,1,0,0,0,83,
        84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,3,1,0,0,0,86,111,3,6,3,
        0,87,111,3,14,7,0,88,111,3,16,8,0,89,111,3,8,4,0,90,111,3,10,5,0,
        91,111,3,18,9,0,92,111,3,20,10,0,93,111,3,22,11,0,94,111,3,24,12,
        0,95,111,3,26,13,0,96,111,3,28,14,0,97,111,3,30,15,0,98,111,3,32,
        16,0,99,111,3,34,17,0,100,111,3,36,18,0,101,111,3,38,19,0,102,111,
        3,40,20,0,103,111,3,42,21,0,104,111,3,44,22,0,105,111,3,46,23,0,
        106,111,3,48,24,0,107,111,3,12,6,0,108,111,3,50,25,0,109,111,3,52,
        26,0,110,86,1,0,0,0,110,87,1,0,0,0,110,88,1,0,0,0,110,89,1,0,0,0,
        110,90,1,0,0,0,110,91,1,0,0,0,110,92,1,0,0,0,110,93,1,0,0,0,110,
        94,1,0,0,0,110,95,1,0,0,0,110,96,1,0,0,0,110,97,1,0,0,0,110,98,1,
        0,0,0,110,99,1,0,0,0,110,100,1,0,0,0,110,101,1,0,0,0,110,102,1,0,
        0,0,110,103,1,0,0,0,110,104,1,0,0,0,110,105,1,0,0,0,110,106,1,0,
        0,0,110,107,1,0,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,5,1,0,0,
        0,112,114,7,0,0,0,113,115,3,54,27,0,114,113,1,0,0,0,114,115,1,0,
        0,0,115,7,1,0,0,0,116,118,7,1,0,0,117,119,3,54,27,0,118,117,1,0,
        0,0,118,119,1,0,0,0,119,9,1,0,0,0,120,122,5,5,0,0,121,123,3,54,27,
        0,122,121,1,0,0,0,122,123,1,0,0,0,123,11,1,0,0,0,124,126,7,2,0,0,
        125,127,3,54,27,0,126,125,1,0,0,0,126,127,1,0,0,0,127,13,1,0,0,0,
        128,129,3,60,30,0,129,131,5,11,0,0,130,132,3,54,27,0,131,130,1,0,
        0,0,131,132,1,0,0,0,132,15,1,0,0,0,133,134,3,60,30,0,134,136,5,12,
        0,0,135,137,3,54,27,0,136,135,1,0,0,0,136,137,1,0,0,0,137,17,1,0,
        0,0,138,139,3,60,30,0,139,141,5,21,0,0,140,142,3,54,27,0,141,140,
        1,0,0,0,141,142,1,0,0,0,142,19,1,0,0,0,143,144,7,3,0,0,144,21,1,
        0,0,0,145,146,3,60,30,0,146,148,5,15,0,0,147,149,3,54,27,0,148,147,
        1,0,0,0,148,149,1,0,0,0,149,23,1,0,0,0,150,151,3,60,30,0,151,153,
        5,16,0,0,152,154,3,54,27,0,153,152,1,0,0,0,153,154,1,0,0,0,154,25,
        1,0,0,0,155,156,3,60,30,0,156,157,5,17,0,0,157,160,1,0,0,0,158,160,
        5,17,0,0,159,155,1,0,0,0,159,158,1,0,0,0,160,27,1,0,0,0,161,162,
        3,60,30,0,162,164,5,18,0,0,163,165,3,54,27,0,164,163,1,0,0,0,164,
        165,1,0,0,0,165,29,1,0,0,0,166,167,5,19,0,0,167,31,1,0,0,0,168,170,
        7,4,0,0,169,171,3,54,27,0,170,169,1,0,0,0,170,171,1,0,0,0,171,33,
        1,0,0,0,172,173,5,44,0,0,173,35,1,0,0,0,174,175,5,45,0,0,175,37,
        1,0,0,0,176,178,7,5,0,0,177,179,3,54,27,0,178,177,1,0,0,0,178,179,
        1,0,0,0,179,39,1,0,0,0,180,181,3,60,30,0,181,183,5,13,0,0,182,184,
        3,54,27,0,183,182,1,0,0,0,183,184,1,0,0,0,184,41,1,0,0,0,185,186,
        3,60,30,0,186,187,5,14,0,0,187,43,1,0,0,0,188,189,3,60,30,0,189,
        190,5,78,0,0,190,45,1,0,0,0,191,192,3,60,30,0,192,194,3,64,32,0,
        193,195,3,54,27,0,194,193,1,0,0,0,194,195,1,0,0,0,195,47,1,0,0,0,
        196,198,3,62,31,0,197,199,3,54,27,0,198,197,1,0,0,0,198,199,1,0,
        0,0,199,49,1,0,0,0,200,202,5,20,0,0,201,203,3,54,27,0,202,201,1,
        0,0,0,202,203,1,0,0,0,203,51,1,0,0,0,204,205,3,54,27,0,205,53,1,
        0,0,0,206,208,3,56,28,0,207,206,1,0,0,0,208,209,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,55,1,0,0,0,211,218,5,81,0,0,212,218,
        5,79,0,0,213,218,5,78,0,0,214,218,3,64,32,0,215,218,3,62,31,0,216,
        218,3,58,29,0,217,211,1,0,0,0,217,212,1,0,0,0,217,213,1,0,0,0,217,
        214,1,0,0,0,217,215,1,0,0,0,217,216,1,0,0,0,218,57,1,0,0,0,219,220,
        7,6,0,0,220,59,1,0,0,0,221,222,5,81,0,0,222,61,1,0,0,0,223,224,7,
        7,0,0,224,63,1,0,0,0,225,226,7,8,0,0,226,65,1,0,0,0,25,68,70,74,
        79,84,110,114,118,122,126,131,136,141,148,153,159,164,170,178,183,
        194,198,202,209,217
    ]

class MasmParser ( Parser ):

    grammarFileName = "Masm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "INCLUDE", "INCLUDELIB", "EXTERN", "EXTERNDEF", 
                      "PUBLIC", "ALIGN", "ASSUME", "OPTION", "ORG", "EVEN", 
                      "EQU", "TYPEDEF", "PROC", "ENDP", "STRUCT", "UNION", 
                      "ENDS", "MACRO", "ENDM", "END", "SEGMENT", "IFDEF", 
                      "IFNDEF", "IFDIF", "IFDIFI", "IFIDN", "IFIDNI", "IFB", 
                      "IFNB", "IF1", "IF2", "IF_BARE", "ELSEIF_BARE", "ELSEIFDEF", 
                      "ELSEIFNDEF", "ELSEIFDIF", "ELSEIFDIFI", "ELSEIFIDN", 
                      "ELSEIFIDNI", "ELSEIFB", "ELSEIFNB", "ELSEIF1", "ELSEIF2", 
                      "ELSE_BARE", "ENDIF_BARE", "FOR", "FORC", "IRP", "IRPC", 
                      "REPT", "WHILE_BARE", "DATA_SEG", "DATAQ_SEG", "CONST_SEG", 
                      "CODE_SEG", "IF_DIR", "ELSEIF_DIR", "ELSE_DIR", "ENDIF_DIR", 
                      "WHILE_DIR", "ENDW_DIR", "REPEAT_DIR", "UNTIL_DIR", 
                      "UNTILCXZ_DIR", "DB", "DW", "DD", "DQ", "DT", "BYTE", 
                      "WORD_TYPE", "DWORD", "QWORD", "TBYTE", "REAL4", "REAL8", 
                      "REAL10", "COLON", "STRING", "COMMENT", "WORD", "WS", 
                      "EOL" ]

    RULE_compilationUnit = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_includeStmt = 3
    RULE_externStmt = 4
    RULE_publicStmt = 5
    RULE_passThroughDirectiveStmt = 6
    RULE_equStmt = 7
    RULE_typedefStmt = 8
    RULE_namedSegmentStmt = 9
    RULE_simpleSegmentStmt = 10
    RULE_structStartStmt = 11
    RULE_unionStartStmt = 12
    RULE_structEndStmt = 13
    RULE_macroStartStmt = 14
    RULE_endmStmt = 15
    RULE_condAssembleStmt = 16
    RULE_condAssembleElse = 17
    RULE_condAssembleEndif = 18
    RULE_macroLoopStmt = 19
    RULE_procStartStmt = 20
    RULE_procEndStmt = 21
    RULE_labelStmt = 22
    RULE_dataDeclStmt = 23
    RULE_structuredDirectiveStmt = 24
    RULE_endStmt = 25
    RULE_instructionStmt = 26
    RULE_lineItems = 27
    RULE_lineAtom = 28
    RULE_anyKeyword = 29
    RULE_identifier = 30
    RULE_structuredDirective = 31
    RULE_dataType = 32

    ruleNames =  [ "compilationUnit", "line", "statement", "includeStmt", 
                   "externStmt", "publicStmt", "passThroughDirectiveStmt", 
                   "equStmt", "typedefStmt", "namedSegmentStmt", "simpleSegmentStmt", 
                   "structStartStmt", "unionStartStmt", "structEndStmt", 
                   "macroStartStmt", "endmStmt", "condAssembleStmt", "condAssembleElse", 
                   "condAssembleEndif", "macroLoopStmt", "procStartStmt", 
                   "procEndStmt", "labelStmt", "dataDeclStmt", "structuredDirectiveStmt", 
                   "endStmt", "instructionStmt", "lineItems", "lineAtom", 
                   "anyKeyword", "identifier", "structuredDirective", "dataType" ]

    EOF = Token.EOF
    INCLUDE=1
    INCLUDELIB=2
    EXTERN=3
    EXTERNDEF=4
    PUBLIC=5
    ALIGN=6
    ASSUME=7
    OPTION=8
    ORG=9
    EVEN=10
    EQU=11
    TYPEDEF=12
    PROC=13
    ENDP=14
    STRUCT=15
    UNION=16
    ENDS=17
    MACRO=18
    ENDM=19
    END=20
    SEGMENT=21
    IFDEF=22
    IFNDEF=23
    IFDIF=24
    IFDIFI=25
    IFIDN=26
    IFIDNI=27
    IFB=28
    IFNB=29
    IF1=30
    IF2=31
    IF_BARE=32
    ELSEIF_BARE=33
    ELSEIFDEF=34
    ELSEIFNDEF=35
    ELSEIFDIF=36
    ELSEIFDIFI=37
    ELSEIFIDN=38
    ELSEIFIDNI=39
    ELSEIFB=40
    ELSEIFNB=41
    ELSEIF1=42
    ELSEIF2=43
    ELSE_BARE=44
    ENDIF_BARE=45
    FOR=46
    FORC=47
    IRP=48
    IRPC=49
    REPT=50
    WHILE_BARE=51
    DATA_SEG=52
    DATAQ_SEG=53
    CONST_SEG=54
    CODE_SEG=55
    IF_DIR=56
    ELSEIF_DIR=57
    ELSE_DIR=58
    ENDIF_DIR=59
    WHILE_DIR=60
    ENDW_DIR=61
    REPEAT_DIR=62
    UNTIL_DIR=63
    UNTILCXZ_DIR=64
    DB=65
    DW=66
    DD=67
    DQ=68
    DT=69
    BYTE=70
    WORD_TYPE=71
    DWORD=72
    QWORD=73
    TBYTE=74
    REAL4=75
    REAL8=76
    REAL10=77
    COLON=78
    STRING=79
    COMMENT=80
    WORD=81
    WS=82
    EOL=83

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MasmParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasmParser.LineContext)
            else:
                return self.getTypedRuleContext(MasmParser.LineContext,i)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(MasmParser.EOL)
            else:
                return self.getToken(MasmParser.EOL, i)

        def statement(self):
            return self.getTypedRuleContext(MasmParser.StatementContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_compilationUnit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilationUnit" ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = MasmParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 66
                        self.line()
                        pass

                    elif la_ == 2:
                        self.state = 67
                        self.match(MasmParser.EOL)
                        pass

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -2) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 73
                self.statement()


            self.state = 76
            self.match(MasmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MasmParser.StatementContext,0)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(MasmParser.EOL)
            else:
                return self.getToken(MasmParser.EOL, i)

        def getRuleIndex(self):
            return MasmParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = MasmParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -2) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 78
                self.statement()


            self.state = 82 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 81
                    self.match(MasmParser.EOL)

                else:
                    raise NoViableAltException(self)
                self.state = 84 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def includeStmt(self):
            return self.getTypedRuleContext(MasmParser.IncludeStmtContext,0)


        def equStmt(self):
            return self.getTypedRuleContext(MasmParser.EquStmtContext,0)


        def typedefStmt(self):
            return self.getTypedRuleContext(MasmParser.TypedefStmtContext,0)


        def externStmt(self):
            return self.getTypedRuleContext(MasmParser.ExternStmtContext,0)


        def publicStmt(self):
            return self.getTypedRuleContext(MasmParser.PublicStmtContext,0)


        def namedSegmentStmt(self):
            return self.getTypedRuleContext(MasmParser.NamedSegmentStmtContext,0)


        def simpleSegmentStmt(self):
            return self.getTypedRuleContext(MasmParser.SimpleSegmentStmtContext,0)


        def structStartStmt(self):
            return self.getTypedRuleContext(MasmParser.StructStartStmtContext,0)


        def unionStartStmt(self):
            return self.getTypedRuleContext(MasmParser.UnionStartStmtContext,0)


        def structEndStmt(self):
            return self.getTypedRuleContext(MasmParser.StructEndStmtContext,0)


        def macroStartStmt(self):
            return self.getTypedRuleContext(MasmParser.MacroStartStmtContext,0)


        def endmStmt(self):
            return self.getTypedRuleContext(MasmParser.EndmStmtContext,0)


        def condAssembleStmt(self):
            return self.getTypedRuleContext(MasmParser.CondAssembleStmtContext,0)


        def condAssembleElse(self):
            return self.getTypedRuleContext(MasmParser.CondAssembleElseContext,0)


        def condAssembleEndif(self):
            return self.getTypedRuleContext(MasmParser.CondAssembleEndifContext,0)


        def macroLoopStmt(self):
            return self.getTypedRuleContext(MasmParser.MacroLoopStmtContext,0)


        def procStartStmt(self):
            return self.getTypedRuleContext(MasmParser.ProcStartStmtContext,0)


        def procEndStmt(self):
            return self.getTypedRuleContext(MasmParser.ProcEndStmtContext,0)


        def labelStmt(self):
            return self.getTypedRuleContext(MasmParser.LabelStmtContext,0)


        def dataDeclStmt(self):
            return self.getTypedRuleContext(MasmParser.DataDeclStmtContext,0)


        def structuredDirectiveStmt(self):
            return self.getTypedRuleContext(MasmParser.StructuredDirectiveStmtContext,0)


        def passThroughDirectiveStmt(self):
            return self.getTypedRuleContext(MasmParser.PassThroughDirectiveStmtContext,0)


        def endStmt(self):
            return self.getTypedRuleContext(MasmParser.EndStmtContext,0)


        def instructionStmt(self):
            return self.getTypedRuleContext(MasmParser.InstructionStmtContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MasmParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.includeStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.equStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.typedefStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.externStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.publicStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.namedSegmentStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 92
                self.simpleSegmentStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 93
                self.structStartStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 94
                self.unionStartStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 95
                self.structEndStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 96
                self.macroStartStmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 97
                self.endmStmt()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 98
                self.condAssembleStmt()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 99
                self.condAssembleElse()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 100
                self.condAssembleEndif()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 101
                self.macroLoopStmt()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 102
                self.procStartStmt()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 103
                self.procEndStmt()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 104
                self.labelStmt()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 105
                self.dataDeclStmt()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 106
                self.structuredDirectiveStmt()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 107
                self.passThroughDirectiveStmt()
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 108
                self.endStmt()
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 109
                self.instructionStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(MasmParser.INCLUDE, 0)

        def INCLUDELIB(self):
            return self.getToken(MasmParser.INCLUDELIB, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_includeStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncludeStmt" ):
                return visitor.visitIncludeStmt(self)
            else:
                return visitor.visitChildren(self)




    def includeStmt(self):

        localctx = MasmParser.IncludeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_includeStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 113
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExternStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTERN(self):
            return self.getToken(MasmParser.EXTERN, 0)

        def EXTERNDEF(self):
            return self.getToken(MasmParser.EXTERNDEF, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_externStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExternStmt" ):
                return visitor.visitExternStmt(self)
            else:
                return visitor.visitChildren(self)




    def externStmt(self):

        localctx = MasmParser.ExternStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_externStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 117
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PublicStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(MasmParser.PUBLIC, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_publicStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPublicStmt" ):
                return visitor.visitPublicStmt(self)
            else:
                return visitor.visitChildren(self)




    def publicStmt(self):

        localctx = MasmParser.PublicStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_publicStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(MasmParser.PUBLIC)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 121
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassThroughDirectiveStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALIGN(self):
            return self.getToken(MasmParser.ALIGN, 0)

        def ASSUME(self):
            return self.getToken(MasmParser.ASSUME, 0)

        def OPTION(self):
            return self.getToken(MasmParser.OPTION, 0)

        def ORG(self):
            return self.getToken(MasmParser.ORG, 0)

        def EVEN(self):
            return self.getToken(MasmParser.EVEN, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_passThroughDirectiveStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassThroughDirectiveStmt" ):
                return visitor.visitPassThroughDirectiveStmt(self)
            else:
                return visitor.visitChildren(self)




    def passThroughDirectiveStmt(self):

        localctx = MasmParser.PassThroughDirectiveStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_passThroughDirectiveStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 125
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def EQU(self):
            return self.getToken(MasmParser.EQU, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_equStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquStmt" ):
                return visitor.visitEquStmt(self)
            else:
                return visitor.visitChildren(self)




    def equStmt(self):

        localctx = MasmParser.EquStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_equStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.identifier()
            self.state = 129
            self.match(MasmParser.EQU)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 130
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def TYPEDEF(self):
            return self.getToken(MasmParser.TYPEDEF, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_typedefStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedefStmt" ):
                return visitor.visitTypedefStmt(self)
            else:
                return visitor.visitChildren(self)




    def typedefStmt(self):

        localctx = MasmParser.TypedefStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typedefStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.identifier()
            self.state = 134
            self.match(MasmParser.TYPEDEF)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 135
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedSegmentStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def SEGMENT(self):
            return self.getToken(MasmParser.SEGMENT, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_namedSegmentStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedSegmentStmt" ):
                return visitor.visitNamedSegmentStmt(self)
            else:
                return visitor.visitChildren(self)




    def namedSegmentStmt(self):

        localctx = MasmParser.NamedSegmentStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_namedSegmentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.identifier()
            self.state = 139
            self.match(MasmParser.SEGMENT)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 140
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleSegmentStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_SEG(self):
            return self.getToken(MasmParser.DATA_SEG, 0)

        def DATAQ_SEG(self):
            return self.getToken(MasmParser.DATAQ_SEG, 0)

        def CONST_SEG(self):
            return self.getToken(MasmParser.CONST_SEG, 0)

        def CODE_SEG(self):
            return self.getToken(MasmParser.CODE_SEG, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_simpleSegmentStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleSegmentStmt" ):
                return visitor.visitSimpleSegmentStmt(self)
            else:
                return visitor.visitChildren(self)




    def simpleSegmentStmt(self):

        localctx = MasmParser.SimpleSegmentStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_simpleSegmentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67553994410557440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructStartStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def STRUCT(self):
            return self.getToken(MasmParser.STRUCT, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_structStartStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructStartStmt" ):
                return visitor.visitStructStartStmt(self)
            else:
                return visitor.visitChildren(self)




    def structStartStmt(self):

        localctx = MasmParser.StructStartStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.identifier()
            self.state = 146
            self.match(MasmParser.STRUCT)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 147
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionStartStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def UNION(self):
            return self.getToken(MasmParser.UNION, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_unionStartStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionStartStmt" ):
                return visitor.visitUnionStartStmt(self)
            else:
                return visitor.visitChildren(self)




    def unionStartStmt(self):

        localctx = MasmParser.UnionStartStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unionStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.identifier()
            self.state = 151
            self.match(MasmParser.UNION)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 152
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructEndStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def ENDS(self):
            return self.getToken(MasmParser.ENDS, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_structEndStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructEndStmt" ):
                return visitor.visitStructEndStmt(self)
            else:
                return visitor.visitChildren(self)




    def structEndStmt(self):

        localctx = MasmParser.StructEndStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structEndStmt)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [81]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.identifier()
                self.state = 156
                self.match(MasmParser.ENDS)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(MasmParser.ENDS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroStartStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def MACRO(self):
            return self.getToken(MasmParser.MACRO, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_macroStartStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroStartStmt" ):
                return visitor.visitMacroStartStmt(self)
            else:
                return visitor.visitChildren(self)




    def macroStartStmt(self):

        localctx = MasmParser.MacroStartStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_macroStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.identifier()
            self.state = 162
            self.match(MasmParser.MACRO)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 163
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndmStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENDM(self):
            return self.getToken(MasmParser.ENDM, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_endmStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndmStmt" ):
                return visitor.visitEndmStmt(self)
            else:
                return visitor.visitChildren(self)




    def endmStmt(self):

        localctx = MasmParser.EndmStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_endmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MasmParser.ENDM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondAssembleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IFDEF(self):
            return self.getToken(MasmParser.IFDEF, 0)

        def IFNDEF(self):
            return self.getToken(MasmParser.IFNDEF, 0)

        def IFDIF(self):
            return self.getToken(MasmParser.IFDIF, 0)

        def IFDIFI(self):
            return self.getToken(MasmParser.IFDIFI, 0)

        def IFIDN(self):
            return self.getToken(MasmParser.IFIDN, 0)

        def IFIDNI(self):
            return self.getToken(MasmParser.IFIDNI, 0)

        def IFB(self):
            return self.getToken(MasmParser.IFB, 0)

        def IFNB(self):
            return self.getToken(MasmParser.IFNB, 0)

        def IF1(self):
            return self.getToken(MasmParser.IF1, 0)

        def IF2(self):
            return self.getToken(MasmParser.IF2, 0)

        def IF_BARE(self):
            return self.getToken(MasmParser.IF_BARE, 0)

        def ELSEIF_BARE(self):
            return self.getToken(MasmParser.ELSEIF_BARE, 0)

        def ELSEIFDEF(self):
            return self.getToken(MasmParser.ELSEIFDEF, 0)

        def ELSEIFNDEF(self):
            return self.getToken(MasmParser.ELSEIFNDEF, 0)

        def ELSEIFDIF(self):
            return self.getToken(MasmParser.ELSEIFDIF, 0)

        def ELSEIFDIFI(self):
            return self.getToken(MasmParser.ELSEIFDIFI, 0)

        def ELSEIFIDN(self):
            return self.getToken(MasmParser.ELSEIFIDN, 0)

        def ELSEIFIDNI(self):
            return self.getToken(MasmParser.ELSEIFIDNI, 0)

        def ELSEIFB(self):
            return self.getToken(MasmParser.ELSEIFB, 0)

        def ELSEIFNB(self):
            return self.getToken(MasmParser.ELSEIFNB, 0)

        def ELSEIF1(self):
            return self.getToken(MasmParser.ELSEIF1, 0)

        def ELSEIF2(self):
            return self.getToken(MasmParser.ELSEIF2, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_condAssembleStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondAssembleStmt" ):
                return visitor.visitCondAssembleStmt(self)
            else:
                return visitor.visitChildren(self)




    def condAssembleStmt(self):

        localctx = MasmParser.CondAssembleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condAssembleStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17592181850112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 169
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondAssembleElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_BARE(self):
            return self.getToken(MasmParser.ELSE_BARE, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_condAssembleElse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondAssembleElse" ):
                return visitor.visitCondAssembleElse(self)
            else:
                return visitor.visitChildren(self)




    def condAssembleElse(self):

        localctx = MasmParser.CondAssembleElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_condAssembleElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MasmParser.ELSE_BARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondAssembleEndifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENDIF_BARE(self):
            return self.getToken(MasmParser.ENDIF_BARE, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_condAssembleEndif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondAssembleEndif" ):
                return visitor.visitCondAssembleEndif(self)
            else:
                return visitor.visitChildren(self)




    def condAssembleEndif(self):

        localctx = MasmParser.CondAssembleEndifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condAssembleEndif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MasmParser.ENDIF_BARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroLoopStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MasmParser.FOR, 0)

        def FORC(self):
            return self.getToken(MasmParser.FORC, 0)

        def IRP(self):
            return self.getToken(MasmParser.IRP, 0)

        def IRPC(self):
            return self.getToken(MasmParser.IRPC, 0)

        def REPT(self):
            return self.getToken(MasmParser.REPT, 0)

        def WHILE_BARE(self):
            return self.getToken(MasmParser.WHILE_BARE, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_macroLoopStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroLoopStmt" ):
                return visitor.visitMacroLoopStmt(self)
            else:
                return visitor.visitChildren(self)




    def macroLoopStmt(self):

        localctx = MasmParser.MacroLoopStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_macroLoopStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4433230883192832) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 177
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcStartStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def PROC(self):
            return self.getToken(MasmParser.PROC, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_procStartStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcStartStmt" ):
                return visitor.visitProcStartStmt(self)
            else:
                return visitor.visitChildren(self)




    def procStartStmt(self):

        localctx = MasmParser.ProcStartStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_procStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.identifier()
            self.state = 181
            self.match(MasmParser.PROC)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 182
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcEndStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def ENDP(self):
            return self.getToken(MasmParser.ENDP, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_procEndStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcEndStmt" ):
                return visitor.visitProcEndStmt(self)
            else:
                return visitor.visitChildren(self)




    def procEndStmt(self):

        localctx = MasmParser.ProcEndStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_procEndStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.identifier()
            self.state = 186
            self.match(MasmParser.ENDP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(MasmParser.COLON, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_labelStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelStmt" ):
                return visitor.visitLabelStmt(self)
            else:
                return visitor.visitChildren(self)




    def labelStmt(self):

        localctx = MasmParser.LabelStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_labelStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.identifier()
            self.state = 189
            self.match(MasmParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataDeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MasmParser.IdentifierContext,0)


        def dataType(self):
            return self.getTypedRuleContext(MasmParser.DataTypeContext,0)


        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_dataDeclStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataDeclStmt" ):
                return visitor.visitDataDeclStmt(self)
            else:
                return visitor.visitChildren(self)




    def dataDeclStmt(self):

        localctx = MasmParser.DataDeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_dataDeclStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.identifier()
            self.state = 192
            self.dataType()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 193
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructuredDirectiveStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structuredDirective(self):
            return self.getTypedRuleContext(MasmParser.StructuredDirectiveContext,0)


        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_structuredDirectiveStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructuredDirectiveStmt" ):
                return visitor.visitStructuredDirectiveStmt(self)
            else:
                return visitor.visitChildren(self)




    def structuredDirectiveStmt(self):

        localctx = MasmParser.StructuredDirectiveStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_structuredDirectiveStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.structuredDirective()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 197
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(MasmParser.END, 0)

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_endStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndStmt" ):
                return visitor.visitEndStmt(self)
            else:
                return visitor.visitChildren(self)




    def endStmt(self):

        localctx = MasmParser.EndStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_endStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MasmParser.END)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0):
                self.state = 201
                self.lineItems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lineItems(self):
            return self.getTypedRuleContext(MasmParser.LineItemsContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_instructionStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructionStmt" ):
                return visitor.visitInstructionStmt(self)
            else:
                return visitor.visitChildren(self)




    def instructionStmt(self):

        localctx = MasmParser.InstructionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_instructionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.lineItems()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineItemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lineAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasmParser.LineAtomContext)
            else:
                return self.getTypedRuleContext(MasmParser.LineAtomContext,i)


        def getRuleIndex(self):
            return MasmParser.RULE_lineItems

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineItems" ):
                return visitor.visitLineItems(self)
            else:
                return visitor.visitChildren(self)




    def lineItems(self):

        localctx = MasmParser.LineItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_lineItems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 206
                self.lineAtom()
                self.state = 209 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -67553994410557442) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 196607) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(MasmParser.WORD, 0)

        def STRING(self):
            return self.getToken(MasmParser.STRING, 0)

        def COLON(self):
            return self.getToken(MasmParser.COLON, 0)

        def dataType(self):
            return self.getTypedRuleContext(MasmParser.DataTypeContext,0)


        def structuredDirective(self):
            return self.getTypedRuleContext(MasmParser.StructuredDirectiveContext,0)


        def anyKeyword(self):
            return self.getTypedRuleContext(MasmParser.AnyKeywordContext,0)


        def getRuleIndex(self):
            return MasmParser.RULE_lineAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineAtom" ):
                return visitor.visitLineAtom(self)
            else:
                return visitor.visitChildren(self)




    def lineAtom(self):

        localctx = MasmParser.LineAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lineAtom)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [81]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(MasmParser.WORD)
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(MasmParser.STRING)
                pass
            elif token in [78]:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(MasmParser.COLON)
                pass
            elif token in [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.dataType()
                pass
            elif token in [56, 57, 58, 59, 60, 61, 62, 63, 64]:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.structuredDirective()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]:
                self.enterOuterAlt(localctx, 6)
                self.state = 216
                self.anyKeyword()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnyKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(MasmParser.INCLUDE, 0)

        def INCLUDELIB(self):
            return self.getToken(MasmParser.INCLUDELIB, 0)

        def EXTERN(self):
            return self.getToken(MasmParser.EXTERN, 0)

        def EXTERNDEF(self):
            return self.getToken(MasmParser.EXTERNDEF, 0)

        def PUBLIC(self):
            return self.getToken(MasmParser.PUBLIC, 0)

        def ALIGN(self):
            return self.getToken(MasmParser.ALIGN, 0)

        def ASSUME(self):
            return self.getToken(MasmParser.ASSUME, 0)

        def OPTION(self):
            return self.getToken(MasmParser.OPTION, 0)

        def ORG(self):
            return self.getToken(MasmParser.ORG, 0)

        def EVEN(self):
            return self.getToken(MasmParser.EVEN, 0)

        def EQU(self):
            return self.getToken(MasmParser.EQU, 0)

        def TYPEDEF(self):
            return self.getToken(MasmParser.TYPEDEF, 0)

        def PROC(self):
            return self.getToken(MasmParser.PROC, 0)

        def ENDP(self):
            return self.getToken(MasmParser.ENDP, 0)

        def STRUCT(self):
            return self.getToken(MasmParser.STRUCT, 0)

        def UNION(self):
            return self.getToken(MasmParser.UNION, 0)

        def ENDS(self):
            return self.getToken(MasmParser.ENDS, 0)

        def MACRO(self):
            return self.getToken(MasmParser.MACRO, 0)

        def ENDM(self):
            return self.getToken(MasmParser.ENDM, 0)

        def END(self):
            return self.getToken(MasmParser.END, 0)

        def SEGMENT(self):
            return self.getToken(MasmParser.SEGMENT, 0)

        def IFDEF(self):
            return self.getToken(MasmParser.IFDEF, 0)

        def IFNDEF(self):
            return self.getToken(MasmParser.IFNDEF, 0)

        def IFDIF(self):
            return self.getToken(MasmParser.IFDIF, 0)

        def IFDIFI(self):
            return self.getToken(MasmParser.IFDIFI, 0)

        def IFIDN(self):
            return self.getToken(MasmParser.IFIDN, 0)

        def IFIDNI(self):
            return self.getToken(MasmParser.IFIDNI, 0)

        def IFB(self):
            return self.getToken(MasmParser.IFB, 0)

        def IFNB(self):
            return self.getToken(MasmParser.IFNB, 0)

        def IF1(self):
            return self.getToken(MasmParser.IF1, 0)

        def IF2(self):
            return self.getToken(MasmParser.IF2, 0)

        def IF_BARE(self):
            return self.getToken(MasmParser.IF_BARE, 0)

        def ELSEIF_BARE(self):
            return self.getToken(MasmParser.ELSEIF_BARE, 0)

        def ELSEIFDEF(self):
            return self.getToken(MasmParser.ELSEIFDEF, 0)

        def ELSEIFNDEF(self):
            return self.getToken(MasmParser.ELSEIFNDEF, 0)

        def ELSEIFDIF(self):
            return self.getToken(MasmParser.ELSEIFDIF, 0)

        def ELSEIFDIFI(self):
            return self.getToken(MasmParser.ELSEIFDIFI, 0)

        def ELSEIFIDN(self):
            return self.getToken(MasmParser.ELSEIFIDN, 0)

        def ELSEIFIDNI(self):
            return self.getToken(MasmParser.ELSEIFIDNI, 0)

        def ELSEIFB(self):
            return self.getToken(MasmParser.ELSEIFB, 0)

        def ELSEIFNB(self):
            return self.getToken(MasmParser.ELSEIFNB, 0)

        def ELSEIF1(self):
            return self.getToken(MasmParser.ELSEIF1, 0)

        def ELSEIF2(self):
            return self.getToken(MasmParser.ELSEIF2, 0)

        def ELSE_BARE(self):
            return self.getToken(MasmParser.ELSE_BARE, 0)

        def ENDIF_BARE(self):
            return self.getToken(MasmParser.ENDIF_BARE, 0)

        def FOR(self):
            return self.getToken(MasmParser.FOR, 0)

        def FORC(self):
            return self.getToken(MasmParser.FORC, 0)

        def IRP(self):
            return self.getToken(MasmParser.IRP, 0)

        def IRPC(self):
            return self.getToken(MasmParser.IRPC, 0)

        def REPT(self):
            return self.getToken(MasmParser.REPT, 0)

        def WHILE_BARE(self):
            return self.getToken(MasmParser.WHILE_BARE, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_anyKeyword

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnyKeyword" ):
                return visitor.visitAnyKeyword(self)
            else:
                return visitor.visitChildren(self)




    def anyKeyword(self):

        localctx = MasmParser.AnyKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_anyKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370494) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(MasmParser.WORD, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = MasmParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MasmParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructuredDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_DIR(self):
            return self.getToken(MasmParser.IF_DIR, 0)

        def ELSEIF_DIR(self):
            return self.getToken(MasmParser.ELSEIF_DIR, 0)

        def ELSE_DIR(self):
            return self.getToken(MasmParser.ELSE_DIR, 0)

        def ENDIF_DIR(self):
            return self.getToken(MasmParser.ENDIF_DIR, 0)

        def WHILE_DIR(self):
            return self.getToken(MasmParser.WHILE_DIR, 0)

        def ENDW_DIR(self):
            return self.getToken(MasmParser.ENDW_DIR, 0)

        def REPEAT_DIR(self):
            return self.getToken(MasmParser.REPEAT_DIR, 0)

        def UNTIL_DIR(self):
            return self.getToken(MasmParser.UNTIL_DIR, 0)

        def UNTILCXZ_DIR(self):
            return self.getToken(MasmParser.UNTILCXZ_DIR, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_structuredDirective

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructuredDirective" ):
                return visitor.visitStructuredDirective(self)
            else:
                return visitor.visitChildren(self)




    def structuredDirective(self):

        localctx = MasmParser.StructuredDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_structuredDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not(((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & 511) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DB(self):
            return self.getToken(MasmParser.DB, 0)

        def DW(self):
            return self.getToken(MasmParser.DW, 0)

        def DD(self):
            return self.getToken(MasmParser.DD, 0)

        def DQ(self):
            return self.getToken(MasmParser.DQ, 0)

        def DT(self):
            return self.getToken(MasmParser.DT, 0)

        def BYTE(self):
            return self.getToken(MasmParser.BYTE, 0)

        def WORD_TYPE(self):
            return self.getToken(MasmParser.WORD_TYPE, 0)

        def DWORD(self):
            return self.getToken(MasmParser.DWORD, 0)

        def QWORD(self):
            return self.getToken(MasmParser.QWORD, 0)

        def TBYTE(self):
            return self.getToken(MasmParser.TBYTE, 0)

        def REAL4(self):
            return self.getToken(MasmParser.REAL4, 0)

        def REAL8(self):
            return self.getToken(MasmParser.REAL8, 0)

        def REAL10(self):
            return self.getToken(MasmParser.REAL10, 0)

        def getRuleIndex(self):
            return MasmParser.RULE_dataType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = MasmParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not(((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 8191) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





