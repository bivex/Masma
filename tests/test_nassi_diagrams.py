import json
import os
import subprocess
import sys
from pathlib import Path

from masma.application.control_flow import (
    BuildNassiDiagramCommand,
    BuildNassiDirectoryCommand,
    NassiDiagramService,
)
from masma.domain.control_flow import (
    ActionFlowStep,
    ControlFlowDiagram,
    ForInFlowStep,
    FunctionControlFlow,
    IfFlowStep,
    InvokeFlowStep,
    RepeatStringFlowStep,
    RepeatWhileFlowStep,
    SwitchFlowStep,
    WhileFlowStep,
)
from masma.domain.model import SourceUnit, SourceUnitId
from masma.infrastructure.filesystem.source_repository import FileSystemSourceRepository
from masma.infrastructure.masm.control_flow_extractor import MasmControlFlowExtractor
from masma.infrastructure.rendering.nassi_html_renderer import HtmlNassiDiagramRenderer


ROOT = Path(__file__).resolve().parent.parent


def _build_service() -> NassiDiagramService:
    return NassiDiagramService(
        source_repository=FileSystemSourceRepository(),
        extractor=MasmControlFlowExtractor(),
        renderer=HtmlNassiDiagramRenderer(),
    )


def test_nassi_service_builds_html_document_for_masm() -> None:
    service = _build_service()
    document = service.build_file_diagram(
        BuildNassiDiagramCommand(path=str(ROOT / "tests" / "fixtures" / "control_flow.asm"))
    )

    assert document.procedure_count == 2
    assert "score" in document.procedure_names
    assert "normalize" in document.procedure_names
    assert "While eax &lt; 100" in document.html
    assert "UNTIL eax = 42" in document.html
    assert "Masma" in document.html


def test_nassi_service_builds_directory_bundle_for_masm() -> None:
    service = _build_service()
    bundle = service.build_directory_diagrams(
        BuildNassiDirectoryCommand(root_path=str(ROOT / "tests" / "fixtures"))
    )

    assert bundle.document_count == 4
    assert bundle.root_path == str((ROOT / "tests" / "fixtures").resolve())
    assert any(document.source_location.endswith("control_flow.asm") for document in bundle.documents)
    assert any(document.procedure_count == 2 for document in bundle.documents)


def test_control_flow_extractor_maps_structured_masm_blocks() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("flow"),
        location="flow.asm",
        content=(ROOT / "tests" / "fixtures" / "control_flow.asm").read_text(encoding="utf-8"),
    )

    diagram = extractor.extract(source)

    assert len(diagram.functions) == 2
    score = diagram.functions[0]
    normalize = diagram.functions[1]
    assert isinstance(score.steps[1], IfFlowStep)
    assert isinstance(score.steps[2], RepeatWhileFlowStep)
    assert isinstance(score.steps[1].else_steps[0], IfFlowStep)
    assert any(
        isinstance(step, WhileFlowStep) for step in score.steps[1].else_steps[0].else_steps
    )
    assert isinstance(normalize.steps[0], ActionFlowStep)
    assert normalize.steps[0].label == "start_loop:"


def test_control_flow_extractor_reconstructs_jump_based_if_else_and_loop() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("jump-flow"),
        location="jump-flow.asm",
        content="""
jumpy PROC
loop_top:
    cmp eax, 10
    jge loop_done
    inc eax
    jmp loop_top
loop_done:
    test ebx, ebx
    jz zero_case
    inc ecx
    jmp after_if
zero_case:
    dec ecx
after_if:
    ret
jumpy ENDP
""".strip(),
    )

    diagram = extractor.extract(source)

    assert len(diagram.functions) == 1
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], WhileFlowStep)
    assert steps[0].condition == "eax < 10"
    assert [step.label for step in steps[0].body_steps] == ["inc eax"]
    assert isinstance(steps[1], IfFlowStep)
    assert steps[1].condition == "ebx & ebx ≠ 0"
    assert [step.label for step in steps[1].then_steps] == ["inc ecx"]
    assert [step.label for step in steps[1].else_steps] == ["dec ecx"]
    assert steps[2].label == "ret"


