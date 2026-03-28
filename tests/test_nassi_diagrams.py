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
    assert "UNTIL eax == 42" in document.html
    assert "Masma" in document.html


def test_nassi_service_builds_directory_bundle_for_masm() -> None:
    service = _build_service()
    bundle = service.build_directory_diagrams(
        BuildNassiDirectoryCommand(root_path=str(ROOT / "tests" / "fixtures"))
    )

    assert bundle.document_count == 3
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
    assert steps[1].condition == "ebx & ebx != 0"
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
    assert payload["document_count"] == 3
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
