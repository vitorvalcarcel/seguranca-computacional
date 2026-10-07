if __name__ == "__main__":
    resultado = []
    entrada = "seguranca"

    for char in entrada:
        nletra = ord(char) - 97
        nletra += 3
        nletra = nletra % 26
        resultado.append(chr(nletra+97))
    
    print(f"Cifrado:  {resultado}")