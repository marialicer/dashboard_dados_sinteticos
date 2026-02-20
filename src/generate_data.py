# %%

import pandas as pd
import random
import unicodedata
import re

# %%
def gerar_slug(titulo: str) -> str:
    texto_normalizado = unicodedata.normalize("NFKD", titulo)
    slug = "".join(c for c in texto_normalizado if not unicodedata.combining(c))
    slug = slug.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s-]+", "-", slug)
    return slug


def gerar_dataset(n_linhas: int = 5000) -> pd.DataFrame:

    componentes = {
        "Política": {
            "quem": ["Câmara", "Senado", "STF", "Governo Federal", "Prefeitura de SP",
                     "Liderança do partido", "Ministério da Justiça", "Itamaraty", "Congresso Nacional"],
            "acao": ["vota amanhã", "suspende", "anuncia novos cortes em",
                     "prioriza investimentos para", "abre investigação sobre",
                     "assina acordo de", "adia decisão sobre"],
            "onde": ["na reforma tributária", "no orçamento de 2024", "na segurança pública",
                     "em políticas educacionais", "no setor de transportes",
                     "em infraestrutura", "na saúde básica"]
        },
        "Economia": {
            "quem": ["Mercado financeiro", "Banco Central", "Ibovespa", "Setor varejista",
                     "Agronegócio brasileiro", "Dólar", "Petrobras", "FMI", "Startup unicórnio"],
            "acao": ["reage a", "projeta crescimento de", "sofre queda após",
                     "bate recorde em", "estuda novas taxas para",
                     "lidera ranking de", "antecipa tendência de"],
            "onde": ["no comércio exterior", "na taxa de juros", "na inflação acumulada",
                     "no mercado de capitais", "na exportação de grãos",
                     "no consumo das famílias"]
        },
        "Tecnologia": {
            "quem": ["Nova IA", "Vazamento de dados", "Apple", "Elon Musk",
                     "Metaverso", "Google", "Criptomoeda", "O avanço do 5G", "ChatGPT"],
            "acao": ["transforma", "ameaça mercado de", "revela futuro de",
                     "impulsiona inovação em", "gera polêmica sobre",
                     "facilita acesso a", "promete mudar"],
            "onde": ["no desenvolvimento de softwares", "na proteção de dados",
                     "em dispositivos móveis", "na inteligência artificial",
                     "no trabalho remoto", "em games"]
        },
        "Cultura": {
            "quem": ["Festival de cinema", "Nova série", "Artista internacional",
                     "Exposição de arte", "Premiação musical",
                     "Livro de estreia", "Show histórico"],
            "acao": ["quebra recordes em", "gera debate sobre",
                     "ganha destaque no", "antecipa tendências em",
                     "revela bastidores de", "anuncia turnê em",
                     "impacta cenário de"],
            "onde": ["no streaming nacional", "na cultura pop",
                     "no entretenimento digital", "nas artes visuais",
                     "no mercado editorial", "no teatro moderno"]
        }
    }

    titulos_unicos = set()
    dados = []

    while len(titulos_unicos) < n_linhas:
        editoria = random.choice(list(componentes.keys()))
        info = componentes[editoria]

        frase = f"{random.choice(info['quem'])} {random.choice(info['acao'])} {random.choice(info['onde'])}"
        detalhe = random.choice([
            "neste mês", "em todo o país", "após nova reunião",
            "segundo especialistas", "de forma urgente",
            "no primeiro trimestre", "em escala global"
        ])

        titulo_final = f"{frase} {detalhe}"

        if titulo_final not in titulos_unicos:
            titulos_unicos.add(titulo_final)

            slug = gerar_slug(titulo_final)
            url = f"https://portal.com.br/{editoria.lower()}/{slug}"
            views = random.randint(800, 1_500_000)

            dados.append([titulo_final, url, editoria, views])

    df = pd.DataFrame(
        dados,
        columns=["titulo", "url", "editoria", "visualizacoes_5_anos"]
    )

    return df


if __name__ == "__main__":
    df = gerar_dataset(5000)
    df.to_csv("dataset_final.csv", index=False, encoding="utf-8-sig")
    print(f"Dataset gerado com {len(df)} linhas.")
# %%
