-- ============================================
-- Impact des promotions sur les ventes
-- Question business :
-- Les ventes avec promotion génèrent-elles plus
-- de chiffre d'affaires que les ventes sans promotion ?
-- ============================================

SELECT
    is_promotional_sale,
    COUNT(transaction_id) AS nb_transactions,
    SUM(sales_amount)     AS total_sales,
    AVG(sales_amount)     AS avg_sales
FROM ANALYTICS.SALES_ENRICHED
GROUP BY is_promotional_sale;
