def index(request):
    
    ideas = Models.Ideas.sort(recency)[0:4]
    allcomments = []
    for eachidea in ideas:
        comments = Models.comments(eachidea.id)
        allcomments = [allcomments,comments]

    return rendertoresponse('/index.html',RequestContext='{ideas:ideas, allcomments:allcomments}')