# Talking Healthcare Chatbot

A voice-enabled healthcare chatbot that uses machine learning to understand user symptoms and provide relevant responses. Built with TensorFlow, scikit-learn, and speech libraries for natural language and audio interaction.

## Features

- Predicts user intent from text or voice input
- Responds with relevant healthcare advice
- Uses speech recognition and text-to-speech for interactive conversations
- Trained on custom healthcare intents

## Project Structure

```
├── inference.ipynb            # Notebook for running inference and voice interaction
├── intents.json               # Intents and responses for the chatbot
├── model.ipynb                # Model training notebook
├── text_utils.py              # Text preprocessing utilities
├── training.ipynb             # Training workflow notebook
```

## Setup Instructions

1. **Clone the repository**
   ```powershell
   git clone <repo-url>
   cd Talking Healthcare Chatbot
   ```
2. **Install dependencies**
   - Required Python packages:
     - tensorflow
     - scikit-learn
     - pandas
     - numpy
     - joblib
     - SpeechRecognition
     - pyttsx3
   - Install with pip:
     ```powershell
     pip install tensorflow scikit-learn pandas numpy joblib SpeechRecognition pyttsx3
     ```
3. **Run the chatbot**
   - Open `inference.ipynb` in Jupyter or VS Code
   - Run the cells to interact with the chatbot using text or voice

## Usage

- The chatbot can be used by running the inference notebook and following the prompts.
- You can speak your symptoms, and the bot will respond with advice using text-to-speech.

## Model Training

- Use `training.ipynb` and `model.ipynb` to train and evaluate the chatbot model.
- Intents and responses are defined in `intents.json`.

## Model Training Notebooks

There are two separate notebooks for training the chatbot model:

- **model.ipynb**: Uses a step-by-step approach for model building and training, suitable for experimentation and manual tuning. This notebook is ideal for users who want to understand and modify each stage of the model pipeline.
- **training.ipynb**: Provides a streamlined workflow for training, focusing on automation and reproducibility. This notebook is best for quickly retraining the model with updated data or parameters.

Both notebooks use the same dataset and intent structure, but follow different patterns to suit various user needs.

## Customization

- Add new intents and responses to `intents.json`.
- Retrain the model using the provided notebooks.

## Troubleshooting

- If audio output does not work, restart the notebook kernel and run only the relevant cells.
- Ensure your microphone and speakers are configured correctly in Windows.
- For issues with dependencies, check your Python environment and reinstall packages as needed.

## License

This project is for educational purposes.

## Author

Ankit Regmi
