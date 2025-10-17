# # import os

# # # Base directory
# # base_dir = "Python-A-Z-Mastry"

# # # Folder structure with files
# # structure = {
# #     "00-README.md": None,
# #     "01-Basics": {
# #         "01-Introduction": ["intro.py"],
# #         "02-Variables-DataTypes": ["variables_datatypes.py"],
# #         "03-Operators": ["operators.py"],
# #         "04-Input-Output": ["io_examples.py"],
# #         "05-Conditionals-Loops": ["conditionals_loops.py"]
# #     },
# #     "02-Data-Structures": ["lists.py", "tuples.py", "dicts.py", "sets.py"],
# #     "03-Functions-Modules": ["functions.py", "modules.py", "packages.py"],
# #     "04-File-Handling": ["text_files.py", "csv_files.py", "json_files.py"],
# #     "05-OOP": ["classes_objects.py", "inheritance.py", "polymorphism.py", "encapsulation_abstraction.py"],
# #     "06-Error-Exceptions": ["exceptions.py"],
# #     "07-Advanced-Topics": ["decorators.py", "generators.py", "iterators.py", "context_managers.py"],
# #     "08-Libraries": {
# #         "numpy": ["basics.py"],
# #         "pandas": ["basics.py"],
# #         "matplotlib": ["basics.py"],
# #         "requests": ["basics.py"]
# #     },
# #     "09-Web-Development": {
# #         "Flask": ["app_example.py"],
# #         "FastAPI": ["app_example.py"]
# #     },
# #     "10-Database": ["sqlite.py", "postgresql.py", "mongodb.py"],
# #     "11-Projects": ["project_01_Calculator", "project_02_WebScraper", "project_03_BlogApp", "project_04_APIService"],
# #     "12-Testing": ["tests_examples.py"],
# #     "13-Tools-Env": ["environment_setup.md"],
# #     "14-Extras": ["python_tips.md", "performance_optimization.py"]
# # }

# # def create_structure(base, struct):
# #     for name, content in struct.items() if isinstance(struct, dict) else enumerate(struct):
# #         if isinstance(struct, dict):
# #             path = os.path.join(base, name)
# #         else:
# #             path = os.path.join(base, content)
# #         if "." in os.path.basename(path):  # It's a file
# #             os.makedirs(base, exist_ok=True)
# #             if not os.path.exists(path):
# #                 open(path, 'w').close()
# #         else:  # It's a folder
# #             os.makedirs(path, exist_ok=True)
# #             if isinstance(content, dict):
# #                 create_structure(path, content)
# #             elif isinstance(content, list):
# #                 create_structure(path, content)

# # # Create the folders and files
# # create_structure(base_dir, structure)

# # print(f"Folder structure for '{base_dir}' has been created successfully!")
# import os

# # Full merged Python-A-Z + Tutorial structure
# structure = {
#     "01-README.md": None,
#     "02-Basics": {
#         "01-Whetting-Your-Appetite": ["intro.py"],
#         "02-Using-Python-Interpreter": {
#             "01-Invoking-Interpreter": ["argument_passing.py", "interactive_mode.py"],
#             "02-Interpreter-Environment": ["source_code_encoding.py"]
#         },
#         "03-Informal-Introduction": ["using_as_calculator.py", "numbers.py", "text.py", "lists.py", "first_steps_programming.py"],
#         "04-Conditionals-Loops": ["if_else.py", "nested_if.py", "for_loop.py", "while_loop.py", "loop_control.py"]
#     },
#     "03-Data-Structures": {
#         "01-Lists": ["lists.py", "using_as_stack.py", "using_as_queue.py", "list_comprehensions.py", "nested_list_comprehensions.py"],
#         "02-Tuples-Sequences": ["tuples.py"],
#         "03-Sets": ["sets.py"],
#         "04-Dictionaries": ["dictionaries.py"],
#         "05-Looping-Techniques": ["looping_techniques.py"],
#         "06-Comparisons": ["more_on_conditions.py", "comparing_sequences.py"]
#     },
#     "04-Functions-Modules": {
#         "01-Functions": ["functions.py", "args_kwargs.py", "lambda_functions.py", "decorators.py", "function_annotations.py", "doc_strings.py"],
#         "02-More-Defining-Functions": {
#             "default_argument_values.py": None,
#             "keyword_arguments.py": None,
#             "special_parameters/positional_or_keyword.py": None,
#             "special_parameters/positional_only.py": None,
#             "special_parameters/keyword_only.py": None,
#             "special_parameters/function_examples.py": None,
#             "special_parameters/recap.py": None,
#             "arbitrary_argument_lists.py": None,
#             "unpacking_argument_lists.py": None
#         },
#         "03-Modules": ["modules_packages.py", "executing_modules.py", "module_search_path.py", "compiled_python_files.py"],
#         "04-Packages": ["import_from_package.py", "intra_package_refs.py", "multi_dir_packages.py"]
#     },
#     "05-Input-Output": ["input_output.py", "formatted_strings.py", "string_format_method.py", "manual_string_formatting.py", "old_string_formatting.py", "reading_writing_files.py", "saving_json.py"],
#     "06-Errors-Exceptions": ["syntax_errors.py", "exceptions.py", "handling_exceptions.py", "raising_exceptions.py", "exception_chaining.py", "user_defined_exceptions.py", "cleanup_actions.py", "predefined_cleanup.py", "multiple_exceptions.py", "enriching_exceptions.py"],
#     "07-OOP": ["classes_objects.py", "inheritance.py", "multiple_inheritance.py", "private_variables.py", "odds_and_ends.py", "iterators.py", "generators.py", "generator_expressions.py"],
#     "08-Advanced-Topics": ["context_managers.py", "decorators_advanced.py", "metaclasses.py", "threading_multiprocessing.py", "async_await.py"],
#     "09-Libraries": {
#         "numpy": ["basics.py", "arrays.py"],
#         "pandas": ["basics.py", "dataframes.py"],
#         "matplotlib": ["basics.py", "plots.py"],
#         "seaborn": ["plots.py"],
#         "requests": ["basics.py"],
#         "beautifulsoup": ["scraping.py"],
#         "selenium": ["automation.py"]
#     },
#     "10-Web-Development": {
#         "Flask": ["app_example.py", "routes_templates.py", "forms_validation.py"],
#         "FastAPI": ["app_example.py", "routes.py", "database.py"]
#     },
#     "11-Database": ["sqlite.py", "postgresql.py", "mongodb.py", "sqlalchemy_basics.py", "peewee_basics.py"],
#     "12-APIs": ["REST_API_flask.py", "REST_API_fastapi.py", "consuming_api_requests.py"],
#     "13-Testing": ["unittest_examples.py", "pytest_examples.py", "mocking_requests.py"],
#     "14-Projects": ["project_01_Calculator", "project_02_WebScraper", "project_03_BlogApp", "project_04_APIService", "project_05_InventorySystem", "project_06_FinanceDashboard"],
#     "15-Tools-Env": ["environment_setup.md", "git_gitignore.md", "python_versions.md"],
#     "16-Extras": ["python_tips.md", "performance_optimization.py", "debugging_tips.py", "code_style_pep8.md", "interview_questions.md"]
# }

