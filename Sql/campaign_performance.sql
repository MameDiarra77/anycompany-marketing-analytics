-- ============================================
-- Performance des campagnes marketing
-- Question business :
-- Quelles campagnes génèrent le plus de ventes ?
-- ============================================

SELECT
    campaign_type,
    COUNT(transaction_id) AS nb_transactions,
    SUM(sales_amount)     AS total_sales,
    AVG(sales_amount)     AS avg_sales
FROM ANALYTICS.SALES_ENRICHED
WHERE campaign_id IS NOT NULL
GROUP BY campaign_type
ORDER BY total_sales DESC;
