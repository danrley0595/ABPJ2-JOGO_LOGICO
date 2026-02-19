# ABPJ2-JOGO-LOGICO - QUIZ DE PERGUNTAS

## Descrição

Este projeto ABPJ2 é um programa Quiz de perguntas sobre Python básico desenvolvido em Python com:

- 10 perguntas
- 5 alternativas por pergunta
- Sistema de pontuação
- Controle de tentativas (máximo 3 por pergunta)
- Encerramento após 3 erros
- Opção de continuar ou finalizar

## Regras do Jogo

1. O usuário responde perguntas de múltipla escolha.
2. Cada pergunta vale 10 pontos.
3. O jogador tem no máximo 3 tentativas por pergunta.
4. Se errar 3 vezes, o jogo é encerrado.
5. O jogador pode escolher continuar ou finalizar após cada acerto.
6. Ao final, é exibida a pontuação acumulada.

## Estrutura Lógica

O sistema utiliza:

- for -> Percorrer as perguntas
- while -> Controlar número de tentativas
- if / else -> Verificar respostas
- break -> Encerrar o jogo quando necessário
- Listas paralelas para:
  - Perguntas
  - Alternativas
  - Respostas corretas

## Fluxo do Programa

1. Início
2. Exibe regras
3. Apresenta pergunta
4. Recebe resposta
5. Verifica:
   - Se correta -> adiciona pontos
   - Se incorreta -> reduz tentativa
6. Se tentativas = 3 -> encerra programa
7. Se usuário não quiser continuar -> encerra
8. Mostra resultado final
9. Fim

## Fluxograma
<img width="566" height="993" alt="image" src="https://github.com/user-attachments/assets/33b9d9ec-33d0-4fc0-84c6-9f3aedda6f82" />


## Como Executar

1. Instale o Python 3
2. Execute o arquivo: main.py
