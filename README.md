# **Task 1: Job Marketing API**

**API Endpoint:**  
[https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo]

### **Requirements:**
- Connect to the API endpoint and extract job roles.
- Create two separate lists:
  - One for **senior roles**
  - One for **manager roles**

# **Task 2: Football API**

**API Endpoint:**  
[http://api.football-data.org/v4/competitions/]

### **Requirements:**
- Connect to the API endpoint and extract all competition names.
- Store the competition names in a separate list.

# **Task 3: Random User API**

**API Endpoint:**  
[https://randomuser.me/api/?results=500]

### **Requirements:**
- Connect to the API endpoint and extract user profiles.
- Create two separate lists:
  - One for **male profiles**
  - One for **female profiles**
- Extract all dates of birth into a list:
  - Only the `date` value from the `dob` object is needed.
- Extract concatenated first and last names into a list:
  - Combine the `first` and `last` name fields to create a full name.
