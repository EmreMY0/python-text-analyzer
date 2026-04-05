
### ** Text Analyzer & Statistics Generator**

This tool is a Python-based text mining script designed to analyze text files and generate detailed statistics. It calculates word counts, sentence counts, character metrics, and word frequency distributions, making it ideal for basic linguistic analysis or academic projects.

#### **Features**
* **Comprehensive Stats:** Tracks total words, sentences, and character counts.
* **Text Cleaning:** Automatically strips punctuation and normalizes text to lowercase for accurate analysis.
* **Sentence Detection:** Corrected logic to identify sentence endings, including support for ellipses (`...`), question marks, and exclamation points.
* **Word Metrics:**
    * Finds the shortest and longest words along with their occurrence percentage.
    * Calculates the average word-to-sentence ratio.
    * Generates a full frequency distribution sorted by usage.
* **Formatted Output:** Writes all results to a neatly aligned `.txt` file.

#### **Usage**
Run the script with two arguments: the input file to analyze and the name of the output file:
```bash
python text_analyzer.py input.txt output.txt
```

#### **Technical Overview**
The script is built with a modular approach:
* `pure_words`: Handles string sanitization and tokenization.
* `sentence_finder`: Analyzes punctuation patterns to determine sentence structure.
* `word_frequency`: Uses Python's `lambda` functions to sort and rank word usage.
* `main`: Orchestrates the entire flow from file reading to the final report generation.

#### **Example Output Format**
```text
Statistics about input.txt:
#Words                  : 150
#Sentences              : 12
#Words/#Sentences       : 12.50
#Characters             : 840
...
Words and Frequencies   :
python                  : 0.0450
analysis                : 0.0210
```
