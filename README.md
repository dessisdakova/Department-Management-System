# Department Management System

This project models an organizational structure with different types of employees and a department system for managing and calculating salaries. The program includes serialization and deserialization capabilities, as well as unit tests for core functionality.

## Requirements

### Task 1: Organization Model
Create an object model with three types of employees:
- **Developer**
- **Designer**
- **Manager**

Each employee type has the following fields:
- `first_name` (str): First name of the employee.
- `last_name` (str): Last name of the employee.
- `base_salary` (float): Base salary of the employee.
- `experience` (int): Years of experience.

**Additional Fields by Type:**
- **Designer:** Has an `efficiency coefficient` (`eff_coeff`) - a float between 0 and 1.
- **Manager:** Has an optional `team` - a list containing any number of Developer and Designer objects.

### Task 2: Department Object
A `Department` object contains:
- A list of `Manager` objects, each with a team of employees.

**Methods:**
- `give_salary()`: Calculates and prints each employee's salary in the format:
<first_name> <last_name> received <salary> money.

The salary calculation is based on experience and specific rules for each employee type.

**Salary Calculation Rules:**
- **General:**
- If experience > 2 years: `base_salary + 200`
- If experience > 5 years: `base_salary * 1.2 + 500`
- **Designer:** `counted_salary * eff_coeff`
- **Manager:** 
- If team > 5 members: `counted_salary + 200`
- If team > 10 members: `counted_salary + 300`
- If team has more than half Developers: additional 10% to salary.

### Task 3: Serialization
The `Department` class includes methods for saving and loading data:
- `save_employees(filename)`: Saves the list of managers and their teams to a JSON file.
- `load_employees(filename)`: Loads data from a JSON file and adds it to the list of managers. Handles file-not-found errors.

### Task 4: Unit Tests
Unit tests are implemented using `pytest` to verify the functionality of the employee and department model, salary calculations, and serialization/deserialization methods.