def test_nassi_cli_writes_html_file_for_masm(tmp_path: Path) -> None:
    output_path = tmp_path / "control_flow.html"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "masma.presentation.cli.main",
            "nassi-file",
            str(ROOT / "tests" / "fixtures" / "control_flow.asm"),
            "--out",
            str(output_path),
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["procedure_count"] == 2
    assert payload["output_path"] == str(output_path.resolve())
    assert output_path.exists()
    assert "Nassi-Shneiderman Control Flow" in output_path.read_text(encoding="utf-8")


def test_nassi_dir_cli_writes_html_bundle_for_masm(tmp_path: Path) -> None:
    output_dir = tmp_path / "nassi-bundle"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "masma.presentation.cli.main",
            "nassi-dir",
            str(ROOT / "tests" / "fixtures"),
            "--out",
            str(output_dir),
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["document_count"] == 4
    assert payload["index_path"] == str((output_dir / "index.html").resolve())
    assert (output_dir / "control_flow.nassi.html").exists()
    assert (output_dir / "invalid.nassi.html").exists()
    assert "Masma NSD Index" in (output_dir / "index.html").read_text(encoding="utf-8")


class TestIfDepthRendering:
    def test_depth_badge_zero_is_empty(self) -> None:
        renderer = HtmlNassiDiagramRenderer()
        assert renderer._depth_badge(0) == ""

    def test_depth_badges_span_supported_ranges(self) -> None:
        renderer = HtmlNassiDiagramRenderer()
        assert renderer._depth_badge(1) == " ①"
        assert renderer._depth_badge(20) == " ⑳"
        assert renderer._depth_badge(35) == " ㉟"
        assert renderer._depth_badge(50) == " ㊿"

    def test_depth_css_generates_full_depth_palette(self) -> None:
        renderer = HtmlNassiDiagramRenderer()
        css = renderer._depth_css()
        assert ".ns-if-depth-0-triangle" in css
        assert ".ns-if-depth-50-triangle" in css
        assert "var(--blue-dim)" in css
        assert "var(--amber-dim)" in css

    def test_renderer_handles_nested_if_depth_markup(self) -> None:
        renderer = HtmlNassiDiagramRenderer()
        diagram = ControlFlowDiagram(
            source_location="nested.asm",
            functions=(
                FunctionControlFlow(
                    name="nested",
                    signature="nested PROC",
                    container=None,
                    steps=(
                        IfFlowStep(
                            condition="eax > 0",
                            then_steps=(
                                IfFlowStep(
                                    condition="ebx > 0",
                                    then_steps=(ActionFlowStep(label="inc eax"),),
                                    else_steps=(),
                                ),
                            ),
                            else_steps=(),
                        ),
                    ),
                ),
            ),
        )

        html = renderer.render(diagram)
        assert "ns-if-depth-0" in html
        assert "ns-if-depth-1" in html


def test_control_flow_extractor_produces_switch_from_cmp_je_chain() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("switch-flow"),
        location="switch-flow.asm",
        content="""
switchy PROC
    cmp eax, 1
    je case1
    cmp eax, 2
    je case2
    cmp eax, 3
    je case3
    jmp default_case
case1:
    mov ebx, 10
    jmp end_switch
case2:
    mov ebx, 20
    jmp end_switch
case3:
    mov ebx, 30
    jmp end_switch
default_case:
    mov ebx, 0
end_switch:
    ret
switchy ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], SwitchFlowStep)
    assert steps[0].expression == "eax"
    assert len(steps[0].cases) == 4
    labels = [c.label for c in steps[0].cases]
    assert "1" in labels
    assert "2" in labels
    assert "3" in labels
    assert "default" in labels
    assert steps[0].cases[0].steps[0].label == "mov ebx, 10"


def test_control_flow_extractor_produces_for_in_from_loop_instruction() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("forin-flow"),
        location="forin-flow.asm",
        content="""
counter PROC
    mov ecx, 10
loop_start:
    dec eax
    loop loop_start
    ret
counter ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], ForInFlowStep)
    assert "10" in steps[0].header
    assert steps[0].body_steps[0].label == "dec eax"


