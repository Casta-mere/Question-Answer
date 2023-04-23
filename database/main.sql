-- 去除掉重复的，以及数词，数量词，名词性语素

CREATE table
    `Distinct_Entity` as (
        SELECT DISTINCT *
        FROM entity
        where
            category not like '%数词%'
            and category not like '%数量词%'
            and category not like '%名词性语素%'
    );

-- 去掉回车

UPDATE Distinct_Entity SET name=REPLACE(name,char(10),'');