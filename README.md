# 🎶Music Genre Classification Website🎶
### Ever wondered how the music you listen gets classified as 'Romantic', 'Jazz', 'Pop', etc.? Well it is mostly done manually. 
### How about a website that allows you to classify a music on your computer? Sounds interesting right..🌟

### Brief Overview about the project
#### Let me give you a brief overview how it's done. So, a music or any audio file is a combination of various tempos, zero-crossings, chromagrams, MFCCS, etc. When we take out a feature suppose MFCCS of a complete audio file it is basically a 2D-array of shape (20,x) where 20 represents parameters of MFCCS feature such as MFCCS1, MFCCS2, MFCCS3, etc. X represents the size values of these parameters. The larger the audio file, the larger is it's value. Finally, a ML algorithm helps in predicting the final genre of the music!

### Before going further and explain you everything, how about taking a look at website?? 😍 Video Link ⬇️

https://github.com/user-attachments/assets/4d70fda9-fde4-42e6-8061-2370599f0b60


### 🚀Steps to use on your local computer (without cloning)🚀-
#### Step-1 : All necessary libraries that you need to install are mentioned in 'Requirements.txt'. Make a file named 'requirements.txt' in your repository. You can use 'pip -r install requirements.txt' to install all files in one go. 
![requirements](https://github.com/user-attachments/assets/661663bd-2bd6-49e3-8a43-ce8d8a6a2b82)

#### Step-2 : Create 'setup.py' file in your repository that will help you install requirements in one go and setup your project.
![setup](https://github.com/user-attachments/assets/742534dd-05bd-49ee-beaf-b6fb0f13e0d5)

#### Step-3 : Create a few folders that are 'src', 'notebooks' and 'templates'. Remember to make a '__init__.py' file in each folder so that they can be used as package. 
##### Step-3.1 : Inside 'src' create two folders namely 'components' and 'pipeline'(create '__init__.py' in these two as well). Also, create 'exceptions.py', 'logger.py', 'utils.py' files in 'src' folder
![src](https://github.com/user-attachments/assets/1a6ae3f5-0525-4403-b28a-430aad5b70c0)
##### Step-3.2 : Create 'exceptions.py' file to use your own Custom Exceprions. 'Logger.py' file to keep a check on progress of your project(it will create a log file). 'utils.py' file that contains functions that are going to be used further in the project.

#### Step-4 : Inside folder 'notebooks' include your 'raw data' and make a '.ipynb' file. In this file, first complete the project so that you get to know what should be the correct approach(consider it as playground)

#### Step-5 : Come back to 'src->components' and create three python files 'data_ingestion.py', 'data_preprocessor.py' and 'model_trainer.py'. After successfully creating go to terminal and type 'python -m src.components.data_ingestion.py'. Voila!! Are you able to see some modifications in your root folder?? 'artifacts' has been created which includes your pickle file of preprocessor and model.

#### Step-6 : Create 'app.py' file, include all necessary libraries and '.pkl' file of your preprocessor and 'model'. Remember to include your 'html' files inside a separate folder namely 'templates'. To run this web-app go to terminal and type 'python app.py'. After it runs, go to your browser and type '127.0.0.1:5000' you should be able to access your website.

### Backend Working-
#### When the music file is uploaded, 'Librosa' library helps in finding out MFCCS feature of the file. It is a 2-D array which is then converted to a Pandas DataFrame. The data frame is preprocessed by 'preprocessor.pkl' file. After preprocessing, the data is feeded to model pipeline 'model.pkl' and final prediction is displayed back to the user.


## GitHub Link
[Music Genre Classification Web App](https://github.com/bhavyaprakash2002/Music-Genre-Classification-Web-App)