def test_control_flow_extractor_produces_invoke_step() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("invoke-flow"),
        location="invoke-flow.asm",
        content="""
caller PROC
    invoke MessageBoxA, 0, offset msg, offset title, MB_OK
    invoke ExitProcess, 0
    ret
caller ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], InvokeFlowStep)
    assert steps[0].target == "MessageBoxA"
    assert "MB_OK" in steps[0].args[-1]
    assert isinstance(steps[1], InvokeFlowStep)
    assert steps[1].target == "ExitProcess"
    assert steps[1].args == ("0",)


def test_control_flow_extractor_produces_repeat_string_step() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("repstr-flow"),
        location="repstr-flow.asm",
        content="""
copier PROC
    mov ecx, 16
    rep movsd
    mov ecx, 32
    repne scasb
    ret
copier ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    # mov ecx, 16 and mov ecx, 32 are absorbed by the following rep instructions
    assert isinstance(steps[0], RepeatStringFlowStep)
    assert steps[0].prefix == "REP"
    assert steps[0].instruction == "movsd"
    assert isinstance(steps[1], RepeatStringFlowStep)
    assert steps[1].prefix == "REPNE"
    assert steps[1].instruction == "scasb"


def test_renderer_renders_invoke_and_repeat_string_steps() -> None:
    from masma.domain.control_flow import InvokeFlowStep, RepeatStringFlowStep
    renderer = HtmlNassiDiagramRenderer()
    diagram = ControlFlowDiagram(
        source_location="smoke.asm",
        functions=(
            FunctionControlFlow(
                name="smoke",
                signature="smoke PROC",
                container=None,
                steps=(
                    InvokeFlowStep(target="MessageBoxA", args=("0", "offset msg", "MB_OK")),
                    RepeatStringFlowStep(prefix="REP", instruction="movsd"),
                ),
            ),
        ),
    )
    html = renderer.render(diagram)
    assert "INVOKE MessageBoxA" in html
    assert "REP movsd" in html
    assert "ns-invoke" in html
    assert "ns-repeat" in html


def test_control_flow_extractor_produces_call_step_for_direct_call() -> None:
    from masma.domain.control_flow import CallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("call-flow"),
        location="call-flow.asm",
        content="""
caller PROC
    call SomeProcedure
    call [ebx]
    ret
caller ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], CallFlowStep)
    assert steps[0].target == "SomeProcedure"
    # indirect call stays as ActionFlowStep
    assert isinstance(steps[1], ActionFlowStep)
    assert steps[1].label == "call [ebx]"


def test_control_flow_extractor_produces_macro_call_step() -> None:
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("macro-flow"),
        location="macro-flow.asm",
        content="""
ZERO_REG MACRO reg
    xor  reg, reg
ENDM

PRINT_MSG MACRO msg_ptr, title_ptr
    invoke MessageBoxA, 0, msg_ptr, title_ptr, MB_OK
ENDM

caller PROC
    ZERO_REG eax
    ZERO_REG ebx
    PRINT_MSG offset msg, offset title
    ret
caller ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], MacroCallFlowStep)
    assert steps[0].target == "ZERO_REG"
    assert steps[0].args == ("eax",)
    assert isinstance(steps[1], MacroCallFlowStep)
    assert steps[1].target == "ZERO_REG"
    assert steps[1].args == ("ebx",)
    assert isinstance(steps[2], MacroCallFlowStep)
    assert steps[2].target == "PRINT_MSG"
    assert steps[2].args[0] == "offset msg"


def test_renderer_renders_macro_call_step() -> None:
    from masma.domain.control_flow import MacroCallFlowStep
    renderer = HtmlNassiDiagramRenderer()
    diagram = ControlFlowDiagram(
        source_location="macro.asm",
        functions=(
            FunctionControlFlow(
                name="demo",
                signature="demo PROC",
                container=None,
                steps=(
                    MacroCallFlowStep(target="ZERO_REG", args=("eax",)),
                    MacroCallFlowStep(target="PRINT_MSG", args=("offset msg", "offset title")),
                ),
            ),
        ),
    )
    html = renderer.render(diagram)
    assert "▷ ZERO_REG" in html
    assert "▷ PRINT_MSG" in html
    assert "ns-macro" in html


