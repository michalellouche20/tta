SELECT film.title ,
film.description,
language.name 
from film 
INNER JOIN language
ON film.language_id = language.language_id ;

CREATE TABLE new_film (film_id serial PRIMARY KEY ,
name varchar (55) unique not null);
	
INSERT INTO new_film 
(film_id,name)
VALUES (1,'Titanic'),
(2,'Xman'),
(3,'Christmas');
 
 --DROP TABLE customer_review
	CREATE TABLE customer_review
(review_id int PRIMARY KEY not null ,
	 film_id int not null ,
 FOREIGN KEY (film_id) REFERENCES film(film_id) ON DELETE CASCADE,
	title varchar (55) not null ,
 language_id integer not null ,
 FOREIGN KEY (language_id) REFERENCES language (language_id),
	score int CHECK (score >=1 AND score <= 10) ,
	review_text text,
	last_update timestamp DEFAULT CURRENT_TIMESTAMP );
	
	INSERT INTO customer_review (review_id,film_id,
								 title,language_id,
								 score,review_text,last_update)
	VALUES(1,1,'one',1,8,'Very good film',CURRENT_TIMESTAMP),
(2,2,'two',2,9,'Bad film',CURRENT_TIMESTAMP)
	
	SELECT customer_review.review_text,
	new_film.name
	FROM customer_review
	INNER JOIN new_film
	ON customer_review.film_id = new_film.film_id
	
		DELETE FROM customer_review WHERE review_text = 'Very good film'
SELECT * FROM customer_review

 update language SET name = 'French'
 WHERE language_id = 2
SELECT * FROM language


