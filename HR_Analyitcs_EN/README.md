<div align='center'> <h1> HR ANALYTICS </div>
  
<div align='center'> 

____


__Tools used : Tableau, MS SQL Server__
[Dataset used](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/hrdata.csv)

__Tableau Dashboard__    
[click here to view](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/HR_Analytics_Dashboard_Tablaeu.pdf)   

__<h1>BUSINESS PROBLEM</h1>__
A Company faces a challenge in efficiently analyzing and monitoring employee data, with around 12k rows of data to make informed decisions regarding retention, development, and recruitment strategies. This lack of comprehensive data analysis inhibits the ability to track progress in reducing attrition rates effectively. Furthermore, without detailed insights into employee demographics such as gender, age group, job satisfaction, and education field, it becomes difficult to identify trends and patterns that could inform targeted interventions.It is also required to test the Dashboards developed on Tableau for QA. Thus, there is a pressing need for a solution that provides robust analytics capabilities, including trend analysis and demographic segmentation to empower HR managers and business leaders in making data-driven decisions for optimizing workforce management practices.

__<h1>SOLUTION</h1>__

__<h2>STEPS OVERVIEW:</h2>__
+ Dataset collection.  
+ Understanding the Data.  
+ Loading Libraries.  
+ Data Cleaning & Finding Missing values.  
+ Data Visualization.
+ QA Testing(Quality Assurance)- Data Validation & Functional validation.

__<h2>DATA CLEANING:</h2>__
+ Opening Dataset in Excel and Make a Copy of Dataset for security purpose.
+ Removing Duplicates.
+ Formatting of columns wherever necessary.
+ Spelling Check.
+ Changing Case - Lower/Upper/Proper.
+ Trimming unwanted spaces.
+ Removing null values wherever necessary.
+ Finding & Replacing values.

__<h2>Data Visualization</h2>__

__1) Tableau Dashboard__

![HR Analytics Tableau Dashboard](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/HR%20Analytics%20Dashboard.png)

__<h2>Dashboard Contents</h2>__

__<h3>KPI:</h3>__

__1. Employee Count:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/1-Employee_Count.png)

This metric helps the department to assess workforce size and plan for future growth or downsizing effectively.

__2. Attrition Count:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/2-Attrition_Count.png)

Gives a complete and reliable data on the number of employees who have left the organization.

__3. Attrition Rate:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/3-Attrition_Rate.png)

Gives a clear measure of attrition rate, such that the organization can assess the overall turnover level or compare it with industry benchmarks, improving the ability to gauge employee satisfaction and engagement.

__4. Active Employees:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/4-Active_Employees.png)

This metric differentiate between active and inactive employees, thus aids in accurately assessing the current workforce's productivity and capacity.

__5. Average Age:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/5-Average_Age.png)

Gives insight into the average age of employees, making it easy to evaluate workforce demographics, succession planning, and the organization's ability to attract and retain younger talent.

__<h3>Charts:</h3>__

__1) Attrition by Gender:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/6-Attrition_by_Gender.png)

Gives insight into the attrition patterns based on gender, making it difficult to identify any gender-related disparities and implement targeted retention strategies.

__2) Department-wise Attrition:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/7-Department_wise_Attrition.png)

This visualization showcases attrition rates across different departments. This boosts their ability to identify departments with higher attrition rates and address any underlying issues or concerns effectively.

__3) Number of Employees by Age Group:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/8-Number_of_Employees_by_Age_Group.png)

The HR department requires visual representations to analyze the distribution of employees across various age groups. This helps in assessing workforce demographics, identifying any age-related gaps or imbalances, and implementing targeted HR policies or programs.

__4) Job Satisfaction Ratings:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/9-Job_Satisfaction_Ratings.png)

This visualization is used to represent job satisfaction ratings, improving their ability to measure employee engagement and overall job satisfaction levels effectively.

__5) Education Field-wise Attrition:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/10-Education_Field_wise_Attrition.png)

This visual representations can be used to analyze attrition rates based on education fields. This helps identify specific educational backgrounds that may be associated with higher attrition, enabling the organization to tailor retention strategies accordingly.

__6) Attrition Rate by Gender for Different Age Groups:__

![image](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/11-Attrition_Rate_by_Gender_for_Different_Age_Groups.png)

This visualizations displays attrition rates based on gender and different age groups making it easy to identify any age and gender-related attrition trends, aiding the organization in implementing targeted retention strategies for specific employee segments.

__<h2>QA Testing (Quality Assurance)</h2>__
1) __Functional Validation -__ Testing if each feature works as per the requirement and verifying if all the filters and Action Filters on the report work as per the requirement.

2) __Data Validation -__ Checking accuracy and quality of data and to match the values in Tableau report with the SQL queries.

[SQL Queries for Analyzing/Testing Reports](https://github.com/meaLumenJucunda/LumenJucunda/blob/projects/HR_Analyitcs/SQL%20Analysis-%20Testing%20Tableau%20%26%20Power%20BI%20Reports.txt)

__<h1>CONCLUSION</h1>__

The HR Analytics Dashboard project utilizing Tableau and SQL aims to offer comprehensive insights into essential HR metrics and trends within an organization. By employing visualizations and data analysis techniques, the dashboard facilitates HR professionals in discerning patterns and making informed, data-driven decisions. It encompasses key visualizations presenting an overarching view of HR-related metrics, including turnover rate, headcount, and employee engagement levels. Additionally, it provides insights into recruitment metrics such as time-to-fill and cost-per-hire.

Moreover, the dashboard delves into employee performance metrics, including training and development, performance appraisals, and career progression, aiding HR professionals in identifying areas for enhancement and formulating strategies to bolster employee engagement and productivity.

Featuring interactive functionalities enabling users to filter and drill down into specific data subsets like department, location, or job level, the dashboard facilitates a more granular analysis, simplifying the identification of patterns and trends.

In essence, this project serves as a vital tool for HR professionals seeking deeper insights into their organization's HR data. Leveraging these robust data visualization and analysis tools, HR professionals can make informed decisions pivotal in driving organizational success. Furthermore, the project entailed thorough QA/testing of Tableau reports using SQL queries to ensure accuracy and reliability.








