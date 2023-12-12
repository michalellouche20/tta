CREATE TABLE items (
 user_id serial PRIMARY KEY,
	name varchar (50) UNIQUE NOT NULL ,
	price integer (50) UNIQUE NOT NULL 
);
INSERT INTO items (name, price) 
 VALUES ('Small Desk',100 ),
        ('Large desk',300 ),
        ('Fan' , 80);
  
   SELECT * FROM items ;
   
   
   CREATE TABLE customers (
id serial PRIMARY KEY ,
   first-name varchar (50)unique not null ,
	      last-name varchar (50)unique not null
);
   
   INSERT INTO customers (first-name, last-name)
   VALUES('Greg' ,'Jones'),
   ('Sandra','Jones'),
   ('Scott','Scott'),
   ('Trevor','Green'),
   ('Melanie','Johnson');
   
   SELECT * FROM customers WHERE last-name = 'Smith' ;
      SELECT *FROM customers WHERE last-name ='Jones';
	        DELETE FROM customers WHERE first-name = 'Scott'


   
CREATE TABLE students (
id serial PRIMARY KEY,
last-name varchar (50) UNIQUE NOT NULL,
first-name varchar(50) UNIQUE NOT NULL,
birth-date varchar (50) UNIQUE NOT NULL);

 INSERT INTO students (last-name, first-name, birth-date)
 VALUES ('benichou','marc',02/11/1998),
      ('cohen','yoan',03/12/2010),
      ('benichou','lea',27/07/1987),
      ('dux','amelia',07/04/1996),
	  ('grez','david',14/06/2003),
	  ('simpson','omer',03/10/1980);
	  
SELECT * FROM students ;
SELECT first-name and last-name FROM students;
	 SELECT * FROM students WHERE last-name = 'benichou' AND first-name = 'Marc';
	  SELECT * FROM students WHERE last-name = 'benichou' OR first-name = 'Marc' ;
	 SELECT * FROM students WHERE first-name LIKE 'a' ;
	 SELECT * FROM students WHERE first-name LIKE 'a%' ;
	 SELECT * FROM students WHERE first-name LIKE '%a' ;
	 SELECT * FROM students WHERE first-name LIKE '%%a' ;
	 SELECT * FROM students WHERE id = 1 and 3 ;
	 SELECT * FROM students WHERE birth-date >= 1/01/2000 ;