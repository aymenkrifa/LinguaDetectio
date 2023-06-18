# LinguaDetect
LinguaDetect is a powerful language detection tool designed to accurately identify the language of textual data. It utilizes state-of-the-art techniques and is powered by the FastText model, integrated with the FastAPI framework.

## Description

LinguaDetect provides a fast and accurate solution for language detection tasks. Whether you are working with large volumes of text or need to determine the language of individual sentences, LinguaDetect can handle it with precision. It incorporates advanced algorithms and linguistic features to deliver reliable language identification results.

## Installation
To install LinguaDetect and its dependencies, follow these steps:

1. Ensure you have Python installed on your system (version 3.6 or higher).

2. Clone the LinguaDetect repository from GitHub:
    ```bash
    git clone https://github.com/aymenkrifa/LinguaDetectio.git
    ```
3. Navigate to the project directory:
    ```bash
    cd LinguaDetectio
    ```
4. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Model Download
To utilize the language detection functionality, you will need to download the FastText model. Follow these steps to acquire the model:
1. Visit the official FastText website for language identification: https://fasttext.cc/docs/en/language-identification.html

2. Download the language identification model (a pre-trained binary file).

3. Once downloaded, create a folder named 'models' in the LinguaDetect project directory.

4. Move the downloaded model file into the 'models' folder.
    ```bash
    mv path/to/downloaded/model.bin models/
    ```
5. The 'models' folder should now contain the FastText language identification model.

## Usage