def test_control_flow_extractor_absorbs_mov_ecx_before_rep() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("repabs"),
        location="repabs.asm",
        content="""
copier PROC
    mov ecx, 16
    rep movsd
    ret
copier ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    # mov ecx, 16 must be absorbed — first step should be RepeatStringFlowStep
    assert isinstance(steps[0], RepeatStringFlowStep)
    assert steps[0].instruction == "movsd"


# ── Complex macro tests ────────────────────────────────────────────────────────

_COMPLEX_MACRO_SOURCE = """
PUSH_SAVED MACRO
    push ebx
    push esi
    push edi
ENDM

POP_SAVED MACRO
    pop  edi
    pop  esi
    pop  ebx
ENDM

SAFE_DIV MACRO dividend, divisor, dest
    LOCAL skip_div
    test divisor, divisor
    jz   skip_div
    mov  eax, dividend
    xor  edx, edx
    div  divisor
    mov  dest, eax
skip_div:
ENDM

worker PROC a:DWORD, b:DWORD, c:DWORD
    PUSH_SAVED
    SAFE_DIV a, b, c
    .WHILE eax > 0
        SAFE_DIV eax, 2, eax
    .ENDW
    POP_SAVED
    ret
worker ENDP
""".strip()


def test_macro_with_local_labels_and_args_detected() -> None:
    """SAFE_DIV has LOCAL + 3 args; PUSH_SAVED/POP_SAVED have no args."""
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("complex-macro"),
        location="complex.asm",
        content=_COMPLEX_MACRO_SOURCE,
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps

    assert isinstance(steps[0], MacroCallFlowStep)
    assert steps[0].target == "PUSH_SAVED"
    assert steps[0].args == ()

    assert isinstance(steps[1], MacroCallFlowStep)
    assert steps[1].target == "SAFE_DIV"
    assert steps[1].args == ("a", "b", "c")


def test_macro_call_inside_while_body() -> None:
    """SAFE_DIV inside .WHILE body is also a MacroCallFlowStep."""
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("macro-while"),
        location="macro-while.asm",
        content=_COMPLEX_MACRO_SOURCE,
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps

    while_step = steps[2]
    assert isinstance(while_step, WhileFlowStep)
    assert while_step.condition == "eax > 0"
    assert len(while_step.body_steps) == 1
    inner = while_step.body_steps[0]
    assert isinstance(inner, MacroCallFlowStep)
    assert inner.target == "SAFE_DIV"
    assert inner.args == ("eax", "2", "eax")


def test_macro_call_inside_switch_cases() -> None:
    """Macro call inside every switch case body."""
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("macro-switch"),
        location="macro-switch.asm",
        content="""
LOG_ERROR MACRO code
    push code
    call PrintError
    pop  eax
ENDM

dispatcher PROC code:DWORD
    mov  eax, code
    cmp  eax, 1
    je   case1
    cmp  eax, 2
    je   case2
    jmp  default_case
case1:
    LOG_ERROR 100
    jmp  done
case2:
    LOG_ERROR 200
    jmp  done
default_case:
    LOG_ERROR 0
done:
    ret
dispatcher ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps

    switch = steps[1]
    assert isinstance(switch, SwitchFlowStep)
    assert switch.expression == "eax"
    assert len(switch.cases) == 3
    for case in switch.cases:
        assert len(case.steps) == 1
        assert isinstance(case.steps[0], MacroCallFlowStep)
        assert case.steps[0].target == "LOG_ERROR"


