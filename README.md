# db-capstone
Coursera's Meta database administror course capstone project. In order to replicate the project follow the next steps.
1. Install git in your system and fork this project or download it as zip.
2. Install Mysql and Mysql Workbench. Set up a user a a connection.
3. Open and execute the database.sql file. It will import all the Little Lemon database structure and 500 rows of data from the original excel file provided by the course. You will see some tables that follow the EER Diagram Schema below.
   <img href="https://github.com/monics-hub/db-capstone/blob/main/screenshots/little_lemon_model.jpg" alt="Select stament screenshot" width = 800>
5. Test the table to see everything is working by some SELECT statements. Notice there are 2 facts tables, namely Orders and Bookings. The data of Orders is the same as the first 500 records of the Excel file and the Bookings data is some ficticious generated data by INSERT Commands recall such data wasn't provided by the course. The Staff table is never used so it's empty and there is an additional table called raw orders with the original 500 rows imported with the MySQL Workbench wizard.
    <img href="https://github.com/monics-hub/db-capstone/blob/main/screenshots/orders.jpg" alt="Select stament screenshot" width = 800>
6. Install python and python-mysql-connector.
7. Test the script connection.py by some command like python connection.py ... You'll see it contain instructions to call the stored procedures with should be already imported once the database.sql file is executed in a open Mysql connection. Notice that the code for each individual store procedure can be found in stored_procedures folder. Notice that the stores procedures are already saved once you execute database.sql file so you don't have to run such scripts. They are just to show how I build them.
  <img href="https://github.com/monics-hub/db-capstone/blob/main/screenshots/scheleton.jpg" alt="Scheleton of the database" width = 300>
8. Check the Tableau dashboard in the page: https://public.tableau.com/views/LittleLemonSales_17598630330730/CustomersCharts?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
