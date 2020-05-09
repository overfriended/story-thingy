import other

def get_story(name):
    return other.get_list(name)

def get_story_info(story, type):
    if story[0][type]:
        return story[0][type]

def get_content(story_list):
    return story_list[0]['content']

def get_title(content, page):
    return content[int(page) - 1]['title']

def get_body(content, page):
    return content[int(page) - 1]['body']