def test_macro_call_inside_if_branches() -> None:
    """Macro calls inside .IF then/else branches."""
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("macro-if"),
        location="macro-if.asm",
        content="""
TRACE MACRO msg
    push offset msg
    call DebugPrint
    pop  eax
ENDM

ASSERT_NZ MACRO reg
    test reg, reg
    jnz  $ + 3
    int  3
ENDM

tricky PROC val:DWORD
    TRACE msg1
    mov  eax, val
    ASSERT_NZ eax
    .IF eax > 0
        TRACE msg2
        ASSERT_NZ eax
    .ENDIF
    ret
tricky ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps

    assert isinstance(steps[0], MacroCallFlowStep)
    assert steps[0].target == "TRACE"
    assert isinstance(steps[2], MacroCallFlowStep)
    assert steps[2].target == "ASSERT_NZ"

    if_step = steps[3]
    assert isinstance(if_step, IfFlowStep)
    assert isinstance(if_step.then_steps[0], MacroCallFlowStep)
    assert if_step.then_steps[0].target == "TRACE"
    assert isinstance(if_step.then_steps[1], MacroCallFlowStep)
    assert if_step.then_steps[1].target == "ASSERT_NZ"


def test_macro_defined_after_procedure_still_detected() -> None:
    """_scan_macro_names scans all lines, so a macro defined after its call site works."""
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("late-macro"),
        location="late.asm",
        content="""
user PROC
    LATE_MACRO eax
    ret
user ENDP

LATE_MACRO MACRO reg
    inc reg
ENDM
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], MacroCallFlowStep)
    assert steps[0].target == "LATE_MACRO"
    assert steps[0].args == ("eax",)


def test_macro_name_substring_of_instruction_not_confused() -> None:
    """'inc ecx' must stay ActionFlowStep even when macro INC_ALL is defined."""
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("substr"),
        location="substr.asm",
        content="""
INC_ALL MACRO
    inc eax
    inc ebx
ENDM

fn PROC
    inc ecx
    INC_ALL
    ret
fn ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], ActionFlowStep)
    assert steps[0].label == "inc ecx"
    assert isinstance(steps[1], MacroCallFlowStep)
    assert steps[1].target == "INC_ALL"
    assert steps[1].args == ()


def test_no_macros_in_source_produces_no_macro_steps() -> None:
    """Without any MACRO definition, no MacroCallFlowStep should appear."""
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("no-macro"),
        location="no-macro.asm",
        content="""
callee PROC
    mov eax, 1
    call SomeProc
    ret
callee ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert not any(isinstance(s, MacroCallFlowStep) for s in steps)


def test_macro_visible_across_multiple_procedures() -> None:
    """Same macro set is visible to all procedures in the file."""
    from masma.domain.control_flow import MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("multi-proc"),
        location="multi.asm",
        content="""
INIT MACRO
    xor eax, eax
    xor ebx, ebx
ENDM

proc_a PROC
    INIT
    inc eax
    ret
proc_a ENDP

proc_b PROC
    INIT
    inc ebx
    ret
proc_b ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    assert len(diagram.functions) == 2
    for fn in diagram.functions:
        assert isinstance(fn.steps[0], MacroCallFlowStep)
        assert fn.steps[0].target == "INIT"


# ── IFDEF / assembly-time conditional block tests ─────────────────────────────

def test_ifdef_block_produces_ifdef_flow_step() -> None:
    from masma.domain.control_flow import IfdefFlowStep, MacroCallFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("ifdef-basic"),
        location="ifdef.asm",
        content="""
PrintText MACRO msg
    push offset msg
    call _DebugPrint
ENDM

PE_OpenFile PROC
    IFDEF DEBUG32
    PrintText 'PE_OpenFile'
    ENDIF
    push ebp
    mov  ebp, esp
    IFDEF DEBUG32
    PrintText 'allocating'
    ENDIF
    sub  esp, 40h
    ret
PE_OpenFile ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps

    # Two IFDEF blocks + the real instructions
    assert isinstance(steps[0], IfdefFlowStep)
    assert steps[0].kind == "IFDEF"
    assert steps[0].condition == "DEBUG32"
    assert len(steps[0].body_steps) == 1
    assert isinstance(steps[0].body_steps[0], MacroCallFlowStep)
    assert steps[0].body_steps[0].target == "PrintText"

    assert steps[1].label == "push ebp"
    assert steps[2].label == "mov ebp, esp"

    assert isinstance(steps[3], IfdefFlowStep)
    assert steps[3].condition == "DEBUG32"

    assert steps[4].label == "sub esp, 40h"
    assert steps[5].label == "ret"


