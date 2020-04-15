# Censor-Dispenser

This is a Codeacademy project with the following scenario:
You’ve recently gotten a job working in the IT department at one of Silicon Valley’s hottest new startups, AirWeb. The company is developing a state-of-the-art artificial intelligence engine designed to help provide a new perspective on the world’s problems. Interestingly, very few people know the details of AirWeb ‘s work and the company is very secretive about its technology, even to its own investors.

You report directly to the Head of Product, a person named Mr. Cloudy, and he has a very important task for you. You see, every month, the head researchers down in the lab send an email to the board of investors to tell them about the status of the project. Cloudy wants you to intercept these emails and censor any “proprietary information” included in them.

The project occurs as follows:
- Create function censoring a specific word/phrase from body of text, then return the text.  Mr Cloudy has asked to censor all instances of phrase "learning algorithms" from the first email, 'email-one'.  Mr.Cloudy doesn't care how it's censored.
- Create function censoring not just specific word or phrase from body of text, but whole list of words, and then return text. Censor all words from "list_two".
- The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’” Censor any occurances of word from "negative words" list after any "negative" word has occured twice, and censoring everything from list from preivous steps as well and censor "email_three".
- This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”  Create function that censors not only all of the words from the negative_words and proprietary_terms lists.  Also, censor any words in email_four that come before AND after a term from those two lists.
- And to extend, make sure can:
  - Handle upper and lowercase characters
  - Handle punctuation
  - censor words while preserving their length
