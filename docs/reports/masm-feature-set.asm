include windows.inc
includelib kernel32.lib

STD_OUTPUT_HANDLE equ -11
MAX_RETRIES equ 3

.const
BannerText db "Masma Feature Set", 0

.data
buffer db 64 dup(0)
counter dd 0
limit dd 100

.data?
scratch dq ?

Point STRUCT
    x DWORD ?
    y DWORD ?
Point ENDS

PrintLine MACRO text:REQ
    invoke StdOut, text
ENDM

.code
normalize PROC value:DWORD
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
normalize ENDP

scan PROC input:DWORD
loop_top:
    cmp eax, MAX_RETRIES
    jge loop_done
    inc eax
    jmp loop_top
loop_done:
    test ebx, ebx
    jz zero_case
    mov ecx, 1
    jmp after_if
zero_case:
    mov ecx, 0
after_if:
    ret
scan ENDP

END normalize
