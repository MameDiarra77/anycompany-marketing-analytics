-- ============================================
-- Analyse des tendances de ventes dans le temps
-- Question business :
-- Comment évoluent les ventes par année et par mois ?
-- ============================================

SELECT
    sales_year,
    sales_month,
    COUNT(transaction_id) AS nb_transactions,
    SUM(sales_amount)     AS total_sales,
    AVG(sales_amount)     AS avg_sales
FROM ANALYTICS.SALES_ENRICHED
GROUP BY sales_year, sales_month
ORDER BY sales_year, sales_month;
