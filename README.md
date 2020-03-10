# Multiple Choice Project

​
This week, you will choose one of three projects to work on.
​
Your creativity and common sense should be used as you work. There are common features to web applications that users expect. If they are not mentioned in the project's description, you should still do them. For example: in the Question Box application, users should have avatar images. You don't have to handle file uploads yourself -- you could use Gravatar with [django-gravatar](https://github.com/twaddington/django-gravatar) -- but you need some way of handling that.
​
Likewise, come up with your own features to make your project unique. You will likely use this project in your portfolio, so make it stand out!
​

## Trying new things

​
You should try something they don't know how to do on their project. This could be a Python or JavaScript library you haven't used before or a feature of Django you haven't tried.
​
Some ideas:
​

- [Allow users to authenticate via Google or other third-party auth](https://www.intenct.nl/projects/django-allauth/)
- [Try Dragula for drag and drop](https://bevacqua.github.io/dragula/)
- [Use Django REST Framework to build an API](https://www.django-rest-framework.org/)
  ​

## Project 3: Flashcards

​
You want to make an application to help people learn via flashcards. You are going to build a web application that has these goals:
​

- Registered users can create multiple decks of flashcards, each with a prompt or question and an answer.
- Registered users can quiz themselves on a deck.
- Success and failure for each card is recorded.
  ​

### How decks and cards work

​
A user can have multiple decks of flashcards. Each deck has a title. Each flash card has a prompt or question and an answer.
​
When a user is quizzing themselves on a deck, they _do not_ have to type in answers. They are shown the prompt, they click to see the answer; they then mark whether they answered it correctly or not. They should see one card at a time.
​
When the user marks success or failure on a card, this should be recorded.
​
The cards should be shown in a random order at a minimum. A preferable method would be to use something like [the Leitner system](https://www.virtualsalt.com/learn10.html) for flash cards. This system uses review times; you could use that, or just use the idea of multiple boxes, with cards in lower boxes coming up more often.
​

### Creating decks and running through decks

​
This application has two very distinct parts -- creating decks and cards and then running through those decks. This is a natural place to split work. Do not forget to make creating decks and cards an easy-to-use experience.
​

### How much of this is JavaScript + Ajax?

​
This can vary, but I imagine a lot of it is JavaScript. To show one card at a time without a page reload in between cards will require talking back and forth via Ajax. Recording whether you answered correctly or not would be another Ajax call.
​
"Flipping" a card (you don't have to animate a card flip, although if you do, that's very cool) will almost certainly require JavaScript.
​
You could have a page load in between cards and reduce your amount of JavaScript. Depending on how you do this, it could also record success or failure, eliminating most of your JavaScript.
