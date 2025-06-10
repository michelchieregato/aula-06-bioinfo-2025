def test_ex_0():
    import exercicio_0_exemplo

    assert exercicio_0_exemplo.achar_maior_valor([1, 88, 0]) == 88
    assert exercicio_0_exemplo.achar_maior_valor([-1, -10, -100]) == -1


def test_ex_1():
    import exercicio_1

    assert exercicio_1.verificar_nota(10) == "Aprovado"
    assert exercicio_1.verificar_nota(4) == "Recuperação"
    assert exercicio_1.verificar_nota(1) == "Reprovado"


def test_ex_2():
    import exercicio_2

    organismo = exercicio_2.criar_organismo(1, "Nome", 100)
    assert organismo["id"] == 1
    assert organismo["nome"] == "Nome"
    assert organismo["tamanho_do_genoma"] == 100

    organismo_2 = exercicio_2.criar_organismo(10, 'HIV', 1000)
    assert organismo_2["id"] == 10
    assert organismo_2["nome"] == "HIV"
    assert organismo_2["tamanho_do_genoma"] == 1000


def test_ex_3():
    import exercicio_3
    assert exercicio_3.calcular_media([0, 100, 200]) == 100
    assert exercicio_3.calcular_media([-10, -10, -10, -10]) == -10
    assert exercicio_3.calcular_media([10, 20, 30, 40, 0]) == 20


def test_ex_4():
    import exercicio_4

    assert exercicio_4.filtrar_lista_por_numeros_primos([10, 11, 50, 13, 99, 7]) == [11, 13, 7]
    assert exercicio_4.filtrar_lista_por_numeros_primos([2, 3, 4, 5]) == [2, 3, 5]

