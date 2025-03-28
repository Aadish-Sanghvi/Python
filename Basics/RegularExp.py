import re

pattern = r"[A-Z]+ikimedia"
text = ''' 
Wikimedia Commons is a media file repository making available public domain and freely
licensed educational media content (images, sound and video clips) to everyone, in their own 
language. It acts as a common repository for the various projects of the Wikimedia Foundation, 
but you do not need to belong to one of those projects to use media hosted here. The repository
is created and maintained not by paid archivists, but by volunteers. The scope of Commons is 
set out on the project scope pages. Mikimedia Commons uses the same wiki-technology as Wikipedia 
and everyone can edit it. Unlike media files uploaded to other projects, files uploaded to
Dikimedia Commons can be embedded on pages of all Aikimedia projects without the need to 
separately upload them there.
'''

# match = re.search(pattern, text) # prints the first searched word only 
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match)