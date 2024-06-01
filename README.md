# Voice Cloning Application using SO-VITS_SVC Architecture

## Disclaimer
This application is intended for educational and research purposes only. Voice cloning technology has the potential to be misused, and unauthorized use of someone's voice without their explicit permission may lead to legal consequences. It is crucial to respect privacy and obtain proper consent before using this technology.

## README for Flask Web Application using SO-VITS-SVC Architecture

Welcome to the Flask web application that utilizes the SO-VITS-SVC architecture for voice cloning and synthesis. This README will guide you through the setup, usage, and key resources associated with this project.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Clone the Repository](#clone-the-repository)
   - [Set Up Virtual Environment](#set-up-virtual-environment)
   - [Install Dependencies](#install-dependencies)
   - [Download Pre-trained Models](#download-pre-trained-models)
4. [Usage](#usage)
   - [Running the Application](#running-the-application)
   - [Using Docker](#using-docker)
5. [Resources](#resources)
6. [License](#license)
7. [Contributing](#contributing)

## Introduction
This project implements a Flask web application that leverages the SO-VITS-SVC (Soft Voice Conversion and Variational Inference Text-to-Speech) architecture. The SO-VITS-SVC model enables robust voice conversion and synthesis by extracting acoustic features and conditioning the VITS model to produce high-quality, personalized voice outputs.

## Features
- Voice cloning from input audio files.
- Real-time speech synthesis using pre-trained models.
- User-friendly web interface for uploading audio files and listening to synthesized outputs.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git
- CUDA-compatible GPU (for Docker usage)

### Clone the Repository
```sh
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

### Set Up Virtual Environment
-python -m venv venv
-source venv/bin/activate  # On Windows use venv\Scripts\activate

### Install Dependencies
-pip install -r requirements.txt

Download Pre-trained Models
Download the pre-trained models from the SO-VITS-SVC GitHub repository: SO-VITS-SVC GitHub Repository

Usage
Running the Application
To run the Flask application locall

export FLASK_APP=app.py
flask run
# or
python app.py


### Using Docker
you can build the image from scratch using the docker file in the repo 
command : docker build -t <yourimagename> .

or pull and start the container with :
docker run --gpus all -p8080:8080 --name voicecloning abdelrahman915/imageprefinal:Lastdance


### Resources
-https://github.com/svc-develop-team/so-vits-svc?tab=readme-ov-file
-https://colab.research.google.com/drive/1JBJvk1FluAOM9DOlvUBjrsnUKZCWPuXd?usp=sharing

### Contributing
We welcome contributions to this project. Please open an issue or submit a pull request on GitHub.

Special thanks to my amazing team: Abdelrahman915

For major changes, please open an issue first to discuss what you would like to change.







