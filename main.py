from dotenv import load_dotenv
import os
import requests
import subprocess
import pandas as pd
import plotly.express as px

# Carrega variáveis do .env
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

# Confere se o token foi carregado
if not TOKEN:
    raise Exception("Token do GitHub não foi carregado. Verifique seu .env!")

# Nome da organização (troque pelo nome real da sua org)
ORG = 'clonadores-tech'

# Cabeçalhos para a API
HEADERS = {
    "Authorization": f"token {TOKEN}"
}

# 🧠 Função para buscar todos os repositórios da organização
def get_repositories(org):
    url = f"https://api.github.com/orgs/{org}/repos?per_page=100"
    repos = []
    while url:
        res = requests.get(url, headers=HEADERS)
        res.raise_for_status()
        repos.extend(res.json())
        url = res.links.get('next', {}).get('url')
    return repos

# 🛠️ Função para clonar repositórios localmente
def clonar_repositorios(repos, destino='repos_clonados'):
    os.makedirs(destino, exist_ok=True)
    for repo in repos:
        nome = repo['name']
        url_clone = repo['clone_url']
        print(f"🔄 Clonando {nome}...")
        subprocess.run(['git', 'clone', url_clone], cwd=destino)

# 📊 Gera visualizações dos dados dos repositórios
def gerar_dashboard(repos):
    if not repos:
        print("⚠️  Nenhum repositório para mostrar no dashboard.")
        return

    df = pd.DataFrame([{
        'Repositório': r['name'],
        'Estrelas': r['stargazers_count'],
        'Forks': r['forks_count'],
        'Issues Abertas': r['open_issues_count'],
        'Privado': r['private']
    } for r in repos])

    print("\n📊 Gerando dashboard...")

    fig1 = px.bar(df, x='Repositório', y='Estrelas', title='⭐ Estrelas por Repositório')
    fig1.show()

    fig2 = px.bar(df, x='Repositório', y='Forks', title='🍴 Forks por Repositório')
    fig2.show()

    fig3 = px.bar(df, x='Repositório', y='Issues Abertas', title='🐛 Issues Abertas por Repositório')
    fig3.show()

# 🚀 Execução principal
if __name__ == "__main__":
    repos = get_repositories(ORG)

    print("\n📊 Repositórios encontrados:")
    for repo in repos:
        print(f"→ {repo['name']} - ⭐ {repo['stargazers_count']} | 🍴 {repo['forks_count']} | 🐛 {repo['open_issues_count']}")

    print("\n📥 Iniciando clonagem...")
    clonar_repositorios(repos)

    gerar_dashboard(repos)
