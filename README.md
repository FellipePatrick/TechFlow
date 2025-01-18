# TechFlow Solutions - Calculadora de Juros Compostos

Bem-vindo ao repositório oficial da **TechFlow Solutions** para o sistema de cálculo de juros compostos! Este projeto foi desenvolvido com foco em boas práticas de versionamento, organização e documentação para garantir um código limpo e de fácil manutenção.

---

## 🚀 Sobre o Projeto

A calculadora de juros compostos é um sistema simples que permite aos usuários calcular rapidamente os resultados de investimentos baseados em juros compostos. O objetivo do projeto é demonstrar práticas de desenvolvimento de software com foco em clareza, modularidade e colaboração.

---

## 📋 Funcionalidades

- Cálculo do montante final com base em:
  - Capital inicial
  - Taxa de juros (%)  - Período de aplicação
- Código modular para fácil adaptação e escalabilidade

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: [Python](https://www.python.org/)
- **Ferramentas de Documentação**: Markdown para o `README` e docstrings no código
- **Versionamento**: Git/GitHub
- **Testes**: pytest para testes automatizados

---

## 📥 Exemplos de Entrada e Saída

### Exemplo 1: Cálculo do Montante Final

#### Entrada:
```python
capital_inicial = 1000
taxa_juros = 0.05
periodo = 12
```

#### Saída:
```
Montante final: R$ 1795.86
```

## 🔧 Como Rodar o Código Localmente

Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado em sua máquina. Você também precisará do pip para gerenciar dependências e do pytest para rodar os testes.

### Passo a Passo

#### 1. Clone o repositório
```
git clone https://github.com/FellipePatrick/TechFlow.git
cd TechFlow
```
#### 2. Crie e ative um ambiente virtual
```
python3 -m venv venv
venv\Scripts\activate
```

#### 3. Instale o pytest
```
pip install pytest
```

#### 4. Rode o projeto
```
cd .\src\
python main.py
```

#### 5. Rode os testes
```
pytest
```