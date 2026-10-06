use shop;
-- create table product(pid int primary key,pname varchar(20),
-- price int)


-- create table order_details(order_id int primary key,p_id int,quantity int,
-- date date, foreign key(p_id) references product(pid))


-- insert into product (pid,pname,price) values(1,'pA',1000),(2,'pB',500),(3,'pC',250),(4,'pD',2000),(5,'pE',3000)

-- insert into order_details(order_id,p_id,quantity,date) values(1,2,2,"2026-08-12"),(2,3,1,"2026-08-13")


-- select * from product;

-- select * from order_details


-- select * from product
-- inner join order_details
-- on product.pid=order_details.p_id


-- select pname,price,order_id from product
-- inner join order_details
-- on product.pid=order_details.p_id


-- select * from product
-- inner join order_details
-- on product.pid=order_details.p_id
-- where order_id=1


-- Display all products that have never been ordered.
-- SELECT *
-- FROM product
-- LEFT JOIN order_details
-- ON product.pid = order_details.p_id
-- WHERE order_details.p_id IS NULL;



-- select * from product
-- left join order_details
-- on product.pid=order_details.p_id


-- select * from product
-- right join order_details
-- on product.pid=order_details.p_id


-- select * from product
-- cross join order_details