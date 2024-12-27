# Defense1 App - Road to beta

![Defense1 icon!](/assets/file.png "Defense1 icon!")

---
# Branches e merges

## O padrão que vamos seguir será o seguinte:

### 1. **main**: 
Branch principal de produção o merge das demais branchs nela só ocorreram quando as funcionalidades desenvolvidas em suas respectivas branchs forem **validadas** na branch **dev-env**

### 2. **dev-env**:
Branch responsavel por manter o ambiente de dev e o ambiente de prod separados, aqui serão realizados todos os testes necessarios antes de serem incorportados a **main**

### 3. **NOME_DA_FUNCIONALIDADE**
Branch que será criada dendo da branch **dev-env** que será a respeito da funcionalidade que está sendo desenvolvida


- Primeira coisa que devemos perceber é que ao clonar o repositorio, você estará na branch "**main**"

	- Para checar isso, basta digitar o código:
	
		`git branch`

	- você deverá ter um retorno parecido com isso em seu terminal
	
		```bash
		damiani@NOTDEF0027:~/Defense1$ git branch
		dev-env
		* main
		``` 	

- Agora comece por criar uma branch que seja de acordo com a atividade que vc esteja realizado nesta sprint

	- Primeiro garante que você esteja na branch dev-env
		```bash
		damiani@NOTDEF0027:~/Defense1$ git checkout dev-env
		damiani@NOTDEF0027:~/Defense1$ git branch
		* dev-env
		main
		```

	- Agora basta criar um da branch dev-env a respeito da funcionalidade que será desenvolvida:

		`git checkout -b <NOME_DA_SUA_BRANCH>`

- Assim que a funcionalidade for desenvolvida faça o merge para a dev-env para validação
	
	- Primeiro volte para a dev-env
		`git checkout dev-env` 
	
	- Agora faça o merge
		`git merge <NOME_DA_SUA_BRANCH>`

- Assim que a funcionalidade for validada faça o merge para a main para enviar para produção
	
	- Primeiro volte para a main
		`git checkout main` 
	
	- Agora faça o merge
		`git merge dev-env`

- Agora basta fazer o push de todas as alterações feitas

# Back-end

## Linguagens

### 1. Instalar o python 3.12.8

1. Começe rodando o comando:

	- `sudo apt update && sudo apt upgrade -y`

	- para garantir que o linux esteja atualizado

2. em seguida rode o comando para instalar o python:

	- `sudo apt install python3.12 python3.12-venv python3.12-dev -y`

3. Confira a instalação através do seguinte comando:

	- `python3 --version`

4. Após instalar a linguagem instale as seguintes bibliotecas

	- Instalação do PIP:

		- O pip é a ferramenta de gerenciamento de pacotes do python, através dela vamos instalar as diversas bibliotecas que vamos usar no projeto
		- Execute o comando:
			- `sudo apt install pip -y`

	- Instalação do virtualenv:

		- O virtualenv é uma bibioteca para fazermos o gerenciamento do ambiente de desenvolvimento nela, poderemos instanciar as instalações de todas as bibliotecas que vamos usar durante o desenvolvimento da aplicação
		- Execute o comando:
			- `sudo apt install python3-virtualenv`

				> # OBS!!
				>	
				> A partir daqui, é para que você já esteja no diretorio do repositorio em sua maquina,
				>
				> Portando, as instalações a seguir deverão ser feitas dentro do ambiente virtual,
				>
				> Para acessa-lo rode o comando:
				>
				> 	`source .venv/bin/activate`
				>
				> O retorno no terminal deve ser algo parecido com isto:
				>
				> 	`damiani@NOTDEF0027:~/Defense1$ source .venv/bin/activate`
				> 
				> 	`(.venv) damiani@NOTDEF0027:~/Defense1$`

	- Instalando o restante das bibliotecas:

		- A partir daqui basta rodar o comando
		- `pip install <NOME_DA_LIB>`
		- para instalar as bibliotecas desta lista na seguinte ordem:
			1. Flask

## Banco de dados

### 2. Instalar o banco de dados


> # Cola de comandos:
> ## Virtual env:
>	 Entrar no ambiente virtual
>
> 	`source .venv/bin/activate`
>
> 	Para sair:
>
> 	`deactivate`
>
> ## Para subir alterações no app:
>
>	`export FLASK_APP=app`
>
>	`flask run`