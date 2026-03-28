;; feature_tour.asm — covers every implemented control-flow step type

.data
    msg_title   db "Masma", 0
    msg_body    db "Feature tour", 0
    src_buf     dd 16 dup(0)
    dst_buf     dd 16 dup(0)

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

; ─── 13. MacroCallFlowStep (user-defined macro expansion) ─────────────────────
demo_macro PROC
    ZERO_REG eax
    ZERO_REG ebx
    PRINT_MSG offset msg_body, offset msg_title
    mov  ecx, 42
    CLAMP ecx, 0, 100
    ret
demo_macro ENDP

END
