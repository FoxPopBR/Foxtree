
# Documentação do Gerador de Estrutura de Diretórios

## Sobre o Projeto

Este projeto foi desenvolvido para fornecer uma visualização clara e intuitiva da estrutura de diretórios de um projeto de software, utilizando ícones personalizados para representar diferentes tipos de arquivos e diretórios. A ferramenta é extremamente útil para documentação e revisão rápida da organização do projeto.

## Componentes do Projeto

O projeto é composto por três arquivos principais, cada um desempenhando um papel crucial na geração da árvore de diretórios:

### `tree.py`

Este é o script de entrada para a geração da árvore de diretórios. Ele invoca a classe `TreeGenerator` do arquivo `treemaker.py`, passando o diretório raiz como argumento. O resultado é uma representação formatada da estrutura de diretórios, que é então salva em `showtree.md`.

### `config.py`

Define as configurações para a geração da árvore, incluindo diretórios e extensões de arquivos a serem ignorados, ícones para diferentes tipos de arquivos e diretórios, e a quantidade de espaços para indentação. Este arquivo é fundamental para personalizar a saída da árvore de diretórios, permitindo que os usuários ajustem a ferramenta às suas necessidades específicas.

### `treemaker.py`

Contém a classe `TreeGenerator` que implementa a lógica para construir a árvore de diretórios. Utiliza as configurações definidas em `config.py` para filtrar diretórios e arquivos, aplicar ícones personalizados e gerar a representação visual final da estrutura do diretório.

## Como Usar

Para gerar a árvore de diretórios do seu projeto, siga estes passos:

1. **Configuração**: Ajuste as preferências no arquivo `config.py` para definir quais diretórios ou arquivos ignorar e personalizar os ícones usados.
2. **Execução**: Rode o script `tree.py` na raiz do seu projeto.
3. **Visualização**: Abra o arquivo `showtree.md` gerado para ver a estrutura de diretórios do seu projeto.

## Personalização

- **Ignorando Diretórios e Arquivos**: No `config.py`, adicione os nomes dos diretórios ou as extensões de arquivos que você deseja ignorar nas listas `ignore_dirs` e `ignore_exts`.
- **Personalizando Ícones**: Associe ícones aos tipos de arquivos ou diretórios modificando o dicionário `icons` em `config.py`.

## Resultado

A execução do script produz um arquivo `showtree.md` na raiz do seu projeto, contendo a estrutura de diretórios formatada com ícones personalizados. Isso facilita a compreensão da organização do projeto e a identificação rápida de diferentes tipos de arquivos.

---

Este documento oferece uma visão geral abrangente do projeto e instruções detalhadas sobre como utilizar e personalizar a ferramenta. A implementação foi projetada para ser flexível, permitindo ajustes que atendam às necessidades específicas de visualização e documentação da estrutura de diretórios de projetos de software.
