# Content Monetization Modeler

A beginner-friendly GUVI AIML capstone project that predicts YouTube ad revenue using regression models.

## Project Goal

The notebook trains five regression models and selects the best one to predict `ad_revenue_usd` from video performance data.

## Files

- `Content_Monetization_Modeler.ipynb` - full notebook from data loading to model saving
- `app.py` - Streamlit app for making predictions
- `requirements.txt` - project dependencies
- `models/` - saved Joblib model file
- `youtube_ad_revenue_dataset.csv` - dataset in the workspace

## Dataset Columns

- `video_id`
- `date`
- `views`
- `likes`
- `comments`
- `watch_time_minutes`
- `video_length_minutes`
- `subscribers`
- `category`
- `device`
- `country`
- `ad_revenue_usd`

## How to Run the Notebook

1. Open `Content_Monetization_Modeler.ipynb` in VS Code.
2. Run the cells from top to bottom.
3. The notebook will clean the data, train the models, compare them, and save the final model.

## How to Run the Streamlit App

Install the packages and start the app:

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

If `streamlit` is not recognized in your terminal, activate the virtual environment first or run the command with the project Python executable:

```bash
.venv\Scripts\python.exe -m streamlit run app.py
```

## Repository Structure

```text
Content_Monetization_Modeler.ipynb
app.py
requirements.txt
README.md
models/
youtube_ad_revenue_dataset.csv
```

## Notes

- The notebook looks for `youtube_monetization.csv` first.
- If that file is not found, it uses `youtube_ad_revenue_dataset.csv` in the workspace.
- The saved model is stored in `models/content_monetization_model.joblib`.
