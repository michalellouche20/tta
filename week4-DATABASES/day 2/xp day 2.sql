SELECT * FROM customer ;
SELECT 
CONCAT (first_name, ' ', last_name)  as full_name FROM customer;

SELECT DISTINCT create_date FROM customer ;
SELECT * FROM customer ORDER BY first_name desc  ;

SELECT * FROM film ;
SELECT film_id ,
title ,
description ,
release_year ,
rental_rate ,
FROM film
ORDER BY rental_rate ASC ;


SELECT address.address ,address.phone
FROM address --where address.address = 'Texas'
inner join customer 
on customer.address_id = address.address_id ;

SELECT * FROM film WHERE film_id in (150,15) ;



SELECT 
film_id ,
title , 
description ,
rental_duration ,
rental_rate 
FROM film
WHERE title = 'TITANIC';

SELECT 
film_id ,
title ,
description ,
rental_duration ,
rental_rate 
FROM film
WHERE title LIKE 'Ti%';

SELECT
film_id ,
title , 
rental_rate;
FROM film
ORDER by rental_rate LIMIT 10;



SELECT
film_id , 
title ,
rental_rate,
FROM film 
ORDER by rental_rate  --i dont know;


SELECT DISTINCT 
customer.first_name ,
customer.last_name, 
payment.amount ,
payment.payment_date 
FROM payment
--ORDER BY customer_id
inner join customer 
on customer.customer_id = payment.customer_id ,


SELECT * FROM inventory WHERE inventory_id = null

SELECT city.city ,country.country
from city 
inner join country on city.country_id = country.country_id

