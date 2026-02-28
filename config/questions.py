'''
Author:     Dheeraj Singh
LinkedIn:   https://www.linkedin.com/in/dheerajshankarsingh/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/dheerajsingh718/Auto_job_applier_linkedIn

Support me: https://github.com/sponsors/dheerajsingh718

version:    26.01.20.5.08
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/Dheeraj Singh Shankar DS V2.pdf"      # (In Development)

# Optional: use different resumes for different job titles.
# Format:
# "comma separated keywords": "path/to/resume.pdf"
# The first matching keyword set wins; if no match is found, `default_resume_path` is used.
role_based_resumes = {
    "data scientist, senior data scientist, junior data scientist, applied scientist, research scientist, machine learning scientist, machine learning engineer, ml engineer, ai engineer, artificial intelligence engineer, ai/ml engineer, generative ai engineer, genai engineer, llm engineer, nlp engineer, computer vision engineer, deep learning engineer, prompt engineer, data engineer, mlops engineer, ml ops engineer, ai platform engineer, applied ml engineer": "all resumes/default/Dheeraj Singh Shankar DS V2.pdf",
    "data analyst, senior data analyst, business intelligence analyst, analytics engineer, product data analyst, quantitative analyst": "all resumes/default/Dheeraj Singh DA.pdf",
}

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "5"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "Yes"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://github.com/dheerajsingh718"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/dheerajshankarsingh/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for any employer"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 100000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 0            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 0                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Data Scientist | AI/ML Engineer | RAG • NLP • Python • AWS | Ex-Mphasis | Handshake AI Model Validation Fellow" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
I am a Data + GenAI professional with 6+ years of software engineering experience, now focused on building reliable, measurable, and useful analytics and AI systems in the real world. 
I work across the full pipeline, data extraction and modeling, dashboards and storytelling, and GenAI (RAG/chatbots) applications, bringing a product-builder mindset to every problem.

Recently, I have been part of Handshake's AI Model Validation Fellowship, contributing across Project Canary, Orion, Lexicon, Hedgehog, and Public Spaces, where I evaluate LLM behavior for reasoning quality, instruction adherence, and robustness. 
My work includes structured rubric scoring, Golden Prompt design, stress testing, and evidence-based error annotation—especially catching failure patterns such as unsupported claims, instruction drift, and evaluation loopholes that undermine reliability.

On the applied analytics side, I supported Second Chance Services as a Data Analyst, performing EDA on engagement and conversion datasets from HubSpot, LinkedIn, and social platforms, scraping and aggregating audience data for targeting, and building Power BI + HubSpot dashboards to track KPIs, funnel performance, and audience insights.

Earlier in my career, I shipped production systems across multiple industries:

Mphasis(Clients: AIG, First Republic Bank(now part of JP Morgan Chase) and Kore ai ): built Kore ai chatbots with NLP + sentiment signals, automated QA workflows with Python, optimized SQL pipelines, and delivered BI dashboards for stakeholder reporting.
Brillio (Client: Verizon): led UI modernization from ExtJS to React, validated improvements through A/B testing, and delivered critical modules ahead of schedule (Team Excellence recognition).
MVerve: developed full-stack products across healthcare and consumer platforms, including secure role-based dashboards and AWS deployments.

My capstone work at Yeshiva University includes building Felix, a Canvas-integrated GenAI assistant (RAG + vector search) designed to help students find course support and career resources responsibly and at scale.

Core skills: Python, SQL, Model Development Life Cycle, Power BI, HubSpot analytics, ETL, experimentation and A/B testing, NLP, RAG, LangChain, ChromaDB, cloud (AWS/Azure), and stakeholder communication.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am a Data Scientist and AI/ML Engineer with over six years of experience building and deploying machine learning, deep learning, and NLP solutions in production environments . I am seeking opportunities where I can design intelligent systems that solve real business problems while operating at scale. I am particularly interested in Data Scientist and AI Engineer roles that combine strong modeling foundations with modern Generative AI and cloud-based deployment practices.

Throughout my career, I have developed and deployed NLP-driven systems, predictive models, and AI-powered applications across banking, telecom, and enterprise platforms . At Mphasis, I built NLP chatbots using intent classification and Named Entity Recognition, improving resolution accuracy and enhancing customer experience . I have also contributed to LLM evaluation and fine-tuning workflows, reducing hallucinations and strengthening model reliability in production settings . My experience spans Python, TensorFlow, PyTorch, scikit-learn, SQL, and cloud platforms such as Azure and AWS, along with MLOps practices including model deployment, monitoring, Docker, and REST APIs .

Beyond model development, I focus on measurable impact. I have improved lead engagement through data-driven cohort analysis and A/B testing, optimized feature adoption through ML-powered dashboards, and enhanced system efficiency using automation and analytics . I enjoy translating complex data into actionable insights and building scalable AI systems that align with business objectives.

I am excited to contribute my expertise in machine learning, NLP, Generative AI, and cloud deployment to forward-thinking teams. I would welcome the opportunity to further discuss how my background can support your organization’s AI and data initiatives.

Sincerely,
Dheeraj Singh Shankar

"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
User Information
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Not Applicable" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.


Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Dheeraj Singh
'''
############################################################################################################
