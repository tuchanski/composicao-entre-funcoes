# Guilherme Tuchanski Rocha, Guilherme Teixeira, Luiz Henrique Matoso
def composicao(f, g):
  return lambda x: f(g(x))  # g(x) é aplicado à função f(x)


def main():
  # Funções f(x) e g(x), recebe a operação substituindo ** por ^ para potência
  f_expressao = input("Digite a expressão para f(x): ").replace('^', '**')
  g_expressao = input("Digite a expressão para g(x): ").replace('^', '**')

  # Definindo as funções f(x) e g(x) usando eval()
  f = eval("lambda x: " + f_expressao)
  g = eval("lambda x: " + g_expressao)

  # Valor de x
  x = float(input("Digite o valor de x: "))

  # Composições de função
  fog = composicao(f, g)
  gog = composicao(g, g)
  fof = composicao(f, f)
  gof = composicao(g, f)

  # Avaliando as funções compostas com o valor de x
  print("(g ° f)({}) =".format(x), gof(x))
  print("(g ° g)({}) =".format(x), gog(x))
  print("(f ° f)({}) =".format(x), fof(x))
  print("(f ° g)({}) =".format(x), fog(x))


main()
