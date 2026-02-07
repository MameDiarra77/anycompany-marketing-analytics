-- ============================================
-- Load_data.sql
-- Objectif : charger les données depuis le schéma SILVER
-- vers le schéma ANALYTICS
-- ============================================

CREATE OR REPLACE TABLE ANALYTICS.SALES_RAW AS
SELECT
    transaction_id,
    transaction_date,
    sales_amount,
    account_code,
    promotion_id,
    campaign_id,
    region
FROM SILVER.FINANCIAL_TRANSACTIONS_CLEAN;
