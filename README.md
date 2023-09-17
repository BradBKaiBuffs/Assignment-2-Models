# Assignment 2: Models

For this assignment, I created three diagrams: ***Conceptual, Logical, and Physical***. Included is Models.py which uses Django ORM.

For the Conceptual diagram, all entities have a many to many relationship. This is illustrated in a Chen diagram.

![Bradley_Kai_Conceptual_SS.png](https://github.com/BradBKaiBuffs/Assignment-2-Models/blob/main/Bradley_Kai_Conceptual_SS.png)

The relationships are clearly illustrated to show how the tables will be connected. The relationships are as follows:
- Students enroll into Courses.
- Students select a major(s).
- Majors have requirements that need to be met.
- Requirements are fulfilled by Courses.

For the Logical diagram, the relationships are more transparent with the fields added. The core design is based off a degree checklist form. An example is the Student table. It only has a primary key, first name and last name. This is how I approached creating the fields for each table.

![Bradley_Kai_Logical_SS.png](https://github.com/BradBKaiBuffs/Assignment-2-Models/blob/main/Bradley_Kai_Logical_SS.png)

The key concept to creating the relationships this way was that Student, Major, Course, and Requirement have many to many relationships. Enroll, Major_selection, Major_requirement and Course_requirement links the tables due to these relationships. There will be multiple times when each table is used.

For the Physical diagram, the foreign keys are introduced to illustrate the relationships.
![Bradley_Kai_Physical_SS.png](https://github.com/BradBKaiBuffs/Assignment-2-Models/blob/main/Bradley_Kai_Physical_SS.png)

The primary and foreign keys are connected with many to many relationships.  
