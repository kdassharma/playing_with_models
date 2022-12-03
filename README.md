Building a CLI to prompt GPT-3 for text queries via CLI string or input file. Code option is available, just provide the file path with the correct type option.

```
alias gpt3="/Users/dashkaus/Documents/Projects/GPT3_CLI/venv/bin/python /Users/dashkaus/Documents/Projects/GPT3_CLI/main.py"
```

Need to investigate:
* How different prompts lead to different results?
* What the effect of long term and short term queries are?
* What are useful, easy to build applications?
  * A module that goes through code in a package and gives an overview of what each class does.
---
![Screen Shot 2022-12-03 at 2 09 23 AM](https://user-images.githubusercontent.com/42706537/205435651-817441f3-1f78-4f1f-9d52-05b7aa60a6fa.png)
---
![Screen Shot 2022-12-03 at 2 09 51 AM](https://user-images.githubusercontent.com/42706537/205435671-c8d6da9e-3265-4f4d-9ef0-94ac28b9023b.png)
---
![Screen Shot 2022-12-03 at 2 10 07 AM](https://user-images.githubusercontent.com/42706537/205435686-76437fc3-4f30-4196-8c49-2b11bcb34011.png)
---
![Screen Shot 2022-12-03 at 2 10 24 AM](https://user-images.githubusercontent.com/42706537/205435700-1d3c7298-54ae-47e0-8e35-85abe4e63142.png)
---
![Screen Shot 2022-12-03 at 2 10 41 AM](https://user-images.githubusercontent.com/42706537/205435711-c6080d97-7dfd-4cde-8ac1-aecbe9e1a064.png)
---
![Screen Shot 2022-12-03 at 2 10 51 AM](https://user-images.githubusercontent.com/42706537/205435721-7ec3abb2-8323-4935-bda7-bad5ed89f746.png)
---
![Screen Shot 2022-12-03 at 2 11 05 AM](https://user-images.githubusercontent.com/42706537/205435725-13f0d4a6-0535-4ccc-b2b3-9807f50c15ba.png)
---
![Screen Shot 2022-12-03 at 2 11 18 AM](https://user-images.githubusercontent.com/42706537/205435738-916829c6-f560-4809-bcda-134e0f0dca77.png)
---
![Screen Shot 2022-12-03 at 2 11 50 AM](https://user-images.githubusercontent.com/42706537/205435755-5aefc27e-452d-498c-91ea-9a95db20a2ae.png)
---
![Screen Shot 2022-12-03 at 2 12 19 AM](https://user-images.githubusercontent.com/42706537/205435785-a2f7fd5c-6f33-4986-b449-d5523cb46b07.png)
---

Code was [this](https://github.com/kdassharma/clipboardRegister/blob/master/clipboard_register.py). Input text was "Write me a Haiku about artificial intelligence.".

```
(venv) dashkaus@bcd0744198df GPT3_CLI % /Users/dashkaus/Documents/Projects/GPT3_CLI/venv/bin/python /Users/dashkaus/Documents/Projects/GPT3_CLI/main.py -t code -i input.py
# 
''
''
('This code creates a graphical user interface using the Tkinter library in '
 'Python. It creates a canvas with a specified height and width and then '
 'creates a frame within the canvas for each new item that is detected in the '
 'clipboard. The frames include labels that display the clipboard content, the '
 'time at which the content was copied, and a copy button (which is not yet '
 'implemented). The code also keeps track of the clipboard content and the '
 'number of frames in the canvas and refreshes the canvas at a specified rate.')

(venv) dashkaus@bcd0744198df GPT3_CLI % /Users/dashkaus/Documents/Projects/GPT3_CLI/venv/bin/python /Users/dashkaus/Documents/Projects/GPT3_CLI/main.py -t normal -i input.txt
''
'AI soars high,'
'Thoughts and data intertwined,'
'A new world awaits.'
(venv) dashkaus@bcd0744198df GPT3_CLI % /Users/dashkaus/Documents/Projects/GPT3_CLI/venv/bin/python /Users/dashkaus/Documents/Projects/GPT3_CLI/main.py -t normal -i input.txt
''
'Robots learn and grow'
'Unseen intelligence grows strong'
'AI is the future'
(venv) dashkaus@bcd0744198df GPT3_CLI % /Users/dashkaus/Documents/Projects/GPT3_CLI/venv/bin/python /Users/dashkaus/Documents/Projects/GPT3_CLI/main.py -t normal -i input.txt
''
'Robots thinking deep'
'AI advances, we sleep'
'Dreaming of the future'
(venv) dashkaus@bcd0744198df GPT3_CLI % 


```
