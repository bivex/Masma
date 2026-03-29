; feature_tour.asm — covers every implemented control-flow step type
; Exercises ActionFlowStep, IfFlowStep, WhileFlowStep, RepeatWhileFlowStep,
; SwitchFlowStep, ForInFlowStep, InvokeFlowStep, CallFlowStep,
; MacroCallFlowStep, RepeatStringFlowStep, IfdefFlowStep, LabelFlowStep,
; LocalDeclFlowStep.

; ─── External symbol declarations ────────────────────────────────────────────
EXTERN  GetProcessHeap:PROC, HeapAlloc:PROC, HeapFree:PROC
EXTERN  ExitProcess:PROC, MessageBoxA:PROC
EXTERNDEF  _errno:DWORD, _environ:DWORD

; ─── Public symbol exports ────────────────────────────────────────────────────
PUBLIC  demo_action, demo_if, demo_while
PUBLIC  demo_composite, demo_call

; ─── Type aliases (TYPEDEF) ───────────────────────────────────────────────────
LPVOID  TYPEDEF PTR
HANDLE  TYPEDEF DWORD
BOOL    TYPEDEF DWORD
SIZE_T  TYPEDEF DWORD

; ─── Struct definitions ───────────────────────────────────────────────────────
POINT STRUCT
    x   DWORD ?
    y   DWORD ?
POINT ENDS

RECT STRUCT
    left    DWORD ?
    top     DWORD ?
    right   DWORD ?
    bottom  DWORD ?
RECT ENDS

; ─── Union definitions ────────────────────────────────────────────────────────
REG32 UNION
    dw_val  DWORD ?
    lo_word WORD  ?
    lo_byte BYTE  ?
REG32 ENDS

VARIANT_VAL UNION
    int_val   DWORD ?
    float_val REAL4 ?
    ptr_val   DWORD ?
VARIANT_VAL ENDS

; ─── User-defined macros ──────────────────────────────────────────────────────
ZERO_REG MACRO reg
    xor  reg, reg
ENDM

PRINT_MSG MACRO msg_ptr, title_ptr
    invoke MessageBoxA, 0, msg_ptr, title_ptr, MB_OK
ENDM

CLAMP MACRO val, lo, hi
    .IF val < lo
        mov  val, lo
    .ELSEIF val > hi
        mov  val, hi
    .ENDIF
ENDM

.data
    msg_title   db "Masma", 0
    msg_body    db "Feature tour", 0
    src_buf     dd 16 dup(0)
    dst_buf     dd 16 dup(0)

.code

; ─── 1. ActionFlowStep ────────────────────────────────────────────────────────
; Plain straight-line instructions — the fallback step type.
demo_action PROC
    mov  eax, 1
    xor  ebx, ebx
    inc  ecx
    ret
demo_action ENDP

; ─── 2. IfFlowStep (.IF structured) ──────────────────────────────────────────
; .IF / .ELSEIF / .ELSE / .ENDIF directive block.
demo_if PROC value:DWORD
    mov  eax, value
    .IF eax > 100
        mov  eax, 100
    .ELSEIF eax < 0
        xor  eax, eax
    .ELSE
        inc  eax
    .ENDIF
    ret
demo_if ENDP

; ─── 3. WhileFlowStep (.WHILE structured) ────────────────────────────────────
demo_while PROC
    mov  eax, 0
    .WHILE eax < 10
        inc  eax
    .ENDW
    ret
demo_while ENDP

; ─── 4. RepeatWhileFlowStep (.REPEAT structured) ─────────────────────────────
demo_repeat PROC
    mov  eax, 0
    .REPEAT
        inc  eax
    .UNTIL eax == 5
    ret
demo_repeat ENDP

; ─── 5. IfFlowStep (recovered cmp/jcc — jump-based if/else) ──────────────────
demo_jump_if PROC
    cmp  eax, 0
    jz   zero_branch
    inc  ebx
    jmp  after_branch
zero_branch:
    dec  ebx
after_branch:
    ret
demo_jump_if ENDP

; ─── 6. WhileFlowStep (recovered top-tested jump loop) ───────────────────────
demo_jump_while PROC
loop_top:
    cmp  ecx, 0
    jle  loop_exit
    dec  ecx
    jmp  loop_top
