# LinguaDetectio

LinguaDetectio is a powerful language detection tool designed to accurately identify the language of textual data. It utilizes state-of-the-art techniques and is powered by the FastText model, integrated with the FastAPI framework.

## Description

LinguaDetectio provides a fast and accurate solution for language detection tasks. Whether you are working with large volumes of text or need to determine the language of individual sentences, LinguaDetectio can handle it with precision. It incorporates advanced algorithms and linguistic features to deliver reliable language identification results.

## Installation

To install LinguaDetectio and its dependencies, follow these steps:

1. Ensure you have Python installed on your system (version 3.6 or higher).

2. Clone the LinguaDetectio repository from GitHub:

    ```bash
    git clone https://github.com/aymenkrifa/LinguaDetectio.git
    ```

3. Navigate to the project directory:

    ```bash
    cd LinguaDetectio
    ```

4. Create and activate a virtual environment via tools like `virtualenv`, `pyenv`, or `Anaconda` ..

5. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Model Download

To utilize the language detection functionality, you will need to download the FastText model. Follow these steps to acquire the model:

1. Visit the official FastText website for language identification: <https://fasttext.cc/docs/en/language-identification.html>

2. Download the language identification model (a pre-trained binary file).

3. Once downloaded, create a folder named 'models' in the LinguaDetectio project directory.

4. Move the downloaded model file into the 'models' folder.

    ```bash
    mv path/to/downloaded/model.bin models/
    ```

5. The 'models' folder should now contain the FastText language identification model.

## Usage

To use LinguaDetectio in different ways depending on your preference and requirements.

### Docker

1. Make sure you have Docker installed on your system.
2. Build the Docker image by running the following command in the project directory:

    ```bash
    docker build -t linguadetectio .
    ```

3. Run the Docker container with the following command, replacing `<port>` with the desired port number:

    ```bash
    docker run -d -p <port>:80 --name -t linguadetectio
    ```

    The LinguaDetect server will start, and the endpoint will be accessible at `http://127.0.0.1:<port>/detect`

4. Make a `POST` request to the endpoint URL with the text you want to identify the language for. The request should be in the following JSON format:

    ```json
    {
        "text": "Hello, how are you?"
    }
    ```

### Uvicorn

1. Start the LinguaDetect server with Uvicorn by running the following command in the project directory, replacing `<port>` with the desired port number:

    ```bash
    uvicorn app.main:app --port <port>
    ```

    The server will start, and the endpoint will be accessible at `http://127.0.0.1:<port>/detect`

2. Make a POST request to the endpoint URL with the text you want to identify the language for. The request should be in the following JSON format:

    ```json
    {
        "text": "Hello, how are you?"
    }
    ```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request on the GitHub repository.

## Acknowledgements

We would like to express our gratitude to the FastText team for providing the powerful language identification model and the FastAPI community for their excellent framework.

## Contact

For any inquiries or feedback, please contact the project maintainer at <aymenkrifa@gmail.com>.

Happy language detection with LinguaDetectio!
