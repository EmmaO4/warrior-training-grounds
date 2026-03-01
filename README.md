# **SUMMARY:**
A community-driven social peer-to-peer platform local to all CSU Stanislaus affiliates (students, professors/instructors, faculty, alumni, and any other affiliated persons).

This project aims to combine the ideas of YouTube, Coursera, Pearson, Facebook, etc. into a social platform in efforts to promote community involvement within Stan State.
 
The application will allow submission of user-created study materials in the form of flashcards, video lectures, and shared notes. These submissions will be heavily monitored and subject to user scrutiny (with a positive emphasis) to ensure creator credibility and overall effectiveness. They may also link relevant materials/videos. The effectiveness of user submission will be scored using an in-house approval rating by users. 

Users will also be able to submit posts on a discussion board of sorts on various topics like: local hangout spots, favorite places to go (off/on campus), announcements for things like active campus library discounts/ local business dicounts/events, overall general stress-relief activities and other using an interactive map.

This project was conceived by ideas presented by Stan State Computer Science Club LEGO Built It Hackathon 2026 Track 3. See relevant pdf for more information on this.

 
# **FAST RECAP SUMMARY:**
user-submitted, Stan-State only tailored youtube/Coursera app: Warrior Training Grounds -- name subject to change:
Stan State API login for authent to ensure relevant users 
Study Hall
    flash card note submission
    volunteered student mentoring (monetized in the future through stan state -- similar to tutoring center) peer-reviewed videos (positive demeanor)/ linked videos by students that they thought were as informative as course material
    discussion board/ forum
map timeline from students/ alumni past semesters (favorite local commutes: food, hangouts, hiking, etc activities)
local discount submission page where students upload discounts for various things, separated by themes


# **NOTES:**
1. Current mentoring program through stan state allows mentors to be paid tangible, real-world currency. This might be a point of contention for user-submitted material by app users. If implemented and integrated by Stan State, negotiations will be discussed on this topic with school board to ensure the mentoring program (a source of income for students and mentors) is not overwritten by this project.
2. Future deployment: should this project be successful in the Stan State ecosystem, ideas of integrating this project in other institutions and localizing it for their tailored needs will be available, probably, maybe, idk.


---
## **Tech Stack:**

Primary framework: Python + Flask 

Frontend:
    undecided 
Backend:
    OAuth: 
        personal Microsoft Azure Entra ID SSO API for development to sim student login (if deployed, will be replaced by StanState login -- they use the same OAuth) 
    DB:
        PostgreSQL
    Cloud Storage:
        need to research this. S3 for now, but costs money 

Optional Services: 
    Redis caching, Celery for background jobs, Analytics/Notifications
Deployment: 
    Dockerized + CI/CD to cloud hosting




Rights reserved for future monitization after implementation, for now this project will serve as practice for real-world application of software and its development collaboration.  