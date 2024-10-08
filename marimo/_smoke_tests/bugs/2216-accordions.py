# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.8.11"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.accordion(
        {
            """**e)** Diria que o trabalho, a educação e a idade explicam muita da variação no sono? Que outros fatores poderiam afetar o tempo passado a dormir? Estarão esses fatores provavelmente correlacionados com o trabalho?""": """
        - O $R^2 = 0.113$ é reduzido
        - Só 11.3% da variabilidade do sono é explicada pelas variáveis explicativas escolhidas para o modelo
        - Há fatores que ficaram de fora do modelo que podem influenciar o sono. Exemplos:
            - _Stress_
            - Idade dos filhos
            - Profissão
        """
        }
    )
    return


@app.cell
def __(mo):
    mo.accordion(
        {
            r"""**a)** Estime os coeficientes da regressão de $Y$ sobre $X_1$, bem como o error padrão da regressão e o $R^2$. O que pensa da estimativa de $\beta_1$?""": mo.md(
                """
                - Introduzindo o commando `regress Y X1` obtemos a estimação abaixo
                - A estimativa para $\beta_1$ é inesperada, pois contradiz a teoria económica de que existe uma relação negativa entre o preço e as vendas.
                """
            )
        }
    )
    return


if __name__ == "__main__":
    app.run()
