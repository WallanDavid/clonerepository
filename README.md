# 🧪 CloneRepository — GitHub Cloner + Dashboard 📊  
Ferramenta em Python para clonar todos os repositórios de uma organização no GitHub **e** gerar um **dashboard visual interativo** com dados de estrelas, forks e issues.  
> 💡 Ideal para DevOps, líderes técnicos, squads de engenharia e entusiastas de automação!

## 🚀 Funcionalidades  
- 🔁 Clona todos os repositórios de uma organização (privados ou públicos)  
- 📈 Gera gráficos com:  
  - Estrelas ⭐  
  - Forks 🍴  
  - Issues abertas 🐛  
- 🧠 Usa a API oficial do GitHub com autenticação por token  
- ⚙️ Tudo construído em Python com Plotly, Requests e dotenv  

## 📦 Tecnologias  
- Python 3+  
- `requests`  
- `python-dotenv`  
- `plotly`  
- `pandas`  
- GitHub REST API v3  

## ⚙️ Como usar  

### 1. Clone este repositório  
```bash
git clone https://github.com/WallanDavid/clonerepository.git  
cd clonerepository
```  

### 2. Instale as dependências  
```bash
pip install -r requirements.txt
```  
Ou manualmente:  
```bash
pip install requests python-dotenv plotly pandas
```  

### 3. Configure seu `.env`  
Crie um arquivo `.env` na raiz do projeto com:  
```env
GITHUB_TOKEN=ghp_seu_token_aqui
```  
> O token deve ter as permissões: `repo`, `read:org`  

### 4. Altere o nome da organização no código  
No arquivo `main.py`, substitua:  
```python
ORG = 'sua-organizacao'
```  

### ▶️ Executando  
```bash
python main.py
```  
Você verá:  
- ✅ Terminal listando os repositórios  
- 📁 Repositórios clonados localmente em `repos_clonados/`  
- 🌐 Navegador abrindo gráficos com métricas interativas  

## 🔒 Segurança  
- O projeto ignora automaticamente:  
  - `.env`  
  - Pasta `repos_clonados/`  
- Tudo protegido via `.gitignore`  

## 🤝 Contribuição  
Pull requests são bem-vindos! Bora construir mais recursos juntos:  
- Exportar CSV  
- Dashboard Web com Dash  
- Suporte a múltiplas orgs  
- Deploy via Streamlit ou Docker  

## 📄 Licença  
MIT © [WallanDavid](https://github.com/WallanDavid)
