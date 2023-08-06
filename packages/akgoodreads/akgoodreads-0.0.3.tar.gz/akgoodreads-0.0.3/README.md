<!--- Heading --->
<div align="center">
  <img src="assets/banner.png" alt="banner" width="auto" height="auto" />
  <h1>Goodreads Scraper</h1>
  <p>
    A python wrapper for <a href="https://www.goodreads.com/api/index">goodreads API</a>
  </p>
<h4>
    <a href="https://github.com/rpakishore/goodreads/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/goodreads">Documentation</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/goodreads/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/goodreads/issues/">Request Feature</a>
  </h4>
</div>
<br />


<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. Getting Started](#1-getting-started)
  - [1.1. Dependencies](#11-dependencies)
  - [1.2. Installation](#12-installation)
- [2. Usage](#2-usage)
  - [2.1. Initialize the client](#21-initialize-the-client)
  - [2.2. Search for books](#22-search-for-books)
  - [2.3. Search for books](#23-search-for-books)
- [3. License](#3-license)
- [4. Contact](#4-contact)
- [5. Acknowledgements](#5-acknowledgements)

<!-- Getting Started -->
## 1. Getting Started
You will need a Goodreads API key for this to work. Unfortunately, Goodreads is not giving out new keys at this time, so unless you have signed up from a while ago - this wont work for you. 

On the launch of the script, you will be prompted for the API key. If you are using windows, you will be prompted to save this key locally for ease (using `keypass` library). 

### 1.1. Dependencies
All the dependencies should automatically be installed when installing the script. This project heavily relies on the `requests` library to make the api calls.

<!-- Installation -->
### 1.2. Installation

Install with pip

```bash
  pip install akgoodreads
```
<!-- Usage -->
## 2. Usage

### 2.1. Initialize the client

```python
import akgoodreads
client = goodreads.Goodreads("<your email>")
```

### 2.2. Search for books
With title
```python
client.book("Ender's Game", limit = 5)
```

or with goodreads ID
```python
client._book_from_id(50)
```

### 2.3. Search for books
With title
```python
client.author("Rowling")
```

or with goodreads ID
```python
client._author_from_id(7995)
```

<!-- License -->
## 3. License
See LICENSE.txt.

<!-- Contact -->
## 4. Contact

Arun Kishore - [@rpakishore](mailto:goodreads@rpakishore.co.in)

Github Link: [https://github.com/rpakishore/](https://github.com/rpakishore/)


<!-- Acknowledgments -->
## 5. Acknowledgements
 - [Awesome README Template](https://github.com/Louis3797/awesome-readme-template/blob/main/README-WITHOUT-EMOJI.md)
 - [Banner Maker](https://banner.godori.dev/)
 - [Shields.io](https://shields.io/)
 - [Carbon](https://carbon.now.sh/)