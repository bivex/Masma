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
        4,1,42,156,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,0,
        1,0,1,1,3,1,57,8,1,1,1,4,1,60,8,1,11,1,12,1,61,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,79,8,2,1,3,1,3,3,3,
        83,8,3,1,4,1,4,1,4,3,4,88,8,4,1,5,1,5,1,5,3,5,93,8,5,1,6,1,6,1,7,
        1,7,1,7,3,7,100,8,7,1,8,1,8,1,8,1,9,1,9,1,9,3,9,108,8,9,1,10,1,10,
        1,11,1,11,1,11,3,11,115,8,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,
        1,14,1,14,3,14,126,8,14,1,15,1,15,3,15,130,8,15,1,16,1,16,3,16,134,
        8,16,1,17,1,17,1,18,4,18,139,8,18,11,18,12,18,140,1,19,1,19,1,19,
        1,19,1,19,3,19,148,8,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,0,0,23,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        0,4,1,0,1,2,1,0,12,15,1,0,16,24,1,0,25,37,164,0,50,1,0,0,0,2,56,
        1,0,0,0,4,78,1,0,0,0,6,80,1,0,0,0,8,84,1,0,0,0,10,89,1,0,0,0,12,
        94,1,0,0,0,14,96,1,0,0,0,16,101,1,0,0,0,18,104,1,0,0,0,20,109,1,
        0,0,0,22,111,1,0,0,0,24,116,1,0,0,0,26,119,1,0,0,0,28,122,1,0,0,
        0,30,127,1,0,0,0,32,131,1,0,0,0,34,135,1,0,0,0,36,138,1,0,0,0,38,
        147,1,0,0,0,40,149,1,0,0,0,42,151,1,0,0,0,44,153,1,0,0,0,46,49,3,
        2,1,0,47,49,5,42,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,
        48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,0,0,
        1,54,1,1,0,0,0,55,57,3,4,2,0,56,55,1,0,0,0,56,57,1,0,0,0,57,59,1,
        0,0,0,58,60,5,42,0,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,
        62,1,0,0,0,62,3,1,0,0,0,63,79,3,6,3,0,64,79,3,8,4,0,65,79,3,10,5,
        0,66,79,3,12,6,0,67,79,3,14,7,0,68,79,3,16,8,0,69,79,3,18,9,0,70,
        79,3,20,10,0,71,79,3,22,11,0,72,79,3,24,12,0,73,79,3,26,13,0,74,
        79,3,28,14,0,75,79,3,30,15,0,76,79,3,32,16,0,77,79,3,34,17,0,78,
        63,1,0,0,0,78,64,1,0,0,0,78,65,1,0,0,0,78,66,1,0,0,0,78,67,1,0,0,
        0,78,68,1,0,0,0,78,69,1,0,0,0,78,70,1,0,0,0,78,71,1,0,0,0,78,72,
        1,0,0,0,78,73,1,0,0,0,78,74,1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,
        78,77,1,0,0,0,79,5,1,0,0,0,80,82,7,0,0,0,81,83,3,36,18,0,82,81,1,
        0,0,0,82,83,1,0,0,0,83,7,1,0,0,0,84,85,3,40,20,0,85,87,5,3,0,0,86,
        88,3,36,18,0,87,86,1,0,0,0,87,88,1,0,0,0,88,9,1,0,0,0,89,90,3,40,
        20,0,90,92,5,11,0,0,91,93,3,36,18,0,92,91,1,0,0,0,92,93,1,0,0,0,
        93,11,1,0,0,0,94,95,7,1,0,0,95,13,1,0,0,0,96,97,3,40,20,0,97,99,
        5,6,0,0,98,100,3,36,18,0,99,98,1,0,0,0,99,100,1,0,0,0,100,15,1,0,
        0,0,101,102,3,40,20,0,102,103,5,7,0,0,103,17,1,0,0,0,104,105,3,40,
        20,0,105,107,5,8,0,0,106,108,3,36,18,0,107,106,1,0,0,0,107,108,1,
        0,0,0,108,19,1,0,0,0,109,110,5,9,0,0,110,21,1,0,0,0,111,112,3,40,
        20,0,112,114,5,4,0,0,113,115,3,36,18,0,114,113,1,0,0,0,114,115,1,
        0,0,0,115,23,1,0,0,0,116,117,3,40,20,0,117,118,5,5,0,0,118,25,1,
        0,0,0,119,120,3,40,20,0,120,121,5,38,0,0,121,27,1,0,0,0,122,123,
        3,40,20,0,123,125,3,44,22,0,124,126,3,36,18,0,125,124,1,0,0,0,125,
        126,1,0,0,0,126,29,1,0,0,0,127,129,3,42,21,0,128,130,3,36,18,0,129,
        128,1,0,0,0,129,130,1,0,0,0,130,31,1,0,0,0,131,133,5,10,0,0,132,
        134,3,36,18,0,133,132,1,0,0,0,133,134,1,0,0,0,134,33,1,0,0,0,135,
        136,3,36,18,0,136,35,1,0,0,0,137,139,3,38,19,0,138,137,1,0,0,0,139,
        140,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,37,1,0,0,0,142,148,
        5,40,0,0,143,148,5,39,0,0,144,148,5,38,0,0,145,148,3,44,22,0,146,
        148,3,42,21,0,147,142,1,0,0,0,147,143,1,0,0,0,147,144,1,0,0,0,147,
        145,1,0,0,0,147,146,1,0,0,0,148,39,1,0,0,0,149,150,5,40,0,0,150,
        41,1,0,0,0,151,152,7,2,0,0,152,43,1,0,0,0,153,154,7,3,0,0,154,45,
        1,0,0,0,16,48,50,56,61,78,82,87,92,99,107,114,125,129,133,140,147
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
                     "<INVALID>", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "INCLUDE", "INCLUDELIB", "EQU", "PROC", 
                      "ENDP", "STRUCT", "ENDS", "MACRO", "ENDM", "END", 
                      "SEGMENT", "DATA_SEG", "DATAQ_SEG", "CONST_SEG", "CODE_SEG", 
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
    RULE_namedSegmentStmt = 5
    RULE_simpleSegmentStmt = 6
    RULE_structStartStmt = 7
    RULE_structEndStmt = 8
    RULE_macroStartStmt = 9
    RULE_endmStmt = 10
    RULE_procStartStmt = 11
    RULE_procEndStmt = 12
    RULE_labelStmt = 13
    RULE_dataDeclStmt = 14
    RULE_structuredDirectiveStmt = 15
    RULE_endStmt = 16
    RULE_instructionStmt = 17
    RULE_lineItems = 18
    RULE_lineAtom = 19
    RULE_identifier = 20
    RULE_structuredDirective = 21
    RULE_dataType = 22

    ruleNames =  [ "compilationUnit", "line", "statement", "includeStmt", 
                   "equStmt", "namedSegmentStmt", "simpleSegmentStmt", "structStartStmt", 
                   "structEndStmt", "macroStartStmt", "endmStmt", "procStartStmt", 
                   "procEndStmt", "labelStmt", "dataDeclStmt", "structuredDirectiveStmt", 
                   "endStmt", "instructionStmt", "lineItems", "lineAtom", 
                   "identifier", "structuredDirective", "dataType" ]

    EOF = Token.EOF
    INCLUDE=1
    INCLUDELIB=2
    EQU=3
    PROC=4
    ENDP=5
    STRUCT=6
    ENDS=7
    MACRO=8
    ENDM=9
    END=10
    SEGMENT=11
    DATA_SEG=12
    DATAQ_SEG=13
    CONST_SEG=14
    CODE_SEG=15
    IF_DIR=16
    ELSEIF_DIR=17
    ELSE_DIR=18
    ENDIF_DIR=19
    WHILE_DIR=20
    ENDW_DIR=21
    REPEAT_DIR=22
    UNTIL_DIR=23
    UNTILCXZ_DIR=24
    DB=25
    DW=26
    DD=27
    DQ=28
    DT=29
    BYTE=30
    WORD_TYPE=31
    DWORD=32
    QWORD=33
    TBYTE=34
    REAL4=35
    REAL8=36
    REAL10=37
    COLON=38
    STRING=39
    WORD=40
    WS=41
    EOL=42

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
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6597069764102) != 0):
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.line()
                    pass

                elif la_ == 2:
                    self.state = 47
                    self.match(MasmParser.EOL)
                    pass


                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
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
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023252998) != 0):
                self.state = 55
                self.statement()


            self.state = 59 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 58
                    self.match(MasmParser.EOL)

                else:
                    raise NoViableAltException(self)
                self.state = 61 
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


        def namedSegmentStmt(self):
            return self.getTypedRuleContext(MasmParser.NamedSegmentStmtContext,0)


        def simpleSegmentStmt(self):
            return self.getTypedRuleContext(MasmParser.SimpleSegmentStmtContext,0)


        def structStartStmt(self):
            return self.getTypedRuleContext(MasmParser.StructStartStmtContext,0)


        def structEndStmt(self):
            return self.getTypedRuleContext(MasmParser.StructEndStmtContext,0)


        def macroStartStmt(self):
            return self.getTypedRuleContext(MasmParser.MacroStartStmtContext,0)


        def endmStmt(self):
            return self.getTypedRuleContext(MasmParser.EndmStmtContext,0)


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
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.includeStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.equStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.namedSegmentStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.simpleSegmentStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.structStartStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.structEndStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.macroStartStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.endmStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 71
                self.procStartStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 72
                self.procEndStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 73
                self.labelStmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 74
                self.dataDeclStmt()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 75
                self.structuredDirectiveStmt()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 76
                self.endStmt()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 77
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
            self.state = 80
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 81
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
            self.state = 84
            self.identifier()
            self.state = 85
            self.match(MasmParser.EQU)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 86
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
        self.enterRule(localctx, 10, self.RULE_namedSegmentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.identifier()
            self.state = 90
            self.match(MasmParser.SEGMENT)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 91
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
        self.enterRule(localctx, 12, self.RULE_simpleSegmentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
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
        self.enterRule(localctx, 14, self.RULE_structStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.identifier()
            self.state = 97
            self.match(MasmParser.STRUCT)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 98
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
        self.enterRule(localctx, 16, self.RULE_structEndStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.identifier()
            self.state = 102
            self.match(MasmParser.ENDS)
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
        self.enterRule(localctx, 18, self.RULE_macroStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.identifier()
            self.state = 105
            self.match(MasmParser.MACRO)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 106
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
        self.enterRule(localctx, 20, self.RULE_endmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MasmParser.ENDM)
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
        self.enterRule(localctx, 22, self.RULE_procStartStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.identifier()
            self.state = 112
            self.match(MasmParser.PROC)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 113
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
        self.enterRule(localctx, 24, self.RULE_procEndStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.identifier()
            self.state = 117
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
        self.enterRule(localctx, 26, self.RULE_labelStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.identifier()
            self.state = 120
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
        self.enterRule(localctx, 28, self.RULE_dataDeclStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.identifier()
            self.state = 123
            self.dataType()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 124
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
        self.enterRule(localctx, 30, self.RULE_structuredDirectiveStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.structuredDirective()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 128
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
        self.enterRule(localctx, 32, self.RULE_endStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MasmParser.END)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0):
                self.state = 132
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
        self.enterRule(localctx, 34, self.RULE_instructionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
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
        self.enterRule(localctx, 36, self.RULE_lineItems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.lineAtom()
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023190016) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_lineAtom)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(MasmParser.WORD)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(MasmParser.STRING)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.match(MasmParser.COLON)
                pass
            elif token in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 145
                self.dataType()
                pass
            elif token in [16, 17, 18, 19, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
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
        self.enterRule(localctx, 40, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
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
        self.enterRule(localctx, 42, self.RULE_structuredDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33488896) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 274844352512) != 0)):
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





