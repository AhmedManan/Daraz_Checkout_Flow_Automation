# Daraz Checkout Flow QA Automation Task

In this repository I have conduct Automation tests on Daraz Bangladesh web application. To conduct the tests I used Python, Pytest, Playwright. I implemented POM (page object model) structure.


# Table of Content
- [Project Setup](#Project-Setup)
- [Tests](#Tests)

## Project Setup

### Prerequisites

Before running the playwright tests, ensure you have the following installed on your system:

- Python (Installed in your device)
- Node ( Installed in your device)
- Java ( Installed in your device)
- A Code Editor ( PyCharm is recommended )

### Installation

- Clone this repository to your local machine.
- Install all prerequisites

To run the project in your local system, you need to install all the libraries listed in ``requirements.txt``.

To install all the libraries at once, go to your project root directory and open terminal. Use the below command:
```bash
python -m pip install -r requirements.txt
```   
Install the browsers Playwright needs:
```bash
playwright install
```   

### Setting Up Environment
A .env file is a plain text file used to store environment variables for an application,
especially during local development or testing. It follows a simple key-value format, making
it easy to manage configuration settings. To setup the project you need to create a .env file
using the .env.example file provided in the project repository.
```bash
user_phone_no='your user phone number'
user_password='your password'
```  

### Run Tests
To execute the entire test suite across all configured browsers (Chromium, Firefox, WebKit) run command:
```bash
npx playwright test
```   
Run only the tests within the ```plugin.spec.js``` file:
```bash
npx playwright test tests/plugin.spec.js
``` 
To open the browser and visually watch the tests execute (useful for debugging):
```bash
npx playwright test --headed
``` 

## Tests
| Serial | Script Name / Details             | Status                   |
|--------|-----------------------------------|--------------------------|
| 01     | Test login with valid credentials | ✔️ |
| 02     | Test search for a product         | ✔️ |
| 03     | Test add items to cart            | ✔️ |
| 04     | Test other item add to cart       | ✔️ |
| 05     | Remove items from cart            | ✔️ |
| 07     | Test Logout                       | ✔️ |
