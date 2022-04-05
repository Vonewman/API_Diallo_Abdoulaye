DROP DATABASE IF EXISTS projet_api;


CREATE DATABASE IF NOT EXISTS projet_api;
USE projet_api;


DROP TABLE IF EXISTS company;
CREATE TABLE company (
      id          INT AUTO_INCREMENT PRIMARY KEY,
      name        VARCHAR(255) NOT NULL UNIQUE,
      catchPhrase VARCHAR(255) NOT NULL,
      bs          VARCHAR(255) NOT NULL
);



DROP TABLE IF EXISTS address;
CREATE TABLE address (
      id         INT AUTO_INCREMENT PRIMARY KEY,
      street     VARCHAR(255) NOT NULL,
      suite      VARCHAR(255) NOT NULL UNIQUE,
      city       VARCHAR(255) NOT NULL,
      zipcode    VARCHAR(255) NOT NULL,
      geo        VARCHAR(255) NOT NULL
);


DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id       INT  AUTO_INCREMENT PRIMARY KEY,
    name     VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    email    VARCHAR(255) NOT NULL UNIQUE,
    phone    VARCHAR(255) NOT NULL UNIQUE,
    website  VARCHAR(255) NOT NULL,
    companyId  INT NOT NULL,
    addressId  INT NOT NULL,
    FOREIGN KEY (companyId) REFERENCES company (id),
    FOREIGN KEY (addressId) REFERENCES address (id)
);


DROP TABLE IF EXISTS todos;
CREATE TABLE todos (
    userId  INT NOT NULL,
    id      INT AUTO_INCREMENT PRIMARY KEY,
    title   VARCHAR(255) NOT NULL,
    completed INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES users(id)
);

DROP TABLE IF EXISTS albums;
CREATE TABLE albums (
    userId  INT NOT NULL,
    id      INT AUTO_INCREMENT PRIMARY KEY,
    title   VARCHAR(255) NOT NULL,
    FOREIGN KEY (userId) REFERENCES users(id)
);



DROP TABLE IF EXISTS photos;
CREATE TABLE photos (
    albumId         INT NOT NULL,
    id              INT AUTO_INCREMENT PRIMARY KEY,
    title           VARCHAR(255) NOT NULL,
    url             VARCHAR(255) NOT NULL,
    thumbnailUrl    VARCHAR(255) NOT NULL,
    FOREIGN KEY (albumId) REFERENCES albums(id)
);


DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    userId  INT NOT NULL,
    id      INT AUTO_INCREMENT PRIMARY KEY,
    title   VARCHAR(255) NOT NULL,
    body    TEXT NOT NULL,
    FOREIGN KEY (userId) REFERENCES users(id)
);


DROP TABLE IF EXISTS comments;
CREATE TABLE comments (
    postId  INT NOT NULL,
    id      INT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(255) NOT NULL,
    email   VARCHAR(255) NOT NULL,
    body    TEXT NOT NULL,
    FOREIGN KEY (postId) REFERENCES posts(id)
);
