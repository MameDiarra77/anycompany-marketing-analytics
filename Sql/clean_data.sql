-- ============================================
-- clean_data.sql
-- Objectif : nettoyer et standardiser les données
-- ============================================

CREATE OR REPLACE TABLE ANALYTICS.SALES_CLEAN AS
SELECT
    transaction_id,
    transaction_date,
    sales_amount,
    account_code AS customer_id,
    promotion_id,
    campaign_id,
    region,
    CASE 
        WHEN promotion_id IS NOT NULL THEN TRUE
        ELSE FALSE
    END AS is_promotional_sale
FROM ANALYTICS.SALES_RAW
WHERE sales_amount > 0;
