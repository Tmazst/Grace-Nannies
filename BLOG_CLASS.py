import json
import os
import secrets
from PIL import Image
from datetime import datetime
# from app import app


class blog_class:

    def __init___(self):
        pass


    def save_pic(self,picture,size_x=25,size_y=25):
        from app import app

        # Create hash for image name
        _img_name, _ext = os.path.splitext(picture)
        gen_random = secrets.token_hex(8)
        new_img_name = gen_random + _ext

        # Image URL
        saved_img_path = os.path.join(app.root_path,'static/images/blog_images', new_img_name)

        #Open and Save the Pic
        output_size = (size_x, size_y)
        i = Image.open(picture)
        # i.thumbnail(output_size)

        i.save(saved_img_path)

        return new_img_name

    def update(self,dict_):

        with open("my_blogs.json", "w") as file:
            file.write(json.dumps(dict_, indent=4, sort_keys=True))

            print("File written Successfully")


    def blogs_filer(self,title, body, author, picture):

        dict_buffer = {}

        blog = dict_buffer[title] = {}

        blog["title"] = title
        blog["body"] = body
        blog["author"] = author
        blog["picture"] = picture
        blog["date"] = datetime.utcnow().strftime("%d %b %Y")

        filename = "my_blogs.json"

        if not os.path.exists(filename):
            with open("my_blogs.json", "w") as w_file:

                w_file.write(json.dumps(dict_buffer, indent=4, sort_keys=True))

                print("Dict Buffer: ", dict_buffer)

        else:
            with open(filename, "r") as file:

                r_file = file.read()

                blogs_dict = json.loads(r_file)
                print("Original: ", blogs_dict)

                blogs_dict.update(dict_buffer)

                # blogs_dict[title] = body
                print("Blog Update: ", dict_buffer)

                print("Check Update: ", blogs_dict)

                self.update(blogs_dict)

    
    def load_blogs(self):

        with open("my_blogs.json","r") as r_file:

            #read file
            file = r_file.read()

            #load to with json
            blogs_dict = json.loads(file)

            return blogs_dict
