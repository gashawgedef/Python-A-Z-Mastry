# import os

# # Base directory
# base_dir = "Python-A-Z-Mastry"

# # Folder structure with files
# structure = {
#     "00-README.md": None,
#     "01-Basics": {
#         "01-Introduction": ["intro.py"],
#         "02-Variables-DataTypes": ["variables_datatypes.py"],
#         "03-Operators": ["operators.py"],
#         "04-Input-Output": ["io_examples.py"],
#         "05-Conditionals-Loops": ["conditionals_loops.py"]
#     },
#     "02-Data-Structures": ["lists.py", "tuples.py", "dicts.py", "sets.py"],
#     "03-Functions-Modules": ["functions.py", "modules.py", "packages.py"],
#     "04-File-Handling": ["text_files.py", "csv_files.py", "json_files.py"],
#     "05-OOP": ["classes_objects.py", "inheritance.py", "polymorphism.py", "encapsulation_abstraction.py"],
#     "06-Error-Exceptions": ["exceptions.py"],
#     "07-Advanced-Topics": ["decorators.py", "generators.py", "iterators.py", "context_managers.py"],
#     "08-Libraries": {
#         "numpy": ["basics.py"],
#         "pandas": ["basics.py"],
#         "matplotlib": ["basics.py"],
#         "requests": ["basics.py"]
#     },
#     "09-Web-Development": {
#         "Flask": ["app_example.py"],
#         "FastAPI": ["app_example.py"]
#     },
#     "10-Database": ["sqlite.py", "postgresql.py", "mongodb.py"],
#     "11-Projects": ["project_01_Calculator", "project_02_WebScraper", "project_03_BlogApp", "project_04_APIService"],
#     "12-Testing": ["tests_examples.py"],
#     "13-Tools-Env": ["environment_setup.md"],
#     "14-Extras": ["python_tips.md", "performance_optimization.py"]
# }

# def create_structure(base, struct):
#     for name, content in struct.items() if isinstance(struct, dict) else enumerate(struct):
#         if isinstance(struct, dict):
#             path = os.path.join(base, name)
#         else:
#             path = os.path.join(base, content)
#         if "." in os.path.basename(path):  # It's a file
#             os.makedirs(base, exist_ok=True)
#             if not os.path.exists(path):
#                 open(path, 'w').close()
#         else:  # It's a folder
#             os.makedirs(path, exist_ok=True)
#             if isinstance(content, dict):
#                 create_structure(path, content)
#             elif isinstance(content, list):
#                 create_structure(path, content)

# # Create the folders and files
# create_structure(base_dir, structure)

# print(f"Folder structure for '{base_dir}' has been created successfully!")
import os

# Full folder structure for Python-A-Z Mastery
structure = {
    "00-README.md": None,
    "01-Basics": {
        "01-Introduction": ["intro.py"],
        "02-Variables-DataTypes": ["variables_datatypes.py"],
        "03-Operators": ["arithmetic_operators.py", "comparison_operators.py", "logical_operators.py", "assignment_operators.py"],
        "04-Input-Output": ["input_output.py", "formatted_strings.py"],
        "05-Conditionals-Loops": ["if_else.py", "nested_if.py", "for_loop.py", "while_loop.py", "loop_control.py"]
    },
    "02-Data-Structures": ["lists.py", "tuples.py", "sets.py", "dictionaries.py", "comprehension.py"],
    "03-Functions-Modules": ["functions.py", "args_kwargs.py", "lambda_functions.py", "decorators.py", "modules_packages.py"],
    "04-File-Handling": ["text_files.py", "csv_files.py", "json_files.py", "file_exceptions.py"],
    "05-OOP": ["classes_objects.py", "inheritance.py", "polymorphism.py", "encapsulation_abstraction.py", "magic_methods.py"],
    "06-Error-Exceptions": ["try_except.py", "custom_exceptions.py", "finally_else.py"],
    "07-Advanced-Topics": ["iterators.py", "generators.py", "context_managers.py", "decorators_advanced.py", "metaclasses.py", "threading_multiprocessing.py", "async_await.py"],
    "08-Libraries": {
        "numpy": ["basics.py", "arrays.py"],
        "pandas": ["basics.py", "dataframes.py"],
        "matplotlib": ["basics.py", "plots.py"],
        "seaborn": ["plots.py"],
        "requests": ["basics.py"],
        "beautifulsoup": ["scraping.py"],
        "selenium": ["automation.py"]
    },
    "09-Web-Development": {
        "Flask": ["app_example.py", "routes_templates.py", "forms_validation.py"],
        "FastAPI": ["app_example.py", "routes.py", "database.py"]
    },
    "10-Database": ["sqlite.py", "postgresql.py", "mongodb.py", "sqlalchemy_basics.py", "peewee_basics.py"],
    "11-APIs": ["REST_API_flask.py", "REST_API_fastapi.py", "consuming_api_requests.py"],
    "12-Testing": ["unittest_examples.py", "pytest_examples.py", "mocking_requests.py"],
    "13-Projects": ["project_01_Calculator", "project_02_WebScraper", "project_03_BlogApp", "project_04_APIService", "project_05_InventorySystem", "project_06_FinanceDashboard"],
    "14-Tools-Env": ["environment_setup.md", "git_gitignore.md", "python_versions.md"],
    "15-Extras": ["python_tips.md", "performance_optimization.py", "debugging_tips.py", "code_style_pep8.md", "interview_questions.md"]
}

def create_structure(base, struct):
    for name, content in struct.items() if isinstance(struct, dict) else enumerate(struct):
        if isinstance(struct, dict):
            path = os.path.join(base, name)
        else:
            path = os.path.join(base, content)
        if "." in os.path.basename(path):  # It's a file
            os.makedirs(base, exist_ok=True)
            if not os.path.exists(path):
                open(path, 'w').close()
        else:  # It's a folder
            os.makedirs(path, exist_ok=True)
            if isinstance(content, dict):
                create_structure(path, content)
            elif isinstance(content, list):
                create_structure(path, content)

# Create folders and files in the current directory
create_structure(".", structure)

print("Python-A-Z Mastery folder structure created successfully in the current directory!")
