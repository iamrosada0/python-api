# Flask Translation API

This project is a Flask-based API for text translation. It uses the `deep_translator` library to translate text between Portuguese and English. The API is configured with CORS to handle cross-origin requests, making it easy to integrate with frontend applications.

## Features
- Translate text from Portuguese to English.
- Translate text from English to Portuguese.
- Validate input data and handle errors gracefully.
- CORS enabled for seamless integration with web clients.

---

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7 or later
- pip (Python package manager)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add the following dependencies to your `requirements.txt` file if not already included:
   ```plaintext
   Flask
   Flask-Cors
   deep-translator
   ```

---

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. The API will run on `http://127.0.0.1:5000/` by default.

3. Endpoints:

   - **Home Endpoint**
     ```
     GET /
     ```
     - Response: `"Hello, Flask is running!"`

   - **Translation Endpoint**
     ```
     POST /translate
     ```
     - Request Body (JSON):
       ```json
       {
         "text": "Olá, como você está?",
         "direction": "Portuguese to English"
       }
       ```
     - Response (JSON):
       ```json
       {
         "translated_text": "Hello, how are you?"
       }
       ```
     - Directions Supported:
       - `Portuguese to English`
       - `English to Portuguese`

---

## Error Handling

The API provides meaningful error messages:

1. **Missing or Invalid Fields**
   - Response (400):
     ```json
     {
       "error": "Fields 'text' and 'direction' are required."
     }
     ```

2. **Invalid Translation Direction**
   - Response (400):
     ```json
     {
       "error": "Invalid translation direction. Use 'Portuguese to English' or 'English to Portuguese'."
     }
     ```

3. **Translation Failure**
   - Response (500):
     ```json
     {
       "error": "Translation failed: <error_message>"
     }
     ```

---

## Deployment

To deploy this API, you can use platforms like [Vercel](https://vercel.com/) or [Heroku](https://www.heroku.com/). For deployment instructions:

### Deploying on Vercel

1. Add a `vercel.json` file to the root of your project:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "index.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "index.py"
       }
     ]
   }
   ```

2. Ensure your main application file is named `index.py`. If it is named differently (e.g., `app.py`), update the `vercel.json` accordingly.

3. Push your project to a GitHub repository.

4. Deploy on Vercel:
   - Link your repository to Vercel.
   - Configure the deployment settings.
   - Deploy your application.

5. Access your deployed application at the URL provided by Vercel.

---

## Improvements and Future Enhancements

- Add support for more languages.
- Implement a frontend interface for the API.
- Add rate limiting to prevent abuse.
- Integrate user authentication for access control.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.

---

## Author

Created by **iamrosada**. You can explore more of my work on [GitHub](https://github.com/iamrosada0).

