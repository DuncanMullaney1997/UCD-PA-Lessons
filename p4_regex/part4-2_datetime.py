# Import datetime
# from datetime import datetime
#
# # Assign date to get_date
# get_date = datetime.now()
#
# # Add named placeholders with format specifiers
# message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"
#
# # Use the format method replacing the placeholder with get_date
# print(message.format(today=get_date))
# -------------------------------------------------------
# family = {"dad": "John", "siblings": "Jack"}
# print("is your dad called {family[dad]}?".format(family=family))
#
# print(f"Is your dad called {family['dad']}?")
#
# # use "\" to use literals
# print("my dad is called \"John\"")
# # -------------------------------------------------------
# # Complete the f-string
# print(f"About {12300000:e} of {'people'} in the world")
# # Complete the f-string
# print(f"{'people'} create around {102.33382:.2f}% of the data but only {1.9282:.1f}% is analyzed")
# # -------------------------------------------------------
# east = {'date': datetime.datetime(2007, 4, 20, 0, 0), 'price': 1232443}
# # Access values of date and price in east dictionary
# print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")
# # Access values of date and price in west dictionary
# print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")
# -------------------------------------------------------
# template strings using substitute
# Import Template
# from string import Template
#
# tool1 = 'Natural Language Toolkit'
# tool2 = 'TextBlob'
# tool3 = 'Gensim'
# description1 = 'suite of libraries and programs for symbolic and statistical natural language processing (NLP).'
# description2 = 'Python library for processing textual data.'
# description3 = 'robust open-source vector space modeling and topic modeling toolkit implemented in Python.'
#
# # Create a template
# wikipedia = Template("$tool is a $description")
#
# # Substitute variables in template
# print(wikipedia.substitute(tool=tool1, description=description1))
# print(wikipedia.substitute(tool=tool2, description=description2))
# print(wikipedia.substitute(tool=tool3, description=description3))
# ----------------------------------------------------------------------
# Import template
from string import Template
tools = ['Natural Language Toolkit', '20', 'month']
# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))
# ----------------------------------------------------------------------
# Import template
from string import Template
answers={'answer1': 'I really like the app. But there are some features that can be improved'}
# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------