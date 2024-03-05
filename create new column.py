import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column 'bonus' containing doubled values of the 'salary' column
    employees['bonus'] = employees['salary'] * 2
    return employees

# Example usage:
employees = pd.DataFrame({
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
})

result = createBonusColumn(employees)
print(result)
