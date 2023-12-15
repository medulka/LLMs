#!usr/bin/env python3

from aleph_alpha_client import Client, Prompt, CompletionRequest

# import pkgutil

# def test_installation(package):
#     if pkgutil.find_loader(package) is not None:
#         return print("installed")
#     else:
#         return print("not installed")
    
# test_installation("aleph_alpha_client")

# to define
client_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxOTQ2MywidG9rZW5faWQiOjQwNzJ9.MsF_ZqRrFDRikisVrfD-8BWNwF60RGrWEXrBWjSrnjk"
model_of_choice="luminous-base"
prompt_text = """Identify matching keywords for each text.
###
Text: The "Whiskey War" is an ongoing conflict between Denmark and Canada over ownership of Hans Island. The dispute began in 1973, when Denmark and Canada reached an agreement on Greenland's borders. However, no settlement regarding Hans Island could be reached by the time the treaty was signed. Since then both countries have used peaceful means - such as planting their national flag or burying liquor - to draw attention to the disagreement.
Keywords: Conflict, Whiskey War, Denmark, Canada, Treaty, Flag, Liquor
###
Text: NASA launched the Discovery program to explore the solar system. It comprises a series of expeditions that have continued from the program's launch in the 1990s to the present day. In the course of the 16 expeditions launched so far, the Moon, Mars, Mercury and Venus, among others, have been explored. Unlike other space programs, the Discovery program places particular emphasis on cost efficiency, true to the motto: "faster, better, cheaper".
Keywords: Space program, NASA, Expedition, Cost efficiency, Moon, Mars, Mercury, Venus
###
Text: Computer vision describes the processing of an image by a machine using external devices (e.g., a scanner) into a digital description of that image for further processing. An example of this is optical character recognition (OCR), the recognition and processing of images containing text. Further processing and final classification of the image is often done using artificial intelligence methods. The goal of this field is to enable computers to process visual tasks that were previously reserved for humans.
Keywords:"""

model = Client(token=client_token)

params = {
    "prompt" : Prompt.from_text(prompt_text),
    "maximum_tokens" : 100,
    "stop_sequences" : ["\n"],
}

request = CompletionRequest(**params)
response = model.complete(request, model=model_of_choice)
print(f"\nKeywords:{response.completions[0].completion}")

#if __name__ == "__main__":
 
