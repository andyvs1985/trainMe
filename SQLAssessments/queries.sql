/*Select Query*/

/*List all the customers for whom the invoices were raised for a particular time period 
(start date time and end date time will be parameter to the query)*/

select 
    cu.customerid, 
    cu.customername, 
    inv.invoiceid, 
    inv.invoicedate
from customers cu
    inner join invoices inv 
    on inv.customerid = cu.customerid

where inv.invoicedate BETWEEN '2016-01-28' and  '2016-06-01'


/*List the total cost of all the invoices for a particular customer*/

select 
    cu.customername,
    sum(invd.unitprice) as total_cost
from invoicedetails invd
    inner join invoices inv on inv.invoiceid = invd.invoiceid
    inner join customers cu on cu.customerid = inv.customerid
where cu.customerid = 2

/*List all the Orders delivered in the given time frame*/

select 
   ord.orderid,
   ord.orderdate,
   dl.ArrivalDate,
   dl.ArrivalTime,
   dl.destinationAddress,
   dl.destinationCity
from Orders ord 
inner join invoicedetails invd on invd.orderid = ord.orderid
inner join invoices inv on inv.invoiceid = invd.invoiceid
inner join deliveries dl on dl.deliveryid = inv.deliveryid

where dl.ArrivalDate BETWEEN '2016-01-28' and  '2016-06-01'


/*Get the total Price of invoices raised by a particular Employee*/

select 
    invd.InvoiceID, 
    emp.EmployeeID,
    (invd.quantity * invd.unitprice - invd.discount) as total_cost

from InvoiceDetails invd
    inner join Invoices inv on inv.invoiceid = invd.invoiceid
    inner join Employees emp on emp.EmployeeID = inv.EmployeeID

where emp.employeeid = 'emp23'


/*List all the Orders delivered to a country/region*/

select 
   ord.orderid,
   ord.orderdate,
   dl.ArrivalDate,
   dl.ArrivalTime,
   dl.CountryOrRegion
from Orders ord 
inner join invoicedetails invd on invd.orderid = ord.orderid
inner join invoices inv on inv.invoiceid = invd.invoiceid
inner join deliveries dl on dl.deliveryid = inv.deliveryid

where dl.CountryOrRegion = 'India'


/*Listing the customers who does not have any invoices*/

select 
    cu.customerid
from customers cu

where cu.customerid not in(
select 
   inv.customerid 
from invoices inv)

/*List the total cost of all the invoices for all the customers*/
/*Group by : helps to arrange identical/similar data into groups.*/

select 
  cu.customername, 
  sum(invd.unitprice) as total_cost
from invoicedetails invd
    inner join invoices inv on inv.invoiceid = invd.invoiceid
    inner join customers cu on cu.customerid = inv.customerid
where cu.customerid
group by cu.customername