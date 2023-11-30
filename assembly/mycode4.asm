MOV AL, 2    ;.1
XOR AH, AH   ; Clear AH
XOR BH, BH   ; Clear BH

MOV BL, 3    ;.2
MUL BL       ;.3
XOR AH, AH   ; Clear AH
XOR BH, BH   ; Clear BH

MOV BL, 4    ;.4
MUL BL       ;.5

XOR AH, AH   ; Clear AH
XOR BH, BH   ; Clear BH

MOV BL, 5    ;.6
MUL BL       ;.7

XOR AH, AH   ; Clear AH
XOR BH, BH   ; Clear BH

MOV AX, 40   ;.8
XOR AH, AH   ; Clear AH
XOR BH, BH   ; Clear BH

MOV BL, 6    ;.9
DIV BL       ;.10

XOR AH, AH   ; Clear AH
XOR BH, BH   ; Clear BH

MOV BL, 3    ;.11
DIV BL       ;.12

XOR AH, AH   ; Clear AH
XOR BH, BH   ; Clear BH

MOV BL, 2    ;.13
DIV BL       ;.14

XOR AH, AH   ; Clear AH
XOR BH, BH   ; Clear BH
