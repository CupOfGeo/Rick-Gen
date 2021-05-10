# Rick and Morty transcript generator
Hello this project started by scraping all the rick and morty transcripts avalible from the wiki https://transcripts.fandom.com/wiki/Rick_and_Morty. I cleaned up about half of them and used them to finetune the smallest 124 million param gpt2 model. I have finetuned the larger 1.5billion param one which was cool but for the sake of putting it on the cloud im gonna start with the smallest. Also both would work much much better if I cleaned the other half of the transcripts. Ideally I would like to turn the fuction that generates the text from the model into a lambda function and use api gateway. I would send it a json file with the prefix, temp and length from my website www.cupofgeo.com. Then it would do the infrence in the lambda and return the text in a json back to the site.

# Setup
Be sure to extract the tar file and install the requierments.txt you must use python 3.7 

difficulties: I'm very new to cloud, the model and tensorflow are over 500MB which is an issue for serverless i dont mind make people wait if its gonna be free for them which is why I'm intrested in serverless.
