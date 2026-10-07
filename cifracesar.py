def cifrar_cesar(texto: str, k: int) -> str:
    resultado = []
    texto = texto.upper()

    for char in texto:
        if "A" <= char <= "Z":
            p = ord(char) - ord("A")
            c = (p + k) % 26
            resultado.append(chr(c + ord("A")))
        else:
            resultado.append(char)

    return "".join(resultado)


def decifrar_cesar(texto: str, k: int) -> str:
    return cifrar_cesar(texto, -k)


if __name__ == "__main__":
    palavra = "SEGURANCA"
    chave = 3

    cifrado = cifrar_cesar(palavra, chave)
    decifrado = decifrar_cesar(cifrado, chave)

    print(f"Original: {palavra}")
    print(f"Cifrado:  {cifrado}")
    print(f"Decifrado: {decifrado}")