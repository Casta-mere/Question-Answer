-- 模糊匹配

CREATE TABLE `Common` as(
        SELECT
            distinct baidubaike_data.id,
            baidubaike_data.name,
            distinct_entity.name as "scource",
            distinct_entity.category
        from
            baidubaike_data,
            distinct_entity
        where
            INSTR(
                baidubaike_data.name,
                distinct_entity.name
            ) > 0
    );

-- 精确匹配

CREATE TABLE `Common_` as(
        SELECT
            distinct baidubaike_data_2.name,
            baidubaike_data_2.id,
            distinct_entity.category
        from
            baidubaike_data_2,
            distinct_entity
        where
            baidubaike_data_2.name = distinct_entity.name
    );

CREATE TABLE `common_name` as( SELECT DISTINCT name from Common_);

-- 查询当前sql进度

select * from sys.session where conn_id != connection_id();

-- 去掉换行符，回车

UPDATE baidubaike_data_2 SET name=REPLACE(name,char(10),'');

-- 在SQuAD中文种搜索，每类问题数量

SELECT * FROM distinct_entity where `category` like "%食品%";

-- 找出未包含的entity

CREATE table `required` as(
        SELECT *
        from distinct_entity
        where name not in (
                select name
                from
                    common_name
            )
    );