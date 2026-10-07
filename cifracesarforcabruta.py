if __name__ == "__main__":
    textocifrado = "L DPRFCLYNL OL TYQZCXLNLZ OPAPYOP OP NZYQTOPYNTLWTOLOP TYEPRCTOLOP P OTDAZYTMTWTOLOP"

    for i in range(26):
        decifrado = []
        
        for char in textocifrado:
            if "A" <= char <= "Z":
                letra = ord(char) - ord("A")
                letra = (letra - i) % 26
                decifrado.append(chr(letra + ord("A")))
            
            else:
                decifrado.append(char)
            
    
        print(f"k={i:2d}: {''.join(decifrado)}")
