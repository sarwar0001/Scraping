{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "import pandas as pd\n",
    "from selenium.common.exceptions import NoSuchElementException\n",
    "from selenium.common.exceptions import StaleElementReferenceException"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Url of page\n",
    "url_careerguide = \"https://www.careerguide.com/career-options\"\n",
    "page_careerguide = requests.get(url_careerguide)\n",
    "soup = BeautifulSoup(page_careerguide.content,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Aerospace & Aviation', 'Agriculture', 'Automobile / Autocomponents', 'Banking / Insurance & Finance', 'Beauty & Wellness Industry', 'Building & Construction', 'Building / Hardware & Home Furnishings', 'Chemicals & Pharmaceuticals', 'Commerce or Humanities Stream', 'Defense & Military', 'Designing & Art', 'Education / Skill Development', 'Electronics & Hardware', 'Emergency Services', 'Engineering & Technology', 'Exams and Syllabus', 'Food Processing', 'Gems & Jewellery', 'Handlooms & Handicrafts', 'Healthcare', 'Humanistic Studies', 'Information Technology / Software', 'Institutes in India', 'ITES / BPO', 'Law & Order', 'Leather & Leather Goods', 'Management & Marketing', 'Media / Entertainment & Animation', 'Organised Retail', 'Psychometric Career Test', 'Public Admin & Government', 'Real Estate', 'Science & Research', 'Sports', 'Study Abroad', 'Telecom', 'Textiles & Garments', 'Tourism / Hospitality & Travel', 'Transportation/Logistics/Warehousing & Packaging']\n",
      "39\n"
     ]
    }
   ],
   "source": [
    "# scrap data or Job Category ffrom careerguide.com\n",
    "heading_tags = [\"h2\"]\n",
    "Job_category = []\n",
    "for tags in soup.find_all(heading_tags):\n",
    "    Job_category.append(tags.text.strip())\n",
    "print(Job_category)\n",
    "print(len(Job_category))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# direct the webdriver to where the browser file is: \n",
    "browser = webdriver.Chrome(\"chromedriver.exe\")\n",
    "# Go to linkedin and login\n",
    "browser.get('https://www.linkedin.com/')\n",
    "browser.maximize_window()\n",
    "# your secret credentials:\n",
    "username = browser.find_element_by_id(\"session_key\")\n",
    "username.send_keys(\"yourmail\")\n",
    "password = browser.find_element_by_id(\"session_password\")\n",
    "password.send_keys(\"abc\")\n",
    "#submit Details\n",
    "login_button = browser.find_element_by_class_name(\"sign-in-form__submit-button\")\n",
    "login_button.click()\n",
    "browser.get(\"https://www.linkedin.com/jobs/search/?currentJobId=2974348409\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scroll Web page\n",
    "browser.execute_script(\"window.scrollBy(0,document.body.scrollHeight)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['WEB DEVELOPMENT STUDENT INTERNSHIP', 'WEB DEVELOPMENT STUDENT INTERN', 'Front end Intern', 'Subject Matter Expert in Web Development', 'WEB DEVELOPMENT STUDENT INTERNSHIP', 'Web Development Training Program', 'React Js Developer (Internship)']\n",
      "\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "#Scrape JOBS\n",
    "job_title = []\n",
    "job9 = browser.find_elements_by_class_name(\"job-card-list__title\")\n",
    "for i in job9:\n",
    "    job_title.append(i.text)\n",
    "print(job_title)\n",
    "print()\n",
    "print(len(job_title))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['SkillVertex', 'SkillVertex', 'Convin', 'XcitEducation Worldwide', 'SkillVertex', 'Growth Central VC', 'Daphnis Labs']\n",
      "\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "#SCRAPE COMPANY NAME\n",
    "comp_name = []\n",
    "job2 = browser.find_elements_by_class_name(\"job-card-container__company-name\")     \n",
    "for i in job2:\n",
    "    comp_name.append(i.text)\n",
    "print(comp_name)\n",
    "print()\n",
    "print(len(comp_name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Pune, Maharashtra, India', 'Remote', 'Bengaluru, Karnataka, India', 'Remote', 'Bengaluru, Karnataka, India', 'Remote', 'New Delhi, Delhi, India', 'Hybrid', 'Pune, Maharashtra, India', 'Remote', 'India', 'Remote', 'Delhi, India', 'Hybrid']\n",
      "\n",
      "14\n"
     ]
    }
   ],
   "source": [
    "#SCRAPE JOB LOCATION\n",
    "loc_name = []\n",
    "job3 = browser.find_elements_by_class_name(\"job-card-container__metadata-item\")\n",
    "for i in job3:\n",
    "    loc_name.append(i.text)\n",
    "print(loc_name)\n",
    "print()\n",
    "print(len(loc_name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['201-500 employees']\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Scrape for Number of employee\n",
    "emp_no = []\n",
    "job4 = browser.find_elements_by_xpath(\"(/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/ul/li[2]/span)\")\n",
    "for i in job4:\n",
    "    emp_no.append(i.text)\n",
    "print(emp_no)\n",
    "print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['It gives me immense pleasure to introduce ourselves as one of the top leading and emerging edtech platforms in India with our head office in Bangalore.']\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Scrape for Descriptin of Company\n",
    "description = []\n",
    "job5 = browser.find_elements_by_xpath(\"(//*[@id='job-details']/span/p[4])\")\n",
    "for i in job5:\n",
    "    description.append(i.text)\n",
    "print(description)\n",
    "print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              Company Name                                 Job Title  \\\n",
      "0              SkillVertex        WEB DEVELOPMENT STUDENT INTERNSHIP   \n",
      "1              SkillVertex            WEB DEVELOPMENT STUDENT INTERN   \n",
      "2                   Convin                          Front end Intern   \n",
      "3  XcitEducation Worldwide  Subject Matter Expert in Web Development   \n",
      "4              SkillVertex        WEB DEVELOPMENT STUDENT INTERNSHIP   \n",
      "5        Growth Central VC          Web Development Training Program   \n",
      "6             Daphnis Labs           React Js Developer (Internship)   \n",
      "\n",
      "                      Location  \n",
      "0     Pune, Maharashtra, India  \n",
      "1                       Remote  \n",
      "2  Bengaluru, Karnataka, India  \n",
      "3                       Remote  \n",
      "4  Bengaluru, Karnataka, India  \n",
      "5                       Remote  \n",
      "6      New Delhi, Delhi, India  \n"
     ]
    }
   ],
   "source": [
    "col = [\"Company Name\",\"Job Title\",\"Location\",\"Employee\",\"Description\"]\n",
    "df = pd.DataFrame({\"Company Name\":comp_name[slice(7)], \"Job Title\":job_title[slice(7)], \"Location\":loc_name[slice(7)]})\n",
    "df.head()\n",
    "df.to_csv(\"linkedin_scraping_Job.csv\")\n",
    "print(df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
