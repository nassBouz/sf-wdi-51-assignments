from flask import Flask, g
from flask import render_template, flash, redirect, url_for

import models
from forms import SubForm, PostForm ,CommentForm
# this import makes a connection to the models


DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

@app.before_request
def before_request():
    """Connect to the DB before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubForm()
    # checks if the form submission is valid
    if form.validate_on_submit():
        # if it is, we create a new Sub
        models.Sub.create(
            name=form.name.data.strip(), 
            description=form.description.data.strip())

        flash("New sub registered. Called: {}".format(form.name.data))
        # and redirect to the main Sub index
        return redirect('/r')   
    # if the submission isn't valid, send the user back to the original view
    return render_template('new_sub.html', title="New Sub", form=form)

@app.route('/r')
@app.route('/r/<sub>', methods=["GET","POST"])
def r(sub=None):
    if sub == None:
        subs = models.Sub.select().limit(100)
        return render_template("subs.html", subs=subs)
    else:
        # Find the right Sub, use the sub_id 
        sub_id = int(sub)
        sub = models.Sub.get(models.Sub.id == sub_id)
        postsData = sub.posts
        form = PostForm()
        if form.validate_on_submit():
            models.Post.create(
                user=form.user.data.strip(),
                title=form.title.data.strip(), 
                text=form.text.data.strip(), 
                sub=sub)
            return redirect("/r/{}".format(sub_id))
        # Send the found Sub to the template 
        return render_template("sub.html", sub=sub, form=form, posts=postsData)

# @app.route('/posts')
# @app.route('/posts/<id>')
# def posts(post=None):
#     return "Something"

@app.route('/posts')
@app.route('/posts/<id>', methods=["GET","POST"])
def posts(post=None):
    if post == None:
        posts = models.Post.select().limit(100)
        return render_template("posts.html", posts=posts)
    else:
        # Find the right post, use the post_id 
        post_id = int(post)
        post = models.Post.get(models.Post.id == post_id)
        commentsData = post.comments
        form = CommentForm()
        if form.validate_on_submit():
            models.Comment.create(
                user=form.user.data.strip(),
                title=form.title.data.strip(), 
                text=form.text.data.strip(), 
                post=post)
            return redirect("/posts/{}".format(post_id))
        # Send the found Sub to the template 
        return render_template("post.html", post=post, form=form, comments=commentsData)


@app.route('/comments')
@app.route('/comments/')
@app.route('/comments/<id>', methods=["GET","POST"])
def comts(id=None):
    if  id == None:
        comments = models.Comment.select().limit(100)
        return render_template("comments.html", comments=comments)
    else:
        # Find the right Sub, use the sub_id 
        comment_id = int(id)
        comment = models.Comment.get(models.Comment.id == comment_id)
        # comments = post.comments
        # form = CommentForm()
        # if form.validate_on_submit():
        #     models.Comment.create(
        #         user=form.user.data.strip(),
        #         title=form.title.data.strip(), 
        #         text=form.text.data.strip(), 
        #         post=post)
        #     return redirect("/r/{}".format(post_id))
        # # Send the found Sub to the template 
        return render_template("comment.html", comment=comment)

if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)
