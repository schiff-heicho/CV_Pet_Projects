<div align='center'> <h1> HR ANALYTICS </div>
  
<div align='center'> 

____


__Tools used : Tableau, Power BI, MS SQL Server__

[Dataset used](https://github.com/sharanya-27/HR-Analytics/files/14546814/hrdata.csv)

__Tableau Dashboard__    
[click here to view](https://github.com/sharanya-27/HR-Analytics/assets/142989454/7ee835be-7022-4a40-b5fa-83102761455d)   
[click here to interact with the Dashboard](https://public.tableau.com/views/HRAnalyticsDashboard_17088846860500/HRAnalyticsDashboard?:language=en-GB&:sid=&:display_count=n&:origin=viz_share_link) 

__Power BI Dashboard__   
[click here to view](https://github.com/sharanya-27/HR-Analytics/files/14546830/HR_Analytics_BI_Dashboard.pdf)   
[click here to interact with the Dashboard](https://app.powerbi.com/view?r=eyJrIjoiODBhYzY1ZGEtMmM0OS00YjkwLTkxYzYtZTBiNWEzYjMyZDE4IiwidCI6IjZmMTFlMWQzLTEyMTAtNDk5YS1iMjY0LTU2NzA0NTY4OGUyNyJ9)

__<h1>BUSINESS PROBLEM</h1>__
A Company faces a challenge in efficiently analyzing and monitoring employee data, with around 12k rows of data to make informed decisions regarding retention, development, and recruitment strategies. This lack of comprehensive data analysis inhibits the ability to track progress in reducing attrition rates effectively. Furthermore, without detailed insights into employee demographics such as gender, age group, job satisfaction, and education field, it becomes difficult to identify trends and patterns that could inform targeted interventions.It is also required to test the Dashboards developed on Tableau and Power BI for QA. Thus, there is a pressing need for a solution that provides robust analytics capabilities, including trend analysis and demographic segmentation to empower HR managers and business leaders in making data-driven decisions for optimizing workforce management practices.

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

![HR Analytics Tableau Dashboard](https://github.com/sharanya-27/HR-Analytics/assets/142989454/2182dc75-cc1b-45d9-a8b9-2ecee6ecc2cc)

__2) Power BI Dashboard__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/9e9c4335-58a2-4e64-8577-b12cc7d4e3c2)

__<h2>Dashboard Contents</h2>__

__<h3>KPI:</h3>__

__1. Employee Count:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/954bc720-0271-4a88-b7c1-6913a07c0207)

This metric helps the department to assess workforce size and plan for future growth or downsizing effectively.

__2. Attrition Count:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/faab3f3c-870a-4355-b4b2-92cdc0843185)

Gives a complete and reliable data on the number of employees who have left the organization.

__3. Attrition Rate:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/79d996ab-5a2b-4d68-a811-b1b779937e38)

Gives a clear measure of attrition rate, such that the organization can assess the overall turnover level or compare it with industry benchmarks, improving the ability to gauge employee satisfaction and engagement.

__4. Active Employees:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/e6454fba-72f6-438a-8262-fcbfd60bb220)

This metric differentiate between active and inactive employees, thus aids in accurately assessing the current workforce's productivity and capacity.

__5. Average Age:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/eca1bc5e-0878-4d0d-abcb-bf4419b3b307)

Gives insight into the average age of employees, making it easy to evaluate workforce demographics, succession planning, and the organization's ability to attract and retain younger talent.

__<h3>Charts:</h3>__

__1) Attrition by Gender:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/d106bfa1-aa05-43c9-9c9e-46140ddceb0c)

Gives insight into the attrition patterns based on gender, making it difficult to identify any gender-related disparities and implement targeted retention strategies.

__2) Department-wise Attrition:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/bb002f8e-7f4b-48a9-acb7-e509a528cdac)

This visualization showcases attrition rates across different departments. This boosts their ability to identify departments with higher attrition rates and address any underlying issues or concerns effectively.

__3) Number of Employees by Age Group:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/47fd090c-fec4-45f1-9790-3540f2aebd14)

The HR department requires visual representations to analyze the distribution of employees across various age groups. This helps in assessing workforce demographics, identifying any age-related gaps or imbalances, and implementing targeted HR policies or programs.

__4) Job Satisfaction Ratings:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/184db909-26ec-4fd4-bcca-5dec5e66bf66)

This visualization is used to represent job satisfaction ratings, improving their ability to measure employee engagement and overall job satisfaction levels effectively.

__5) Education Field-wise Attrition:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/254a6cdd-7d53-4f95-be43-f57e489dd611)

This visual representations can be used to analyze attrition rates based on education fields. This helps identify specific educational backgrounds that may be associated with higher attrition, enabling the organization to tailor retention strategies accordingly.

__6) Attrition Rate by Gender for Different Age Groups:__

![image](https://github.com/sharanya-27/HR-Analytics/assets/142989454/c70ab8d7-d4bd-4564-bc83-56f1212e5e5b)

This visualizations displays attrition rates based on gender and different age groups making it easy to identify any age and gender-related attrition trends, aiding the organization in implementing targeted retention strategies for specific employee segments.

__<h2>QA Testing (Quality Assurance)</h2>__
1) __Functional Validation -__ Testing if each feature works as per the requirement and verifying if all the filters and Action Filters on the report work as per the requirement.

2) __Data Validation -__ Checking accuracy and quality of data and to match the values in Tableau and Power BI report with the SQL queries.

[SQL Queries for Analyzing/Testing Reports](https://github.com/sharanya-27/HR-Analytics/blob/main/SQL%20Analysis-%20Testing%20Tableau%20%26%20Power%20BI%20Reports)

__<h1>CONCLUSION</h1>__

The HR Analytics Dashboard project utilizing Tableau, Power BI and SQL aims to offer comprehensive insights into essential HR metrics and trends within an organization. By employing visualizations and data analysis techniques, the dashboard facilitates HR professionals in discerning patterns and making informed, data-driven decisions. It encompasses key visualizations presenting an overarching view of HR-related metrics, including turnover rate, headcount, and employee engagement levels. Additionally, it provides insights into recruitment metrics such as time-to-fill and cost-per-hire.

Moreover, the dashboard delves into employee performance metrics, including training and development, performance appraisals, and career progression, aiding HR professionals in identifying areas for enhancement and formulating strategies to bolster employee engagement and productivity.

Featuring interactive functionalities enabling users to filter and drill down into specific data subsets like department, location, or job level, the dashboard facilitates a more granular analysis, simplifying the identification of patterns and trends.

In essence, this project serves as a vital tool for HR professionals seeking deeper insights into their organization's HR data. Leveraging these robust data visualization and analysis tools, HR professionals can make informed decisions pivotal in driving organizational success. Furthermore, the project entailed thorough QA/testing of Tableau and Power BI reports using SQL queries to ensure accuracy and reliability.