loop_exit:
    ret
demo_jump_while ENDP

; ─── 7. RepeatWhileFlowStep (recovered bottom-tested jump loop) ───────────────
demo_jump_repeat PROC
do_top:
    inc  eax
    cmp  eax, 10
    jl   do_top
    ret
demo_jump_repeat ENDP

; ─── 8. SwitchFlowStep (cmp/je chain) ────────────────────────────────────────
demo_switch PROC code:DWORD
    mov  eax, code
    cmp  eax, 1
    je   case_create
    cmp  eax, 2
    je   case_read
    cmp  eax, 3
    je   case_update
    cmp  eax, 4
    je   case_delete
    jmp  case_default
case_create:
    mov  ebx, 10
    jmp  switch_end
case_read:
    mov  ebx, 20
    jmp  switch_end
case_update:
    mov  ebx, 30
    jmp  switch_end
case_delete:
    mov  ebx, 40
    jmp  switch_end
case_default:
    xor  ebx, ebx
switch_end:
    ret
demo_switch ENDP

; ─── 9. ForInFlowStep (MASM loop instruction, ECX-counted) ───────────────────
demo_forin PROC
    mov  ecx, 8
count_loop:
    shl  eax, 1
    loop count_loop
    ret
demo_forin ENDP

; ─── 10. InvokeFlowStep (MASM INVOKE macro) ───────────────────────────────────
demo_invoke PROC
    invoke MessageBoxA, 0, offset msg_body, offset msg_title, MB_OK
    invoke ExitProcess, 0
    ret
demo_invoke ENDP

; ─── 11. RepeatStringFlowStep (REP/REPNE string instructions) ─────────────────
demo_repstr PROC
    mov  ecx, 16
    rep  movsd
    mov  ecx, 64
    rep  stosb
    mov  ecx, 32
    repne scasb
    ret
demo_repstr ENDP

; ─── 12. Composite — all nested together ─────────────────────────────────────
demo_composite PROC buf:DWORD, len:DWORD
    mov  eax, len
    .IF eax == 0
        ret
    .ENDIF

    ; fill destination
    mov  ecx, eax
    rep  stosd

    ; process each entry
    mov  ecx, eax
proc_loop:
    cmp  ebx, 1
    je   do_fast
    cmp  ebx, 2
    je   do_slow
    jmp  do_default
do_fast:
    shl  edx, 2
    jmp  proc_next
do_slow:
    imul edx, 10
    jmp  proc_next
do_default:
    inc  edx
proc_next:
    loop proc_loop

    invoke HeapFree, 0, 0, buf
    ret
demo_composite ENDP

; ─── 13. CallFlowStep (direct call proc) ─────────────────────────────────────
demo_call PROC
    call demo_action
    call demo_while
    ; indirect call [reg] stays as ActionFlowStep
    call eax
    ret
demo_call ENDP

; ─── 14. IfdefFlowStep (assembly-time IFDEF / IFNDEF conditional) ─────────────
IFDEF DEBUG32
    DEBUG_FLAG EQU 1
ENDIF

demo_ifdef PROC
    mov  eax, 0
    IFDEF DEBUG32
        int  3
        mov  eax, 0DEADBEEFh
    ENDIF
    IFNDEF RELEASE
        mov  ebx, 1
    ENDIF
    IF DEBUG_FLAG
        call demo_action
    ENDIF
    ret
demo_ifdef ENDP

; ─── 15. LabelFlowStep + AlignFlowStep ────────────────────────────────────────
demo_label PROC
    mov  eax, 0
setup_phase:
    mov  ebx, 1
    mov  ecx, 2
    align 16
process_phase:
    add  eax, ebx
    add  eax, ecx
    align 4
teardown_phase:
    xor  ebx, ebx
    xor  ecx, ecx
    ret
demo_label ENDP

