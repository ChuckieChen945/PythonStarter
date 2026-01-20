-- 用于开发时试验的测试表
CREATE TABLE
    dev (
        id SERIAL PRIMARY KEY, -- 自增主键
        url TEXT NOT NULL, -- URL 字段，设置为必填
        title VARCHAR(255), -- 标题字段，限制长度为 255 字符
        created_at TIMESTAMP DEFAULT NOW () -- 记录创建时间
    );