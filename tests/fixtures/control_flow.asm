include windows.inc

.data
limit dd 100

.code
score PROC value:DWORD
    mov eax, value
    .IF eax > 100
        mov eax, 100
    .ELSEIF eax < 0
        xor eax, eax
    .ELSE
        .WHILE eax < 100
            add eax, 10
        .ENDW
    .ENDIF

    .REPEAT
        dec eax
    .UNTIL eax == 42

    ret
score ENDP

normalize PROC input:DWORD
start_loop:
    mov eax, input
    .IF eax == 0
        inc eax
    .ENDIF
    ret
normalize ENDP

END
