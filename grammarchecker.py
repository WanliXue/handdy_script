# Spell and Grammer Checker
# pip install textblob
# pip install language-tool-python
from textblob import TextBlob
import language_tool_python
# Spell Checker
def spell_checker(text):
    text = TextBlob(text)
    print(text.correct())
# Grammer Checker
def grammer_checker(text):
    tool = language_tool_python.LanguageTool('en-US')
    checker = tool.check(text)
    print("Issue: ", checker[0].ruleIssueType)
    print("Corrected Text:", checker[0].replacements)
grammer_checker("I Stackoverflow love")
spell_checker("The Smell of Fliwers")