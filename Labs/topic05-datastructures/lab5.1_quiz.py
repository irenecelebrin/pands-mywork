# week 05 
# author: icelebrin 
# lab 5, excersice 1: quiz 

# task: Look at this code and answer the questions below, answers at the end of the lab sheet


numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
"firstName" : "Andrew",
"teaching" : [{
"courseName" : "programming",
"semester" : 1
},{
"courseName" : "Data Representation",
"semester" : 2
}
]
}

print(type(someone["firstname"]))


'''
Questions
What are the variable types of the following variables in the code above
a. numberOfQuestions                                 **int**
b. averageAge                                        **float**
c. debugMode                                         **boolean**  
d. name                                              **string**
e. ages                                              **list**
f. months                                            **tuple**
g. months[1]                                         **string**
h. book                                              **dict**
i. stuff                                             **list**
j. stuff[2]                                          **boolean**
k. someone                                           **dict**
l. someone["firstname"]                              **string**
m. me                                                **dict**
n. me["teaching"]                                    **list**
o. me["teaching"][0]["semester"]                     **int**
p is a trick question look at it carefully           **error, the name of the key is courseName**
p. me["teaching"][0]["coursename"]

'''