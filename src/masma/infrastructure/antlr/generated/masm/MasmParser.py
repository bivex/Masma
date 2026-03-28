# Generated from resources/grammars/masm/patched/Masm.g4 by ANTLR 4.13.2
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
        4,1,58,199,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,5,0,61,8,0,10,0,12,0,64,9,0,1,0,1,0,
        1,1,3,1,69,8,1,1,1,4,1,72,8,1,11,1,12,1,73,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,97,8,2,1,3,1,3,3,3,101,8,3,1,4,1,4,1,4,3,4,106,8,4,1,5,1,5,1,5,
        3,5,111,8,5,1,6,1,6,1,6,3,6,116,8,6,1,7,1,7,1,8,1,8,1,8,3,8,123,
        8,8,1,9,1,9,1,9,3,9,128,8,9,1,10,1,10,1,10,1,10,3,10,134,8,10,1,
        11,1,11,1,11,3,11,139,8,11,1,12,1,12,1,13,1,13,3,13,145,8,13,1,14,
        1,14,1,15,1,15,1,16,1,16,3,16,153,8,16,1,17,1,17,1,17,3,17,158,8,
        17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,3,20,169,8,20,1,
        21,1,21,3,21,173,8,21,1,22,1,22,3,22,177,8,22,1,23,1,23,1,24,4,24,
        182,8,24,11,24,12,24,183,1,25,1,25,1,25,1,25,1,25,3,25,191,8,25,
        1,26,1,26,1,27,1,27,1,28,1,28,1,28,0,0,29,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,6,
        1,0,1,2,1,0,28,31,1,0,14,19,1,0,22,27,1,0,32,40,1,0,41,53,212,0,
        62,1,0,0,0,2,68,1,0,0,0,4,96,1,0,0,0,6,98,1,0,0,0,8,102,1,0,0,0,
        10,107,1,0,0,0,12,112,1,0,0,0,14,117,1,0,0,0,16,119,1,0,0,0,18,124,
        1,0,0,0,20,133,1,0,0,0,22,135,1,0,0,0,24,140,1,0,0,0,26,142,1,0,
        0,0,28,146,1,0,0,0,30,148,1,0,0,0,32,150,1,0,0,0,34,154,1,0,0,0,
        36,159,1,0,0,0,38,162,1,0,0,0,40,165,1,0,0,0,42,170,1,0,0,0,44,174,
        1,0,0,0,46,178,1,0,0,0,48,181,1,0,0,0,50,190,1,0,0,0,52,192,1,0,
        0,0,54,194,1,0,0,0,56,196,1,0,0,0,58,61,3,2,1,0,59,61,5,58,0,0,60,
        58,1,0,0,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,
        0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,0,0,1,66,1,1,0,0,0,67,69,3,
        4,2,0,68,67,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,72,5,58,0,0,71,
        70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,3,1,0,0,
        0,75,97,3,6,3,0,76,97,3,8,4,0,77,97,3,10,5,0,78,97,3,12,6,0,79,97,
        3,14,7,0,80,97,3,16,8,0,81,97,3,18,9,0,82,97,3,20,10,0,83,97,3,22,
        11,0,84,97,3,24,12,0,85,97,3,26,13,0,86,97,3,28,14,0,87,97,3,30,
        15,0,88,97,3,32,16,0,89,97,3,34,17,0,90,97,3,36,18,0,91,97,3,38,
        19,0,92,97,3,40,20,0,93,97,3,42,21,0,94,97,3,44,22,0,95,97,3,46,
        23,0,96,75,1,0,0,0,96,76,1,0,0,0,96,77,1,0,0,0,96,78,1,0,0,0,96,
        79,1,0,0,0,96,80,1,0,0,0,96,81,1,0,0,0,96,82,1,0,0,0,96,83,1,0,0,
        0,96,84,1,0,0,0,96,85,1,0,0,0,96,86,1,0,0,0,96,87,1,0,0,0,96,88,
        1,0,0,0,96,89,1,0,0,0,96,90,1,0,0,0,96,91,1,0,0,0,96,92,1,0,0,0,
        96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,97,5,1,0,0,0,98,100,7,
        0,0,0,99,101,3,48,24,0,100,99,1,0,0,0,100,101,1,0,0,0,101,7,1,0,
        0,0,102,103,3,52,26,0,103,105,5,3,0,0,104,106,3,48,24,0,105,104,
        1,0,0,0,105,106,1,0,0,0,106,9,1,0,0,0,107,108,3,52,26,0,108,110,
        5,4,0,0,109,111,3,48,24,0,110,109,1,0,0,0,110,111,1,0,0,0,111,11,
        1,0,0,0,112,113,3,52,26,0,113,115,5,13,0,0,114,116,3,48,24,0,115,
        114,1,0,0,0,115,116,1,0,0,0,116,13,1,0,0,0,117,118,7,1,0,0,118,15,
        1,0,0,0,119,120,3,52,26,0,120,122,5,7,0,0,121,123,3,48,24,0,122,
        121,1,0,0,0,122,123,1,0,0,0,123,17,1,0,0,0,124,125,3,52,26,0,125,
        127,5,8,0,0,126,128,3,48,24,0,127,126,1,0,0,0,127,128,1,0,0,0,128,
        19,1,0,0,0,129,130,3,52,26,0,130,131,5,9,0,0,131,134,1,0,0,0,132,
        134,5,9,0,0,133,129,1,0,0,0,133,132,1,0,0,0,134,21,1,0,0,0,135,136,
        3,52,26,0,136,138,5,10,0,0,137,139,3,48,24,0,138,137,1,0,0,0,138,
        139,1,0,0,0,139,23,1,0,0,0,140,141,5,11,0,0,141,25,1,0,0,0,142,144,
        7,2,0,0,143,145,3,48,24,0,144,143,1,0,0,0,144,145,1,0,0,0,145,27,
        1,0,0,0,146,147,5,20,0,0,147,29,1,0,0,0,148,149,5,21,0,0,149,31,
        1,0,0,0,150,152,7,3,0,0,151,153,3,48,24,0,152,151,1,0,0,0,152,153,
        1,0,0,0,153,33,1,0,0,0,154,155,3,52,26,0,155,157,5,5,0,0,156,158,
        3,48,24,0,157,156,1,0,0,0,157,158,1,0,0,0,158,35,1,0,0,0,159,160,
        3,52,26,0,160,161,5,6,0,0,161,37,1,0,0,0,162,163,3,52,26,0,163,164,
        5,54,0,0,164,39,1,0,0,0,165,166,3,52,26,0,166,168,3,56,28,0,167,
        169,3,48,24,0,168,167,1,0,0,0,168,169,1,0,0,0,169,41,1,0,0,0,170,
        172,3,54,27,0,171,173,3,48,24,0,172,171,1,0,0,0,172,173,1,0,0,0,
        173,43,1,0,0,0,174,176,5,12,0,0,175,177,3,48,24,0,176,175,1,0,0,
        0,176,177,1,0,0,0,177,45,1,0,0,0,178,179,3,48,24,0,179,47,1,0,0,
        0,180,182,3,50,25,0,181,180,1,0,0,0,182,183,1,0,0,0,183,181,1,0,
        0,0,183,184,1,0,0,0,184,49,1,0,0,0,185,191,5,56,0,0,186,191,5,55,
        0,0,187,191,5,54,0,0,188,191,3,56,28,0,189,191,3,54,27,0,190,185,
        1,0,0,0,190,186,1,0,0,0,190,187,1,0,0,0,190,188,1,0,0,0,190,189,
        1,0,0,0,191,51,1,0,0,0,192,193,5,56,0,0,193,53,1,0,0,0,194,195,7,
        4,0,0,195,55,1,0,0,0,196,197,7,5,0,0,197,57,1,0,0,0,21,60,62,68,
        73,96,100,105,110,115,122,127,133,138,144,152,157,168,172,176,183,
        190
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
                     "<INVALID>", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "INCLUDE", "INCLUDELIB", "EQU", "TYPEDEF", 
                      "PROC", "ENDP", "STRUCT", "UNION", "ENDS", "MACRO", 
                      "ENDM", "END", "SEGMENT", "IFDEF", "IFNDEF", "IF1", 
                      "IF2", "IF_BARE", "ELSEIF_BARE", "ELSE_BARE", "ENDIF_BARE", 
                      "FOR", "FORC", "IRP", "IRPC", "REPT", "WHILE_BARE", 
                      "DATA_SEG", "DATAQ_SEG", "CONST_SEG", "CODE_SEG", 
                      "IF_DIR", "ELSEIF_DIR", "ELSE_DIR", "ENDIF_DIR", "WHILE_DIR", 
                      "ENDW_DIR", "REPEAT_DIR", "UNTIL_DIR", "UNTILCXZ_DIR", 
                      "DB", "DW", "DD", "DQ", "DT", "BYTE", "WORD_TYPE", 
                      "DWORD", "QWORD", "TBYTE", "REAL4", "REAL8", "REAL10", 
                      "COLON", "STRING", "WORD", "WS", "EOL" ]

    RULE_compilationUnit = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_includeStmt = 3
    RULE_equStmt = 4
    RULE_typedefStmt = 5
    RULE_namedSegmentStmt = 6
    RULE_simpleSegmentStmt = 7
    RULE_structStartStmt = 8
    RULE_unionStartStmt = 9
    RULE_structEndStmt = 10
    RULE_macroStartStmt = 11
    RULE_endmStmt = 12
    RULE_condAssembleStmt = 13
    RULE_condAssembleElse = 14
    RULE_condAssembleEndif = 15
    RULE_macroLoopStmt = 16
    RULE_procStartStmt = 17
    RULE_procEndStmt = 18
    RULE_labelStmt = 19
    RULE_dataDeclStmt = 20
    RULE_structuredDirectiveStmt = 21
    RULE_endStmt = 22
    RULE_instructionStmt = 23
    RULE_lineItems = 24
    RULE_lineAtom = 25
    RULE_identifier = 26
    RULE_structuredDirective = 27
    RULE_dataType = 28

    ruleNames =  [ "compilationUnit", "line", "statement", "includeStmt", 
                   "equStmt", "typedefStmt", "namedSegmentStmt", "simpleSegmentStmt", 
                   "structStartStmt", "unionStartStmt", "structEndStmt", 
                   "macroStartStmt", "endmStmt", "condAssembleStmt", "condAssembleElse", 
                   "condAssembleEndif", "macroLoopStmt", "procStartStmt", 
                   "procEndStmt", "labelStmt", "dataDeclStmt", "structuredDirectiveStmt", 
                   "endStmt", "instructionStmt", "lineItems", "lineAtom", 
                   "identifier", "structuredDirective", "dataType" ]

    EOF = Token.EOF
    INCLUDE=1
    INCLUDELIB=2
    EQU=3
    TYPEDEF=4
    PROC=5
    ENDP=6
    STRUCT=7
    UNION=8
    ENDS=9
    MACRO=10
    ENDM=11
    END=12
    SEGMENT=13
    IFDEF=14
    IFNDEF=15
    IF1=16
    IF2=17
    IF_BARE=18
    ELSEIF_BARE=19
    ELSE_BARE=20
    ENDIF_BARE=21
    FOR=22
    FORC=23
    IRP=24
    IRPC=25
    REPT=26
    WHILE_BARE=27
    DATA_SEG=28
    DATAQ_SEG=29
    CONST_SEG=30
    CODE_SEG=31
    IF_DIR=32
    ELSEIF_DIR=33
    ELSE_DIR=34
    ENDIF_DIR=35
    WHILE_DIR=36
    ENDW_DIR=37
    REPEAT_DIR=38
    UNTIL_DIR=39
    UNTILCXZ_DIR=40
    DB=41
    DW=42
    DD=43
    DQ=44
    DT=45
    BYTE=46
    WORD_TYPE=47
    DWORD=48
    QWORD=49
    TBYTE=50
    REAL4=51
    REAL8=52
    REAL10=53
    COLON=54
    STRING=55
    WORD=56
    WS=57
    EOL=58

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
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 432345564227557894) != 0):
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.line()
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.match(MasmParser.EOL)
                    pass


                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
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
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188075846150) != 0):
                self.state = 67
                self.statement()


            self.state = 71 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 70
                    self.match(MasmParser.EOL)

                else:
                    raise NoViableAltException(self)
                self.state = 73 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.includeStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.equStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.typedefStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.namedSegmentStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.simpleSegmentStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.structStartStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.unionStartStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 82
                self.structEndStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 83
                self.macroStartStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 84
                self.endmStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 85
                self.condAssembleStmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 86
                self.condAssembleElse()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 87
                self.condAssembleEndif()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 88
                self.macroLoopStmt()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 89
                self.procStartStmt()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 90
                self.procEndStmt()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 91
                self.labelStmt()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 92
                self.dataDeclStmt()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 93
                self.structuredDirectiveStmt()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 94
                self.endStmt()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 95
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
            self.state = 98
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 99
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
        self.enterRule(localctx, 8, self.RULE_equStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.identifier()
            self.state = 103
            self.match(MasmParser.EQU)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 104
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
        self.enterRule(localctx, 10, self.RULE_typedefStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.identifier()
            self.state = 108
            self.match(MasmParser.TYPEDEF)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 109
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
        self.enterRule(localctx, 12, self.RULE_namedSegmentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.identifier()
            self.state = 113
            self.match(MasmParser.SEGMENT)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 114
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
        self.enterRule(localctx, 14, self.RULE_simpleSegmentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_structStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.identifier()
            self.state = 120
            self.match(MasmParser.STRUCT)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 121
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
        self.enterRule(localctx, 18, self.RULE_unionStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.identifier()
            self.state = 125
            self.match(MasmParser.UNION)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 126
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
        self.enterRule(localctx, 20, self.RULE_structEndStmt)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.identifier()
                self.state = 130
                self.match(MasmParser.ENDS)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
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
        self.enterRule(localctx, 22, self.RULE_macroStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.identifier()
            self.state = 136
            self.match(MasmParser.MACRO)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 137
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
        self.enterRule(localctx, 24, self.RULE_endmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
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

        def IF1(self):
            return self.getToken(MasmParser.IF1, 0)

        def IF2(self):
            return self.getToken(MasmParser.IF2, 0)

        def IF_BARE(self):
            return self.getToken(MasmParser.IF_BARE, 0)

        def ELSEIF_BARE(self):
            return self.getToken(MasmParser.ELSEIF_BARE, 0)

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
        self.enterRule(localctx, 26, self.RULE_condAssembleStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 143
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
        self.enterRule(localctx, 28, self.RULE_condAssembleElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
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
        self.enterRule(localctx, 30, self.RULE_condAssembleEndif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
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
        self.enterRule(localctx, 32, self.RULE_macroLoopStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 151
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
        self.enterRule(localctx, 34, self.RULE_procStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.identifier()
            self.state = 155
            self.match(MasmParser.PROC)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 156
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
        self.enterRule(localctx, 36, self.RULE_procEndStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.identifier()
            self.state = 160
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
        self.enterRule(localctx, 38, self.RULE_labelStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.identifier()
            self.state = 163
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
        self.enterRule(localctx, 40, self.RULE_dataDeclStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.identifier()
            self.state = 166
            self.dataType()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 167
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
        self.enterRule(localctx, 42, self.RULE_structuredDirectiveStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.structuredDirective()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 171
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
        self.enterRule(localctx, 44, self.RULE_endStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MasmParser.END)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0):
                self.state = 175
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
        self.enterRule(localctx, 46, self.RULE_instructionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
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
        self.enterRule(localctx, 48, self.RULE_lineItems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 180
                self.lineAtom()
                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 144115183780888576) != 0)):
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


        def getRuleIndex(self):
            return MasmParser.RULE_lineAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineAtom" ):
                return visitor.visitLineAtom(self)
            else:
                return visitor.visitChildren(self)




    def lineAtom(self):

        localctx = MasmParser.LineAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lineAtom)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(MasmParser.WORD)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(MasmParser.STRING)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(MasmParser.COLON)
                pass
            elif token in [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.dataType()
                pass
            elif token in [32, 33, 34, 35, 36, 37, 38, 39, 40]:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.structuredDirective()
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
        self.enterRule(localctx, 52, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
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
        self.enterRule(localctx, 54, self.RULE_structuredDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2194728288256) != 0)):
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
        self.enterRule(localctx, 56, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18012199486226432) != 0)):
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





