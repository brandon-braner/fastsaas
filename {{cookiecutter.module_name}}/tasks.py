from invoke import task
import os
import shutil


@task
def module(ctx, name):
    def _create_module():
        # Create a new folder in the "modules" directory
        new_folder_path = os.path.join("{{cookiecutter.module_name}}/modules", name)
        os.makedirs(new_folder_path)

        # Copy the files from "_module_template" to the new folder
        template_folder_path = os.path.join(
            "{{cookiecutter.module_name}}/_module_template"
        )

        shutil.copy(os.path.join(template_folder_path, "__init__.py"), new_folder_path)
        shutil.copy(
            os.path.join(template_folder_path, "api_routes.py"), new_folder_path
        )
        shutil.copy(os.path.join(template_folder_path, "service.py"), new_folder_path)
        shutil.copy(
            os.path.join(template_folder_path, "web_routes.py"), new_folder_path
        )

        # Replace text in the files that matches "{name}" with the name passed in
        for file_name in os.listdir(new_folder_path):
            file_path = os.path.join(new_folder_path, file_name)
            with open(file_path, "r") as file:
                file_content = file.read()
            file_content = file_content.replace("{module_name}", name)
            with open(file_path, "w") as file:
                file.write(file_content)

        # # Print success message
        print(f"Module {name} created successfully!")

    _create_module()
