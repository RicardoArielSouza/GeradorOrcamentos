# GeradorOrcamentos
Aplicação web feita em Django para geração de orçamentos que se enquadram nas regras de negócio estabelecidas pela empresa

Esse projeto foi criado para a disciplina de Sistemas Distribuidos do curso de Engenharia da Computação da Universidade Federal do Vale do São Francisco (Univasf) 
Para fins educacionais trabalharemos com uma empresa ficticia de venda de brigadeiros, mas podendo ser adaptada para diversos segmentos.

A escolha do tema da aplicação foi pensada para empreendedores otimizarem seu tempo a partir da automatização do processo de orçamentos e pedidos. 

Regras de negócio:
- Cada produto estará relacionado a uma categoria na qual terá seus preços padrão estabelecidos;
- O cliente deverá estar devidamente cadastrado no sistema para conseguir fazer um orçamento e pedido;
- Todo orçamento será relacionado a um cliente e a uma lista de produtos;
- Os pedidos podem ser feitos a partir de um orçamento, mas nem todo orçamento é convertido em pedido;
- Todo pedido será relacionado a um cliente e a uma lista de produtos;

Esquema relacional do Banco de Dados utilizado:
![image](https://github.com/RicardoArielSouza/GeradorOrcamentos/assets/68856854/e2e59483-5559-4f91-b5ca-619860a85a9b)
