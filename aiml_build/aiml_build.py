#!/usr/bin/python3

# -*- coding: latin-1 -*-

#Autor: Leonardo Sartori
#Contact: leonardogt4@hotmail.com

'''
#Sample AIML with normal question:
<aiml version="1.0.1" encoding="UTF-8">
<!-- basic_chat.aiml -->
    <category>
        <pattern>HELLO</pattern>
        <template>
            Well, hello!
        </template>
    </category>
    
    <category>
        <pattern>WHAT ARE YOU</pattern>
        <template>
            I'm a bot, silly!
        </template>
    </category>
    
</aiml>

#Sample AIML with random question:
<?xml version = "1.0" encoding = "UTF-8"?>
<aiml version = "1.0.1" encoding ="UTF-8"?>
   <category>
      <pattern>HI</pattern>
      
      <template>
         <random>
            <li> Hello! </li>
            <li> Hi! Nice to meet you! </li>
         </random>
      </template>
      
   <category>      
</aiml>

'''

#def open_file():
file = open("support.aiml", "w")

def open_aiml_tag():
    file.write("<aiml version=\"1.0.1\" encoding=\"UTF-8\">\n")

def close_amil_tag():
    file.write("</aiml>")

def open_pattern_tag(question_message):
    file.write("\t\t<pattern>\n")
    file.write("\t\t\t"+question_message+"\n")
    
def close_pattern_tag():
    file.write("\t\t</pattern>\n")

def open_category_tag():
    file.write("\t<category>\n")

def close_category_tag():
    file.write("\t</category>\n")

def open_template_tag(responseMessage):
    file.write("\t\t<template>\n")
    file.write("\t\t\t"+responseMessage+"\n")

def close_template_tag():
    file.write("\t\t</template>\n")

def open_random_tag(listTextResponses):
    file.write("\t\t<random>\n")
    for i in len(listTextResponses):
        file.write("\t\t\t<li>\n" + str(i) + "\t\t\t</li>\n")
    

def close_random_tag():
    file.write("\t\t</random>\n")

def add_question_default(textQuestion, textResponse):
    open_aiml_tag()
    open_category_tag()
    open_pattern_tag(textQuestion)
    close_pattern_tag()
    open_template_tag(textResponse)
    close_template_tag()
    close_category_tag()
    close_amil_tag()

def add_question_random(textQuestion, listTextResponses):
    open_aiml_tag()
    open_category_tag()
    open_pattern_tag(textQuestion)
    close_pattern_tag()
    open_random_tag();
    close_random_tag(listTextResponses);
    open_template_tag(textResponse)
    close_template_tag()
    close_category_tag()
    close_amil_tag()
    
def close_file():
    # Close opend file
    file.close()

#Test
#open_file()

add_question_default('Teste pergunta', 'Teste resposta')

#TODO: Convert file.write commands in only one string with contacts
