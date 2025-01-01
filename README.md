# home-price-prediction



# 📋 Project Overview
The Bengaluru Home Price Predictor is a full-stack MLOps project designed to predict property prices based on location, size, number of rooms, and other key features. The project includes:

◾ Data Preprocessing and Feature Engineering for high-quality training data.
◾ Model Training and Tuning using advanced algorithms and optimization techniques.
◾ API Deployment for real-time predictions accessible through a simple front-end interface.
This project serves as a stepping stone toward creating impactful, real-world AI solutions.



# 🔍 Project Details
## Project Name: Bengaluru Home Price Predictor
### Development Time: 10 hours
### Code Size: Over 2000 lines of code
### Technologies Used:
#### Python
#### Flask
#### Pickle
#### JSON
#### Scikit-learn
#### HTML/CSS


# 📂 Project Structure

`plaintext`
├── data/                   # Raw and processed data  
├── notebooks/              # Jupyter Notebooks for experimentation  
├── server/                    # Source code files 
│   ├── util.py       # Data preprocessing pipeline  
│   ├── server.py              # Flask API for deployment
│   ├── artifacts/
│       ├── banglore_home_prices_model.pickle      # model 
        ├── columns.json              # columns  
├── model/                    # Source code files  
│   ├── banglore_home_prices_model.pickle      # final model  
│   ├── bhp.csv  # new data
│   ├── columns.json              # columns  
│   ├── last.ipynb              # notebook  
├── client/                 # Front-end assets (HTML/CSS/JS)    
├── README.md               # Project documentation  
└── requirements.txt        # Python dependencies  



# 🔧 Setup Instructions
## 1-Clone the repository:
`bash` git clone https://github.com/lourimiyassine/home-price-prediction.git  
`bash` cd BengaluruHomePricePredictor 

## 2-Install dependencies:
`bash`
pip install -r requirements.txt 
## 3-Run the Flask app:
`bash`
python server/server.py  
## 4-Test the API using Postman or any HTTP client.




# 📊 Results
◾ Model Accuracy: Achieved a score of 85% on test data using Linear Regression.
◾ Hyperparameter Tuning: Optimal parameters for Decision Tree improved prediction accuracy.

# 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

# 📬 Contact
For questions or feedback, reach out to:

Name: Yassine Lourimi
Email: yassinelourimi85@gmail.com
LinkedIn: https://www.linkedin.com/in/yassine-lourimi-74591a2a1/
