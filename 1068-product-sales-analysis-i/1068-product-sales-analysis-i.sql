select product_name , year , price from Sales
left join Product 
on sales.product_id = product.product_id
