# Frequency Analysis

A little Python script to analyze the frequency of letters in a given text and display a graph for each letter.

## Requirements

Install the required Python dependency:

```bash
pip install matplotlib
```

## Arguments

- If you add the `--sort` argument, the results will be sorted.
- You need to provide either a filename or a string to the script.

## Example

```bash
$> python frequency_analysis.py example_file.txt --sort
f: 13.33%
m: 10.48%
x: 7.62%
a: 7.62%
u: 6.67%
t: 5.71%
q: 5.71%
k: 5.71%
e: 5.71%
y: 4.76%
z: 4.76%
g: 3.81%
n: 3.81%
i: 2.86%
w: 1.90%
d: 1.90%
s: 1.90%
o: 1.90%
p: 0.95%
c: 0.95%
r: 0.95%
l: 0.95%
```

## Usage Cases

- **Cryptanalysis:**  
  Frequency analysis is a fundamental technique in breaking classical ciphers such as Caesar or substitution ciphers by comparing letter frequencies in the ciphertext to typical frequencies in the target language.

- **Language Analysis:**  
  Useful for linguists or language learners to study letter distribution in different languages or texts.

- **Text Profiling:**  
  Can help identify the language or author of a text based on characteristic letter frequency patterns.

- **Data Cleaning:**  
  Detect anomalies or errors in large text datasets by spotting unusual frequency distributions.
