# 🏦 Sistema Bancário Orientado a Objetos

Evolução do sistema bancário funcional para **Programação Orientada a Objetos (POO)**, implementando conceitos avançados como herança, encapsulamento, polimorfismo e abstração.



## 🎯 Objetivo Geral

Modelar o sistema bancário em POO, adicionando classes para cliente e as operações bancárias: depósito e saque, seguindo princípios de design orientado a objetos e boas práticas de desenvolvimento.

## 🏗️ Arquitetura do Sistema

### **Estrutura de Arquivos**

```plainext
📁 Sistema Bancário OOP/
├── 📄 classes.py        # Classes do domínio bancário
├── 📄 utils.py         # Funções auxiliares e validações
├── 📄 main.py          # Interface principal e execução
└── 📄 README.md        # Documentação do projeto
```

### **Diagrama de Classes UML**

![Imagem da classe UML](<img width="1058" height="640" alt="Image" src="https://github.com/user-attachments/assets/94a2772b-f5ab-4e65-916c-3de6131393bd" />)

## 🔧 Classes Implementadas

### 👤 **Cliente e PessoaFisica**

```python
class Cliente:
    - endereco: str
    - contas: List[Conta]
    + realizar_transacao(conta, transacao)
    + adicionar_conta(conta)

class PessoaFisica(Cliente):
    - nome: str
    - data_nascimento: str
    - cpf: str
```

**Características:**

- **Herança**: `PessoaFisica` herda de `Cliente`
- **Composição**: Cliente possui múltiplas contas
- **Responsabilidade**: Gerenciar informações pessoais e contas

### 🏦 **Conta e ContaCorrente**

```python
class Conta:
    - _saldo: float
    - _numero: int
    - _agencia: str
    - _cliente: Cliente
    - _historico: Historico
    + sacar(valor): bool
    + depositar(valor): bool

class ContaCorrente(Conta):
    - _limite: float
    - _limite_saques: int
    + sacar(valor): bool  # Override com validações extras
```

**Características:**

- **Encapsulamento**: Atributos privados com `_`
- **Properties**: Acesso controlado aos dados
- **Herança**: `ContaCorrente` especializa `Conta`
- **Override**: Método `sacar()` sobrescrito

### 📊 **Historico**

```python
class Historico:
    - _transacoes: List[Dict]
    + adicionar_transacao(transacao)
    + gerar_relatorio(tipo_transacao)
```

**Características:**

- **Responsabilidade única**: Gerenciar histórico
- **Generator**: Método `gerar_relatorio()` usa `yield`
- **Encapsulamento**: Lista privada de transações

### 💰 **Transacao, Saque e Deposito**

```python
class Transacao(ABC):
    @abstractmethod
    + valor: float
    @abstractmethod
    + registrar(conta)

class Saque(Transacao):
    + registrar(conta)

class Deposito(Transacao):
    + registrar(conta)
```

**Características:**

- **Abstração**: Classe abstrata com `ABC`
- **Polimorfismo**: Diferentes implementações de `registrar()`
- **Template Method**: Estrutura comum para transações

## 🎯 Funcionalidades Implementadas

### 💸 **Operações Bancárias**

#### **Depósito**

- ✅ Validação de valor positivo
- ✅ Atualização automática do saldo
- ✅ Registro no histórico
- ✅ Feedback visual para o usuário

#### **Saque**

- ✅ Validação de saldo suficiente
- ✅ Limite de valor por saque (R$ 500)
- ✅ Limite de saques diários (3 saques)
- ✅ Registro no histórico

#### **Extrato**

- ✅ Histórico completo de transações
- ✅ Data e hora de cada operação
- ✅ Saldo atual formatado
- ✅ Interface visual aprimorada

### 👥 **Gestão de Clientes**

#### **Cadastro de Clientes**

- ✅ Validação de CPF com algoritmo
- ✅ Formatação automática de dados
- ✅ Verificação de duplicatas
- ✅ Armazenamento orientado a objetos

#### **Listagem de Clientes**

- ✅ Formatação visual organizada
- ✅ Contagem de contas por cliente
- ✅ CPF formatado para exibição

### 🏛️ **Gestão de Contas**

#### **Criação de Contas**

- ✅ Vinculação automática com cliente
- ✅ Numeração sequencial
- ✅ Agência padrão (0001)
- ✅ Relacionamento bidirecional

#### **Listagem de Contas**

- ✅ Informações completas do titular
- ✅ Saldo atual da conta
- ✅ Dados de agência e número

## 🛠️ Principais Conceitos de POO Aplicados

### 🔒 **1. Encapsulamento**

```python
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0          # Atributo privado
        self._numero = numero    # Atributo privado
    
    @property
    def saldo(self):            # Acesso controlado
        return self._saldo
```

**Benefícios:**

- Proteção dos dados internos
- Controle de acesso via properties
- Validações centralizadas

### 🧬 **2. Herança**

```python
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Reutiliza construtor da classe pai
        self.nome = nome
```

**Benefícios:**

- Reutilização de código
- Especialização de comportamentos
- Hierarquia lógica de classes

### 🎭 **3. Polimorfismo**

```python
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def registrar(self, conta):
        # Implementação específica para saque
        pass

class Deposito(Transacao):
    def registrar(self, conta):
        # Implementação específica para depósito
        pass
```

**Benefícios:**

- Interface comum para diferentes tipos
- Flexibilidade na implementação
- Código mais extensível

### 🎨 **4. Abstração**

```python
from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass
```

**Benefícios:**

- Define contratos claros
- Força implementação de métodos essenciais
- Padroniza interfaces

## 🔍 Validações e Tratamentos

### **CPF**

- ✅ Formato: 11 dígitos numéricos
- ✅ Rejeita sequências iguais (111.111.111-11)
- ✅ Formatação automática para exibição
- ✅ Remoção de caracteres especiais

### **Valores Monetários**

- ✅ Apenas valores positivos
- ✅ Tratamento de exceções `ValueError`
- ✅ Formatação com 2 casas decimais
- ✅ Feedback claro para usuário

### **Operações Bancárias**

- ✅ Saldo suficiente para saques
- ✅ Limites de valor e quantidade
- ✅ Histórico completo e rastreável

- 



### ** Interface do Sistema**

```plaintext
╔══════════════════════════════════════╗
║         BANCO TABAJARA POO           ║
╠══════════════════════════════════════╣
║  [1] Depositar                       ║
║  [2] Sacar                           ║
║  [3] Extrato                         ║
║  [4] Novo cliente                    ║
║  [5] Nova conta                      ║
║  [6] Listar contas                   ║
║  [7] Listar clientes                 ║
║  [0] Sair                            ║
╚══════════════════════════════════════╝
```



---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 04 - POO e Boas Práticas  
**👨‍💻 Desenvolvido por:**Carlos Santos

🔄 Versão:** Sistema Bancário Orientado a Objetos  
