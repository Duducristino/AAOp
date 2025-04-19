# Agente Autônomo de Análise e Indicação de Opções no Mercado Brasileiro

## Estrutura de Projeto (com Streamlit e Telegram integrados)

### Módulos:
1. **Coleta de Dados**:
   - Histórico de preços de ações e opções (via yfinance, B3 API, etc.)
   - Indicadores macroeconômicos (IPCA, Selic, câmbio)
   - Fundamentos (via scraping ou APIs: StatusInvest, Fundamentus)

2. **Análise Técnica Multi-Temporal**:
   - Timeframes: Diário, 60min, 15min
   - Indicadores: RSI, MACD, MME9/21/50/200, IFR, Estocástico
   - Validação cruzada de tendências nos diferentes tempos gráficos

3. **Análise Fundamentalista** (NOVO):
   - P/L, ROE, Margem líquida, Dívida/Patrimônio
   - Histórico de lucros e dividendos
   - Risco setorial e volatilidade

4. **Estratégias de Opções**:
   - Compra seca de call/put
   - Travas de alta e baixa
   - Borboleta
   - Lançamento coberto
   - Operações com base no delta e IV

5. **Gestão de Risco (NOVO)**:
   - Cálculo de valor em risco (VaR)
   - Gestão de capital por operação (Kelly Criterion, 2% Rule)
   - Definição de perfil do usuário (conservador, moderado, agressivo)

6. **Simulação Automática (NOVO)**:
   - Modo paper trading: registra entrada, saída, resultado por operação
   - Estatísticas de performance: taxa de acerto, payoff, drawdown
   - Log de operações (CSV + visual no painel)

7. **Validação de Estratégias (NOVO)**:
   - Backtest de estratégias com dados dos últimos 5 anos
   - Ranking de estratégias por resultado histórico
   - Score por tipo de operação (Ex: trava de alta = 76% acerto, etc.)

8. **Painel Streamlit**:
   - Visualização gráfica de dados e indicadores
   - Botão para ativar simulação ou operar real
   - Histórico de recomendações e performance
   - Interface para definir perfil de risco
   - **Gráfico de evolução da performance semanal** (NOVO):
     - Visualização clara do lucro/prejuízo semanal
     - Tendência de acerto ao longo do tempo
     - Linha base de acurácia esperada (Ex: 65%)
   - **Botão para exportar relatório semanal em PDF** (NOVO)
     - Compila estatísticas, gráfico e resumo analítico
     - Permite download local para arquivamento e comparação

9. **Alertas com Telegram**:
   - Envio automático de sinais de compra e venda
   - Resumo diário das estratégias ativas
   - Alerta em tempo real para operações próximas ao alvo ou stop

10. **Autoavaliação Semanal Inteligente (NOVO)**:
   - Análise de performance da semana anterior
   - Relatório automatizado enviado via Telegram com:
     - Taxa de acerto semanal
     - Operações com maior e menor lucro
     - Estratégias com melhor e pior performance
     - Sugestões de ajuste automático de pesos nas estratégias
   - Recalibração automática das estratégias com base no relatório
   - Gatilho para alerta se desempenho cair abaixo de 50% por duas semanas

## Plano de Maximização de Acerto (Implementado no Sistema)
- Etapas:
  1. Modo simulação obrigatório por 30 dias
  2. Avaliação automática da performance (gráficos, estatísticas)
  3. Ajuste automático dos pesos das estratégias com base em resultado
  4. Operação real liberada com capital gradual (ex: 5% do portfólio)
  5. Log semanal de performance e ajustes automáticos

---

## Executável e Configuração
- Script `.bat` para execução local
- Gerador `.nsi` para instalador com ícone customizado
- Painel com interface em português e comunicação direta via Telegram
- Suporte ao Streamlit Cloud ou execução local agendada (Task Scheduler)

---

**Todos os componentes acima estão interligados e preparados para um agente autônomo de alto desempenho com análise de dados, controle de risco e execução sistemática.**
