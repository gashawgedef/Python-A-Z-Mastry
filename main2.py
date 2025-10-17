import os

# Grouped structure with similar concepts
structure = {
    # Basics / Intro
    "01-Basics": {
        "Whetting-Your-Appetite": ["intro.py"],
        "Using-Python-Interpreter": ["argument_passing.py", "interactive_mode.py", "source_code_encoding.py"],
        "Informal-Introduction": ["using_as_calculator.py", "numbers.py", "text.py", "lists.py", "first_steps_programming.py"],
        "Conditionals-Loops": ["if_else.py", "nested_if.py", "for_loop.py", "while_loop.py", "loop_control.py"]
    },

    # Data Structures
    "02-Data-Structures": {
        "Lists": ["lists.py", "using_as_stack.py", "using_as_queue.py", "list_comprehensions.py", "nested_list_comprehensions.py"],
        "Tuples-Sequences": ["tuples.py"],
        "Sets": ["sets.py"],
        "Dictionaries": ["dicts.py", "dictionaries.py"],
        "Looping-Techniques": ["looping_techniques.py"],
        "Comparisons": ["more_on_conditions.py", "comparing_sequences.py"]
    },

    # Functions and Modules
    "03-Functions-Modules": {
        "Functions": ["functions.py", "args_kwargs.py", "lambda_functions.py", "decorators.py", "function_annotations.py", "doc_strings.py"],
        "More-Defining-Functions": {
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
        "Modules": ["modules.py", "modules_packages.py", "executing_modules.py", "module_search_path.py", "compiled_python_files.py"],
        "Packages": ["packages.py", "import_from_package.py", "intra_package_refs.py", "multi_dir_packages.py"]
    },

    # Input / Output
    "04-Input-Output": ["io_examples.py", "input_output.py", "formatted_strings.py", "string_format_method.py", "manual_string_formatting.py", "old_string_formatting.py", "reading_writing_files.py", "saving_json.py"],

    # Errors / Exceptions
    "05-Errors-Exceptions": ["exceptions.py", "syntax_errors.py", "handling_exceptions.py", "raising_exceptions.py", "exception_chaining.py", "user_defined_exceptions.py", "cleanup_actions.py", "predefined_cleanup.py", "multiple_exceptions.py", "enriching_exceptions.py"],

    # Object-Oriented Programming
    "06-OOP": ["classes_objects.py", "inheritance.py", "multiple_inheritance.py", "private_variables.py", "odds_and_ends.py", "iterators.py", "generators.py", "generator_expressions.py", "polymorphism.py", "encapsulation_abstraction.py"],

    # Advanced Topics
    "07-Advanced-Topics": ["context_managers.py", "decorators_advanced.py", "metaclasses.py", "threading_multiprocessing.py", "async_await.py"],

    # Libraries
    "08-Libraries": {
        "numpy": ["basics.py", "arrays.py"],
        "pandas": ["basics.py", "dataframes.py"],
        "matplotlib": ["basics.py", "plots.py"],
        "seaborn": ["plots.py"],
        "requests": ["basics.py"],
        "beautifulsoup": ["scraping.py"],
        "selenium": ["automation.py"]
    },

    # Web Development
    "09-Web-Development": {
        "Flask": ["app_example.py", "routes_templates.py", "forms_validation.py"],
        "FastAPI": ["app_example.py", "routes.py", "database.py"]
    },

    # Database
    "10-Database": ["sqlite.py", "postgresql.py", "mongodb.py", "sqlalchemy_basics.py", "peewee_basics.py"],

    # APIs
    "11-APIs": ["REST_API_flask.py", "REST_API_fastapi.py", "consuming_api_requests.py"],

    # Testing
    "12-Testing": ["tests_examples.py", "unittest_examples.py", "pytest_examples.py", "mocking_requests.py"],

    # Projects
    "13-Projects": ["project_01_Calculator", "project_02_WebScraper", "project_03_BlogApp", "project_04_APIService", "project_05_InventorySystem", "project_06_FinanceDashboard"],

    # Extras / Tools
    "14-Extras": ["performance_optimization.py", "debugging_tips.py", "python_tips.py", "code_style_pep8.py", "interview_questions.py"]
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

# Run the script in current directory
create_structure(".", structure)
print("Python-A-Z-Mastery folder structure created successfully in current directory!")
