import handlers
import os

index = None
STORY_NAME = None

if __name__ == "__main__":
    index = 1
    STORY_NAME = input("Name of story to get:\n")

def clear():
    os.system("cls")

def display_chapter(story, content, page):
    title = handlers.get_title(content, page)
    body = handlers.get_body(content, page)

    if story == None:
        print("Story does not exist.")
        return

    print(STORY_NAME + " by " + handlers.get_story_info(story, "author"))
    print("Chapter " + str(page) + ": " + title + "\n\nChapter Content:")
    print(body + "\n")

    print("Press the ENTER key for next chapter...")
    input("")
    clear()

if handlers.get_story(STORY_NAME):
    story = handlers.get_story(STORY_NAME)
    content = handlers.get_content(story)
    title = handlers.get_title(content, index)
    body = handlers.get_body(content, index)

    if story != None:
        clear()

        display_chapter(story, content, 1)

        if len(content) > 1:
            while len(content) > index:
                index += 1
                display_chapter(story, content, index)

                if len(content) == index:
                    clear()
                    print(story[0]['end-message'])
