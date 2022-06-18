# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

st.title("Resume Screening System")

resume_df = pd.read_csv(r"C:\Users\dsingh38\Downloads\Resume.csv", encoding="unicode_escape")
jobdesc_df = pd.read_csv(r"C:\Users\dsingh38\Downloads\JobDesc.csv", encoding="unicode_escape")



st.subheader("Job IDs")
jobs = []
a = jobdesc_df['JOB_ID'].sort_values(ascending=True).unique().tolist()
jobs.extend(a) 

job_id = st.selectbox("Select your Job ID",jobs)


st.subheader("How many candidates?")


candidates = st.slider("from low to high!",min_value=0,max_value = 20, value=20)


st.subheader("Top Matching Resumes")
vectorizer = TfidfVectorizer(stop_words='english', binary=False, use_idf=False, norm=None, max_features=300)
doc_vectors=vectorizer.fit_transform(resume_df['Resume'])

#Defining function to show top resumes for any job description based on cosine similarity
def match_job_resume(job_id, candidates):
  ids = jobdesc_df.index[jobdesc_df.iloc[:,0].str.contains(job_id)].tolist()
  s = [str(integer) for integer in ids]
  a_string = "".join(s)
  res = int(a_string)
  query=jobdesc_df["Skills"][res]

  q_vector= vectorizer.transform([query])
  print("Complete Job Description:")
  print("---------------")
  print(query)
  print("---------------")

  cosine_sim={}
  for i in range(doc_vectors.shape[0]):
    content_cosine_similarity=cosine_similarity(q_vector, doc_vectors[i].toarray())
    cosine_sim.update({i:content_cosine_similarity[0][0]})

  k= Counter(cosine_sim)
  high=k.most_common(candidates)
  top_10_resume=dict(high)
  matched = []
  for key,val in top_10_resume.items():
      matched.append(resume_df.iloc[key:key+1,0].values[0])
      print('Job-ID-',id,'--Resume ID : ', resume_df.iloc[key:key+1,0].values[0], ' ---Similarity Matched=',str(val))
    
  return matched



display = match_job_resume(job_id, candidates)


for i in display:
    st.write(i)
