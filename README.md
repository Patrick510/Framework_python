# O QUE INSTALAR

- FLASK e SQLAlchemy
- numpy

# CRIANDO AMBIENTE VIRTUAL

```
PS C:\estudos\4 PERIODO\frameworks\Proj1> python -m venv env
PS C:\estudos\4 PERIODO\frameworks\Proj1>
PS C:\estudos\4 PERIODO\frameworks\Proj1> .\env\Scripts\Activate
>>
(env) PS C:\estudos\4 PERIODO\frameworks\Proj1> python -m ensurepip --upgrade
>>
Looking in links: c:\Users\PATRIC~1\AppData\Local\Temp\tmptq6sntbz
Requirement already satisfied: setuptools in c:\estudos\4 periodo\frameworks\proj1\env\lib\site-packages (65.5.0)
Requirement already satisfied: pip in c:\estudos\4 periodo\frameworks\proj1\env\lib\site-packages (24.0)
(env) PS C:\estudos\4 PERIODO\frameworks\Proj1> pip install numpy
Collecting numpy
  Using cached numpy-2.1.2-cp311-cp311-win_amd64.whl.metadata (59 kB)
Using cached numpy-2.1.2-cp311-cp311-win_amd64.whl (12.9 MB)
Installing collected packages: numpy
Successfully installed numpy-2.1.2

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(env) PS C:\estudos\4 PERIODO\frameworks\Proj1>
```

# CONFIGURANDO ACESSO CASO DE ERRO

```
PS C:\Windows\system32> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Alteração da Política de Execução
A política de execução ajuda a proteger contra scripts não confiáveis. A alteração da política de execução pode
implicar exposição aos riscos de segurança descritos no tópico da ajuda about_Execution_Policies em
https://go.microsoft.com/fwlink/?LinkID=135170. Deseja alterar a política de execução?
[S] Sim  [A] Sim para Todos  [N] Não  [T] Não para Todos  [U] Suspender  [?] Ajuda (o padrão é "N"): S
PS C:\Windows\system32>
```
