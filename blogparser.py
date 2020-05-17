from os import listdir

def blog_parse(blogname):

    raw_blog_name = blogname
    blog = open("./rawblogs/"+raw_blog_name, "r").read()
    pieces = blog.split("\n\n")

    title = pieces[0]
    date = pieces[1]
    body = pieces[2:]

    return_dict = {'title': title, 'date': date, 'body': []}

    def body_piece_to_dict(body_piece):
        fragments = body_piece.split("//image//")
        if len(fragments) > 1:
            body_piece = fragments[1]
            ret = {'type': 'image'}
        else:
            ret = {'type': 'text'}

        ret['content'] = body_piece
        return ret

    for piece in body:
        return_dict['body'].append(body_piece_to_dict(piece))

    return return_dict


def form_blog_html():
    skeleton = open("./html/blogtemplate.html", "r").read().split("{{posts}}")
    print(skeleton)

    f = open("./html/blog.html", "w")


    blogs = listdir("./rawblogs")
    formated_blogs = ""

    print(blogs)
    for blog in blogs:
        post = blog_parse(blog)
        formated_blogs += "<h1 class='text-center blogTitle'>" + post['title'] + "</h1>\n"
        formated_blogs += "<h4 class='date my-5'>" + post['date'] + "</h4>\n"
        print(post['body'])
        for paragraph in post['body']:
            if paragraph['type'] == "text":
                formated_blogs += "<p class='text-md-left'>" + paragraph['content'] + "</p>\n"
            else:
                formated_blogs += "<img src=\"" + paragraph['content'] + "\" class=\"img-thumbnail\">\n"
        print(post)

    print(formated_blogs)
    f.write(skeleton[0]+formated_blogs+skeleton[1])

form_blog_html()