; ─── 16. JumpFlowStep (unstructured goto / conditional branch) ────────────────
; Standalone jumps without a preceding cmp — not absorbed into if/while/switch.
demo_jumps PROC
    ; conditional jumps — FLAGS already set by caller (no cmp here)
    jz   lbl_a               ; equal / zero         → amber
    jnz  lbl_a               ; not equal / not zero → amber
    jg   lbl_a               ; signed greater       → amber
    jge  lbl_a               ; signed ≥             → amber
    jl   lbl_a               ; signed less          → amber
    jle  lbl_a               ; signed ≤             → amber
    ja   lbl_a               ; unsigned above       → amber
    jae  lbl_a               ; unsigned ≥           → amber
    jb   lbl_a               ; unsigned below       → amber
    jbe  lbl_a               ; unsigned ≤           → amber
    jo   lbl_a               ; overflow             → amber
    jno  lbl_a               ; no overflow          → amber
    js   lbl_a               ; sign (negative)      → amber
    jns  lbl_a               ; no sign (positive)   → amber
    jp   lbl_a               ; parity even          → amber
    jnp  lbl_a               ; parity odd           → amber
    jcxz  lbl_a              ; CX == 0              → amber
    jecxz lbl_a              ; ECX == 0             → amber
lbl_a:
    ; unconditional jumps — always red
    jmp  lbl_a               ; symbolic label
    jmp  eax                 ; register indirect
    jmp  [ebx]               ; memory indirect
    jmpf far_label           ; far jump
lbl_b:
    ret
demo_jumps ENDP

; ─── 17. LocalDeclFlowStep (stack-frame local variable aliases) ───────────────
; EQU aliases for bp-relative stack slots — compiler/assembler generated.
demo_locals PROC
AllocFlags  equ byte ptr [bp - 2]
MemSize     equ word ptr [bp - 4]
BufPtr      equ [bp - 8]
    push bp
    mov  bp, sp
    sub  sp, 8
    mov  AllocFlags, 0
    mov  MemSize, 512
    mov  BufPtr, 0
    pop  bp
    ret
demo_locals ENDP

; ─── 18. MacroCallFlowStep (user-defined macro expansion) ─────────────────────
demo_macro PROC
    ZERO_REG eax
    ZERO_REG ebx
    PRINT_MSG offset msg_body, offset msg_title
    mov  ecx, 42
    CLAMP ecx, 0, 100
    ret
demo_macro ENDP

; ─── 19. Segments — procs in named and standard segments ──────────────────────
INIT_SEG SEGMENT
demo_init PROC
    ; runs before main code — a typical init-segment pattern
    xor  eax, eax
    mov  [init_flag], eax
    ret
demo_init ENDP
INIT_SEG ENDS

PAGE_SEG SEGMENT
demo_page PROC
    push ebp
    mov  ebp, esp
    .IF eax == 0
        call demo_init
    .ELSE
        inc  eax
    .ENDIF
    pop  ebp
    ret
demo_page ENDP
PAGE_SEG ENDS

; ─── 20. CommentFlowStep (full-line comments inside procedures) ──────────────
; Comments are captured and shown as muted blocks; toggle on/off in toolbar.
demo_comments PROC
    ; Initialize the counter to zero
    xor  eax, eax
    ; Load the base address of the buffer
    mov  esi, offset src_buf
    ; Copy loop — process all 16 elements
    mov  ecx, 16
copy_loop:
    ; Read next DWORD from source
    lodsd
    ; Double the value
    shl  eax, 1
    ; Store to destination
    stosd
    ; Continue if elements remain
    loop copy_loop
    ; Done — return to caller
    ret
demo_comments ENDP

; ─── 21. OPTION directive — bare prologue/epilogue control ──────────────────
; option PROLOGUE:NONE / EPILOGUE:NONE disables auto frame generation.
; These are filtered out of the control flow (passthrough directives).
malloc PROC dwBytes:DWORD
    ; Allocate from the current process heap
    option PROLOGUE:NONE
    option EPILOGUE:NONE
    invoke GetProcessHeap
    invoke HeapAlloc, eax, 0, dwBytes
    ret (sizeof DWORD)
    option PROLOGUE:PROLOGUEDEF
    option EPILOGUE:EPILOGUEDEF
malloc ENDP

; ─── 22. Breakpoint & halt instructions ─────────────────────────────────────
; int 3 — software breakpoint (red stop icon)
; hlt / ud2 — CPU halt/undefined (orange stop icon)
demo_stop PROC
    mov  eax, 0
    int  3
    hlt
    ud2
    ret
demo_stop ENDP

END demo_init
