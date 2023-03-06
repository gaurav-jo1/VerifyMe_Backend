<h1 align='center'> VerifyMe </h1>

The user authentication and authorization functionalities of the application are served by the backend, which is built with Django and Django Rest Framework. Python is the primary language used for this backend. One of the features of this application is the use of JSON Web Tokens (JWTs) to authorize users.

<div align='center'>
<img src="https://user-images.githubusercontent.com/93304640/221342691-61189881-a5c8-4660-9a6d-7bf588a2dadd.png" alt="VerifyMe-TS" height="386" width="686"/>
 </div>


<hr/>

<h1 align='center'> My Blog Post About VerifyMe </h1>


<p align="left">
 
<a href="https://gauravjoshi.hashnode.dev/building-a-system-for-user-registration-and-login-using-python-part-1" title="Building a System for User Registration and Login using Python (Part 1 )"><img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1676974049877/b42b5a77-b31a-4caf-afb5-bae6cad2bc3a.png?w=1600&h=840&fit=crop&crop=entropy&auto=compress,format&format=webp" alt="Building a System for User Registration and Login using Python (Part 1)"  width="250px" align="left" /></a>
<a href="https://gauravjoshi.hashnode.dev/building-a-system-for-user-registration-and-login-using-python-part-1" title="Building a System for User Registration and Login using Python (Part 1)"><strong>Building a System for User Registration and Login using Python (Part 1 )</strong></a>
<div><strong>Feb 22, 2023 </strong></div>
<br/>This article is a tutorial on building a backend for user sign-up, login, and authentication using Python
</p> <br/> 

<p align="left">
 
<a href="https://gauravjoshi.hashnode.dev/building-a-system-for-user-registration-and-login-using-typescript-part-2" title="Building a System for User Registration and Login using TypeScript (Part 2 )"><img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1677313533900/a1bc56f9-e1ba-459c-85e6-55da79f5ce33.png?w=1600&h=840&fit=crop&crop=entropy&auto=compress,format&format=webp" alt="Building a System for User Registration and Login using TypeScript (Part 2 )"  width="250px" align="left" /></a>
<a href="https://gauravjoshi.hashnode.dev/building-a-system-for-user-registration-and-login-using-typescript-part-2" title="Building a System for User Registration and Login using TypeScript (Part 2 )"><strong>Building a System for User Registration and Login using TypeScript (Part 2 )</strong></a>
<div><strong>Mar 3, 2023 </strong></div>
<br/>To begin with, we will be building the front end using React with TypeScript.
</p> <br/> 

<hr/>
<h1 align='center'> Getting Started </h1>

## Prerequisites
Make sure you have the following installed on your system:

<ul>
 <li><a href="https://www.python.org/downloads/"> Python </a> </li>
 <li> virtualenv </li>
</ul>

You can install virtualenv using the following command:

```pip install virtualenv```

## Installation

1. Clone this repository:

 &nbsp;  &nbsp;  &nbsp;    ```git clone https://github.com/Gaurav-jo1/VerifyMe_Backend.git```

2. Navigate to the project directory: &nbsp; 

 &nbsp;  &nbsp;  &nbsp;    ```cd VerifyMe_Backend```

3. Create a virtual environment for your project (optional but recommended):

 &nbsp;  &nbsp;  &nbsp;    ```virtualenv venv```

4. Activate the virtual enviroment:

 &nbsp;  &nbsp;  &nbsp;   For Windows: &nbsp;  &nbsp;   ``` ./venv/Scripts/activate```

 &nbsp;  &nbsp;  &nbsp;   For Linux: &nbsp;  &nbsp; &nbsp;   &nbsp;  ```source ./venv/bin/activate```


5. Install the required packages listed in the requirements.txt file:

 &nbsp;  &nbsp;  &nbsp;  ```pip install -r requirements.txt```
 
6. Set up the app by running the following commands:

 &nbsp;  &nbsp;  &nbsp;  ```python manage.py makemigrations```
 
 &nbsp;  &nbsp;  &nbsp;  ```python manage.py migrate```
 
7. Create a superuser (optional) by running:

 &nbsp;  &nbsp;  &nbsp;  ```python manage.py createsuperuser```
 
## Running the App
To run the app, simply run the following command: &nbsp; ```python manage.py runserver```

## License
This project is licensed under the <a href="https://opensource.org/license/mit/">MIT License.</a>
