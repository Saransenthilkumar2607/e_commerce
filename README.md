# Setup Instructions

1. Create a virtual environment
      ```
      python3.12.1 -m venv venv
      ```

2. Activate the virtual environment
      ```
      source .\env\Scripts\Activate.ps1
      /venv/Scripts/Activate.ps1
      ```
      deactivate
 

3. Install the dependencies
      ```
      pip install -r requirements.txt
      ```

4. Create a .env file in the root directory and add the following environment variables

5. Run the applications
      ```
      python app.py
      ```

6. if you want to find the version of the reqyirements
      ```
      python -m pip show pandas
      ```

7. Initialize Migrations Folder
      ```
      flask --app app:create_app db init --directory app/migrations
      ```
   Generate Migration Script
      ```
      flask --app app:create_app db migrate -m "Add customer table" --directory app/migrations
      ```
   Apply Migration to Database
      ```
      flask --app app:create_app db upgrade --directory app/migrations
      ```
      