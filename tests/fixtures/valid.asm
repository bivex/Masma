include windows.inc
includelib kernel32.lib

STD_OUTPUT_HANDLE equ -11

.data
message db "Hello, MASM", 0
counter dd 0

Point STRUCT
    x DWORD ?
    y DWORD ?
Point ENDS

PrintLine MACRO text:REQ
    invoke StdOut, text
ENDM

.code
main PROC
    mov eax, counter
    ret
main ENDP

helper PROC value:DWORD
    LOCAL total:DWORD
    mov eax, value
    ret
helper ENDP

END main