def test_ifndef_block_produces_ifdef_flow_step() -> None:
    from masma.domain.control_flow import IfdefFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("ifndef-basic"),
        location="ifndef.asm",
        content="""
fn PROC
    IFNDEF RELEASE
    int  3
    ENDIF
    mov  eax, 1
    ret
fn ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], IfdefFlowStep)
    assert steps[0].kind == "IFNDEF"
    assert steps[0].condition == "RELEASE"
    assert steps[0].body_steps[0].label == "int 3"
    assert steps[1].label == "mov eax, 1"
    assert steps[2].label == "ret"


def test_nested_ifdef_blocks_handled_correctly() -> None:
    from masma.domain.control_flow import IfdefFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("ifdef-nested"),
        location="nested.asm",
        content="""
fn PROC
    IFDEF OUTER
        mov  eax, 1
        IFDEF INNER
            mov  ebx, 2
        ENDIF
        mov  ecx, 3
    ENDIF
    mov  edx, 4
    ret
fn ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps

    # Outer IFDEF block + two real instructions
    assert isinstance(steps[0], IfdefFlowStep)
    assert steps[0].kind == "IFDEF"
    assert steps[0].condition == "OUTER"

    outer_body = steps[0].body_steps
    assert outer_body[0].label == "mov eax, 1"
    assert isinstance(outer_body[1], IfdefFlowStep)
    assert outer_body[1].condition == "INNER"
    assert outer_body[1].body_steps[0].label == "mov ebx, 2"
    assert outer_body[2].label == "mov ecx, 3"

    assert steps[1].label == "mov edx, 4"
    assert steps[2].label == "ret"


def test_ifdef_before_and_after_real_flow() -> None:
    from masma.domain.control_flow import IfdefFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("ifdef-around-if"),
        location="mixed.asm",
        content="""
fn PROC val:DWORD
    IFDEF DEBUG32
    push eax
    ENDIF
    mov  eax, val
    .IF eax > 0
        inc  eax
    .ENDIF
    IFDEF DEBUG32
    pop  eax
    ENDIF
    ret
fn ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert len(steps) == 5
    assert isinstance(steps[0], IfdefFlowStep)
    assert steps[0].condition == "DEBUG32"
    assert isinstance(steps[1], ActionFlowStep)
    assert steps[1].label == "mov eax, val"
    assert isinstance(steps[2], IfFlowStep)
    assert steps[2].condition == "eax > 0"
    assert isinstance(steps[3], IfdefFlowStep)
    assert steps[3].condition == "DEBUG32"
    assert isinstance(steps[4], ActionFlowStep)
    assert steps[4].label == "ret"


def test_if_bare_conditional_assembly_produces_ifdef_step() -> None:
    from masma.domain.control_flow import IfdefFlowStep
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("if-bare"),
        location="if-bare.asm",
        content="""
fn PROC
    IF @WordSize EQ 4
    mov  eax, 0
    ENDIF
    inc  ebx
    ret
fn ENDP
""".strip(),
    )
    diagram = extractor.extract(source)
    steps = diagram.functions[0].steps
    assert isinstance(steps[0], IfdefFlowStep)
    assert steps[0].kind == "IF"
    assert steps[0].condition == "@WordSize EQ 4"
    assert steps[0].body_steps[0].label == "mov eax, 0"
    assert steps[1].label == "inc ebx"
    assert steps[2].label == "ret"


def test_renderer_renders_ifdef_step() -> None:
    from masma.domain.control_flow import IfdefFlowStep
    renderer = HtmlNassiDiagramRenderer()
    diagram = ControlFlowDiagram(
        source_location="ifdef.asm",
        functions=(
            FunctionControlFlow(
                name="fn",
                signature="fn PROC",
                container=None,
                steps=(
                    IfdefFlowStep(
                        kind="IFDEF",
                        condition="DEBUG32",
                        body_steps=(ActionFlowStep(label="int 3"),),
                    ),
                    ActionFlowStep(label="ret"),
                ),
            ),
        ),
    )
    html = renderer.render(diagram)
    assert "# IFDEF DEBUG32" in html
    assert "ns-ifdef" in html
    assert "int 3" in html
