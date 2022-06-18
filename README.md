# Workforce-Acquisition-using-Text-Mining

# Dataset -
Job Description dataset scraped from Amazon.jobs.
Resume Dataset downloaded from Kaggle.

# Web Scraping - 
Using **Selenium** as the automation tool, I created my own dataset by scraping job descriptions from **Amazon.jobs**. The XPATH technique was used to navigate through the different jobs in all the web pages.

# Data Preprocessing - 
Performed Natural Language Processing steps to clean the Resume and Job Description datasets.

# Cosine Similarity - 
Performed Tokenization, stopword removal, and converted the dataset to a tf-idf matrix using **TfidfVectorizer**. Utilized Cosine Similarity metric to find the top 20 Resumes matching any Job ID.

# Topic Modeling - 
**Latent Dirichlet Allocation(LDA)** was used to perform topic modeling on both the Resume and Job Description datasets, to identify the top 20 topics. Top topic clusters were visualized as well using pyLDAvis library.

# Deployment
The Resume Screening Application is hoted on Heroku. Cosine Similiraity is used to find the top resumes matching any job id. You can check the application using the below link.
https://resume-screening-sys.herokuapp.com/
