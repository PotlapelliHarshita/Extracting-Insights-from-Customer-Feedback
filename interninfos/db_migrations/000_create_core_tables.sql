CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    review_text TEXT NOT NULL,
    product_id VARCHAR(100) NULL,
    category VARCHAR(100),
    uploaded_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    overall_sentiment VARCHAR(50),
    overall_sentiment_score DOUBLE PRECISION,
    CONSTRAINT fk_reviews_user
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS admins (
    admin_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_reviews_uploaded_at ON reviews (uploaded_at);
CREATE INDEX IF NOT EXISTS idx_reviews_category ON reviews (category);
CREATE INDEX IF NOT EXISTS idx_reviews_sentiment ON reviews (overall_sentiment);
