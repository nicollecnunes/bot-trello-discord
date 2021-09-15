import Author
import random

def DigaOi(ctx):
    nome = Author.GetName(ctx)

    p1 = ["Opa, ", "Fala comigo, ", "Eaí, ", "Oláá, ", "Oii, ", "Hey, "]
    n1 = (random.randint(0, len(p1)-1))

    p2 = ["! Beleza?", "!", "...", ". Tudo bem?", "!! Tranquilo?", "! Como você está?", "! Seu clockify tá ligado?", ". Já subiu pontos da gamificação hoje?"]
    n2 = (random.randint(0, len(p2)-1))
    
    return (p1[n1] + nome + p2[n2])