# # Python file header template
# header_template = '''"""
# File: {filename}
# Author: Gashaw Gedef
# Purpose: To be filled
# """
# '''

# def create_structure(base, struct):
#     for name, content in struct.items() if isinstance(struct, dict) else enumerate(struct):
#         path = os.path.join(base, name) if isinstance(struct, dict) else os.path.join(base, content)
#         if "." in os.path.basename(path):  # It's a file
#             os.makedirs(os.path.dirname(path), exist_ok=True)
#             with open(path, 'w', encoding='utf-8') as f:
#                 f.write(header_template.format(filename=os.path.basename(path)))
#         else:  # It's a folder
#             os.makedirs(path, exist_ok=True)
#             if isinstance(content, dict):
#                 create_structure(path, content)
#             elif isinstance(content, list):
#                 create_structure(path, {item: None for item in content})

# # Run the script
# create_structure(".", structure)
# print("Merged Python-A-Z + tutorial folder structure created successfully!")
import os

# Full merged Python-A-Z + Tutorial structure including previous simple structure
structure = {
    # From your commented simple Python-A-Z
    "00-README.md": None,
    "01-Basics": {
        "01-Introduction": ["intro.py"],
        "02-Variables-DataTypes": ["variables_datatypes.py"],
        "03-Operators": ["operators.py"],
        "04-Input-Output": ["io_examples.py"],
        "05-Conditionals-Loops": ["conditionals_loops.py"]
    },
    "02-Data-Structures": ["lists.py", "tuples.py", "dicts.py", "sets.py"],
    "03-Functions-Modules": ["functions.py", "modules.py", "packages.py"],
    "04-File-Handling": ["text_files.py", "csv_files.py", "json_files.py"],
    "05-OOP": ["classes_objects.py", "inheritance.py", "polymorphism.py", "encapsulation_abstraction.py"],
    "06-Error-Exceptions": ["exceptions.py"],
    "07-Advanced-Topics": ["decorators.py", "generators.py", "iterators.py", "context_managers.py"],
    "08-Libraries": {
        "numpy": ["basics.py"],
        "pandas": ["basics.py"],
        "matplotlib": ["basics.py"],
        "requests": ["basics.py"]
    },
    "09-Web-Development": {
        "Flask": ["app_example.py"],
        "FastAPI": ["app_example.py"]
    },
    "10-Database": ["sqlite.py", "postgresql.py", "mongodb.py"],
    "11-Projects": ["project_01_Calculator", "project_02_WebScraper", "project_03_BlogApp", "project_04_APIService"],
    "12-Testing": ["tests_examples.py"],
    "13-Tools-Env": ["environment_setup.md"],
    "14-Extras": ["python_tips.md", "performance_optimization.py"],
    
    # From your full merged tutorial structure
    "15-Full-Tutorial": {
        "01-Whetting-Your-Appetite": ["intro.py"],
        "02-Using-Python-Interpreter": {
            "01-Invoking-Interpreter": ["argument_passing.py", "interactive_mode.py"],
            "02-Interpreter-Environment": ["source_code_encoding.py"]
        },
        "03-Informal-Introduction": ["using_as_calculator.py", "numbers.py", "text.py", "lists.py", "first_steps_programming.py"],
        "04-Conditionals-Loops": ["if_else.py", "nested_if.py", "for_loop.py", "while_loop.py", "loop_control.py"],
        "05-Data-Structures": {
            "01-Lists": ["lists.py", "using_as_stack.py", "using_as_queue.py", "list_comprehensions.py", "nested_list_comprehensions.py"],
            "02-Tuples-Sequences": ["tuples.py"],
            "03-Sets": ["sets.py"],
            "04-Dictionaries": ["dictionaries.py"],
            "05-Looping-Techniques": ["looping_techniques.py"],
            "06-Comparisons": ["more_on_conditions.py", "comparing_sequences.py"]
        },
        "06-Functions-Modules": {
            "01-Functions": ["functions.py", "args_kwargs.py", "lambda_functions.py", "decorators.py", "function_annotations.py", "doc_strings.py"],
            "02-More-Defining-Functions": {
                "default_argument_values.py": None,
                "keyword_arguments.py": None,
                "special_parameters/positional_or_keyword.py": None,
                "special_parameters/positional_only.py": None,
                "special_parameters/keyword_only.py": None,
                "special_parameters/function_examples.py": None,
                "special_parameters/recap.py": None,
                "arbitrary_argument_lists.py": None,
                "unpacking_argument_lists.py": None
            },
            "03-Modules": ["modules_packages.py", "executing_modules.py", "module_search_path.py", "compiled_python_files.py"],
            "04-Packages": ["import_from_package.py", "intra_package_refs.py", "multi_dir_packages.py"]
        },
        "07-Input-Output": ["input_output.py", "formatted_strings.py", "string_format_method.py", "manual_string_formatting.py", "old_string_formatting.py", "reading_writing_files.py", "saving_json.py"],
        "08-Errors-Exceptions": ["syntax_errors.py", "exceptions.py", "handling_exceptions.py", "raising_exceptions.py", "exception_chaining.py", "user_defined_exceptions.py", "cleanup_actions.py", "predefined_cleanup.py", "multiple_exceptions.py", "enriching_exceptions.py"],
        "09-OOP": ["classes_objects.py", "inheritance.py", "multiple_inheritance.py", "private_variables.py", "odds_and_ends.py", "iterators.py", "generators.py", "generator_expressions.py"],
        "10-Advanced-Topics": ["context_managers.py", "decorators_advanced.py", "metaclasses.py", "threading_multiprocessing.py", "async_await.py"],
        "11-Libraries": {
            "numpy": ["basics.py", "arrays.py"],
            "pandas": ["basics.py", "dataframes.py"],
            "matplotlib": ["basics.py", "plots.py"],
            "seaborn": ["plots.py"],
            "requests": ["basics.py"],
            "beautifulsoup": ["scraping.py"],
            "selenium": ["automation.py"]
        },
        "12-Web-Development": {
            "Flask": ["app_example.py", "routes_templates.py", "forms_validation.py"],
            "FastAPI": ["app_example.py", "routes.py", "database.py"]
        },
        "13-Database": ["sqlite.py", "postgresql.py", "mongodb.py", "sqlalchemy_basics.py", "peewee_basics.py"],
        "14-APIs": ["REST_API_flask.py", "REST_API_fastapi.py", "consuming_api_requests.py"],
        "15-Testing": ["unittest_examples.py", "pytest_examples.py", "mocking_requests.py"],
        "16-Projects": ["project_01_Calculator", "project_02_WebScraper", "project_03_BlogApp", "project_04_APIService", "project_05_InventorySystem", "project_06_FinanceDashboard"],
        "17-Tools-Env": ["environment_setup.md", "git_gitignore.md", "python_versions.md"],
        "18-Extras": ["python_tips.md", "performance_optimization.py", "debugging_tips.py", "code_style_pep8.md", "interview_questions.md"]
    }
}

# Python file header template
header_template = '''"""
File: {filename}
Author: Gashaw Gedef
Purpose: To be filled
"""
'''

def create_structure(base, struct):
    for name, content in struct.items() if isinstance(struct, dict) else enumerate(struct):
        path = os.path.join(base, name) if isinstance(struct, dict) else os.path.join(base, content)
        if "." in os.path.basename(path):  # It's a file
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not os.path.exists(path):
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(header_template.format(filename=os.path.basename(path)))
        else:  # It's a folder
            os.makedirs(path, exist_ok=True)
            if isinstance(content, dict):
                create_structure(path, content)
            elif isinstance(content, list):
                create_structure(path, {item: None for item in content})

# Run the script
create_structure(".", structure)
print("Combined Python-A-Z + Tutorial folder structure created successfully!")
