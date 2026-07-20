-- =========================================================
-- Projeto: Visualização de Dados e Business Intelligence
-- Base: FreeSQL - Esquema HR (Human Resources)
-- =========================================================

-- Query 1: Salário por Departamento e Cargo
-- Objetivo: analisar a distribuição de salários por
-- departamento e cargo.
SELECT
    e.EMPLOYEE_ID,
    e.FIRST_NAME,
    e.LAST_NAME,
    e.SALARY,
    d.DEPARTMENT_NAME,
    j.JOB_TITLE
FROM HR.EMPLOYEES e
LEFT JOIN HR.DEPARTMENTS d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
LEFT JOIN HR.JOBS j ON e.JOB_ID = j.JOB_ID
WHERE e.SALARY > 3000;


-- Query 2: Funcionários por Região (com localização)
-- Objetivo: analisar salários e distribuição geográfica
-- (Cidade, Estado, País e Região).
SELECT
    e.EMPLOYEE_ID,
    e.FIRST_NAME,
    e.LAST_NAME,
    e.SALARY,
    d.DEPARTMENT_NAME,
    l.CITY,
    l.STATE_PROVINCE,
    c.COUNTRY_NAME,
    r.REGION_NAME
FROM HR.EMPLOYEES e
LEFT JOIN HR.DEPARTMENTS d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
LEFT JOIN HR.LOCATIONS l ON d.LOCATION_ID = l.LOCATION_ID
LEFT JOIN HR.COUNTRIES c ON l.COUNTRY_ID = c.COUNTRY_ID
LEFT JOIN HR.REGIONS r ON c.REGION_ID = r.REGION_ID
WHERE r.REGION_NAME IS NOT NULL;