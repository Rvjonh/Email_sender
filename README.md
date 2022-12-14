# Email sender (API)

First version of an app (API) to send email with flask, tipically for contact forms.
You can send a message through the internet (STMP), with some requirements.

## Requirements

* Python 3.9v or above
* An Code editor
* Two email accounts (recommended Gmail, other can require more changes in code base in your choice)
* a backend server, or server to deploy python flask apps (recommended, [railway](https://railway.app/))

## Development

If you want to add changes (like, personalize the sent email) or improve it adding more features this section should help you.

* `Easier`: You will need [git](https://git-scm.com/), a control system that allows you download easier the code.

* `Manually`: [Download the Zip file](https://github.com/Rvjonh/Email_sender/archive/refs/heads/main.zip), and use Winrar to unpack the folder.

Now you have the folder project, follow next steps:

1. Open the folder and see the next structure:
    * .env-vars
    * .gitignore
    * email_sender.py
    * json_responder.py
    * main.py
    * Procfile
    * README.md
    * requirements.txt

2. Create an enviroment for your flask application:

    * init enviroment, in the root directory with name 'venv' of enviroment

    ```bash
        python -m venv venv
    ```

    * Activate your enviroment (Windows) or check [others](https://docs.python.org/3/tutorial/venv.html)

    ```bash
        venv\Scripts\activate.bat
    ```

    * Install the dependencies, flask, flask-mail, flask-cors...

    ```bash
        pip3 install -r requirements.txt
    ```

3. Add Emails to put it to work:

    * On Windows copy the enviromental vars

    ```bash
        copy .env-vars .env
    ```

    Fill with the emails information int the new file .env, remember, keeping this file save , because it's yours and only yours, this file in server it's replaced with enviromental variables for every project, and can be setted in the server but they always be private, but only yours, do not share it with anyone.

4. **Coding:** it's really recommended to know the [flask framework](https://flask.palletsprojects.com/en/2.2.x/) if you want to add new features or make changes so check itout for further information.

5. The app specification is in main.py, you can star runnig a debug mode (which is a local server to delopment) with next command:

    ```bash
        python main.py
    ```

    or

    ```bash
        flask --app main --debug run
    ```

6. Frecuently you can make a request to 'http://127.0.0.1:5000/email' direction.

    * Example: A full use of the API /email with POST method with javascript.

    ```javascript
        fetch('http://127.0.0.1:5000/email',{
            method : 'POST',
            headers: {'Content-Type': 'application/json'},
            body:JSON.stringify({
                "name":"Jonh Gomez",
                "email":"jonhvelasco3@gmail.com",
                "subject":"An Email API",
                "message":"This is a great idea to discuss"
            })
        }).then((res)=>{
            console.log("Email sent")
        }).catch(err=>{
            console.log("Email not sent")
        })
    ```

## Thank you, for watching this repository, if you have any questions share them with me through, as you can see my [PORTFOLIO](https://rvjonh-portfolio.netlify.app/) WHICH uses this API for a contact form
