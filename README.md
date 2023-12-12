# Malicious JS and Url detection

## **Research Motivation and Objectives**

With the increasing reliance on online services, particularly government websites, the threat from phishing sites and malicious JavaScript has intensified. This project is driven by the need to empower ordinary users with the ability to recognize and be alerted about potentially malicious websites. Our objectives are:

- To develop a user-friendly tool that can identify harmful JavaScript and phishing URLs.
- To ensure our solution alerts users effectively without causing unnecessary inconvenience.

## **How to Use This Repository**

To utilize our Malicious JavaScript and URL Detection tool, follow these detailed instructions:

### **System Requirements**

- **Operating System**: Linux (e.g., Kali Linux)
- **Memory**: At least 4 GB for optimal performance

### **Installation Steps**

1. **Download Necessary Files**:
   - Navigate to our Google Drive folder: https://drive.google.com/drive/folders/1Rd1Mg-fSYpe6q2TY64MNpMXPjovK0NXf
   - Download **`install_script.py`**, **`server.py`**, and the two model files.
2. **Run Installation Script**:
   - Open a terminal and execute the installation script by typing **`python install_script.py`**.
   - This script sets up the necessary environment and dependencies. Once completed, a server icon will be created on your desktop.
3. **Start the Server**:
   - Launch the server by running **`python server.py`** in your terminal.
   - This command initiates the server side of the application, enabling the processing of JavaScript and URL data.
4. **Set Up the Chrome Extension**:
   - Download the extension files from the repository and unzip them.
   - Open Google Chrome and navigate to Extensions (chrome://extensions/).
   - Enable "Developer mode", select "Load unpacked", and point to the location of the unzipped extension files.
   - After loading the extension, pin it to your browser for easy access.
5. **Using the Extension**:
   - Click on the extension icon in your browser to activate it.
   - The extension interacts with the running server to analyze websites you visit, alerting you to any potential threats detected by our models

## **Project Components**

### **1. Server with Machine Learning Models**

- **Malicious JavaScript Detection (BiLSTM Model)**: Utilizes a BiLSTM network for analyzing and identifying malicious JavaScript patterns. This model is chosen for its proficiency in handling long-term dependencies in complex JavaScript data structures.
- **Malicious URL Detection (BERT Model)**: Employs a BERT model for the detection of phishing URLs. BERT's advanced natural language processing capabilities allow for effective analysis of URL patterns to identify potential threats.

### **2. Chrome Extension**

- **Displaying Results**: The Chrome extension serves as the user interface, displaying results of the analysis conducted by the server models. It interacts with the server to check visited websites and alerts users if a potential threat is detected.
- **User Interaction**: Designed to be intuitive and non-intrusive, ensuring users are informed of risks without disrupting their browsing experience.

## **Malicious JavaScript Detection Steps**

1. **Data Collection**: Gathering normal and malicious JavaScript samples from various sources.
2. **JavaScript Parsing**: Utilizing Esprima, an ECMAScript parser, we convert JavaScript codes into abstract syntax trees (ASTs). ASTs are crucial for lexical analysis as they effectively represent the structural hierarchy of code.
3. **Syntactic Sequence Extraction**: We perform a depth-first search on the ASTs to represent JavaScript codes as sequences of syntactic units. This method captures the intricate details of the code structure.
4. **Fasttext Model Training**: The extracted syntactic unit sequences are transformed into vector forms using the Fasttext model, which excels in converting words into character-level n-gram representations. This contrasts with models like Word2Vec, as Fasttext considers the internal structure of words, which is essential for understanding JavaScript syntax.
5. **Bi-LSTM Model Training**: These vector sequences are then fed into a Bi-LSTM model. Our model configuration includes a single-layer Bi-LSTM with 12 hidden nodes. The model predicts an output of 0 for benign scripts and 1 for malicious scripts, enabling effective differentiation.

## **Phishing Website Detection Process**

The detection of malicious URLs in our project undergoes a comprehensive preprocessing and analysis pipeline:

1. **Data Preprocessing**: Recognizing the importance of preprocessing in malicious URL detection, our initial step involves cleaning and preparing the dataset for analysis.
2. **Tokenization**: Utilizing NLTK's RegexpTokenizer, we split URLs into words using regular expressions, ensuring effective segmentation of textual data.
3. **Stemming**: We apply NLTK's Snowball stemmer to reduce words to their base forms, aiding in the normalization and consistency of text data.
4. **Vectorization**: Employing scikit-learn's CountVectorizer, we transform the preprocessed text into a matrix of token counts, an essential step for extracting features useful in classification.
5. **Data Splitting**: To evaluate our models' performance reliably, we divide our dataset into training and testing subsets. This approach ensures our models are tested on unseen data, minimizing the risk of overfitting.
6. **Model Selection**: We explore and select the most effective machine learning models for identifying and classifying malicious URLs, focusing on those demonstrating the highest performance in our tests.
