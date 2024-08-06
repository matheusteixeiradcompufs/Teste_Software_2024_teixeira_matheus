# Matheus Cardoso Teixeira

## Tutorial da Atividade 1

1. **Acessar o Stack Overflow**: Vá para [Stack Overflow](https://stackoverflow.com/).

2. **Pesquisar Perguntas**: Use a string de busca: `[unit-testing] or [junit] or [pytest]`.

3. **Filtrar por Pontuação**: Ordene as perguntas por "Highest score".

4. **Selecionar a Pergunta**: Escolha uma pergunta com pelo menos 400 votos e uma resposta aceita como correta.
   - **Pergunta Selecionada**: Python unittest - oposto de assertRaises?
   - **Link**: [https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises](https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises)

5. **Registrar a Pergunta**: Poste a pergunta selecionada na thread do Google Classroom para evitar duplicidade.

6. **Simular Pergunta**: Gerar um código de teste para simular a pergunta selecionada no Stack Overflow.

   Esse código cria constantes com um path supostamente sempre válido e outro path sempre inválido. O código também cria uma classe que testa, assim que é chamada, um path e verifica se este é válido e levanta uma exceção se este não for. Utilizando essas bases, um teste é criado para verificar se o método `assertRaises` quando MyObject verifica um path inválido. Outro teste criado testa o comando `assertNotRaises`, sugerido pelo autor da pergunta, utilizando os mesmos parâmetros.

   Como esperado, o teste passa na primeira situação e falha na segunda, pois como foi mencionado pelo autor, o método `assertNotRaises` não existe e ele solicita uma alternativa.

7. **Aplicar Solução**: O código da solução cria um teste utilizando um bloco try-except dentro do método. Se uma exceção for lançada, o teste falhará com uma mensagem indicando a exceção inesperada.

8. **Teste da Solução**: A imagem abaixo apresenta o resultado dos testes após aplicação da solução.

9. **Motivos para Rejeição de Outras Respostas**:
   - **Simplicidade e Clareza**: A resposta aceita é direta e fácil de entender, focando exatamente no problema de verificar se uma exceção não é lançada.
   - **Cobertura Completa**: Algumas respostas podem não ter tratado adequadamente todos os cenários em que exceções poderiam ser lançadas.
   - **Padrões de Código**: A resposta aceita segue práticas recomendadas de escrita de testes unitários, garantindo que o código seja claro e de fácil manutenção.

Para mais informações ou consultar o código, acesse o repositório: [https://github.com/matheusteixeiradcompufs/Teste_Software_2024_teixeira_matheus](https://github.com/matheusteixeiradcompufs/Teste_Software_2024_teixeira_matheus)
