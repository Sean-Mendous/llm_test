from llm.chatgpt_setting import chatgpt_4o, chatgpt_4omini, chatgpt_4o_image_model
from llm.gemini_setting import gemini_20_flash_with_video, upload_video

"""
- for text = 1
need "prompt.md"

- for image = 2
need "prompt.md" and "image.png"

- for video = 3
need "prompt.md" and "video.mp4"
"""

#change the setting here
system_setting = 1

image_path = 'INPUT/image.png'

video_path = 'INPUT/video.mp4'


#----- system -----


def main(image_path=image_path, video_path=video_path, system_setting=system_setting):

    prompt = input('INPUT/prompt.md')

    if not prompt:
        raise ValueError("Prompt is required")

    if system_setting == 1:
        responce = text(prompt)
    elif system_setting == 2:
        if not image_path:
            raise ValueError("Image path is required")
        responce = image(prompt, image_path)
    elif system_setting == 3:
        if not video_path:
            raise ValueError("Video path is required")
        responce = video(prompt, video_path)
    else:
        raise ValueError("Invalid system setting")
    
    output('OUTPUT/output.md', responce)
    
    return responce

def text(prompt, model='chatgpt_4omini'):
    if model == 'chatgpt_4o':
        try:
            responce = chatgpt_4o(prompt)
            print(' - got responce')
        except Exception as e:
            raise ValueError(f"Error: {e}")
    elif model == 'chatgpt_4omini':
        try:
            responce = chatgpt_4omini(prompt)
            print(' - got responce')
        except Exception as e:
            raise ValueError(f"Error: {e}")
    else:
        raise ValueError("Invalid model")
    
    return responce

def image(prompt, image_path):
    try:
        responce = chatgpt_4o_image_model(prompt, image_path)
        print(' - got responce')
    except Exception as e:
        raise ValueError(f"Error: {e}")
    
    return responce

def video(prompt, video_path):
    try:
        uploaded_file = upload_video(video_path)
        print(' - uploaded file')
    except Exception as e:
        raise ValueError(f"Error: {e}")
    
    try:
        responce = gemini_20_flash_with_video(prompt, uploaded_file)
        print(' - got responce')
    except Exception as e:
        raise ValueError(f"Error: {e}")
    
    return responce

def input(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            input = file.read()
            print(' - input complete')
    except Exception as e:
        raise ValueError(f"Error: {e}")
    
    return input

def output(path, output):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(output)
            print(' - output complete')
    except Exception as e:
        raise ValueError(f"Error: {e}")
    
    return path

if __name__ == "__main__":
    print('~~~~~ 💥 START 💥 ~~~~~')
    main()
    print('~~~~~ 🍺 ALL DONE 🍺 ~~~~~')

    