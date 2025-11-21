1. Create an Entity-Relationship Diagram (ERD) showing entities, attributes, and relationships.

You may:
Hand-draw the ERD, and take a clear photo of the drawing.
OR use a digital tool (e.g., Figma, Canva, draw.io), and take a screenshot.

2. Save the image and place it in a “Task2” folder.

3. SQL Schema

Write CREATE TABLE statements for at least three entities, including:
- Primary keys (PK)
- Foreign keys (FK)
- Appropriate data types and NOT NULL constraints.

Please add your SQL query below AND add an explanation: 
CREATE TABLE [Employee Info](
    [Employee ID] INT PRIMARY KEY,
    Name VARCHAR(150) NOT NULL,
    Department VARCHAR(150) NOT NULL, 
    Position VARCHAR(150) NOT NULL
    Phone VARCHAR(15),
    [Date of Hire] DATE NOT NULL
)

CREATE TABLE [Employee Sales (Weekly)] (
    [Employee ID] INT PRIMARY KEY,
    Sales DECIMAL(10,2) NOT NULL,
    Tips DECIMAL(10,2) NOT NULL,
    [Tip Out] DECIMAL(10,2) NOT NULL,
)

CREATE TABLE [Payroll (Weekly)] (
    [Employee ID] INT PRIMARY KEY,
    [Employee Name] VARCHAR(150) NOT NULL
    [Hours Worked] DECIMAL(5, 1) NOT NULL,
    [Gross Pay] DECIMAL(10,2) NOT NULL,
    [Tips Recieved] DECIMAL(10,2) NOT NULL,
    [Tip Out Recieved] DECIMAL(10,2) NOT NULL
)

CREATE TABLE [Profit & Loss](
    [Line Item Number] INT PRIMARY KEY
    [Total Sales] DECIMAL(15,2) NOT NULL,
    [Fixed Expenses] DECIMAL(15,2) NOT NULL,
    [Variable Expenses] DECIMAL(15,2) NOT NULL,
    [Labor Hours] DECIMAL(5,1) NOT NULL,
    [Labor Gross] DECIMAL(15,2) NOT NULL,
    Incidentals DECIMAL(15,2) NOT NULL,
 )



Query will etsablish four tables (Employee Info, Employee Sales, Payroll (Weekly), Profit & Loss), and populate with appropriate fields within. VARCHAR(150) used for single line text inputs, DECIMAL used for hours and currency. Phone held in VARCHAR(15) to allow for special characters (-, +, (), etc)


4. Save this file in a "Task2" folder along with your ERD diagram

5. For submission, commit and push your "Task2" folder with the two files to your GitHub.
