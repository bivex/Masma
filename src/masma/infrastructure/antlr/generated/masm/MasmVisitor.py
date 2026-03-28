# Generated from resources/grammars/masm/patched/Masm.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MasmParser import MasmParser
else:
    from MasmParser import MasmParser

# This class defines a complete generic visitor for a parse tree produced by MasmParser.

class MasmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MasmParser#compilationUnit.
    def visitCompilationUnit(self, ctx:MasmParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#line.
    def visitLine(self, ctx:MasmParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#statement.
    def visitStatement(self, ctx:MasmParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#includeStmt.
    def visitIncludeStmt(self, ctx:MasmParser.IncludeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#equStmt.
    def visitEquStmt(self, ctx:MasmParser.EquStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#typedefStmt.
    def visitTypedefStmt(self, ctx:MasmParser.TypedefStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#namedSegmentStmt.
    def visitNamedSegmentStmt(self, ctx:MasmParser.NamedSegmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#simpleSegmentStmt.
    def visitSimpleSegmentStmt(self, ctx:MasmParser.SimpleSegmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#structStartStmt.
    def visitStructStartStmt(self, ctx:MasmParser.StructStartStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#unionStartStmt.
    def visitUnionStartStmt(self, ctx:MasmParser.UnionStartStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#structEndStmt.
    def visitStructEndStmt(self, ctx:MasmParser.StructEndStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#macroStartStmt.
    def visitMacroStartStmt(self, ctx:MasmParser.MacroStartStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#endmStmt.
    def visitEndmStmt(self, ctx:MasmParser.EndmStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#condAssembleStmt.
    def visitCondAssembleStmt(self, ctx:MasmParser.CondAssembleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#condAssembleElse.
    def visitCondAssembleElse(self, ctx:MasmParser.CondAssembleElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#condAssembleEndif.
    def visitCondAssembleEndif(self, ctx:MasmParser.CondAssembleEndifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#macroLoopStmt.
    def visitMacroLoopStmt(self, ctx:MasmParser.MacroLoopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#procStartStmt.
    def visitProcStartStmt(self, ctx:MasmParser.ProcStartStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#procEndStmt.
    def visitProcEndStmt(self, ctx:MasmParser.ProcEndStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#labelStmt.
    def visitLabelStmt(self, ctx:MasmParser.LabelStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#dataDeclStmt.
    def visitDataDeclStmt(self, ctx:MasmParser.DataDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#structuredDirectiveStmt.
    def visitStructuredDirectiveStmt(self, ctx:MasmParser.StructuredDirectiveStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#endStmt.
    def visitEndStmt(self, ctx:MasmParser.EndStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#instructionStmt.
    def visitInstructionStmt(self, ctx:MasmParser.InstructionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#lineItems.
    def visitLineItems(self, ctx:MasmParser.LineItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#lineAtom.
    def visitLineAtom(self, ctx:MasmParser.LineAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#identifier.
    def visitIdentifier(self, ctx:MasmParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#structuredDirective.
    def visitStructuredDirective(self, ctx:MasmParser.StructuredDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasmParser#dataType.
    def visitDataType(self, ctx:MasmParser.DataTypeContext):
        return self.visitChildren(ctx)



del MasmParser