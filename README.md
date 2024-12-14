### LLM Agents MOOC Hackathon - fund-analyzer

1. Example fund information in the urls.csv file. Note - first entry is the link to factsheet definition file.
2. Use 'download_pdfs.py' and then 'convert_pdfs.py' to get the fund data
3. Use 'mooc-analyzer.ipynb' to then step through the main application.
4. If files in right directory it should generate questions and create a csv file with the extracted info that you can query.
5. If you want to just see the output of processing over 100 fund pdf files using gpt-4o-mini using this method then look at the extracted_fund_data.csv file.
   
e.g. 


> ask_advisor("What is the most common holding across all of the funds? Just return the name of the one holding.")

> The most common holding across all these funds is **Microsoft Corporation**, appearing in multiple funds with varying levels of allocation.
>

The application uses OpenAI gpt-4o-mini and OpenAI Swarm agent workflow

![image](https://github.com/user-attachments/assets/7dc0b1a8-823b-4700-9eaf-4ac886a0672f)


Prepared for:

![image](https://github.com/user-attachments/assets/ccab7e15-cd54-41f7-be7a-ec46b2401b5e)
